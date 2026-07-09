import os
import google.generativeai as genai

# Setup API Key
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def generate_resume():
    # 1. Load the template
    try:
        with open("template.txt", "r") as f:
            template_content = f.read()
    except FileNotFoundError:
        print("Error: template.txt not found.")
        return

    print("--- AI Resume Builder ---")
    # Collect inputs
    name = input("Enter your full name: ")
    experience = input("Enter your experience (jobs, dates, details): ")
    skills = input("Enter your skills (technical, tools, soft skills): ")
    education = input("Enter your education: ")

    # 2. Update the prompt to use the template
    prompt = f"""
    Act as a professional resume writer. Fill in the following resume template 
    using the provided user information. 
    
    IMPORTANT: Follow the structure below exactly and replace the placeholders.
    
    TEMPLATE:
    {template_content}
    
    USER INFORMATION:
    Name: {name}
    Experience: {experience}
    Skills: {skills}
    Education: {education}
    """
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    print("\nGenerating your resume... please wait.")
    response = model.generate_content(prompt)
    
    # Save to file
    filename = f"{name.replace(' ', '_')}_Resume.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
        
    print(f"\nSuccess! Resume saved as {filename}")

"""
### Prerequisites
First, install the necessary library in your terminal:

```Bash
pip install -q -U google-generativeai
```
"""

"""
How to use this:
1. API Key: You can get a free API key from Google AI Studio.

2. Execution: Run the script using python builder.py.

3. Output: The script will print the generated resume in your terminal and create a text file (e.g., John_Doe_Resume.txt) in your folder.
"""