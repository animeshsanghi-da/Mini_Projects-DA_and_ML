import os
import google.generativeai as genai

# Function to setup the connection to Google's API
def configure_api():
    # Retrieve the API key from the environment variables (best security practice)
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # Check if the key exists, otherwise stop the program with a helpful message
    if not api_key:
        raise ValueError("API Key not found. Please set GOOGLE_API_KEY environment variable.")
    
    # Initialize the library with your key
    genai.configure(api_key=api_key)

# Function to handle the AI interaction
def stream_social_media_post(topic, platform):
    """
    Generates and streams a social media post based on the topic and platform.
    """
    # Initialize the specific model (Gemini 1.5 Flash is fast and efficient)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Construct a structured prompt to guide the AI's behavior
    prompt = f"""
    You are an expert social media manager. Write an engaging post for {platform} about '{topic}'.
    - For LinkedIn: Professional, insightful, includes hashtags, and encourages discussion.
    - For Twitter (X): Concise, punchy, under 280 characters, includes relevant hashtags.
    - For Instagram: Casual, engaging tone, includes emojis, and a strong call-to-action.
    
    Output the post content clearly.
    """
    
    try:
        # Generate the content with streaming enabled (so text appears as it is generated)
        response = model.generate_content(prompt, stream=True)
        
        # Iterate over the response chunks and print them to the console immediately
        for chunk in response:
            print(chunk.text, end="", flush=True)
        
        # Print a final newline for clean formatting
        print("\n") 

    except Exception as e:
        # If the API fails or connectivity issues occur, catch the error and inform the user
        print(f"\nError generating content: {e}")

# The entry point of the script
if __name__ == "__main__":
    # 1. Prepare the API connection
    configure_api()
    
    # 2. Gather user input for the generator
    print("--- Social Media Content Generator ---")
    user_topic = input("Enter the topic you want to post about: ")
    user_platform = input("Choose platform (LinkedIn/Twitter/Instagram): ")
    
    # 3. Inform the user and execute the generation function
    print("\n--- Generating your content ---\n")
    stream_social_media_post(user_topic, user_platform)

"""
How to get this running:

1. Install the library:
    Open your terminal in the project folder and run:
        pip install google-generativeai

2. Get your API Key:
    Go to Google AI Studio to create your free API key.

3. Set your Environment Variable:
    Before running the script, set your key in the terminal:
        1. Windows (Command Prompt): set GOOGLE_API_KEY=your_actual_key_here
        2. Mac/Linux/Git Bash: export GOOGLE_API_KEY='your_actual_key_here'

4. Run the script: python generator.py
"""