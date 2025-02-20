from typing import List
from typing import cast

import chainlit as cl
import pandas as pd
import yaml
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.agents import UserProxyAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.messages import ModelClientStreamingChunkEvent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.teams import SelectorGroupChat
from autogen_core import CancellationToken
from autogen_core.models import ChatCompletionClient
from sqlalchemy import create_engine
from sqlalchemy import text

from agents.sql import get_schema
from agents.sql import get_sql_fix_system_prompt
from agents.sql import get_sql_system_prompt


DB_URI = "postgresql+psycopg2://localhost:5432/imf_sydonia"


def execute_sql(sql_query: str) -> str:
    """Execute SQL query to reply to retrieve results of query."""
    engine = create_engine(DB_URI)
    with engine.connect() as connection:
        df = pd.read_sql_query(text(sql_query), connection)
        dfs = cl.user_session.get("sql_results")
        if dfs is None:
            dfs = []
        dfs.append(df)
        cl.user_session.set("sql_results", dfs)
            
        if df.empty:
            raise ValueError("No results found with the given query. Try to fix the query.")
        else:
            if len(df) > 10:
                return f"Trimmed only to get the first 10 df: {df.head(10).to_string()}, the complete df not displayed but accessible inside the user_session.get('sql_results')."
            else:
                return df.to_string()


@cl.on_chat_start  # type: ignore
async def start_chat() -> None:
    # Load model configuration and create the model client.
    with open("configs/coder_agent.yaml", "r") as f:
        model_config = yaml.safe_load(f)
    coder_client = ChatCompletionClient.load_component(model_config)

    with open("configs/normal_agent.yaml", "r") as f:
        model_config = yaml.safe_load(f)
    normal_agent = ChatCompletionClient.load_component(model_config)

    with open("configs/normal_agent.yaml", "r") as f:
        model_config = yaml.safe_load(f)
    thinking_client = ChatCompletionClient.load_component(model_config)

    # Create the assistant agent.
    sql_coder = AssistantAgent(
        name="sql_coder",
        model_client=coder_client,
        tools=[
            execute_sql,
        ],
        system_message=get_sql_system_prompt(get_schema()),
        model_client_stream=True,
    )

    data_analyst = AssistantAgent(
        name="data_analyst",
        model_client=thinking_client,
        system_message="""
        You should provide concise and clear answer and never come up with fake data.
        If data is needed it should be asked to sql_coder.
        The results of SQL queries are stored in the variable df.
        You are building reports for the customs organisation of Madagascar.
        If you don't have the data, you should ask SQL_Coder to provide the data for you.
        If you need more data to answer the question, you should ask SQL_Coder to provide the data for you.
        You never create fake data and should only rely on SQL_Executor data.
        You never repeat yourself twice in a row
        You never ask a followup question to the user.
        Always save figures to file in the current directory.
        """,
        model_client_stream=True,
    )

    admin = AssistantAgent(
        name="admin",
        model_client=normal_agent,
        system_message="You are an admin if this done you write APPROVE.",
        model_client_stream=True,
    )
    
    # Termination condition.
    termination = TextMentionTermination("APPROVE", sources=["admin"])
    
    group_chat = SelectorGroupChat([data_analyst, sql_coder, admin], termination_condition=termination, model_client=normal_agent)

    # Set the assistant agent in the user session.
    cl.user_session.set("prompt_history", "")  # type: ignore
    cl.user_session.set("team", group_chat)  # type: ignore


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
    # Get the team from the user session.
    team = cast(SelectorGroupChat, cl.user_session.get("team"))  # type: ignore
    # Streaming response message.
    step_response: cl.Step | None = None
    streaming_response: cl.Message | None = None
    # Stream the messages from the team.

    async for msg in team.run_stream(
        task=[TextMessage(content=message.content, source="user")],
        cancellation_token=CancellationToken(),
    ):
        

        if isinstance(msg, ModelClientStreamingChunkEvent):
            # Stream the model client response to the user.
            print(msg.source)
            if msg.source in ["data_analyst", "sql_coder"]:
                if step_response is None:
                    step_response = cl.Step(name=f"{msg.source.replace('_', ' ')} agent")
                await step_response.stream_token(msg.content)
            else:
              if streaming_response is None:
                  # Start a new streaming response.
                  streaming_response = cl.Message(content="", author=msg.source)
              await streaming_response.stream_token(msg.content)
        elif step_response is not None:
            # Done streaming the model client response.
            # We can skip the current message as it is just the complete message
            # of the streaming response.
            await step_response.send()
            # Reset the streaming response so we won't enter this block again
            # until the next streaming response is complete.
            step_response = None
        elif streaming_response is not None:
            # Done streaming the model client response.
            # We can skip the current message as it is just the complete message
            # of the streaming response.
            await streaming_response.send()
            # Reset the streaming response so we won't enter this block again
            # until the next streaming response is complete.
            streaming_response = None
        elif isinstance(msg, TaskResult):
            # Send the task termination message.
            final_message = "Task terminated. "
            if msg.stop_reason:
                final_message += msg.stop_reason
            await cl.Message(content=final_message).send()
        else:
            pass            # Skip all other message types.
