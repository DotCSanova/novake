from novake_agent import graph
from langchain_core.messages import HumanMessage
import os, getpass
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

def _set_env(var: str):

    # Check if the variable is set in the OS environment
    env_value = os.environ.get(var)
    if not env_value:
        # If not set, prompt the user for input
        env_value = getpass.getpass(f"{var}: ")
    
    # Set the environment variable for the current process
    os.environ[var] = env_value

def main():

    print("Hello from novake!")
    config = {"configurable": {"model": "openai"}}
    input_messages = [HumanMessage(content="how many days are in a week?")]
    for chunk in graph.stream({"messages": input_messages}, config, stream_mode="values"):
        chunk["messages"][-1].pretty_print()


if __name__ == "__main__":

    main()
