"""
Main application file for the Bedtime Story Generator.
"""

import streamlit as st
from src import StoryGenerator, UIComponents, ChildPreferences

class BedtimeStoryApp:
    """Main Streamlit application class."""
    
    def __init__(self):
        self.initialize_session_state()
        self.story_generator = None
    
    def initialize_session_state(self):
        """Initialize session state variables."""
        if 'story_generated' not in st.session_state:
            st.session_state.story_generated = False
        if 'current_story' not in st.session_state:
            st.session_state.current_story = ""
        if 'child_preferences' not in st.session_state:
            st.session_state.child_preferences = None
        if 'huggingfacehub_api_token' not in st.session_state:
            st.session_state.huggingfacehub_api_token = ""
    
    def run(self):
        """Main application runner."""
        
        # Setup UI
        UIComponents.setup_page_config()
        UIComponents.load_custom_css()
        UIComponents.display_header()
        
        # Sidebar for preferences
        with st.sidebar:
            st.markdown("### 👶 Child's Information")
            st.markdown("#### 🔑 Hugging Face API Token")
            token = st.text_input(
                "Enter your Hugging Face API Token",
                type="password",
                value=st.session_state.huggingfacehub_api_token
            )
            st.session_state.huggingfacehub_api_token = token

            preferences = UIComponents.collect_preferences()
            
            if preferences:
                st.session_state.child_preferences = preferences
                st.session_state.story_generated = False
                st.rerun()
        
        # Main content area
        if not st.session_state.huggingfacehub_api_token:
            st.warning("Please enter your Hugging Face API token in the sidebar to use the story generator.")
            UIComponents.display_welcome()
            return

        if self.story_generator is None:
            self.story_generator = StoryGenerator(st.session_state.huggingfacehub_api_token)

        if st.session_state.child_preferences:
            UIComponents.display_story_section(self.story_generator, st.session_state.child_preferences)
        else:
            UIComponents.display_welcome()

def main():
    """Main function to run the application."""
    
    # Initialize the app
    app = BedtimeStoryApp()
    
    # Run the app
    app.run()

if __name__ == "__main__":
    main() 