"""
Search tool for providing educational content and facts.
"""

import random
from typing import Dict, List

class SearchTool:
    """
    Tool to search for educational content.
    Provides fun and interesting facts for various story topics (animals, space, nature, etc.).
    Used to enrich stories with educational tidbits based on the child's interests.
    """
    
    def __init__(self):
        # A dictionary mapping topic categories to lists of fun facts.
        # This acts as a simple in-memory database for quick fact lookup.
        self.facts_database = {
            'animals': [
                "Elephants are the only mammals that can't jump!",
                "A group of flamingos is called a 'flamboyance'.",
                "Penguins can jump as high as 6 feet out of water.",
                "Giraffes have the same number of neck bones as humans - seven!",
                "Butterflies taste with their feet.",
                "A baby kangaroo is called a joey.",
                "Dolphins sleep with one eye open.",
                "A group of lions is called a pride."
            ],
            'space': [
                "A day on Venus is longer than its year!",
                "The Sun makes up 99.86% of our solar system's mass.",
                "There are more stars in the universe than grains of sand on Earth.",
                "The footprints on the moon will last for 100 million years.",
                "Saturn's rings are mostly made of ice and rock.",
                "Jupiter has the biggest storm in our solar system.",
                "A year on Mars is 687 Earth days long.",
                "The Milky Way galaxy is shaped like a spiral."
            ],
            'nature': [
                "Trees can communicate with each other through their roots.",
                "A single cloud can weigh more than 1 million pounds.",
                "Rainbows are actually full circles, we just see half of them.",
                "The Great Barrier Reef is the largest living structure on Earth.",
                "Some plants can grow up to 3 feet in a single day.",
                "Bees can recognize human faces.",
                "A group of trees is called a grove.",
                "The oldest tree in the world is over 5,000 years old."
            ],
            'ocean': [
                "The ocean contains 97% of Earth's water.",
                "The deepest part of the ocean is 36,000 feet deep.",
                "Jellyfish have been around for 650 million years.",
                "The blue whale is the largest animal ever known to exist.",
                "Coral reefs are home to 25% of all marine life.",
                "Octopuses have three hearts.",
                "A group of fish is called a school.",
                "The ocean produces half of the world's oxygen."
            ],
            'princesses': [
                "Princesses in fairy tales often represent kindness and courage.",
                "The word 'princess' comes from the Latin word 'princeps'.",
                "Many princesses in stories help others and show bravery.",
                "Princesses often have magical friends and helpers.",
                "In stories, princesses teach us about friendship and love.",
                "Princesses can be found in cultures all around the world.",
                "Some princesses are warriors and protect their kingdoms.",
                "Princesses often have special powers or magical abilities."
            ],
            'dragons': [
                "Dragons appear in stories from many different cultures.",
                "Some dragons are friendly and help people.",
                "Dragons in stories often guard treasure or knowledge.",
                "Baby dragons are called dragonets.",
                "Some dragons can breathe fire, others can fly.",
                "Dragons are often very wise and magical creatures.",
                "In some stories, dragons can change their size.",
                "Dragons often live in caves or on mountain tops."
            ],
            'fairies': [
                "Fairies are magical creatures that love nature.",
                "Some fairies can fly and have wings like butterflies.",
                "Fairies often help animals and plants grow.",
                "Baby fairies are called fairy children.",
                "Fairies love to dance and sing in the moonlight.",
                "Some fairies can grant wishes to kind people.",
                "Fairies often live in flower gardens or forests.",
                "Fairies are known for their kindness and magic."
            ],
            'castles': [
                "Castles were built to protect people from enemies.",
                "The first castles were built over 1,000 years ago.",
                "Castles often have towers, walls, and moats.",
                "Some castles have secret passages and hidden rooms.",
                "Castles were homes for kings, queens, and knights.",
                "Many castles have beautiful gardens and courtyards.",
                "Castles are often built on hills for better protection.",
                "Some castles have dungeons and treasure rooms."
            ]
        }
    
    def search_facts(self, topic: str) -> str:
        """
        Search for interesting facts about a topic.
        Tries to match the topic to a category in the database and returns a random fact.
        If no match is found, returns a default positive fact.
        Args:
            topic (str): The topic or interest to search for (e.g., 'animals', 'space').
        Returns:
            str: A fun fact related to the topic, or a default fact if not found.
        """
        for category, facts in self.facts_database.items():
            if category in topic.lower():
                return random.choice(facts)
        
        # Default fact if no specific category is found
        default_facts = [
            "Every day is a new adventure waiting to be discovered!",
            "The best stories are the ones we create together.",
            "Magic is everywhere if you know where to look.",
            "Friendship makes every adventure more special.",
            "Dreams can come true if you believe in them."
        ]
        return random.choice(default_facts)
    
    def get_facts_for_interests(self, interests: List[str]) -> List[str]:
        """
        Get facts for multiple interests.
        Loops through a list of interests and collects a fact for each.
        Args:
            interests (List[str]): List of topics/interests.
        Returns:
            List[str]: List of fun facts, one for each interest.
        """
        facts = []
        for interest in interests:
            fact = self.search_facts(interest)
            facts.append(fact)
        return facts 