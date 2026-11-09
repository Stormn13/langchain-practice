from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import SecretStr
import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage



load_dotenv()

model = ChatOpenAI(model="default", api_key=SecretStr(os.environ["LLM7_API_KEY"]), base_url="https://api.llm7.io/v1")

chat_history: list[SystemMessage | HumanMessage | AIMessage] = [
    SystemMessage(content="you are a helpful chat assistant")
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    else:
        result = model.invoke(chat_history)
        print("AI: ", result.content)
        chat_history.append(AIMessage(content=result.content))