import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("💰 Loan Approval Prediction")

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
income = st.number_input("Applicant Income")
loan = st.number_input("Loan Amount")
credit = st.selectbox("Credit History", [1, 0])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_emp = st.selectbox("Self Employed", ["Yes", "No"])

# Convert input
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_emp = 1 if self_emp == "Yes" else 0

# Prediction
if st.button("Predict"):
    data = np.array([[gender, married, income, loan, credit, education, self_emp]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")