"""
Story formatting utilities for the Bedtime Story Generator.
"""

import re
from typing import List

class StoryFormatter:
    """Class to format stories for display."""
    
    @staticmethod
    def format_story(text: str, child_name: str) -> str:
        """Format the generated story for display."""
        # Clean up the story text
        cleaned_text = StoryFormatter._clean_text(text, child_name)
        
        # Add formatting
        formatted_story = StoryFormatter._add_html_formatting(cleaned_text)
        
        return formatted_story
    
    @staticmethod
    def _clean_text(text: str, child_name: str) -> str:
        """Clean up the story text."""
        # Remove AI model artifacts
        text = re.sub(rf'{child_name}:\s*', '', text)
        text = re.sub(r'Assistant:\s*', '', text)
        text = re.sub(r'Human:\s*', '', text)
        text = re.sub(r'AI:\s*', '', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        
        return text
    
    @staticmethod
    def _add_html_formatting(text: str) -> str:
        """Add HTML formatting to the story."""
        # Split into paragraphs
        paragraphs = text.split('\n\n')
        formatted_paragraphs = []
        
        for paragraph in paragraphs:
            if paragraph.strip():
                # Add paragraph formatting
                formatted_paragraph = f"<p style='margin-bottom: 1rem; line-height: 1.8;'>{paragraph.strip()}</p>"
                formatted_paragraphs.append(formatted_paragraph)
        
        return '\n'.join(formatted_paragraphs)
    
    @staticmethod
    def add_illustrations(text: str) -> str:
        """Add simple ASCII art illustrations to the story."""
        import re
        illustrations = {
            'unicorn': '🦄',
            'dragon': '🐉',
            'fairy': '🧚',
            'princess': '👑',
            'star': '⭐',
            'moon': '🌙',
            'sun': '☀️',
            'flower': '🌸',
            'tree': '🌳',
            'ocean': '🌊',
            'mountain': '🏔️',
            'castle': '🏰',
            'rainbow': '🌈',
            'butterfly': '🦋',
            'bird': '🐦',
            'cat': '🐱',
            'dog': '🐕',
            'elephant': '🐘',
            'lion': '🦁',
            'tiger': '🐯'
        }

        def insert_emoji(match):
            paragraph = match.group(2)
            for word, emoji in illustrations.items():
                if word in paragraph.lower():
                    return f"<p{match.group(1)}>{emoji} {paragraph}</p>"
            return match.group(0)

        # Regex to match <p ...>...</p>
        pattern = re.compile(r'<p([^>]*)>(.*?)</p>', re.DOTALL)
        text = pattern.sub(insert_emoji, text)
        return text
    
    @staticmethod
    def create_story_summary(preferences, weather, time_info) -> str:
        """Create a summary of the story context."""
        summary = f"""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h4>📖 Story Details</h4>
            <p><strong>Child:</strong> {preferences.name} (Age: {preferences.age})</p>
            <p><strong>Mood:</strong> {preferences.mood}</p>
            <p><strong>Interests:</strong> {', '.join(preferences.interests)}</p>
            <p><strong>Favorite Animal:</strong> {preferences.favorite_animal}</p>
            <p><strong>Favorite Color:</strong> {preferences.favorite_color}</p>
            <p><strong>Weather:</strong> {weather.description} ({weather.temperature}°C)</p>
            <p><strong>Time:</strong> {time_info.time_of_day} in {time_info.season}</p>
        </div>
        """
        return summary 