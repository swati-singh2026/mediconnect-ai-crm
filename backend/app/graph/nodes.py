from app.graph.state import GraphState


def detect_intent(state: GraphState):
    text = state["user_input"].lower()

    if "summary" in text:
        state["intent"] = "summary"
    else:
        state["intent"] = "save"

    return state


def save_interaction(state: GraphState):
    state["response"] = "Interaction saved successfully."
    return state


def generate_summary(state: GraphState):
    state["response"] = "AI Summary generated successfully."
    return state