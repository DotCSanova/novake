from .state import State
from langgraph.graph import END
from langchain_core.messages import SystemMessage, HumanMessage, RemoveMessage
from langchain_core.runnables.config import RunnableConfig
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import os, getpass

models = {
    "openai": ChatOpenAI(model="gpt-4o", temperature=0),
    "ollama": ChatOllama(model="llama3.2", temperature=0)
}

def _call_model(state: State, config: RunnableConfig):

    model_name = config["configurable"].get("model", "openai")
    model = models[model_name]
    response = model.invoke(state["messages"])

    return {"messages": [response]}
