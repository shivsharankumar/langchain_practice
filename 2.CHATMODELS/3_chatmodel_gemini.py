from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os   

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-3-flash-preview",temperature=0.9)
result = model.invoke("write a 5 line poem on cricket?")
print(result.content)   