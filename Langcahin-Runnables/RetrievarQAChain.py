from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI
from langchain_classic.chains import retrieval_qa
#load the documents
loader=TextLoader('sample.txt')
documents=loader.load()

#split the text into smaller chunks 
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
texts=text_splitter.split_documents(documents)

#convert text into vector embeddings and store in FAISS
vectorstore=FAISS.from_documents(texts,OpenAIEmbeddings())

#create a retriever fetch relevant documents based on a query
retriever = vectorstore.as_retriever()

# #manually retriever relevant documents
query='What is the main topic of the text?'
# relevant_docs=retriever.get_relevant_documents(query)

# # combine retrieved text into single prompt
# retrieved_text='\n'.join([doc.page_content for doc in relevant_docs])

llm=OpenAI(model_name='gpt-3.5-turbo-instruct',temperature=0.7)
#create retrieval qa chain
qa_chain=retrieval_qa.RetrievalQA.from_chain_type(llm=llm,retriever=retriever)
#manually pass retrieved text to llm

prompt=f"Based on the following text, answer the question: {query}\n\n{retrieved_text}"
answer=qa_chain.run(query)

# print the answer
print(f'Answer: {answer}')