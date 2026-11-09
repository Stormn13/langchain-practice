from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import SecretStr
import os


load_dotenv()

model = ChatOpenAI(model="default", api_key=SecretStr(os.environ["LLM7_API_KEY"]), base_url="https://api.llm7.io/v1")

chat_history = []

while True:
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    else:
        result = model.invoke(chat_history)
        print("AI: ", result.content)
        chat_history.append(result.content)