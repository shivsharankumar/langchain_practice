from langchain_community.llms import OpenAI
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
llm=OpenAI(model_name='gpt-3.5-turbo-instruct',temperature=0.7)
#create a prompt
prompt=PromptTemplate(
    input_variables=['topic'],
    template='Suggest a catchy title for a blog post about {topic}'
)
# create a chain
chain=LLMChain(llm=llm,prompt=prompt)

#run the chain with specific topic
topic=input('Enter a topic')
output=chain.run(topic)
print(f'Catchy title for the blog post: {output}')