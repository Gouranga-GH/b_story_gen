"""
Story generation prompts for the Bedtime Story Generator.
"""

from typing import Dict
from ..models import ChildPreferences, WeatherInfo, TimeInfo

class StoryPrompts:
    """Class to manage story generation prompts."""
    
    @staticmethod
    def create_story_prompt(preferences: ChildPreferences, weather: WeatherInfo, 
                           time_info: TimeInfo, educational_fact: str) -> str:
        """Create a detailed prompt for story generation."""
        
        length_guide = {
            "short": "about 3-4 paragraphs",
            "medium": "about 5-6 paragraphs", 
            "long": "about 7-8 paragraphs"
        }
        
        prompt = f"""
        Create a magical bedtime story for {preferences.name}, who is {preferences.age} years old.
        
        Child's Preferences:
        - Current mood: {preferences.mood}
        - Interests: {', '.join(preferences.interests)}
        - Favorite animal: {preferences.favorite_animal}
        - Favorite color: {preferences.favorite_color}
        - Story length: {length_guide.get(preferences.story_length, 'medium')}
        
        Context:
        - Current weather: {weather.description} ({weather.temperature}°C)
        - Time of day: {time_info.time_of_day}
        - Season: {time_info.season}
        - Educational fact to include: {educational_fact}
        
        Story Requirements:
        1. Make it age-appropriate and child-friendly
        2. Include {preferences.name} as the main character
        3. Incorporate the {preferences.favorite_animal} and {preferences.favorite_color} color
        4. Match the {preferences.mood} mood
        5. Include elements from their interests: {', '.join(preferences.interests)}
        6. Weave in the weather and seasonal context naturally
        7. Include the educational fact in a fun way
        8. End with a gentle, calming message perfect for bedtime
        9. Use simple, engaging language
        10. Make it magical and imaginative
        
        Create a heartwarming story that will help {preferences.name} drift off to sleep with beautiful dreams.
        """
        
        return prompt
    
    @staticmethod
    def get_fallback_story_templates() -> list:
        """Get fallback story templates."""
        return [
            """
            <p style='margin-bottom: 1rem;'>Once upon a time, in a magical {season} evening, little {name} was getting ready for bed. The sky was filled with {weather}, and {name} could see the stars twinkling like diamonds.</p>
            
            <p style='margin-bottom: 1rem;'>Suddenly, a friendly {animal} appeared at the window! This {animal} was the most beautiful shade of {color} and had the kindest eyes {name} had ever seen.</p>
            
            <p style='margin-bottom: 1rem;'>"Hello, {name}!" the {animal} said with a gentle smile. "I've come to share a special secret with you. Did you know that {fact}?"</p>
            
            <p style='margin-bottom: 1rem;'>Together, {name} and the {animal} went on a magical adventure through the {season} night. They visited places filled with {interests} and discovered wonders beyond imagination.</p>
            
            <p style='margin-bottom: 1rem;'>As the night grew deeper, the {animal} gently tucked {name} into bed. "Remember," whispered the magical friend, "every dream is a new adventure waiting for you."</p>
            
            <p style='margin-bottom: 1rem;'>With a heart full of joy and wonder, {name} drifted off to sleep, knowing that tomorrow would bring another magical day filled with possibilities.</p>
            """,
            
            """
            <p style='margin-bottom: 1rem;'>In a cozy little house where {name} lived, the {time_of_day} was filled with the gentle sounds of {weather}. The {color} curtains danced in the breeze, and {name} felt the magic of bedtime approaching.</p>
            
            <p style='margin-bottom: 1rem;'>That's when a tiny, sparkly {animal} fairy appeared! She was no bigger than a flower petal and glowed with the most beautiful {color} light. "Hello, dear {name}!" she chimed in a voice like silver bells.</p>
            
            <p style='margin-bottom: 1rem;'>The fairy told {name} the most amazing fact: "{fact}" {name} was so excited to learn something new about {interests}!</p>
            
            <p style='margin-bottom: 1rem;'>Together, they flew through the {season} night, visiting magical places where {interests} came to life. Everywhere they went, they spread joy and wonder.</p>
            
            <p style='margin-bottom: 1rem;'>When it was time to sleep, the fairy sprinkled magical {color} dust over {name}'s pillow. "Sweet dreams, little one," she whispered. "Tomorrow is another day full of magic and adventure."</p>
            
            <p style='margin-bottom: 1rem;'>And with that, {name} fell into the most peaceful sleep, dreaming of {animal}s and magical adventures.</p>
            """
        ] 