def activity_recommendation(weather_data):
    temperature = weather_data["current"]["temp_c"]
    if temperature > 35:
        return "Great day to stay indoors and enjoy some coding or a movie marathon!"
    elif temperature > 25:
        return "Nice day for a walk or outdoor sports!"
    else:
        return "Maybe a cup of hot cocoa and a book indoors?"
