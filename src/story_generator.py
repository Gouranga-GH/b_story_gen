"""
Main story generator module for the Bedtime Story Generator.
"""

import random
import time
from typing import Dict, List, Optional

# Import LangChain components for LLMs, tools, and agent orchestration
from langchain.llms import HuggingFaceHub
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType

# Import local models, tools, prompts, and utilities
from .models import ChildPreferences, WeatherInfo, TimeInfo, StoryContext
from .tools import WeatherTool, TimeTool, SearchTool
from .prompts import StoryPrompts
from .utils import ContentFilter, StoryFormatter

class StoryGenerator:
    """Main story generation class using LangChain and Hugging Face LLMs."""
    
    def __init__(self, huggingfacehub_api_token: str):
        """
        Initialize the story generator with a Hugging Face LLM and contextual tools.
        Args:
            huggingfacehub_api_token (str): API token for Hugging Face Hub.
        """
        # Set up the language model (DialoGPT-medium) from Hugging Face
        self.llm = HuggingFaceHub(
            repo_id="microsoft/DialoGPT-medium",
            model_kwargs={"temperature": 0.8, "max_length": 500},
            huggingfacehub_api_token=huggingfacehub_api_token
        )
        
        # Initialize context tools for weather, time, and educational facts
        self.weather_tool = WeatherTool()
        self.time_tool = TimeTool()
        self.search_tool = SearchTool()
        
        # Wrap tools as LangChain Tool objects for agent use
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
        
        # Initialize a LangChain agent that can use the above tools
        self.agent = initialize_agent(
            self.tools,
            self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False
        )
    
    def generate_story(self, preferences: ChildPreferences) -> str:
        """
        Generate a personalized bedtime story based on child preferences and real-world context.
        Args:
            preferences (ChildPreferences): The child's preferences and story settings.
        Returns:
            str: The final, formatted, and filtered story.
        """
        
        # Gather real-world context for the story
        weather_info = self.weather_tool.get_weather()
        time_info = self.time_tool.get_time_info()
        
        # Get an educational fact related to one of the child's interests
        educational_fact = self.search_tool.search_facts(
            random.choice(preferences.interests)
        )
        
        # Bundle all context into a StoryContext object
        context = StoryContext(
            preferences=preferences,
            weather=weather_info,
            time_info=time_info,
            educational_fact=educational_fact
        )
        
        try:
            # Create a prompt for the LLM using all gathered context
            story_prompt = StoryPrompts.create_story_prompt(
                preferences, weather_info, time_info, educational_fact
            )
            # Use the agent (with tools) to generate the story
            response = self.agent.run(story_prompt)
            
            # Format the story for readability and personalization
            formatted_story = StoryFormatter.format_story(response, preferences.name)
            # Filter the story for safety and appropriateness
            filtered_story = ContentFilter.filter_content(formatted_story)
            # Simplify language based on the child's age
            simplified_story = ContentFilter.simplify_language(filtered_story, preferences.age)
            
            # Optionally add illustrations (e.g., emojis or text art)
            final_story = StoryFormatter.add_illustrations(simplified_story)
            
            return final_story
            
        except Exception as e:
            # If anything fails, print the error and generate a fallback story
            print(f"Story generation error: {e}")
            return self._generate_fallback_story(context)
    
    def _generate_fallback_story(self, context: StoryContext) -> str:
        """
        Generate a fallback story using templates if the main generation fails.
        Args:
            context (StoryContext): All context information for the story.
        Returns:
            str: The fallback story, formatted and filtered.
        """
        
        # Get a list of fallback story templates
        templates = StoryPrompts.get_fallback_story_templates()
        # Randomly select a template
        template = random.choice(templates)
        
        # Fill in the template with context values
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
        
        # Format, filter, and simplify the fallback story
        formatted_story = StoryFormatter.format_story(story, context.preferences.name)
        filtered_story = ContentFilter.filter_content(formatted_story)
        simplified_story = ContentFilter.simplify_language(filtered_story, context.preferences.age)
        final_story = StoryFormatter.add_illustrations(simplified_story)
        
        return final_story
    
    def get_story_context(self, preferences: ChildPreferences) -> StoryContext:
        """
        Gather all context information (weather, time, fact) for a given set of preferences.
        Args:
            preferences (ChildPreferences): The child's preferences and story settings.
        Returns:
            StoryContext: The complete context for story generation.
        """
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