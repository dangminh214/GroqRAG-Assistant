from langchain_core.tools import tool 
import requests


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