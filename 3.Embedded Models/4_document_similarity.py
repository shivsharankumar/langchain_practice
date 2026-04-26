from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)
documents = [
    "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn. It is widely used in applications like chatbots, recommendation systems, and autonomous vehicles.",
    "Machine Learning is a subset of AI that focuses on building systems that learn from data. It includes supervised learning, unsupervised learning, and reinforcement learning techniques.",
    "Deep Learning is a specialized field within machine learning that uses neural networks with many layers. It is commonly used in image recognition, natural language processing, and speech recognition.",
    "Natural Language Processing (NLP) enables computers to understand, interpret, and generate human language. It is used in translation systems, sentiment analysis, and chatbots.",
    "Computer Vision is a field of AI that allows machines to interpret and make decisions based on visual data. Applications include facial recognition, object detection, and self-driving cars."
    ]

query="Explain machine learning types"

doc_embedding=embeddings.embed_documents(documents)
query_embedding=embeddings.embed_query(query)
similarity_scores=cosine_similarity([query_embedding],doc_embedding)[0]
index,score=sorted(list(enumerate(similarity_scores)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print(f"Similarity Score: {score}")
# queries = [
#     "What is artificial intelligence?",
#     "Explain machine learning types",
#     "How do neural networks work?",
#     "What is NLP used for?",
#     "How do computers understand images?"
# ]