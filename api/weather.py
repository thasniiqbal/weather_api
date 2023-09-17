from fastapi import APIRouter
from services import fetcher, openai_service, activity, outfit

router = APIRouter()


@router.get("/weather/{city}")
async def get_weather(city: str):
    weather_data = await fetcher.fetch_weather_data(city)
    if "error" in weather_data:
        return weather_data

    funny_summary = openai_service.generate_funny_summary(weather_data)
    activity_rec = activity.activity_recommendation(weather_data)
    outfit_rec = outfit.outfit_recommendation(weather_data)

    return {
        "city": city,
        "weather_summary": funny_summary,
        "activity_recommendation": activity_rec,
        "outfit_recommendation": outfit_rec
    }
