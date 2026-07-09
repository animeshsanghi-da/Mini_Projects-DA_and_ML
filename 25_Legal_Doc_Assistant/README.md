# Legal Document Assistant ⚖️

A secure and robust Python CLI tool that uses Google’s Gemini API to analyze legal documents. It helps you summarize text, extract critical dates/obligations, and identify potential red flags in contracts or agreements.

## 🚀 What's New?
This version has been upgraded for production-grade usage:
* **Secure API Handling:** Now uses `.env` files to keep your keys safe (no more hardcoding!).
* **Flexible Input:** You can either point the script to a `.txt` file or paste the text directly into your terminal.
* **Robust Architecture:** Built with `system_instruction` for consistent, reliable legal analysis.

---

## ⚠️ Critical Legal Disclaimer
**This tool is for educational and informational purposes only.** It does not constitute professional legal advice. AI models can make mistakes or "hallucinate." Always consult with a qualified attorney for legal document review.

---

## 🛠️ Setup Instructions

### 1. Prerequisites
Ensure you have **Python 3.7+** installed.

### 2. Install Dependencies
Open your terminal in the project folder and run:
``` bash
pip install -q -U google-generativeai python-dotenv
```

### 3. Configure Your API Key
To keep your API key secure, we use a `.env` file.
1. Create a new file in your project folder named exactly `.env`.
2. Open it with a text editor and add this line:
``` text
GOOGLE_API_KEY=your_actual_api_key_here
```
*(Replace `your_actual_api_key_here` with your key from [Google AI Studio](https://aistudio.google.com/)).*

---

## 📖 How to Use

Run the script from your terminal:
``` bash
python assistant.py
```

### The Interface
When the program starts, it will ask for a file path:

1.  **To analyze a file:** Type the path to your `.txt` document (e.g., `contract.txt`) and press `Enter`.
2.  **To paste text manually:** Just press `Enter` without typing anything. You can then paste your legal text.
    * *On Mac/Linux:* Press `Ctrl+D` when finished.
    * *On Windows:* Press `Ctrl+Z` and then `Enter` when finished.

The script will automatically process the text and print a structured report including:
* **Summary:** A high-level overview.
* **Obligations & Dates:** A list of deadlines and responsibilities.
* **Risk Assessment:** Flagging ambiguous or concerning language.

---

## 📂 Project Structure
* `assistant.py`: The main logic. It handles API communication, file reading, and user interaction.
* `.env`: A hidden configuration file that stores your private API key.
* `README.md`: You are here!

---

## 👨‍💻 Author
**Animesh Sanghi** | *Google Certified Data Analyst* [LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## ⚖️ License
Open-source and free to use.