from dotenv import load_dotenv
import os

# Load the file .env
load_dotenv(dotenv_path=".env")

# Required keys list
required_keys = [
    "OPENAI_API_KEY",
    "LANGCHAIN_API_KEY",
    #"TAVILY_API_KEY",
    #"HUGGINGFACEHUB_API_TOKEN"
]

# Check if all the required keys are present
missing_keys = [key for key in required_keys if not os.getenv(key)]
if missing_keys:
    raise ValueError(f"Faltan las siguientes claves en el archivo .env: {', '.join(missing_keys)}")

print("Todas las claves necesarias están configuradas.")
