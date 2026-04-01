
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("calorie_model.pkl")  

#title and description
st.title(" Calories Burned Predictor")
st.write("Enter your daily activity data to predict calories burned.")

# User inputs 
steps = st.number_input("Steps", min_value=0, max_value=50000, value=8000)
active_minutes = st.number_input("Active Minutes", min_value=0, max_value=300, value=60)
distance_km = st.number_input("Distance (km)", min_value=0.0, max_value=50.0, value=6.0)

# Predict button
if st.button("Predict Calories Burned"):
    # Prepare input data for prediction
    input_data = pd.DataFrame({
        "steps": [steps],
        "active_minutes": [active_minutes],
        "distance_km": [distance_km]
    })

    prediction = model.predict(input_data)
    st.success(f" Estimated Calories Burned: {prediction[0]:.2f}")

    #Download same environment by running  "pip install -r requirements.txt" in the terminal

    # run the ml_model.py and app.py by going into the terminal and running ".\run.bat" 
    
    # run by going into the terminal and running "streamlit run app.py"