from dataclasses import dataclass
from typing import List

import yaml
from autogen_core import MessageContext
from autogen_core import RoutedAgent
from autogen_core import SingleThreadedAgentRuntime
from autogen_core import TopicId
from autogen_core import message_handler
from autogen_core import type_subscription
from autogen_core.models import ChatCompletionClient
from autogen_core.models import SystemMessage
from autogen_core.models import UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient

from data_schema.config import REFORMULATOR_PROMPT


@dataclass
class Message:
    content: str

query_reformulator_type = "QueryReformulatorAgent"
summarizer_reformulator_type = "SummarizerAgent"
user_topic_type = "User"

@type_subscription(topic_type=query_reformulator_type)
class QueryReformulator(RoutedAgent):
    def __init__(self, model_client: ChatCompletionClient) -> None:
        super().__init__("A reformulator agent.")
        self._system_message = SystemMessage(
            content=REFORMULATOR_PROMPT
        )
        self._model_client = model_client

    @message_handler
    async def handle_intermediate_text(self, message: Message, ctx: MessageContext) -> None:
        prompt = f"User query :\n{message.content}."
        llm_result = await self._model_client.create(
            messages=[self._system_message, UserMessage(content=prompt, source=self.id.key)],
            cancellation_token=ctx.cancellation_token,
        )
        response = llm_result.content
        assert isinstance(response, str)

        await self.publish_message(Message(response), topic_id=TopicId(summarizer_reformulator_type, source=self.id.key))


@type_subscription(topic_type=summarizer_reformulator_type)
class SummarizerAgent(RoutedAgent):
    def __init__(self, model_client: ChatCompletionClient) -> None:
        super().__init__("A writer agent.")
        self._system_message = SystemMessage(
            content=(
                "You are a synthetizer agent, you are transforming into 3 prompts based on the discussion made before to run against a RAG. "
                "You seperate your prompt with a comma (;) and a space ( ). You just reply with the prompts."
            )
        )
        self._model_client = model_client

    @message_handler
    async def handle_intermediate_text(self, message: Message, ctx: MessageContext) -> None:
        prompt = f"Below is the discussion:\n\n{message.content}"

        llm_result = await self._model_client.create(
            messages=[self._system_message, UserMessage(content=prompt, source=self.id.key)],
            cancellation_token=ctx.cancellation_token,
        )
        response = llm_result.content
        assert isinstance(response, str)
        print(f"{'-'*80}\n{self.id.type}:\n{response}")

        await self.publish_message(Message(response), topic_id=TopicId(user_topic_type, source=self.id.key))

@type_subscription(topic_type=user_topic_type)
class UserAgent(RoutedAgent):
    def __init__(self) -> None:
        super().__init__("A user agent that outputs the final copy to the user.")

    @message_handler
    async def handle_final_copy(self, message: Message, ctx: MessageContext) -> None:
        print(f"\n{'-'*80}\n{self.id.type} received final copy:\n{message.content}")

with open("configs/small_agent.yaml", "r") as f:
    model_config = yaml.safe_load(f)
small_model = ChatCompletionClient.load_component(model_config)


async def refornulate_prompt(prompt: str) -> List[str]:  
    runtime = SingleThreadedAgentRuntime()

    await QueryReformulator.register(runtime, type=query_reformulator_type, factory=lambda: QueryReformulator(model_client=small_model))
    await SummarizerAgent.register(runtime, type=summarizer_reformulator_type, factory=lambda: SummarizerAgent(model_client=small_model))
    await UserAgent.register(runtime, type=user_topic_type, factory=lambda: UserAgent())    
    
    runtime.start()

    await runtime.publish_message(Message(prompt), topic_id=TopicId(query_reformulator_type, source="default"))
    await runtime.stop_when_idle()
    
    return []
