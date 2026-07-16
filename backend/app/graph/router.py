from app.graph.state import GraphState


def route(state: GraphState):
    return state["intent"]
def save_interaction(state: GraphState):
    state["response"] = "Interaction saved successfully."
    return state


def generate_summary(state: GraphState):
    state["response"] = "AI Summary generated."
    return state