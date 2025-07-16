"""
Data models for the Bedtime Story Generator application.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

# This dataclass stores all the preferences and information about the child
# that are needed to generate a personalized story.
@dataclass
class ChildPreferences:
    """Data class to store child's preferences for story generation."""
    name: str                # Child's name
    age: int                 # Child's age
    mood: str                # Current mood (e.g., happy, sleepy)
    interests: List[str]     # List of interests (e.g., animals, space)
    story_length: str        # Desired story length (short, medium, long)
    favorite_animal: str     # Favorite animal
    favorite_color: str      # Favorite color

# This dataclass holds weather information to add real-world context to stories.
@dataclass
class WeatherInfo:
    """Data class to store weather information."""
    description: str         # Weather description (e.g., 'clear sky')
    temperature: float       # Temperature in Celsius
    condition: str           # Main weather condition (e.g., 'rain', 'sunny')

# This dataclass holds time and date information for context in stories.
@dataclass
class TimeInfo:
    """Data class to store time and date information."""
    time: str                # Current time (e.g., '21:00')
    date: str                # Current date (e.g., 'April 27, 2024')
    season: str              # Current season (e.g., 'spring')
    time_of_day: str         # Time of day (e.g., 'evening', 'night')
    is_bedtime: bool         # Whether it's bedtime (True/False)

# This dataclass aggregates all context needed for story generation,
# including preferences, weather, time, and an educational fact.
@dataclass
class StoryContext:
    """Data class to store all context information for story generation."""
    preferences: ChildPreferences   # Child's preferences
    weather: WeatherInfo           # Weather context
    time_info: TimeInfo            # Time/date context
    educational_fact: str          # Educational fact to include in the story 