from typing import TypedDict


class GraphState(TypedDict):
    user_input: str
    intent: str
    response: str