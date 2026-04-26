from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()


model1=ChatOpenAI()
model2= ChatGroq(
    model="llama-3.1-8b-instant", # Groq hosts Gemma!
)
parser=StrOutputParser()
class FeedbackSentiment(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="The sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=FeedbackSentiment)
prompt1=PromptTemplate(
    template='classify the sentiment of the following feedback text into positive, negative \n  {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions() }
)

classifier_chain=prompt1 | model2 | parser2
# result=classifier_chain.invoke({'feedback': 'This is a terrible smartphone with a very bad battery life.'}).sentiment
# print(result)
prompt2=PromptTemplate(
    template='write an appropiate response to this positive feedback \n  {feedback}',
    input_variables=['feedback']
)
prompt3=PromptTemplate(
    template='write an appropiate response to this negative feedback \n  {feedback}',
    input_variables=['feedback']
)
branch_chain=RunnableBranch(
    # (condition1,chain1),
    # (condition2,chain2),
    # default
    (lambda x:x.sentiment == 'positive', prompt2 | model1 | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model1 | parser),
    RunnableLambda(lambda x: "Sorry, I couldn't classify the sentiment of the feedback.")
)

#merge classifier chain and branch chain''

chain=classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a terrible smartphone with a very bad battery life.'}))
chain.get_graph().print_ascii()