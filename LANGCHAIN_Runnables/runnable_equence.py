from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_aws import ChatBedrock
# from model_call import get_llm
from langchain_groq import ChatGroq
load_dotenv()


# ---- Get model (THIS is what you wanted) ----
# model = get_llm("llama")   # or "openai"
model=ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)
prompt1=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)
# model=ChatOpenAI()
parser=StrOutputParser()

prompt2=PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)
chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)
print(chain.invoke({'topic':'pizza'}))x