#to create conditional chain

#normal python fucntion to Runnable
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch
from langchain_groq import ChatGroq
load_dotenv()
def count_words(response):
    return len(response.split())

prompt1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()

prompt2=PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)
passthrough=RunnablePassthrough()
model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)
parser=StrOutputParser()
report_gen_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>250,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)
final_chain=RunnableSequence(report_gen_chain,branch_chain)
# parallel_chain=RunnableParallel({
#     'joke':RunnablePassthrough(),
#     'joke_len':RunnableLambda(count_words)

# })
# final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
result=final_chain.invoke({'topic':'Russia vs Ukraine'})
print(result)