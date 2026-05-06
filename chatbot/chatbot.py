from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import ChatMessage, HumanMessage, SystemMessage, AIMessage

load_dotenv()

models=ChatOpenAI(model="gpt-5.4-nano",temperature=1.5)
chat_history=[
    SystemMessage(content="You are a helpful assistant"),
    
]
while True:
    user_input=input("You: ")
    # chat_history.append({"role": "user", "content": user_input})#it is identified by langchain and it will be used to generate response based on the user input and the previous conversation history
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    result = models.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    # chat_history.append({"role": "assistant", "content": result.content})
    print("Chatbot: ", result.content)
print("Chat history: ", chat_history)