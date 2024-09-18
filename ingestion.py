import os


from dotenv import load_dotenv, find_dotenv

from langchain_community.document_loaders import ReadTheDocsLoader

from langchain_openai import OpenAIEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_pinecone import PineconeVectorStore

_ = load_dotenv(find_dotenv())

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
_ = len(os.listdir('./langchain-docs/api.python.langchain.com/en/latest/')) > 0


def ingest_docs():
    """
    Ingest documents from ReadTheDocs and store them in Pinecone.
    """
    docs_path = './langchain-docs/api.python.langchain.com/en/latest/'
    loader = ReadTheDocsLoader(
        docs_path
    )
    raw_documents = loader.load()
    print(f"loaded {len(raw_documents)} documents")
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)
    
    for doc in documents:
        new_url = doc.metadata["source"]
        new_url = new_url.replace("langchain-docs", "https:/")
        doc.metadata.update({"source": new_url})

    print(f"Going to add {len(documents)} to Pinecone")
    PineconeVectorStore.from_documents(
        documents, embeddings, index_name="langchain-doc-index"
    )

        
if __name__ == "__main__":
    ingest_docs()
