from langgraph.graph import StateGraph, END

from app.graph.state import GraphState
from app.graph.nodes import (
    detect_intent,
    save_interaction,
    generate_summary,
)
from app.graph.router import route


workflow = StateGraph(GraphState)

workflow.add_node("intent", detect_intent)
workflow.add_node("save", save_interaction)
workflow.add_node("summary", generate_summary)

workflow.set_entry_point("intent")

workflow.add_conditional_edges(
    "intent",
    route,
    {
        "save": "save",
        "summary": "summary",
    },
)

workflow.add_edge("save", END)
workflow.add_edge("summary", END)

graph = workflow.compile()