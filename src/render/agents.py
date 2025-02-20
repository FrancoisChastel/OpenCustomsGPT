# Copyright (C) 2025 Francois Chastel
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import json
import pickle
from pathlib import Path
from typing import List
from typing import Sequence

import pandas as pd
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import AgentEvent
from autogen_agentchat.messages import ChatMessage
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.messages import ToolCallSummaryMessage
from autogen_agentchat.teams import SelectorGroupChat
from autogen_core import CancellationToken
from streamlit.runtime.state import SessionStateProxy

from agents.config import EXECUTION_WORK_DIR
from agents.tools import OutputType
from render.messages import AgentMessage
from render.messages import DataFrameMessage
from render.messages import FunctionMessage
from render.messages import MainMesage
from render.messages import PlotlyMessage


class TrackableGroupChatManager(SelectorGroupChat):
    async def run(
        self,
        *,
        session_state: SessionStateProxy,
        task: str | ChatMessage | Sequence[ChatMessage] | None = None,
        cancellation_token: CancellationToken | None = None,
    ) -> TaskResult:
        result: TaskResult | None = None
        async for message in self.run_stream(
            task=task,
            cancellation_token=cancellation_token,
        ):
            if isinstance(message, TaskResult):
                result = message
            render_message(message)
            session_state.messages.append(message)
            
        if result is not None:
            return result
        raise AssertionError("The stream should have returned the final result.")
        
        
def render_message(message: AgentEvent | ChatMessage | TaskResult) -> None:
    if isinstance(message, TextMessage):
        if message.source in ["user", "admin"]:
          MainMesage(author=message.source, content=message.content).render()
        elif message.source in ["code_executor"]:
          print(message.content, message.source, type(message.content))
          if message.content.startswith("["):
            render_serialize_variable(json.loads(message.content))
          else:
            AgentMessage(author=message.source, content=message.content).render()
        else:
          AgentMessage(author=message.source, content=message.content).render()
    elif isinstance(message, ToolCallSummaryMessage):
        function_results = json.loads(message.content)
        if message.source == "sql_executor":
            for result in function_results:
              variables = result.get("variables", {})
              output_type = variables.get("output_type", OutputType.UNKNOWN.value)
              if output_type == OutputType.PICKLED_DATAFRAME.value:
                  dataframe = pd.read_pickle(Path(EXECUTION_WORK_DIR) / variables.get("file_path", ""))
                  DataFrameMessage(author=message.source, dataframe=dataframe).render()
              else: 
                  FunctionMessage(author=message.source, results=message.content).render()
        else:
            FunctionMessage(author=message.source, results=message.content).render()

def render_serialize_variable(content: List[dict]) -> None:
    for variable in content:
        if variable.get("output_type") == OutputType.PICKLED_DATAFRAME.value:
            dataframe = pd.read_pickle(Path(EXECUTION_WORK_DIR) / variable.get("file_path", ""))
            DataFrameMessage(author="code_executor", dataframe=dataframe).render()
        elif variable.get("output_type") == OutputType.PLOT.value:
            with open(Path(EXECUTION_WORK_DIR) / variable.get("file_path", ""), "rb") as f:
                figure = pickle.load(f)
                PlotlyMessage(author="code_executor", figure=figure).render()
        elif variable.get("output_type") == OutputType.STRING.value:
            FunctionMessage(author="code_executor", results=variable.get("value", "")).render()
        else:
            FunctionMessage(author="code_executor", results=json.dumps(variable)).render()