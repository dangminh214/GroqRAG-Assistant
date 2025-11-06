from json import tool
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from pydantic import SecretStr
import requests
from langchain.agents import create_agent
from langchain_core.tools import tool 


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_KEY")
GROQ_KEY = os.getenv("GROQ_KEY") # I use free model Groq

assert GROQ_KEY, "Missing GROQ_KEY in .env file"


@tool
def get_weather(city: str) -> str:
    """Get real weather information from Open-Meteo."""
    cities = {
        "paris": (48.8566, 2.3522),
        "sf": (37.7749, -122.4194),
        "hanoi": (21.0285, 105.8542)
    }
    lat, lon = cities.get(city.lower(), (37.7749, -122.4194))
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    r = requests.get(url).json()
    temp = r["current_weather"]["temperature"]
    desc = r["current_weather"]["weathercode"]
    return f"The current temperature in {city} is {temp}°C (code {desc})."


groq_model = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=SecretStr(GROQ_KEY)
)

groq_agent = create_agent(
    model=groq_model, 
    tools=[get_weather],  
    system_prompt="You are a helpful assistant that can answer questions and provide weather information.",
)

def send_message_to_agent(agent, prompt: str):
    messages = {
        "messages": [
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ]
    }

    response = agent.invoke(messages)
    return response


user_prompt = "what is the weather today in hanoi ?"

response = send_message_to_agent(groq_agent, prompt=user_prompt)

print(response)