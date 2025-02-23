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
        if message.source == "sql_executor":
            # We should always use text as a way to render the message as these are streamlit limitations.
            # Some more engineering is needed to make the rendering more dynamic.
            # But I suggest once again to go away from streamlit and use react+flask.
            if message.content.startswith("|"):
              dataframe = pd.read_table(StringIO(message.content), sep="|", header=0, index_col=1, skipinitialspace=True).dropna(axis=1, how='all').iloc[1:]
              DataFrameMessage(author=message.source, dataframe=dataframe).render()
            else: 
               FunctionMessage(author=message.source, results=message.content).render()
        else:
          FunctionMessage(author=message.source, results=message.content).render()
          FunctionMessage(author=message.source, results=message.content).render()
