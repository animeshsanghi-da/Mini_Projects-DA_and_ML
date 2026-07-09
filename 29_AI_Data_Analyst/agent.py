import os
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd

# 1. Place your API key here. 
# The agent will use this directly.
os.environ["OPENAI_API_KEY"] = "your-actual-api-key-here"

def run_agent(data_path: str, user_query: str):
    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    
    # Load the data
    # Note: Ensure data.csv is in the same folder
    df = pd.read_csv(data_path)
    
    # Create the agent
    # The agent handles all data manipulation automatically
    agent = create_pandas_dataframe_agent(
        llm, 
        df, 
        verbose=True,
        allow_dangerous_code=True
    )
    
    # Execute the query
    response = agent.invoke(user_query)
    return response

if __name__ == "__main__":
    # Ensure your data.csv is in the same directory
    data_file = "data.csv" 
    query = "What is the total sales amount and which category is the highest?"
    
    # Run the process
    result = run_agent(data_file, query)
    print(result['output'])

"""
Quick Setup Instructions
1. Install Dependencies:

    pip install pandas langchain langchain-openai matplotlib

2. Environment: Replace "your-api-key-here" with your actual OpenAI API key.

3. Data: Ensure you have a CSV file named data.csv in the same directory as these scripts for testing.

4. Execution: Run python agent.py to start the analysis.
"""