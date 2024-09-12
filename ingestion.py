import os
from dotenv import load_dotenv, find_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv(find_dotenv())

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def ingest_docs():
    """
    Ingest documents from ReadTheDocs and store them in Pinecone.
    """
    loader = ReadTheDocsLoader(
        './langchain-docs/api.python.langchain.com/en/latest/'
    )
    raw_documents = loader.load()
    print(f"loaded {len(raw_documents)} documents")


if __name__ == "__main__":
    ingest_docs()