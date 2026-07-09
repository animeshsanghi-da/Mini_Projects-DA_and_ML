# 💬 Gemini-Powered PDF Chatbot

A simple, fast, and intelligent application that lets you chat with your PDF documents. Built with **Streamlit** and powered by **Google Gemini 1.5 Pro**, this app uses Retrieval-Augmented Generation (RAG) to provide accurate answers directly from your uploaded files.

---

## 🚀 How It Works
Instead of reading through long documents, this app does the heavy lifting for you:
1. **Extraction:** It reads your PDF pages and extracts the raw text.
2. **Chunking:** It breaks the text into manageable pieces (`RecursiveCharacterTextSplitter`).
3. **Embeddings:** It converts these pieces into numerical vectors using Google's embedding model.
4. **Search:** When you ask a question, it finds the most relevant "chunks" of text using FAISS.
5. **Answer:** It sends those specific chunks to **Gemini 1.5 Pro**, which generates a precise answer based only on your document.

---

## 🛠️ Prerequisites
* **Python 3.8+**
* **Google API Key:** You need an API key to access the Gemini model.

### Get Your API Key
1. Visit [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click on **"Get API key"**.
4. Click **"Create API key"**.
5. Copy the key safely.

---

## 📦 Installation

1. **Clone the repository:**
``` bash
git clone <your-repo-url>
cd 24_PDF_Chatbot
```

2. **Install dependencies:**
Make sure you have a `requirements.txt` file in the folder.
``` bash
pip install -r requirements.txt
```

3. **Configure API Key:**
Open `app.py` in your code editor. Find the line:
`os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY_HERE"`
Replace `"YOUR_GOOGLE_API_KEY_HERE"` with your actual key copied from Google AI Studio.

---

## 🏃‍♂️ Running the App

Launch the application by running this command in your terminal:

``` bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 💡 How to Use
1. **Upload:** Use the sidebar to upload your PDF files.
2. **Process:** Click **"Submit & Process"**. Wait for the "Done!" success message.
3. **Chat:** Type your questions in the main text box, and get answers based on your documents.

---

## 📂 Project Structure
* `app.py`: The main application logic and UI.
* `requirements.txt`: List of dependencies needed to run the app.
* `faiss_index/`: Local folder created after processing (stores your document data).

---

## ⚠️ Notes
* **Local Storage:** The app creates a local folder called `faiss_index` to store your document vectors. If you upload new documents, simply process them again to overwrite the old index.
* **Cost/Limits:** Ensure your Google AI Studio account has a valid billing profile or is within the free tier limits for Gemini API calls.

---

## 👤 Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

---

## License
This project is open-source and free to use.