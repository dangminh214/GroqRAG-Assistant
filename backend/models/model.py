from pydantic import SecretStr
from langchain.agents import create_agent
from backend.tools import get_weather
from langchain_groq import ChatGroq


def load_llm_model(model: str, key: str): 
    groq_model = ChatGroq(
        model=model,
        api_key=SecretStr(key)
    )

    groq_agent = create_agent(
        model=groq_model, 
        tools=[get_weather],  
        system_prompt="You are a helpful assistant that can answer questions and provide weather information.",
    )

    return groq_agent