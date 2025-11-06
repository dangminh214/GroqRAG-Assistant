from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

def build_vector_db(texts): 
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_texts(
        texts, 
        embeddings,
        persist_directory="backend/db"
    )
    

