import pyttsx3
import os

def tts(text):                      # Definig a function
    engine = pyttsx3.init()                     # Initialize engine
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)             # Set properties
    engine.setProperty('voice', voices[1].id)   # Use female voice
    if not text or not text.strip():
        return  # Don't speak if text is empty
    engine.say(text)
    engine.runAndWait()

try:
    # 1. Welcome message
    tts("Initialising Python... Hello user! How would you like to provide input?")

    method = input('Enter input type (text/file): ').lower().strip()

    # 2. Code execution
    if method == "text":
        tts("Please enter your text.")
        user_text = input("Enter text: ")
        tts(user_text)
        
    elif method == "file":
        file_path = "input.txt"
        tts("Reading your file now.")
        with open(file_path, "r") as file:
            content = file.read()
            tts(content)
            
    else:
        tts("Invalid option selected.")

    # 3. Exit message
    tts("Task complete. Signing off.")

except Exception as e:
    print(f"Error occurred during execution: {e}")