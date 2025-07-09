"""
Main story generator module for the Bedtime Story Generator.
"""

import random
import time
from typing import Dict, List, Optional

from langchain.llms import HuggingFaceHub
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType

from .models import ChildPreferences, WeatherInfo, TimeInfo, StoryContext
from .tools import WeatherTool, TimeTool, SearchTool
from .prompts import StoryPrompts
from .utils import ContentFilter, StoryFormatter

class StoryGenerator:
    """Main story generation class using LangChain."""
    
    def __init__(self, huggingfacehub_api_token: str):
        # Initialize with a free Hugging Face model
        # Note: In production, you'd use your Hugging Face API token
        self.llm = HuggingFaceHub(
            repo_id="microsoft/DialoGPT-medium",
            model_kwargs={"temperature": 0.8, "max_length": 500},
            huggingfacehub_api_token=huggingfacehub_api_token
        )
        
        # Initialize tools
        self.weather_tool = WeatherTool()
        self.time_tool = TimeTool()
        self.search_tool = SearchTool()
        
        # Create LangChain tools
        self.tools = [
            Tool(
                name="weather_tool",
                func=self.weather_tool.get_weather,
                description="Get current weather information for story context"
            ),
            Tool(
                name="time_tool",
                func=self.time_tool.get_time_info,
                description="Get current time, date, and season information"
            ),
            Tool(
                name="search_tool",
                func=self.search_tool.search_facts,
                description="Search for educational facts about topics"
            )
        ]
        
        # Initialize agent
        self.agent = initialize_agent(
            self.tools,
            self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False
        )
    
    def generate_story(self, preferences: ChildPreferences) -> str:
        """Generate a personalized bedtime story."""
        
        # Get context information
        weather_info = self.weather_tool.get_weather()
        time_info = self.time_tool.get_time_info()
        
        # Get educational fact based on interests
        educational_fact = self.search_tool.search_facts(
            random.choice(preferences.interests)
        )
        
        # Create story context
        context = StoryContext(
            preferences=preferences,
            weather=weather_info,
            time_info=time_info,
            educational_fact=educational_fact
        )
        
        try:
            # Generate story using LangChain
            story_prompt = StoryPrompts.create_story_prompt(
                preferences, weather_info, time_info, educational_fact
            )
            response = self.agent.run(story_prompt)
            
            # Format and filter the story
            formatted_story = StoryFormatter.format_story(response, preferences.name)
            filtered_story = ContentFilter.filter_content(formatted_story)
            simplified_story = ContentFilter.simplify_language(filtered_story, preferences.age)
            
            # Add illustrations
            final_story = StoryFormatter.add_illustrations(simplified_story)
            
            return final_story
            
        except Exception as e:
            print(f"Story generation error: {e}")
            # Generate fallback story
            return self._generate_fallback_story(context)
    
    def _generate_fallback_story(self, context: StoryContext) -> str:
        """Generate a fallback story if the main generation fails."""
        
        templates = StoryPrompts.get_fallback_story_templates()
        template = random.choice(templates)
        
        # Fill in the template
        story = template.format(
            name=context.preferences.name,
            age=context.preferences.age,
            mood=context.preferences.mood,
            interests=', '.join(context.preferences.interests),
            animal=context.preferences.favorite_animal,
            color=context.preferences.favorite_color,
            weather=context.weather.description,
            season=context.time_info.season,
            time_of_day=context.time_info.time_of_day,
            fact=context.educational_fact
        )
        
        # Format the fallback story
        formatted_story = StoryFormatter.format_story(story, context.preferences.name)
        filtered_story = ContentFilter.filter_content(formatted_story)
        simplified_story = ContentFilter.simplify_language(filtered_story, context.preferences.age)
        final_story = StoryFormatter.add_illustrations(simplified_story)
        
        return final_story
    
    def get_story_context(self, preferences: ChildPreferences) -> StoryContext:
        """Get all context information for story generation."""
        weather_info = self.weather_tool.get_weather()
        time_info = self.time_tool.get_time_info()
        educational_fact = self.search_tool.search_facts(
            random.choice(preferences.interests)
        )
        
        return StoryContext(
            preferences=preferences,
            weather=weather_info,
            time_info=time_info,
            educational_fact=educational_fact
        ) 