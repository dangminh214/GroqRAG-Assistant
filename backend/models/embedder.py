from langchain_community.embeddings.spacy_embeddings import SpacyEmbeddings
import spacy
from nltk.stem import WordNetLemmatizer

def get_embedded(texts: list[str]):
    # Load spAcy english model 
    nlp = spacy.load("en_core_web_md")

    lemmatizer = WordNetLemmatizer()

    embeddings = []
    
    # Preprocess: lowercase + lemmatize each token
    for text in texts: 
        
        tokens = [lemmatizer.lemmatize(t.lower()) for t in text.split()]
        clean_text = " ".join(tokens)

        doc = nlp(clean_text)
        embeddings.append(doc.vector)

    return embeddings

