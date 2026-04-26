from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
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
# Step 1: Define schema (clean & typed)
class FactSchema(BaseModel):
    fact1: str = Field(description="The first fact about the topic")
    fact2: str = Field(description="The second fact about the topic")
    fact3: str = Field(description="The third fact about the topic")
    fact4: str = Field(description="The fourth fact about the topic")
    fact5: str = Field(description="The fifth fact about the topic")
#old way of defining schema
# schema=[
#     ResponseSchema(name="fact1", description="The first fact about the topic"),
#     ResponseSchema(name="fact2", description="The second fact about the topic"),
#     ResponseSchema(name="fact3", description="The third fact about the topic"),
#     ResponseSchema(name="fact4", description="The fourth fact about the topic"),
#     ResponseSchema(name="fact5", description="The fifth fact about the topic")
# ]
# parser=StructuredOutputParser.from_response_schemas(schema)
# Step 3: Attach structured output
structured_llm = model.with_structured_output(FactSchema)
# template=PromptTemplate(
#     template='Give me 5 facts about {topic} \n {format_instruction}',
#     input_variables=['topic'],
#     partial_variables={'format_instruction': structured_llm.get_format_instructions() }#Return a JSON object
# )
# prompt=template.invoke({"topic": "Python programming"})
prompt=f"Give me 5 facts about Python programming"
print(prompt)
result=structured_llm.invoke(prompt)
print(result)
# final_result=structured_llm.parse(result.content)
# print(final_result)
# print(type(final_result))
# chain=template | model | structured_llm
# result=chain.invoke({'topic': 'Python programming'})# but 
