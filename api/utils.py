from django.conf import settings
import random
from datetime import datetime
import requests

def get_mock_data():
    mock_data = {
        "sensor_id": "phewa-001",
        "timestamp": datetime.now(),  
        "air_quality_index": random.randint(50, 200), 
        "water_quality_index": random.randint(20, 50), 
        "ph_level": round(random.uniform(6.5, 8.5), 1)  
    }
    return mock_data

def get_weather_data():
    try:
        response = requests.get(settings.OPEN_WEATHER_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return None

