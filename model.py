from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import SecretStr
import os

load_dotenv()

model = ChatOpenAI(model="default", api_key=SecretStr(os.environ["LLM7_API_KEY"]), base_url="https://api.llm7.io/v1")
