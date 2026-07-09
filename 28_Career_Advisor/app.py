import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables (optional: create a .env file for your API Key)
load_dotenv()

# Page Config
st.set_page_config(page_title="AI Career Advisor", page_icon="🚀")

st.title("🚀 AI Career Advisor")
st.subheader("Your Personalized Career Coach")

# Sidebar for API Key (Best practice: keep it out of the code)
api_key = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")

# User Input
user_profile = st.text_area("Tell me about yourself (Experience, Skills, Education):", 
                            placeholder="e.g., I am a fresher with a degree in Computer Science and strong interest in Data Analysis.")
goal = st.text_input("What is your career goal?", placeholder="e.g., I want to become a Junior Data Analyst.")

# Initialize session state for the response
if "roadmap" not in st.session_state:
    st.session_state.roadmap = None

if st.button("Get Career Advice"):
    if not api_key:
        st.error("Please enter your API key in the sidebar.")
    elif not user_profile or not goal:
        st.warning("Please fill in both your profile and your goal.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash') # Suggestion: Use 'gemini-1.5-flash' for faster, cost-effective responses
            
            prompt = f"Act as an expert career coach. User Profile: {user_profile}. Career Goal: {goal}. Provide a professional roadmap including: 1. Skill gaps, 2. Recommended projects, 3. 3-month timeline, 4. Interview tips."
            
            with st.spinner("Analyzing your profile..."):
                response = model.generate_content(prompt)
                st.session_state.roadmap = response.text
                
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Display the stored roadmap
if st.session_state.roadmap:
    st.markdown("### Your Career Roadmap:")
    st.write(st.session_state.roadmap)

st.sidebar.markdown("---")
st.sidebar.info("Built for Career Development Portfolio")

"""
Steps to run this project:

1. Install dependencies:
    Open your terminal, navigate to the 28_Career_Advisor folder, and run:

        pip install -r requirements.txt

2. Run the application:
    In your terminal, execute:

        streamlit run app.py

3. Get your API Key:
    If you don't have one, get a free Google Gemini API Key from Google AI Studio. Paste it into the sidebar when the browser window opens.
"""