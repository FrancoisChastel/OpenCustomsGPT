from typing import List
from typing import cast

import chainlit as cl
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import ModelClientStreamingChunkEvent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.messages import ToolCallSummaryMessage
from autogen_agentchat.teams import SelectorGroupChat
from autogen_core import CancellationToken

from agents.setup import setup_group_chat
from cache import init


@cl.on_chat_start  # type: ignore
async def start_chat() -> None:
    init()
    cl.user_session.set("sql_results", [])  # type: ignore
    cl.user_session.set("prompt_history", "")  # type: ignore
    cl.user_session.set("team", setup_group_chat())  # type: ignore


@cl.set_starters  # type: ignore
async def set_starts() -> List[cl.Starter]:
    return [
        cl.Starter(
            label="Data extraction",
            message="Give me the biggest importer.",
        ),
        cl.Starter(
            label="SQL Query",
            message="Write me an SQL query to get all the countries of origins.",
        ),
        cl.Starter(
            label="Plot data",
            message="Plot a bar chart for the biggest importer of hscode starting with 1511.",
        ),
    ]

@cl.on_message  # type: ignore
async def chat(message: cl.Message) -> None:
    team = cast(SelectorGroupChat, cl.user_session.get("team"))  # type: ignore

    tool_response: cl.Step | None = None
    step_response: cl.Step | None = None
    streaming_response: cl.Message | None = None

    async for msg in team.run_stream(
        task=[TextMessage(content=message.content, source="user")],
        cancellation_token=CancellationToken(),
    ):
        if isinstance(msg, ToolCallSummaryMessage):
            with cl.Step(name=f"{msg.source.replace('_', ' ')} call summary", type="tool") as step:
                step.output = msg.content
        elif isinstance(msg, ModelClientStreamingChunkEvent):
            if msg.source in ["data_analyst", "sql_coder"]:
                if step_response is None:
                    step_response = cl.Step(name=f"{msg.source.replace('_', ' ')} agent")
                await step_response.stream_token(msg.content)
            else:
              if streaming_response is None:
                  streaming_response = cl.Message(content="", author=msg.source)
              await streaming_response.stream_token(msg.content)
        elif tool_response is not None:
            await tool_response.send()
            tool_response = None
        elif step_response is not None:
            await step_response.send()
            step_response = None
        elif streaming_response is not None:
            await streaming_response.send()
            streaming_response = None
        elif isinstance(msg, TaskResult):
            final_message = "Task terminated."
            if msg.stop_reason:
                final_message += msg.stop_reason
            await cl.Message(content=final_message).send()
        else:
            pass           
