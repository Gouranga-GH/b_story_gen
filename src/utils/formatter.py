"""
Story formatting utilities for the Bedtime Story Generator.
"""

import re
from typing import List

class StoryFormatter:
    """Class to format stories for display."""
    
    @staticmethod
    def format_story(text: str, child_name: str) -> str:
        """
        Format the generated story for display.
        Cleans up the text and adds HTML formatting for better appearance in the UI.
        Args:
            text (str): The raw story text from the AI model.
            child_name (str): The child's name (for cleaning artifacts).
        Returns:
            str: The formatted story as HTML.
        """
        # Clean up the story text (remove artifacts, extra whitespace, etc.)
        cleaned_text = StoryFormatter._clean_text(text, child_name)
        
        # Add HTML formatting (paragraphs, line height, etc.)
        formatted_story = StoryFormatter._add_html_formatting(cleaned_text)
        
        return formatted_story
    
    @staticmethod
    def _clean_text(text: str, child_name: str) -> str:
        """
        Clean up the story text by removing AI model artifacts and extra whitespace.
        Args:
            text (str): The raw story text.
            child_name (str): The child's name (to remove name-based artifacts).
        Returns:
            str: The cleaned story text.
        """
        # Remove lines like 'ChildName:', 'Assistant:', 'Human:', 'AI:' that sometimes appear in LLM outputs
        text = re.sub(rf'{child_name}:\s*', '', text)
        text = re.sub(r'Assistant:\s*', '', text)
        text = re.sub(r'Human:\s*', '', text)
        text = re.sub(r'AI:\s*', '', text)
        
        # Remove extra whitespace and newlines
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        
        return text
    
    @staticmethod
    def _add_html_formatting(text: str) -> str:
        """
        Add HTML formatting to the story for better display in Streamlit.
        Splits the story into paragraphs and wraps each in a styled <p> tag.
        Args:
            text (str): The cleaned story text.
        Returns:
            str: The HTML-formatted story.
        """
        # Split the text into paragraphs by double newlines (if any)
        paragraphs = text.split('\n\n')
        formatted_paragraphs = []
        
        for paragraph in paragraphs:
            if paragraph.strip():
                # Wrap each paragraph in a styled <p> tag
                formatted_paragraph = f"<p style='margin-bottom: 1rem; line-height: 1.8;'>{paragraph.strip()}</p>"
                formatted_paragraphs.append(formatted_paragraph)
        
        return '\n'.join(formatted_paragraphs)
    
    @staticmethod
    def add_illustrations(text: str) -> str:
        """
        Add simple emoji illustrations to the story based on keywords.
        Looks for certain words in each paragraph and prepends a relevant emoji.
        Args:
            text (str): The HTML-formatted story.
        Returns:
            str: The story with emojis added to relevant paragraphs.
        """
        import re
        # Mapping of keywords to emojis for illustration
        illustrations = {
            'unicorn': '\U0001F984',
            'dragon': '\U0001F409',
            'fairy': '\U0001F9DA',
            'princess': '\U0001F451',
            'star': '\u2B50',
            'moon': '\U0001F319',
            'sun': '\u2600\uFE0F',
            'flower': '\U0001F338',
            'tree': '\U0001F333',
            'ocean': '\U0001F30A',
            'mountain': '\U0001F3D4\uFE0F',
            'castle': '\U0001F3F0',
            'rainbow': '\U0001F308',
            'butterfly': '\U0001F98B',
            'bird': '\U0001F426',
            'cat': '\U0001F431',
            'dog': '\U0001F415',
            'elephant': '\U0001F418',
            'lion': '\U0001F981',
            'tiger': '\U0001F42F'
        }

        def insert_emoji(match):
            paragraph = match.group(2)
            # For each keyword, if found in the paragraph, prepend the emoji
            for word, emoji in illustrations.items():
                if word in paragraph.lower():
                    return f"<p{match.group(1)}>{emoji} {paragraph}</p>"
            return match.group(0)

        # Regex to match <p ...>...</p> blocks
        pattern = re.compile(r'<p([^>]*)>(.*?)</p>', re.DOTALL)
        text = pattern.sub(insert_emoji, text)
        return text
    
    @staticmethod
    def create_story_summary(preferences, weather, time_info) -> str:
        """
        Create a summary of the story context for display.
        Shows the child's preferences, weather, and time context in a styled HTML block.
        Args:
            preferences: ChildPreferences object
            weather: WeatherInfo object
            time_info: TimeInfo object
        Returns:
            str: HTML summary of the story context.
        """
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