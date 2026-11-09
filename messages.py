from model import model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

messages = [
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content='tell me about langchain')
]


print(model.invoke(messages).content)
