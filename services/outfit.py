def outfit_recommendation(weather_data):
    temperature = weather_data["current"]["temp_c"]
    if temperature > 35:
        return "It's scorching! Stick to light fabrics like cotton and wear a hat if you're stepping out."
    elif temperature > 25:
        return "Light clothing is advisable. Maybe a hat too!"
    else:
        return "Time to bring out the jackets and scarves!"
