# Project 34: Python Text-to-Speech Engine

This project is a lightweight Python application designed to convert text into spoken audio using the `pyttsx3` library. It provides an interactive interface allowing users to either provide text directly via the console or read content from a local text file.

## Features
* **Dual Input Modes:** Supports both real-time text entry and file-based reading (`input.txt`).
* **Voice Configuration:** Pre-configured with a specific voice ID and speech rate for consistent output.
* **Interactive Feedback:** Includes synthesized speech for welcome messages, status updates, and exit confirmations.
* **Robustness:** Includes basic input validation to prevent errors with empty strings.

## Prerequisites
* Python 3.x
* `pyttsx3` library

## Installation
Ensure you have the required library installed by running the following command in your terminal:

```
pip install pyttsx3
```

## Usage
1.  Navigate to the project directory:
```
cd minor_projects/34_Python-Text_to_Speach_Engine/
```
.  Execute the main script:
```
python main.py
```
3.  Follow the voice and on-screen prompts:
    * Enter **"text"** to type your message directly.
    * Enter **"file"** to have the engine read from `input.txt`.

## Project Structure
* `main.py`: The main execution script containing the `tts` function and input logic.
* `input.txt`: A text file used for demonstrating the file-reading capability.

## Logic Overview
The core logic resides in the `tts` function, which handles engine initialization, rate setting, and voice properties:

```
def tts(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('voice', voices[1].id)
    if not text or not text.strip():
        return
    engine.say(text)
    engine.runAndWait()
```

## Error Handling
The application is wrapped in a `try-except` block to ensure that if any issues occur during the synthesis process or file reading, they are caught and printed to the console rather than crashing the script.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License
This project is open-source and free to use.