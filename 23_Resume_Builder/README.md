# AI Resume Builder 🚀

Automated, professional resume generation powered by Google Gemini.

## 💡 About
Tired of formatting resumes from scratch? This project acts as your personal resume architect. By combining your specific details with a predefined structural template, it uses the Google Gemini API to draft, format, and export a polished resume in seconds.

## ✨ Why this project?
* **Template-Driven:** You maintain full control over the structure via `template.txt`. The AI fills in the blanks without breaking your formatting.
* **Clean Output:** Automatically generates a formatted text file ready for you to copy into Word or Google Docs.
* **Simple & Fast:** Minimal setup—just your API key and your career details.

## ⚙️ How it Works
1.  **Input:** The script prompts you for your professional details (Name, Experience, Skills, Education).
2.  **Context Injection:** The script loads `template.txt` and combines it with your inputs into a structured prompt.
3.  **AI Processing:** Google Gemini analyzes your input and maps it into the template structure.
4.  **Export:** A clean, generated text file is saved directly to your folder.

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed. Install the required Google Generative AI library:

```bash
pip install -q -U google-generativeai
```

### 2. Setup
1.  Get your free API key from [Google AI Studio](https://aistudio.google.com/).
2.  Open `builder.py`.
3.  Replace `"YOUR_ACTUAL_API_KEY_HERE"` with your unique key.

### ⚠️ Critical Note on Templates
Ensure your `template.txt` file is clean. If you see tags like `` in your template, **delete them**. The AI will read exactly what is in that file, so a clean template results in a clean resume.

## 💻 Usage
Run the builder from your terminal:

```bash
python builder.py
```

Follow the prompts, and your resume will be saved as `[Your_Name]_Resume.txt` in the same directory.

## 📂 Project Structure
* `builder.py`: The engine. Handles inputs, API communication, and file saving.
* `template.txt`: The blueprint. Keeps your resume structure consistent.
* `[Name]_Resume.txt`: (Generated) Your final result.

---
**Author**
**Animesh Sanghi** | *Google Certified Data Analyst*
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da) | Email: animeshsanghi.da@gmail.com

*License: Open-source and free to use.*