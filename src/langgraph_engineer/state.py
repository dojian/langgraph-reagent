from langgraph.graph import MessagesState
from typing import TypedDict, Literal
class AgentState(MessagesState):
    requirements: str
    code: str
    accepted: bool


class OutputState(TypedDict):
    code: str


class GraphConfig(TypedDict):
    gather_model: Literal['openai', 'openai-mini', 'anthropic']
    draft_model: Literal['openai', 'openai-mini', 'anthropic']
    critique_model: Literal['openai', 'openai-mini', 'anthropic']
