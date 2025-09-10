💧 Water Quality Prediction App

This project is a Streamlit web application that predicts whether water is safe to drink based on its chemical properties. The app uses a trained machine learning model (model.pkl) and allows users to enter parameters like pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity.

Features

Interactive sidebar for entering water quality parameters

Real-time prediction of water safety (Safe / Not Safe)

Clean and simple Streamlit interface

Handles missing and invalid values from the dataset (waterQuality1.csv)

Tech Stack

Python (pandas, numpy, scikit-learn, joblib)

Streamlit for the user interface

Machine Learning Model trained on water quality data

How to Run

Clone the repository

Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

Use Case

This app is useful for demonstrating how machine learning can assist in environmental monitoring and public health decisions by providing quick assessments of water potability.
