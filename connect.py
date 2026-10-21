import os

from dotenv import load_dotenv

# from langchain_openai import ChatOpenAI
# from langchain_groq import ChatGroq
from langchain_openrouter import ChatOpenRouter

load_dotenv()

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")


def llmconnect():
    return ChatOpenRouter(model="poolside/laguna-s-2.1:free")
