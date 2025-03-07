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


from pathlib import Path

import yaml
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.agents import CodeExecutorAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_core.models import ChatCompletionClient

from agents.config import EXECUTION_WORK_DIR
from agents.executor import DataAwareExecutor
from agents.prompts import ADMIN_PROMPT
from agents.prompts import CODE_WRITER_PROMPT
from agents.prompts import SQL_EXECUTOR_PROMPT
from agents.sql import get_sql_coder_prompt
from agents.tools import execute_sql
from render.agents import TrackableGroupChatManager


def setup_group_chat() -> TrackableGroupChatManager:
  with open("configs/coder_agent.yaml", "r") as f:
      model_config = yaml.safe_load(f)
  coder_model = ChatCompletionClient.load_component(model_config)

  with open("configs/normal_agent.yaml", "r") as f:
      model_config = yaml.safe_load(f)
  writer_model = ChatCompletionClient.load_component(model_config)

  with open("configs/normal_agent.yaml", "r") as f:
      model_config = yaml.safe_load(f)
  thinking_client = ChatCompletionClient.load_component(model_config)

  with open("configs/sql_agent.yaml", "r") as f:
      model_config = yaml.safe_load(f)
  sql_client = ChatCompletionClient.load_component(model_config)

  sql_coder = AssistantAgent(
        name="sql_coder",
        model_client=sql_client,
        system_message=get_sql_coder_prompt(),
        model_client_stream=True,
    )

  sql_executor = AssistantAgent(
      name="sql_executor",
      model_client=coder_model,
      tools=[
          execute_sql,
      ],
      system_message=SQL_EXECUTOR_PROMPT,
      model_client_stream=True,
  )

  code_writer = AssistantAgent(
      name="code_writer",
      model_client=thinking_client,
      system_message=CODE_WRITER_PROMPT,
      model_client_stream=True,
  )
  
  code_executor = CodeExecutorAgent(
      name="code_executor",
      code_executor=DataAwareExecutor(work_dir=Path(EXECUTION_WORK_DIR)),
      description="You run python code that should be provided to you by code_writer, if you don't have it, ask for it.",
      sources=["code_writer"],
  )

  admin = AssistantAgent(
      name="admin",
      model_client=thinking_client,
      system_message=ADMIN_PROMPT,
      model_client_stream=True,
  )
  termination = TextMentionTermination("APPROVE", sources=["admin"])

  return TrackableGroupChatManager([admin, code_writer, sql_coder, sql_executor, code_executor], termination_condition=termination, model_client=writer_model)
