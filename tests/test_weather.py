from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_weather_endpoint():
    response = client.get("/weather/Dubai")
    assert response.status_code == 200
    data = response.json()
    assert "weather_summary" in data
    assert "activity_recommendation" in data
    assert "outfit_recommendation" in data
