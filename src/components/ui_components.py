"""
UI components for the Bedtime Story Generator Streamlit interface.
"""

import streamlit as st
import datetime
from typing import List, Dict

from ..models import ChildPreferences

class UIComponents:
    """Class to manage UI components for the application."""
    
    @staticmethod
    def setup_page_config():
        """Setup Streamlit page configuration."""
        st.set_page_config(
            page_title="Bedtime Story Generator",
            page_icon="🌙",
            layout="wide",
            initial_sidebar_state="expanded"
        )
    
    @staticmethod
    def load_custom_css():
        """Load custom CSS for child-friendly design."""
        st.markdown("""
        <style>
            .main-header {
                background: linear-gradient(135deg, #d72660 0%, #6a0572 100%);
                color: white;
                font-size: 3rem;
                text-align: center;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                margin-bottom: 2rem;
                padding: 2rem 0;
                border-radius: 20px;
            }
            .story-box {
                background: linear-gradient(135deg, #ff6b9d 0%, #764ba2 100%);
                padding: 2rem;
                border-radius: 20px;
                color: white;
                font-size: 1.2rem;
                line-height: 1.8;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                margin: 1rem 0;
            }
            .preference-card {
                background: linear-gradient(135deg, #8f5fd7 0%, #d72660 100%);
                padding: 1.5rem;
                border-radius: 15px;
                color: white;
                margin: 1rem 0;
            }
            .emoji-button {
                font-size: 2rem;
                padding: 1rem;
                margin: 0.5rem;
                border-radius: 50%;
                border: none;
                cursor: pointer;
                transition: transform 0.2s;
            }
            .emoji-button:hover {
                transform: scale(1.1);
            }
            .loading-animation {
                text-align: center;
                font-size: 1.5rem;
                color: #FF6B9D;
            }
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def display_header():
        """Display the main header."""
        st.markdown('<h1 class="main-header">🌙 Bedtime Story Generator ✨</h1>', unsafe_allow_html=True)
    
    @staticmethod
    def display_welcome():
        """Display welcome message when no preferences are set."""
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("""
            <div style='text-align: center; padding: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; color: white;'>
                <h2>🌟 Welcome to the Magical Story World! 🌟</h2>
                <p style='font-size: 1.2rem; margin: 2rem 0;'>
                    Create personalized bedtime stories for your little ones! 
                    Each story is crafted with love, magic, and your child's unique preferences.
                </p>
                <h3>✨ How it works:</h3>
                <ul style='text-align: left; font-size: 1.1rem;'>
                    <li>Tell us about your child in the sidebar</li>
                    <li>Choose their mood and interests</li>
                    <li>Pick their favorite animal and color</li>
                    <li>Generate a magical, personalized story!</li>
                </ul>
                <p style='font-size: 1.1rem; margin-top: 2rem;'>
                    🌙 Perfect for bedtime routines and creating lasting memories ✨
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    @staticmethod
    def collect_preferences() -> ChildPreferences:
        """Collect child preferences in the sidebar."""
        
        # Child's name
        child_name = st.text_input("Child's Name:", placeholder="Enter name...")
        
        # Age
        age = st.slider("Age:", 2, 12, 6)
        
        # Mood selection
        st.markdown("### 😊 How is the child feeling today?")
        mood_options = {
            "😊 Happy": "happy and cheerful",
            "🌟 Excited": "excited and energetic", 
            "😴 Sleepy": "sleepy and calm",
            "🤔 Curious": "curious and thoughtful",
            "😌 Peaceful": "peaceful and relaxed",
            "🎉 Adventurous": "adventurous and brave"
        }
        
        mood = st.selectbox("Select mood:", list(mood_options.keys()))
        mood_value = mood_options[mood]
        
        # Interests
        st.markdown("### 🎯 What does the child love?")
        interest_options = [
            "🐾 Animals", "🚀 Space", "👑 Princesses", "🦸 Superheroes", 
            "🌳 Nature", "🏰 Castles", "🐉 Dragons", "🧚 Fairies",
            "🌊 Ocean", "🏔️ Mountains", "🌺 Flowers", "⭐ Stars"
        ]
        
        interests = st.multiselect(
            "Select interests (choose 2-4):",
            interest_options,
            default=["🐾 Animals", "⭐ Stars"]
        )
        
        # Story length
        st.markdown("### ⏰ Story Length")
        story_length = st.selectbox(
            "How long should the story be?",
            ["short", "medium", "long"],
            format_func=lambda x: {"short": "Short (5 min)", "medium": "Medium (10 min)", "long": "Long (15 min)"}[x]
        )
        
        # Favorite animal
        favorite_animal = st.text_input("Favorite Animal:", placeholder="e.g., elephant, dragon, unicorn...")
        
        # Favorite color
        favorite_color = st.selectbox(
            "Favorite Color:",
            ["Pink", "Blue", "Purple", "Green", "Yellow", "Orange", "Red", "Rainbow"]
        )
        
        # Generate button
        if st.button("✨ Generate Magical Story ✨", type="primary"):
            if child_name and interests and favorite_animal:
                preferences = ChildPreferences(
                    name=child_name,
                    age=age,
                    mood=mood_value,
                    interests=[interest.split(" ", 1)[1] for interest in interests],
                    story_length=story_length,
                    favorite_animal=favorite_animal,
                    favorite_color=favorite_color
                )
                return preferences
            else:
                st.error("Please fill in all required fields!")
        
        return None
    
    @staticmethod
    def display_story_section(story_generator, preferences: ChildPreferences):
        """Display the story generation and display section."""
        
        # Story generation
        if not st.session_state.get('story_generated', False):
            st.markdown("### 🎭 Ready to Create Magic?")
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🌟 Generate Story for " + preferences.name + " 🌟", type="primary"):
                    with st.spinner("✨ Creating your magical story..."):
                        # Add some delay for effect
                        import time
                        time.sleep(2)
                        
                        # Generate the story
                        story = story_generator.generate_story(preferences)
                        
                        st.session_state.current_story = story
                        st.session_state.story_generated = True
                        st.rerun()
        
        # Display generated story
        if st.session_state.get('story_generated', False):
            st.markdown("### 📖 Your Magical Story")
            
            # Story display
            st.markdown(f"""
            <div class="story-box">
                {st.session_state.current_story}
            </div>
            """, unsafe_allow_html=True)
            
            # Action buttons
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                if st.button("🔄 Generate New Story"):
                    st.session_state.story_generated = False
                    st.rerun()
            
            with col2:
                if st.button("💾 Save Story"):
                    st.success("Story saved! (Feature coming soon)")
            
            with col3:
                if st.button("📤 Share Story"):
                    st.info("Share feature coming soon!")
            
            # Story details
            with st.expander("📋 Story Details"):
                st.write(f"**Child:** {preferences.name} (Age: {preferences.age})")
                st.write(f"**Mood:** {preferences.mood}")
                st.write(f"**Interests:** {', '.join(preferences.interests)}")
                st.write(f"**Favorite Animal:** {preferences.favorite_animal}")
                st.write(f"**Favorite Color:** {preferences.favorite_color}")
                st.write(f"**Story Length:** {preferences.story_length}")
                st.write(f"**Generated:** {datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')}") 