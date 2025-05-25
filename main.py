from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
from typing import Optional

app = FastAPI(title="Weather API", description="A simple weather API that returns random weather data")

# Weather conditions and temperatures
WEATHER_CONDITIONS = [
    "sunny", "cloudy", "rainy", "snowy", "foggy", "windy", "stormy", "partly cloudy"
]

TEMPERATURE_RANGES = {
    "sunny": (20, 35),
    "cloudy": (15, 25),
    "rainy": (10, 20),
    "snowy": (-10, 5),
    "foggy": (5, 15),
    "windy": (10, 25),
    "stormy": (5, 20),
    "partly cloudy": (15, 28)
}

class WeatherResponse(BaseModel):
    city: str
    temperature: int
    condition: str
    humidity: int
    wind_speed: int

@app.get("/")
async def root():
    return {"message": "Welcome to the Weather API! Use /weather/{city} to get weather data."}

@app.get("/weather/{city}", response_model=WeatherResponse)
async def get_weather(city: str):
    """Get random weather data for a given city"""
    if not city or len(city.strip()) == 0:
        raise HTTPException(status_code=400, detail="City name cannot be empty")
    
    # Generate random weather data
    condition = random.choice(WEATHER_CONDITIONS)
    temp_min, temp_max = TEMPERATURE_RANGES[condition]
    temperature = random.randint(temp_min, temp_max)
    humidity = random.randint(30, 90)
    wind_speed = random.randint(5, 30)
    
    return WeatherResponse(
        city=city.title(),
        temperature=temperature,
        condition=condition,
        humidity=humidity,
        wind_speed=wind_speed
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 