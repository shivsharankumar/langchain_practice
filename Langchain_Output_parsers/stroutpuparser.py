# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

parser=StrOutputParser()
chain=template1 | model | parser | template2 | model | parser
#frist we created parser object ab ham chain execute krenge to sabse pehle aa rha hai template 1
#template 1 mein user kuch bhej raha hai jiska topic hai "the impact of climate change on polar bears" to template 1 is topic ko leke ek prompt banayega aur usko model ko dega model us 
#   prompt ka response dega usko parser se pass karega jisse hume sirf text milega us text ko template 2 mein daal ke ek naya prompt banayega aur usko model ko dega model uska response dega aur usko parser se pass karega jisse hume sirf text milega
result=chain.invoke({'topic': 'the impact of climate change on polar bears'})
print(result)