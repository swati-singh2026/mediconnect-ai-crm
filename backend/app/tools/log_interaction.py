from app.graph.state import GraphState


def log_interaction(state: GraphState):
    """
    Log a new HCP interaction.
    """

    state["response"] = {
        "doctor": "Dr Sharma",
        "summary": "Discussed diabetes medicine.",
        "follow_up": "Next visit Friday",
        "status": "Saved"
    }

    return state