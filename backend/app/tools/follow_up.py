from app.graph.state import GraphState


def generate_follow_up(state: GraphState):
    """
    Generate follow-up recommendations.
    """

    state["response"] = {
        "next_action": "Schedule a visit next Monday.",
        "questions_to_ask": [
            "How are patients responding to the medicine?",
            "Any challenges with the current treatment?"
        ],
        "material_to_carry": [
            "Diabetes brochure",
            "Product samples"
        ]
    }

    return state
