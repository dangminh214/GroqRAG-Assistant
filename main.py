from backend.models.model import load_llm_model
from backend.utils import send_message_to_agent
from backend.config import GROQ_KEY, OPENAI_API_KEY
from backend.models.embedder import get_embedded
import numpy as np


assert GROQ_KEY, "Missing GROQ_KEY in .env file"


def main():
    agent = load_llm_model(
        model="llama-3.1-8b-instant", 
        key=GROQ_KEY
    )

    texts = ["what is the weather today in sf ?", 
             "how is the weather in San Francisco today?"]
    
    embeddings = get_embedded(texts)

    # Cosine similarity
    similarity = (np.dot(embeddings[0], embeddings[1]) / 
                  (np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1])))
    
    print("Embedding vector size:", len(embeddings[0]))
    print("Cosine similarity between texts:", similarity)

    for prompt in texts:
        response = send_message_to_agent(agent, prompt=prompt)

        # Accesss the main data
        print(response["messages"][2].content) 


if __name__=="__main__":
    main()



