import pytest
from services.activity import activity_recommendation

# Test data
test_data = [
    ({"current": {"temp_c": 40}},
     "Great day to stay indoors and enjoy some coding or a movie marathon!"),
    ({"current": {"temp_c": 30}}, "Nice day for a walk or outdoor sports!"),
    ({"current": {"temp_c": 20}}, "Maybe a cup of hot cocoa and a book indoors?")
]


@pytest.mark.parametrize("weather_data, expected_output", test_data)
def test_activity_recommendation(weather_data, expected_output):
    result = activity_recommendation(weather_data)
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"
