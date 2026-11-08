from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from pydantic import SecretStr

load_dotenv()


llm = ChatOpenAI(model="default", api_key=SecretStr(os.environ["LLM7_API_KEY"]), base_url="https://api.llm7.io/v1")

result = llm.invoke("hi how are you?")

print(result.content)

#this is a chatbot model not an llm demo because llm7 doesn't support the llms only chatbots
 