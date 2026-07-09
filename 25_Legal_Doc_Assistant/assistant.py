import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load environment variables from .env file
load_dotenv()

# Configure API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API Key not found. Please set GOOGLE_API_KEY in your .env file.")
genai.configure(api_key=api_key)

# 2. Use system_instruction for better role adherence
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction="""You are an expert Legal Assistant. 
    Analyze the provided legal document. Output your analysis in clear, 
    structured sections: 1. Summary, 2. Key Obligations/Dates, 3. Red Flags/Ambiguities."""
)

def get_legal_analysis(document_text):
    try:
        response = model.generate_content(document_text)
        return response.text
    except Exception as e:
        return f"Error: {e}"

def main():
    print("--- Legal Document Assistant ---")
    file_path = input("Enter the path to your .txt file (or press Enter to paste text): ").strip()
    
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                doc_text = f.read()
        except FileNotFoundError:
            print(f"Error: The file at '{file_path}' was not found.")
            return
    else:
        print("Paste your text (Ctrl+D/Z to finish):")
        doc_text = ""
        while True:
            try:
                doc_text += input() + "\n"
            except EOFError:
                break
    
    print("\nAnalyzing... please wait.\n")
    print(get_legal_analysis(doc_text))

if __name__ == "__main__":
    main()

"""
Steps to follow to run this file:
1. Install the library: Open your terminal and run:
    pip install -q -U google-generativeai

2. Get an API Key: If you don't have one, visit Google AI Studio and create an API key.

3. Update the Script: Replace 'YOUR_API_KEY' in the script with the key you just created.

4. Run the script: python assistant.py

5. Test: Copy and paste a sample paragraph from a terms-of-service agreement or a contract to see how it performs.
"""