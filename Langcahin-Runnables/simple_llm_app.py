from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model=OpenAI(model_name='gpt-3.5-turbo-instruct',temperature=0.7)

prompt=PromptTemplate(
    input_variables=['topic'],
    template='Suggest a catchy title for a blog post about {topic}'
)
#define input

topic=input('Enter a topic for the blog post: ')

#format the prompt manually using prompttemplate
formatted_prompt=prompt.format(topic=topic)

#call the LLM directly
blog_title=model.invoke(formatted_prompt)

#print the output
print(f'Catchy title for the blog post: {blog_title}')