# 🚀 Social Media Content Generator

An elegant, lightweight Python utility that turns your ideas into platform-ready social media posts. Powered by **Google Gemini 1.5 Flash**, this tool acts as your personal AI assistant to save time and spark creativity.

## 💡 Why use this tool?
* **No Bloat:** Minimal dependencies. Just Python and the Google Generative AI SDK.
* **Platform-Optimized:** Content is automatically tailored to the nuances of LinkedIn, Twitter (X), and Instagram.
* **Real-time Output:** Uses streaming to display text as it generates, giving you an interactive experience.
* **Secure by Design:** Uses environment variables to ensure your API credentials stay off your hard drive.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **AI Engine:** Google Gemini (`gemini-1.5-flash`)
* **Dependencies:** `google-generativeai`

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have [Python](https://www.python.org/) installed on your system.

### 2. Installation
Open your terminal in the project folder and install the required library:
```bash
pip install google-generativeai
```

### 3. Obtain Your Google API Key
To use the Gemini model, you need a free API key from Google:
1. Navigate to [Google AI Studio](https://aistudio.google.com/).
2. Click on the **"Get API key"** button on the top left sidebar.
3. Click **"Create API key"**.
4. Select a project (or create a new one if prompted).
5. Copy the generated key. **Keep this secret!**

### 4. Setting the API Key (Environment Variable)
For security, we use environment variables instead of hardcoding the key.

#### For Windows (Command Prompt/PowerShell)
To set the key for your *current* terminal session:
```cmd
set GOOGLE_API_KEY=your_actual_key_here
```

#### For Mac / Linux / Git Bash
To set the key for your *current* terminal session:
```bash
export GOOGLE_API_KEY='your_actual_key_here'
```

> *Tip: To make this permanent, add the export/set command to your shell configuration file (e.g., `.bashrc`, `.zshrc`, or Windows System Environment Variables).*

## ⚡ Usage
Execute the generator:
```bash
python generator.py
```

Follow the interactive prompts to define your topic, choose your platform, and watch the AI write your post in real-time.

---

### Example Workflow
**User:** * Topic: "Learning Python for Data Science"
* Platform: "Twitter"

**Output:**
> "Just started my journey into Data Science with Python! 🐍 The syntax is so intuitive. Excited to build my portfolio and solve real-world problems. #DataScience #Python #LearningJourney"

---

## 👤 Author
**Animesh Sanghi** *Google Certified Data Analyst*

[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da) | [Email](mailto:animeshsanghi.da@gmail.com)

## 📄 License
This project is open-source and free to use.