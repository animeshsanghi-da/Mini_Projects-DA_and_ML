import streamlit as st
import pandas as pd
import joblib
import os

# Set page title
st.title("Restaurant Sales Prediction App")

# Load the trained model
# Ensure 'model.pkl' is in the same directory
model_path = 'model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file 'model.pkl' not found. Please ensure it is uploaded.")
    model = None

# Sidebar for user input
st.sidebar.header("Input Features")
def user_input_features():
    day_of_week = st.sidebar.slider("Day of Week (1=Mon, 7=Sun)", 1, 7, 1)
    is_weekend = 1 if day_of_week >= 6 else 0
    promotion = st.sidebar.selectbox("Promotion Active", [0, 1])
    footfall = st.sidebar.number_input("Expected Footfall", min_value=0, max_value=1000, value=100)
    data = {
        'day_of_week': day_of_week,
        'is_weekend': is_weekend,
        'promotion': promotion,
        'footfall': footfall
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display input
st.subheader("User Input Parameters")
st.write(input_df)

# Prediction
if st.button("Predict Sales"):
    if model:
        prediction = model.predict(input_df)
        st.subheader("Prediction")
        st.write(f"Estimated Sales: ${prediction[0]:,.2f}")
    else:
        st.warning("Model not loaded.")