from app.graph.state import GraphState


def interaction_history(state: GraphState):
    """
    Return interaction history for an HCP.
    """

    state["response"] = [
        {
            "doctor": "Dr Sharma",
            "date": "2025-07-15",
            "summary": "Discussed diabetes medicine."
        },
        {
            "doctor": "Dr Sharma",
            "date": "2025-07-22",
            "summary": "Reviewed patient feedback."
        }
    ]

    return state