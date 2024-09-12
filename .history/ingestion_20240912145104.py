import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def ingest_docs():
    loader = ReadTheDocsLoader(:

if __name__ == "__main__":
   ingest_docs()
   loader = 