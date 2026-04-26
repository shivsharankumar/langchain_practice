from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import ChatMessage, HumanMessage, SystemMessage, AIMessage

chat_template=ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert"),
    ('human', "Explain in simple terms, what is {topic}?")
])

prompt=chat_template.invoke({'domain': 'cricket', 'topic': 'Dusra'})
print(prompt)