from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_groq import ChatGroq
load_dotenv()

prompt1=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()

prompt2=PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)
passthrough=RunnablePassthrough()
model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)
parser=StrOutputParser()
joke_gen_chain=RunnableSequence(prompt1,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination':RunnableSequence(prompt2,model,parser)

})
final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
result=final_chain.invoke({'topic':'cricket'})
print(result)