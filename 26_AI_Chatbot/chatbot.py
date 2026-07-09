import google.generativeai as genai
import os

# 1. Setup API Key
# Replace 'YOUR_API_KEY' with your actual key from https://aistudio.google.com/
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def run_chatbot():
    # Initialize the model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Start a chat session to maintain conversation history
    chat = model.start_chat(history=[])

    print("--- AI Chatbot Initialized (Type 'quit' to exit) ---")
    
    while True:
        user_input = input("You: ")
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Bot: Goodbye!")
            break
        
        try:
            # Send message to model
            response = chat.send_message(user_input)
            print(f"Bot: {response.text}")
        except Exception as e:
            print(f"Bot: Error - {e}")

if __name__ == "__main__":
    run_chatbot()


"""
Steps to run this file:
1. Install the library: Open your terminal and run:
    pip install -q -U google-generativeai

2. Get an API Key: Go to Google AI Studio, click "Get API key," and copy it.

3. Update Code: Paste your key into the script where it says 'YOUR_API_KEY'.

4. Run: Execute the script using: python chatbot.py
"""