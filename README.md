💧 Water Quality Prediction App

This project is a Streamlit web application that predicts whether water is safe to drink based on its chemical properties. The app uses a trained machine learning model (model.pkl) and allows users to enter parameters like pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity.

Data set link: https://www.kaggle.com/datasets/mssmartypants/water-quality

Info of the data set:
  This is a set of data created from imaginary data of water quality in an urban environment. I recommend using this dataset for educational purposes, for practice and to acquire the necessary knowledge.
  

Description
All attributes are numeric variables and they are listed bellow:

aluminium - dangerous if greater than 2.8
ammonia - dangerous if greater than 32.5
arsenic - dangerous if greater than 0.01
barium - dangerous if greater than 2
cadmium - dangerous if greater than 0.005
chloramine - dangerous if greater than 4
chromium - dangerous if greater than 0.1
copper - dangerous if greater than 1.3
flouride - dangerous if greater than 1.5
bacteria - dangerous if greater than 0
viruses - dangerous if greater than 0
lead - dangerous if greater than 0.015
nitrates - dangerous if greater than 10
nitrites - dangerous if greater than 1
mercury - dangerous if greater than 0.002
perchlorate - dangerous if greater than 56
radium - dangerous if greater than 5
selenium - dangerous if greater than 0.5
silver - dangerous if greater than 0.1
uranium - dangerous if greater than 0.3
is_safe - class attribute {0 - not safe, 1 - safe}


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

This app is useful for demonstrating how machine learning can assist in environmental monitoring and public health
decisions by providing quick assessments of water potability.
===================================================================================================================


<img width="1919" height="796" alt="Screenshot 2025-09-10 123225" src="https://github.com/user-attachments/assets/ed016912-3590-40f4-bd29-80a1e1396488" />


===================================================================================================================


<img width="388" height="854" alt="Screenshot 2025-09-10 123212" src="https://github.com/user-attachments/assets/c6ef7189-5006-4cc8-be9a-6d6b9dbcadd6" />


===================================================================================================================

<img width="1063" height="393" alt="Screenshot 2025-09-10 123205" src="https://github.com/user-attachments/assets/3d03bfa7-59de-4668-9dd4-0c824125b63c" />
