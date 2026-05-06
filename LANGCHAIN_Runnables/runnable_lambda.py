#normal python fucntion to Runnable
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_groq import ChatGroq
load_dotenv()
def count_words(response):
    return len(response.split())

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
    'joke_len':RunnableLambda(count_words)

})
final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
result=final_chain.invoke({'topic':'joker'})
print(result)