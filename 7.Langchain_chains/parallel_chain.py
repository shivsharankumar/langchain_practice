from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_groq import ChatGroq

load_dotenv()


model1=ChatOpenAI()
model2= ChatGroq(
    model="llama-3.1-8b-instant", # Groq hosts Gemma!
)

prompt1=PromptTemplate(
    template='Generate short and simple notes from the following text \n  {text}',
    input_variables=['text']
)
prompt2=PromptTemplate(
    template='Generate 5 short question answers from the following text \n  {text}',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} \n quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser=StrOutputParser()

# parallel_chain=RunnableParallel(
#     runnables=[
#         prompt1 | model1 | parser,
#         prompt2 | model2 | parser
#     ],
#     input_variables=['text']
# )
parallel_chain=RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merging_chain=prompt3 | model1 | parser

chain=parallel_chain | merging_chain

result=chain.invoke({'text': 'Climate change is a long-term change in the average weather patterns that have come to define Earth’s local, regional and global climates. These changes have a broad range of observed effects that are synonymous with the term. Climate change is primarily caused by human activities such as burning fossil fuels, deforestation, and industrial processes, which release greenhouse gases into the atmosphere. The consequences of climate change include rising sea levels, more frequent and severe weather events, loss of biodiversity, and impacts on agriculture and human health.'})

print(result)

chain.get_graph().print_ascii()