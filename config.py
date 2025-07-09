"""
Configuration settings for the Bedtime Story Generator.
"""

import os
from typing import Dict, List

class Config:
    """Configuration class for the application."""
    
    # Application settings
    APP_NAME = "Bedtime Story Generator"
    APP_VERSION = "1.0.0"
    APP_ICON = "🌙"
    
    # Streamlit settings
    STREAMLIT_PAGE_TITLE = "Bedtime Story Generator"
    STREAMLIT_PAGE_ICON = "🌙"
    STREAMLIT_LAYOUT = "wide"
    STREAMLIT_SIDEBAR_STATE = "expanded"
    
    # AI Model settings
    HUGGINGFACE_MODEL = "microsoft/DialoGPT-medium"
    MODEL_TEMPERATURE = 0.8
    MODEL_MAX_LENGTH = 500
    
    # Weather API settings
    WEATHER_API_KEY = "demo"  # Using demo key for free access
    WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    DEFAULT_CITY = "London"
    
    # Age settings
    MIN_AGE = 2
    MAX_AGE = 12
    DEFAULT_AGE = 6
    
    # Story length options
    STORY_LENGTHS = {
        "short": "Short (5 min)",
        "medium": "Medium (10 min)", 
        "long": "Long (15 min)"
    }
    
    # Mood options
    MOOD_OPTIONS = {
        "😊 Happy": "happy and cheerful",
        "🌟 Excited": "excited and energetic", 
        "😴 Sleepy": "sleepy and calm",
        "🤔 Curious": "curious and thoughtful",
        "😌 Peaceful": "peaceful and relaxed",
        "🎉 Adventurous": "adventurous and brave"
    }
    
    # Interest options
    INTEREST_OPTIONS = [
        "🐾 Animals", "🚀 Space", "👑 Princesses", "🦸 Superheroes", 
        "🌳 Nature", "🏰 Castles", "🐉 Dragons", "🧚 Fairies",
        "🌊 Ocean", "🏔️ Mountains", "🌺 Flowers", "⭐ Stars"
    ]
    
    # Color options
    COLOR_OPTIONS = [
        "pink", "blue", "purple", "green", "yellow", "orange", "red", "rainbow"
    ]
    
    # Content filtering
    INAPPROPRIATE_WORDS = [
        'scary', 'frightening', 'terrifying', 'horror', 'nightmare',
        'dangerous', 'violent', 'angry', 'hate', 'kill', 'death',
        'darkness', 'evil', 'wicked', 'mean', 'cruel'
    ]
    
    REPLACEMENT_WORDS = {
        'scary': 'exciting',
        'frightening': 'amazing',
        'terrifying': 'wonderful',
        'horror': 'adventure',
        'nightmare': 'dream',
        'dangerous': 'exciting',
        'violent': 'energetic',
        'angry': 'determined',
        'hate': 'dislike',
        'kill': 'help',
        'death': 'sleep',
        'darkness': 'twilight',
        'evil': 'mischievous',
        'wicked': 'playful',
        'mean': 'silly',
        'cruel': 'funny'
    }
    
    # UI Colors
    COLORS = {
        'primary': '#FF6B9D',
        'secondary': '#667eea',
        'accent': '#764ba2',
        'gradient_start': '#f093fb',
        'gradient_end': '#f5576c'
    }
    
    # Session state keys
    SESSION_KEYS = {
        'story_generated': 'story_generated',
        'current_story': 'current_story',
        'child_preferences': 'child_preferences'
    }
    
    @classmethod
    def get_environment_variable(cls, key: str, default: str = None) -> str:
        """Get environment variable with fallback to default."""
        return os.getenv(key, default)
    
    @classmethod
    def get_huggingface_token(cls) -> str:
        """Get Hugging Face API token from environment."""
        return cls.get_environment_variable('HUGGINGFACE_API_TOKEN')
    
    @classmethod
    def get_weather_api_key(cls) -> str:
        """Get weather API key from environment or use demo key."""
        return cls.get_environment_variable('WEATHER_API_KEY', cls.WEATHER_API_KEY) 