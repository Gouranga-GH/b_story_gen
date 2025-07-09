"""
Data models for the Bedtime Story Generator application.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class ChildPreferences:
    """Data class to store child's preferences for story generation."""
    name: str
    age: int
    mood: str
    interests: List[str]
    story_length: str
    favorite_animal: str
    favorite_color: str

@dataclass
class WeatherInfo:
    """Data class to store weather information."""
    description: str
    temperature: float
    condition: str

@dataclass
class TimeInfo:
    """Data class to store time and date information."""
    time: str
    date: str
    season: str
    time_of_day: str
    is_bedtime: bool

@dataclass
class StoryContext:
    """Data class to store all context information for story generation."""
    preferences: ChildPreferences
    weather: WeatherInfo
    time_info: TimeInfo
    educational_fact: str 