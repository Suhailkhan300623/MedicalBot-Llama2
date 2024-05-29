from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

#data Loader
def pdf_loder(data):
    loader=DirectoryLoader(data, glob='*.pdf', loader_cls=PyPDFLoader)
    doc=loader.load()
    return doc


# Chunks
def chunks(ext_data):
    text=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    chunk=text.split_documents(ext_data)
    return chunk


#embedding
def hf_embedding():
    embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model


