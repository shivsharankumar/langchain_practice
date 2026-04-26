from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-3-1b-it",
#     task="text-generation"
# )
# llm = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen2.5-1.5B-Instruct", 
#     task="text-generation",
#     max_new_tokens=256,
#     # Reads HUGGINGFACEHUB_API_TOKEN from your environment.
# )
model= ChatGroq(
    model="llama-3.1-8b-instant", # Groq hosts Gemma!
)
# model=ChatHuggingFace(llm=llm)
# print(model)

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age",gt=18)
    city: str = Field(description="The city where the person lives")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='Give the name ,age and  city of fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions() }#Return a JSON object.
)
# prompt=template.invoke({'place': 'Indian'})
# print(prompt)
# result=model.invoke(prompt)
# # print(result.content)
# final_result=parser.parse(result.content)
# print(final_result)
chain=template | model | parser
result=chain.invoke({'place': 'Pakistani'})
print(result)
