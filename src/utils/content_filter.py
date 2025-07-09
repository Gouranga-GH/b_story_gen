"""
Content filtering utilities for age-appropriate stories.
"""

import re
from typing import List

class ContentFilter:
    """Class to filter and clean content for children."""
    
    # Words to avoid in children's stories
    INAPPROPRIATE_WORDS = [
        'scary', 'frightening', 'terrifying', 'horror', 'nightmare',
        'dangerous', 'violent', 'angry', 'hate', 'kill', 'death',
        'darkness', 'evil', 'wicked', 'mean', 'cruel'
    ]
    
    # Replacement words for inappropriate content
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
    
    @staticmethod
    def filter_content(text: str) -> str:
        """Filter content to make it age-appropriate."""
        filtered_text = text.lower()
        
        # Replace inappropriate words
        for word, replacement in ContentFilter.REPLACEMENT_WORDS.items():
            filtered_text = re.sub(r'\b' + word + r'\b', replacement, filtered_text)
        
        # Ensure positive endings
        if not any(positive in filtered_text for positive in ['happy', 'joy', 'love', 'friend', 'magic', 'dream']):
            filtered_text += " And they all lived happily ever after."
        
        return filtered_text.capitalize()
    
    @staticmethod
    def is_age_appropriate(text: str, age: int) -> bool:
        """Check if content is appropriate for the given age."""
        # For very young children (2-4), ensure very simple language
        if age <= 4:
            complex_words = ['complicated', 'difficult', 'challenging', 'complex']
            if any(word in text.lower() for word in complex_words):
                return False
        
        # Check for inappropriate content
        if any(word in text.lower() for word in ContentFilter.INAPPROPRIATE_WORDS):
            return False
        
        return True
    
    @staticmethod
    def simplify_language(text: str, age: int) -> str:
        """Simplify language based on child's age."""
        if age <= 4:
            # Very simple sentences for toddlers
            sentences = text.split('.')
            simple_sentences = []
            for sentence in sentences:
                if sentence.strip():
                    # Keep sentences short
                    words = sentence.split()
                    if len(words) > 8:
                        # Split long sentences
                        simple_sentences.append(' '.join(words[:8]) + '.')
                        simple_sentences.append(' '.join(words[8:]) + '.')
                    else:
                        simple_sentences.append(sentence + '.')
            return ' '.join(simple_sentences)
        
        return text 