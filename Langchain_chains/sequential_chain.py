from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1=PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)
model=ChatOpenAI()

prompt2=PromptTemplate(
    template='Summarize the following report in 5 bullet points:\n{report}',
    input_variables=['report']
)

parser=StrOutputParser()

chain=prompt1 | model | parser | prompt2 | model | parser

result=chain.invoke({'topic': 'Climate Change'})
print(result)