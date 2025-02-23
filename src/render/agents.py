import json
import pickle
from io import StringIO
from pathlib import Path
from typing import Sequence

import pandas
import pandas as pd
import streamlit as st
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import AgentEvent
from autogen_agentchat.messages import ChatMessage
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.messages import ToolCallSummaryMessage
from autogen_agentchat.teams import SelectorGroupChat
from autogen_core import CancellationToken
from streamlit.runtime.state import SessionStateProxy

from agents.config import EXECUTION_WORK_DIR
from agents.tools import FunctionResult
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
          variables = json.loads(message.content)
          
          for variable in variables:
            if variable.get("type") == "dataframe":
              DataFrameMessage(author=message.source, dataframe=pandas.DataFrame(variable.get("data", {}))).render()
            elif variable.get("type") == "plotly":
              PlotlyMessage(author=message.source, figure=variable.get("data")).render()
            else:
              AgentMessage(author=message.source, content=message.content).render()

          

          # A bit hacky, we should intercept the renderer loop in case of figure rendering
          # The next good step is to go away from streamlit and use react+flask. 
          # Time limitations made me use streamlit as a quick solution.
          pickel_path = Path("run_tmp") / message.content.strip()
          print(pickel_path.name.endswith(".pkl"))
          if pickel_path.name.endswith(".pkl"):
            with open(pickel_path, "rb") as f:
                code_executor = pickle.load(f)
                PlotlyMessage(author=message.source, figure=code_executor).render()
          else:
            AgentMessage(author=message.source, content=message.content).render()
        else:
          AgentMessage(author=message.source, content=message.content).render()
    elif isinstance(message, ToolCallSummaryMessage):
        print(message.content)
        function_results = json.loads(message.content)
        if message.source == "sql_executor":
            for result in function_results:
              variables = result.get("variables", {})
              output_type = variables.get("output_type", OutputType.UNKNOWN.value)
              if output_type == OutputType.PICKLED_DATAFRAME.value:
                  dataframe = pd.read_pickle(Path(EXECUTION_WORK_DIR) / variables.get("path", ""))
                  DataFrameMessage(author=message.source, dataframe=dataframe).render()
              elif output_type == OutputType.DATAFRAME.value:
                  DataFrameMessage(author=message.source, dataframe=pandas.DataFrame(variables.get("data", {}))).render()
              else: 
                  FunctionMessage(author=message.source, results=message.content).render()
        else:
            FunctionMessage(author=message.source, results=message.content).render()