import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('breast_cancer_model.pkl', 'rb'))

st.title("Breast Cancer Prediction")

radius_mean = st.number_input("Radius Mean")
texture_mean = st.number_input("Texture Mean")
perimeter_mean = st.number_input("Perimeter Mean")

if st.button("Predict"):
    features = np.array([[radius_mean, texture_mean, perimeter_mean]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Malignant")
    else:
        st.success("Benign")