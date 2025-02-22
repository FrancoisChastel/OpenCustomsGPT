import chainlit as cl
import yaml
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_core.models import ChatCompletionClient

import cache
from agents.prompts import ADMIN_PROMPT
from agents.prompts import DATA_ANLYST_PROMPT
from agents.prompts import SQL_EXECUTOR_PROMPT
from agents.sql import get_sql_coder_prompt
from agents.tools import ContextualTools


def setup_group_chat() -> SelectorGroupChat:
  with open("configs/coder_agent.yaml", "r") as f:
      model_config = yaml.safe_load(f)
  coder_model = ChatCompletionClient.load_component(model_config)

  with open("configs/normal_agent.yaml", "r") as f:
      model_config = yaml.safe_load(f)
  writer_model = ChatCompletionClient.load_component(model_config)

  with open("configs/normal_agent.yaml", "r") as f:
      model_config = yaml.safe_load(f)
  thinking_client = ChatCompletionClient.load_component(model_config)

  tools = ContextualTools(cache.cached_variables)
  sql_coder = AssistantAgent(
        name="sql_coder",
        model_client=coder_model,
        system_message=get_sql_coder_prompt(),
        model_client_stream=True,
    )

  sql_executor = AssistantAgent(
      name="sql_executor",
      model_client=coder_model,
      tools=[
          tools.execute_sql,
      ],
      system_message=SQL_EXECUTOR_PROMPT,
      model_client_stream=True,
  )

  data_analyst = AssistantAgent(
      name="data_analyst",
      model_client=thinking_client,
      system_message=DATA_ANLYST_PROMPT,
      model_client_stream=True,
  )

  admin = AssistantAgent(
      name="admin",
      model_client=writer_model,
      system_message=ADMIN_PROMPT,
      model_client_stream=True,
  )
  termination = TextMentionTermination("APPROVE", sources=["admin"])

  return SelectorGroupChat([admin, data_analyst, sql_coder, sql_executor], termination_condition=termination, model_client=writer_model)
  return SelectorGroupChat([admin, data_analyst, sql_coder, sql_executor], termination_condition=termination, model_client=writer_model)
  return SelectorGroupChat([admin, data_analyst, sql_coder, sql_executor], termination_condition=termination, model_client=writer_model)
