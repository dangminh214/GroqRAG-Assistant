from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

# Load documents
loader = TextLoader("../sample.txt")
documents = loader.load()

# Split documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)