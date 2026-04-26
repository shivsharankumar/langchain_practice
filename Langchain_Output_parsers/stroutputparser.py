# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


model=ChatOpenAI()


#1st prompt-> detailed report
template1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

#2nd prompt-> summmary
template2=PromptTemplate(
    template='Write a 5 line summary on the following text: {text}',
    input_variables=['text']
)

# prompt1=template1.format(topic="the impact of climate change on polar bears")
# response1=model.invoke(prompt1)

prompt1=template1.invoke({'topic': 'the impact of climate change on polar bears'})
response1=model.invoke(prompt1)

prompt2=template2.invoke({'text': response1.content})
response2=model.invoke(prompt2)
print(response2.content)