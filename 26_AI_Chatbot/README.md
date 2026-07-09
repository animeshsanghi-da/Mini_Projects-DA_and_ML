# Gemini Terminal Chatbot

A lightweight, interactive command-line interface (CLI) chatbot powered by Google’s Gemini 1.5 Flash model. This project transforms your terminal into a conversational AI assistant, complete with memory and error handling.

## 🚀 How It Works (The "Under the Hood" Details)

This script isn't just a basic prompt-response tool; it’s designed to handle a full conversation flow. Here is the step-by-step logic:

1. **Initialization:** The script uses the `google-generativeai` library to create a bridge between your terminal and Google's AI servers.
2. **Configuration:** It sets the API key via `os.environ` so the library knows who you are and has permission to request responses.
3. **The "Brain" (Chat Session):** By using `model.start_chat(history=[])`, we create a persistent session. Unlike a standard API call, this specific method keeps track of every message you've sent, allowing the AI to "remember" the context of your conversation.
4. **The Infinite Loop:** The `while True` loop is the heart of the bot. It keeps the program running, constantly waiting for your next sentence via `input()`.
5. **Safety Net:** The entire API interaction is wrapped in a `try...except` block. If the internet goes down, the API key is invalid, or the server blips, the script won't crash—it will simply print the error, keeping your terminal clean.
6. **Exit Strategy:** The bot checks for specific "kill signals" (`quit`, `exit`, `bye`) before sending your text to the AI, ensuring you can stop the process gracefully.

---

## 🛠️ Setup Instructions

### 1. Requirements
Ensure you have Python installed. You will need the Google Generative AI library. Open your terminal and run:

```bash
pip install -q -U google-generativeai
```

### 2. Configuration
1. Obtain your API Key from [Google AI Studio](https://aistudio.google.com/).
2. Open `chatbot.py` in your code editor.
3. Locate the line: `os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"`
4. Replace `'YOUR_API_KEY'` with your actual API string.

### 3. Execution
Run the chatbot directly from your terminal:

```bash
python chatbot.py
```

---

## 💡 Project Features

* **Contextual Memory:** Because it uses `start_chat`, you can ask follow-up questions (e.g., "What is the capital of France?" followed by "What is its population?") and the bot will know exactly what you are referring to.
* **Efficient:** Uses `gemini-1.5-flash`, which is optimized for speed, ensuring your terminal feels snappy.
* **Robust:** Basic error handling ensures that network interruptions don't break the user experience.
* **Zero Dependencies:** Only requires the official Google SDK, keeping your environment clutter-free.

## 🎓 Portfolio Significance

This project highlights essential modern development skills:
* **API Integration:** Managing secure communication with third-party AI services.
* **Session Management:** Understanding state and history in conversational AI.
* **UX/CLI Design:** Building user-friendly interactions in non-graphical environments.
* **Defensive Coding:** Implementing `try/except` logic to ensure application stability.

## 👤 Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

---
*License: This project is open-source and free to use.*