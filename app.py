import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# If your model has feature_names_in_ attribute (sklearn >=1.0)
if hasattr(model, "feature_names_in_"):
    features = list(model.feature_names_in_)
else:
    # Fallback: manually specify features if needed
    features = ['ph', 'Hardness', 'Solids', 'Chloramines', 
                'Sulfate', 'Conductivity', 'Organic_carbon', 
                'Trihalomethanes', 'Turbidity']  # <-- update if different

# Streamlit App
st.set_page_config(page_title="Water Quality Prediction", layout="centered")

st.title("💧 Water Quality Prediction App")
st.write("Check if water is safe or not based on its chemical properties.")

# Load dataset (only for default ranges, not for training)
data = pd.read_csv("waterQuality1.csv")
data = data.replace("#NUM!", np.nan)
data = data.apply(pd.to_numeric, errors="coerce")
data = data.fillna(data.mean())

# Sidebar inputs
st.sidebar.header("Enter Water Parameters")
user_input = []

for feature in features:
    if feature in data.columns:
        value = st.sidebar.number_input(
            f"{feature}",
            float(data[feature].min()),
            float(data[feature].max()),
            float(data[feature].mean())
        )
    else:
        # If column not in CSV, just ask for a reasonable input
        value = st.sidebar.number_input(f"{feature}", 0.0, 1000.0, 1.0)
    user_input.append(value)

# Convert input into dataframe with same feature order
input_df = pd.DataFrame([np.array(user_input)], columns=features)

# Prediction
if st.button("Predict Water Quality"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.success("✅ The water is **Safe to Drink**.")
    else:
        st.error("❌ The water is **Not Safe to Drink**.")
