#sentence-transformers/all-MiniLM-L6-v2

from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vector = embedding.embed_query("What is the capital of France?")
print(str(vector))


# documents=[
#     "Paris is the capital of France.",
#     "Berlin is the capital of Germany.",
#     "Madrid is the capital of Spain."
# ]
# result = embeddings.embed_documents(documents)
# for i, doc_embedding in enumerate(result):
#     print(f"Document {i + 1}: {str(doc_embedding)}")