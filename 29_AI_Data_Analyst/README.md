# 29. AI Data Analyst

## Overview
The AI Data Analyst is an intelligent agent designed to bridge the gap between raw data and actionable insights. By leveraging Large Language Models (LLMs) and the LangChain framework, this tool allows users to query CSV datasets using natural language. The agent automatically writes and executes Pandas code to provide data summaries, perform trend analysis, and generate visualizations.

## Key Features
- **Natural Language Interaction:** Ask questions about your data without writing manual Python code.
- **Agentic Workflow:** The LangChain agent interprets the query, selects the appropriate Pandas operations, and executes them safely.
- **Statistical Summary:** Built-in tools for quick EDA (Exploratory Data Analysis).
- **Visualization:** Automated generation of charts based on user queries.

## Technologies Used
- **Language:** Python
- **Frameworks:** LangChain, OpenAI
- **Data Manipulation:** Pandas
- **Visualization:** Matplotlib

## Project Structure
- `agent.py`: The core application that initializes the LangChain Agent.
- `data.csv`: The source dataset (ensure this file is present).

## Setup Instructions

### 1. Prerequisites
Ensure you have Python installed and an OpenAI API key.

### 2. Install Dependencies
Run the following command in your terminal:

```bash
pip install pandas langchain langchain-openai langchain-experimental matplotlib
```

### 3. Configuration
1. Open `agent.py`.
2. Replace `"your-actual-api-key-here"` with your actual OpenAI API key.

### 4. Running the Project
Place your `data.csv` file in the same directory and run:

```bash
python agent.py
```

## How It Works
The system uses the `create_pandas_dataframe_agent` from LangChain. When you provide a prompt like *"What is the total sales amount?"*, the model:
1. Analyzes the dataframe schema.
2. Generates the necessary Python/Pandas code.
3. Executes the code on the dataframe.
4. Returns the natural language answer.

## Example Queries
- "What is the average price per category?"
- "Plot a bar chart of sales by region."
- "Show me the top 5 rows of the dataset."

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License
This project is open-source and free to use.