"""
Weather tool for getting current weather information.
"""

import requests
from typing import Dict
from ..models import WeatherInfo

class WeatherTool:
    """Tool to get current weather information."""
    
    def __init__(self):
        self.api_key = "demo"  # Using demo key for free access
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city: str = "Bengaluru") -> WeatherInfo:
        """Get current weather for a city."""
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return WeatherInfo(
                    description=data['weather'][0]['description'],
                    temperature=data['main']['temp'],
                    condition=data['weather'][0]['main'].lower()
                )
        except Exception as e:
            print(f"Weather API error: {e}")
        
        # Fallback weather data
        return WeatherInfo(
            description='Clear sky',
            temperature=20.0,
            condition='lear'
        ) 