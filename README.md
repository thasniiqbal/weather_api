# Weather API with Activity & Outfit Recommendations

This FastAPI project provides real-time weather data, generates a funny summary using OpenAI's API, and offers activity and outfit recommendations based on the current weather for a given city.

## 📂 Project Structure

- `weather_api/`: The root directory of the project.

    - `main.py`: The entry point for your FastAPI app.

- `api/`: Contains endpoint functions and logic.

    - `weather.py`: Logic related to weather data endpoints.

- `services/`: Contains various services and logic used by the app.

    - `fetcher.py`: Logic for fetching data from the WeatherAPI.

    - `openai_service.py`: Logic for interacting with OpenAI to generate funny summaries.

    - `activity.py`: Logic for activity recommendations.

    - `outfit.py`: Logic for outfit recommendations.

- `tests/`: Contains test cases for the project.

    - `test_weather.py`: Tests related to weather functionality.

    - `test_activity.py`: Tests related to activity recommendations.

    - `test_outfit.py`: Tests related to outfit recommendations.

- `requirements.txt`: Lists the main project dependencies.

- `test_requirements.txt`: Lists the testing-specific dependencies.



## 🔧 Setup

### Environment Variables

Before starting the application, make sure to set up the necessary environment variables:

- `WEATHER_API_KEY`: Your WeatherAPI key.
- `OPENAI_API_KEY`: Your OpenAI API key.

### Dependencies

1. Install the primary project dependencies:

```bash
pip install -r requirements.txt
```

2. For testing purposes, install the testing dependencies:

```bash
pip install -r test_requirements.txt
```

## ▶ Running the API

Start the API server with the following command:

uvicorn main:app --reload

## 🧪 Testing

`pytest` is the chosen framework for testing to validate code reliability and to guard against potential issues.

To run the tests, simply execute:

```bash
pytest
```
