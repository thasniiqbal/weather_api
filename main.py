from fastapi import FastAPI
from api import weather

# Create FastAPI instance
app = FastAPI()

# Include weather router in the application
app.include_router(weather.router)
