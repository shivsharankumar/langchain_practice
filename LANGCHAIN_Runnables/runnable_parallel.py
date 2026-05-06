from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel
from langchain_groq import ChatGroq
load_dotenv()

prompt1=PromptTemplate(
    template='Generate a tweet about a {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='Generate a Linkedin post about a {topic}',
    input_variables=['topic']
)

model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)
parser=StrOutputParser()
parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)

})

result=parallel_chain.invoke({'topic':'AI'})
print(result)