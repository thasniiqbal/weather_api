import pytest
from services.outfit import outfit_recommendation

# Test data
test_data = [
    ({"current": {"temp_c": 40}},
     "It's scorching! Stick to light fabrics like cotton and wear a hat if you're stepping out."),
    ({"current": {"temp_c": 30}}, "Light clothing is advisable. Maybe a hat too!"),
    ({"current": {"temp_c": 20}}, "Time to bring out the jackets and scarves!")
]


@pytest.mark.parametrize("weather_data, expected_output", test_data)
def test_outfit_recommendation(weather_data, expected_output):
    result = outfit_recommendation(weather_data)
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"
