from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
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
parser=JsonOutputParser()
template=PromptTemplate(
    # template='Give the name ,age and  city of fictional person \n {format_instruction}',
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions() }#Return a JSON object.
)
# prompt=template.format()

# print(prompt)
# result=model.invoke(prompt)
# print(result)

# final_result=parser.parse(result.content)
# print(final_result)
# print(type(final_result))
chain=template | model | parser
result=chain.invoke({'topic': 'Python programming'})# but we cannot do it like {'fact1: "..." , "fact2": "..." ...} because the output parser will take care of that for us. We just need to give the topic and the output parser will return a JSON object with the facts.
print(result)
