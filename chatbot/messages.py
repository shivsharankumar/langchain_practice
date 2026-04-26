from langchain_core.messages import ChatMessage, HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

models=ChatOpenAI(model="gpt-5.4-nano",temperature=1.5)
chat_history=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about langchain")
]

result=models.invoke(chat_history)
print(result.content)
chat_history.append(AIMessage(content=result.content))
print("messages: ", chat_history)