# GroqRAG-Assistant

## Personal Project: RAG (Retrieval-Augmented Generation) Prototype

**GroqRAG-Assistant** is a personal project exploring **Retrieval-Augmented Generation (RAG)**, a hybrid approach combining retrieval-based methods with large language models (LLMs) to enhance question answering and text generation. The goal is to build a prototype pipeline where an LLM can access relevant contextual documents through semantic search, improving the accuracy and relevance of its responses.

---

## Project Focus

1. **Document Embedding:** Convert text into semantic vectors using **spaCy**.  
2. **Vector Store:** Implement **FAISS** for similarity-based retrieval of document embeddings.  
3. **LLM Integration:** Connect retrieved documents to an LLM (GROQ Basic model) for answering user queries.

---

## Current State

The project is actively under development. Current progress includes:

- **LLM Integration:**  
  - Working on connecting the pipeline with the **GROQ Basic model**.  
- **NLP Preprocessing & Embedding:**  
  - Implemented text preprocessing (lowercasing and lemmatization).  
  - Using **spaCy embeddings** to convert text into semantic vectors.  
- **Vector Database:**  
  - Setting up **FAISS** to store document embeddings.  
  - Implemented **cosine similarity** for semantic search and retrieval.  
- **Pipeline Testing:**  
  - Able to embed documents and perform basic retrieval for testing purposes.

### Next Steps

- **@tool Integration:**  
  - Add tools to enhance model capabilities and interact efficiently with the vector database.  
- **Enhanced Retrieval & Ranking:**  
  - Support multi-document retrieval and improved ranking strategies.  
- **RAG Pipeline Completion:**  
  - Fully integrate retrieval and LLM response generation for interactive question answering.

---

## Requirements & Installation

### System Requirements

- Python >= 3.10  
- pip >= 23.0  
- At least 4GB RAM (more recommended for LLM experiments)  
- Internet connection (for spaCy models and dependencies)

### Python Dependencies

Key Python packages:

- **Core NLP & Embedding:** `spacy`, `nltk`, `en_core_web_md`  
- **RAG & LLM Integration:** `langchain`, `langchain-community`, `langchain-groq`, `groq`  
- **Vector Database:** `faiss` (via `langchain` integrations)  
- **Utilities:** `numpy`, `tqdm`, `python-dotenv`, `requests`, `orjson`  
- **Other Dependencies:** see full list in `requirements.txt`

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/dangminh214/GroqRAG-Assistant.git
cd GroqRAG-Assistant
```

2. Create and activate a virtual environment
```bash 
python -m venv venv
# Activate on Linux/macOS
source venv/bin/activate
# Activate on Windows
venv\Scripts\activate
```

3. Install Python dependencies
```bash 
pip install --upgrade pip
pip install -r requirements.txt
```

4. Set up Groq key
```bash 
GROQ_KEY=<your-groq-api-key>
```

5. Run the script 
```bash 
python main.py
```

