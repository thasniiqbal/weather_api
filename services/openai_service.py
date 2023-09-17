import openai
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def generate_funny_summary(weather_data):
    temperature = weather_data["current"]["temp_c"]
    weather_description = weather_data["current"]["condition"]["text"]
    prompt = f"Provide a funny summary for the weather. It's currently {temperature}°C with {weather_description}."
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=100)
    return response.choices[0].text.strip()
