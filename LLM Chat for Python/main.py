import os
import streamlit as st
import pickle       
import langchain
import time
from langchain_community.llms import Ollama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS

st.header("Chat with Web")

st.sidebar.markdown("URLS")

llm = Ollama(model="deepseek-r1:1.5b")

file_path = "New_vector_index.pkl"

list_urls = []

for i in range(3):
    url = st.sidebar.text_input(f"URL:- {i+1}")
    list_urls.append(url)
process_btn = st.sidebar.button("Process")


main_Input = st.empty()


if process_btn:

    #load Data from URLs
    load_url = UnstructuredURLLoader(urls=list_urls)
    
    main_Input.text("Loading Data... Please wait")
    main_Input.text("Processing Data... Please wait")

    data_url = load_url.load()


    #Split the Data 
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],
        chunk_size = 1000,
        chunk_overlap = 200
    )
    doc = splitter.split_documents(data_url)
    main_Input.text("Vectorizing Data... Please wait")
    time.sleep(2)


    #Create Embeddings
    embeding = OllamaEmbeddings(model="nomic-embed-text")
    main_Input.text("Vector Embeding Start... Please wait")
    New_vector_index = FAISS.from_documents(doc, embeding)      
    main_Input.text("Data Vectorizing Completed")

    #Save the Vector Index
    with open("New_vector_index.pkl", "wb") as f:   
        pickle.dump(New_vector_index, f)

    

User_Input = main_Input.text_input("Ask a question :")
if User_Input:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            New_Vector_DB = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm = llm, retriever = New_Vector_DB.as_retriever())
            results = chain({"question":User_Input}, return_only_outputs = True)
            st.header("Answer")
            st.subheader(results["answer"])
