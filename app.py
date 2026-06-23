import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("breast_cancer_model.pkl", "rb"))

st.title("Breast Cancer Prediction")

ct = st.number_input("Clump Thickness", min_value=1, max_value=10)
ucs = st.number_input("Uniformity of Cell Size", min_value=1, max_value=10)
ucs2 = st.number_input("Uniformity of Cell Shape", min_value=1, max_value=10)
ma = st.number_input("Marginal Adhesion", min_value=1, max_value=10)
secs = st.number_input("Single Epithelial Cell Size", min_value=1, max_value=10)
bn = st.number_input("Bare Nuclei", min_value=1, max_value=10)
bc = st.number_input("Bland Chromatin", min_value=1, max_value=10)
nn = st.number_input("Normal Nucleoli", min_value=1, max_value=10)
m = st.number_input("Mitoses", min_value=1, max_value=10)

if st.button("Predict"):
    features = np.array([[ct, ucs, ucs2, ma, secs, bn, bc, nn, m]])
    prediction = model.predict(features)

    st.write("Prediction:", prediction[0])