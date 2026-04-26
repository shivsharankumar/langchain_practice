from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
documents=[
    "Paris is the capital of France.",
    "Berlin is the capital of Germany.",
    "Madrid is the capital of Spain."
]
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
result = embeddings.embed_documents(documents)
for i, doc_embedding in enumerate(result):
    print(f"Document {i + 1}: {str(doc_embedding)}")