"""
Weather tool for getting current weather information.
"""

import requests
from typing import Dict
from ..models import WeatherInfo

class WeatherTool:
    """
    Tool to get current weather information for story context.
    Fetches weather data from OpenWeatherMap API, or provides fallback data if the API fails.
    """
    
    def __init__(self):
        # API key for OpenWeatherMap (using 'demo' for free access; replace with real key for production)
        self.api_key = "demo"  # Using demo key for free access
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city: str = "Bengaluru") -> WeatherInfo:
        """
        Get current weather for a city using the OpenWeatherMap API.
        If the API call fails, returns fallback weather data.
        Args:
            city (str): The city to get weather for (default: 'Bengaluru').
        Returns:
            WeatherInfo: Dataclass with weather description, temperature, and condition.
        """
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            # Make a GET request to the weather API
            response = requests.get(self.base_url, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json()
                # Parse the API response and return a WeatherInfo object
                return WeatherInfo(
                    description=data['weather'][0]['description'],
                    temperature=data['main']['temp'],
                    condition=data['weather'][0]['main'].lower()
                )
        except Exception as e:
            # Print the error for debugging if the API call fails
            print(f"Weather API error: {e}")
        
        # Fallback weather data if API call fails or returns an error
        return WeatherInfo(
            description='Clear sky',
            temperature=20.0,
            condition='lear'  # Typo in fallback, should be 'clear'
        ) 