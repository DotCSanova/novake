from langgraph.graph import END, StateGraph, START
from novake_agent.utils import State, _call_model

builder = StateGraph(State)

builder.add_node("model",_call_model)
builder.add_edge(START, "model")
builder.add_edge("model", END)
graph = builder.compile()