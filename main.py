from backend.models.model import load_llm_model
from backend.utils import send_message_to_agent
from backend.config import GROQ_KEY, OPENAI_API_KEY

assert GROQ_KEY, "Missing GROQ_KEY in .env file"


def main():
    agent = load_llm_model(
        model="llama-3.1-8b-instant", 
        key=GROQ_KEY
    )

    user_prompt = "what is the weather today in sf ?"


    response = send_message_to_agent(agent, prompt=user_prompt)


    # Accesss the main data
    print(response["messages"][2].content) 


if __name__=="__main__":
    main()



