from app.graph.state import GraphState


def get_hcp_summary(state: GraphState):
    """
    Generate overall HCP summary.
    """

    state["response"] = {
        "doctor": "Dr Sharma",
        "overall_summary": (
            "Dr Sharma is interested in diabetes products and "
            "prefers monthly follow-up meetings."
        )
    }

    return state