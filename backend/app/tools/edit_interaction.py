from app.graph.state import GraphState


def edit_interaction(state: GraphState):
    """
    Edit an existing interaction.
    """

    state["response"] = {
        "status": "Updated",
        "message": "Next visit changed to Monday."
    }

    return state