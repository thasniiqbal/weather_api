import httpx
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"


async def fetch_weather_data(city: str):
    if not city or not city.strip():
        return {"error": "City name is required and cannot be empty"}

    async with httpx.AsyncClient() as client:
        params = {
            "q": city,
            "key": WEATHER_API_KEY,
            "aqi": "no"
        }
        response = await client.get(BASE_URL, params=params)

        if response.status_code != 200:
            # Check for specific status codes if necessary
            if response.status_code == 400:
                return {"error": "City not found."}
            else:
                return {"error": f"Failed to fetch data from WeatherAPI with status code: {response.status_code}"}

        # If the status code is 200, but there's no 'current' key in the data, then it's unexpected
        data = response.json()
        if "current" not in data:
            return {"error": "Unexpected response from WeatherAPI."}

        return data
