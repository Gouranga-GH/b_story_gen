# Bedtime Story Generator

A web application that generates personalized bedtime stories for children based on their preferences. Built with Python, Streamlit, and LangChain, this app provides a fun, interactive way to create magical stories for kids.

---

## Features
- Collects child preferences (name, age, mood, interests, favorite animal, color, etc.)
- Generates unique bedtime stories using AI (Hugging Face models)
- Enriches stories with weather, time, and fun facts
- Simple, interactive Streamlit UI
- Emoji illustrations for extra fun
- No image generation (text and emoji only)

---

## Directory Structure
```
Story_Gen/
  app.py                # Main Streamlit app
  config.py             # App configuration (if any)
  requirements.txt      # Python dependencies
  src/
    components/         # UI components
    models.py           # Data models
    prompts/            # Story prompt templates
    story_generator.py  # Story generation logic
    tools/              # Weather, time, search tools
    utils/              # Content filtering, formatting
```

---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Story_Gen
   ```

2. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the App Locally

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
2. **Open the app in your browser:**
   - Go to the URL shown in the terminal (usually http://localhost:8501)

---

## Usage
- Enter your Hugging Face API token in the sidebar (get one from https://huggingface.co/settings/tokens)
- Fill in the child’s preferences
- Click to generate a personalized bedtime story!

---

## Hugging Face API Token
- The app requires a Hugging Face API token to access language models.
- Enter your token in the sidebar when prompted.
- [Get your token here](https://huggingface.co/settings/tokens) (sign up/log in required).

---

## Deploying on Hugging Face Spaces

1. **Push your code to a public GitHub repository.**
2. **Create a new Space:**
   - Go to [Hugging Face Spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose "Streamlit" as the SDK
   - Link your GitHub repo or upload your code
3. **Set the `HUGGINGFACEHUB_API_TOKEN` as a secret in the Space settings** (or enter it in the app sidebar at runtime).
4. **Click "Deploy".**
5. **Access your app via the provided Hugging Face Spaces URL.**

---

## License
This project is for educational and personal use. See `LICENSE` for more details. 