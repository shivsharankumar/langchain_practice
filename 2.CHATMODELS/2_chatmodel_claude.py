from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os   

load_dotenv()

model=ChatAnthropic(model="claude-haiku-4-5",temperature=0.9)
result = model.invoke("write a 5 line poem on cricket?")
print(result.content)