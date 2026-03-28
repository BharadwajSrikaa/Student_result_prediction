import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("./StudentsPerformance.csv")

# Preprocessing
df['gender'] = df['gender'].map({'male': 0, 'female': 1})
df['result'] = df['math score'].apply(lambda x: 1 if x >= 60 else 0)

# Drop unnecessary columns
df = df.drop(['race/ethnicity', 'parental level of education', 
              'lunch', 'test preparation course'], axis=1)

# Features (no math score to avoid leakage)
X = df.drop(['result', 'math score'], axis=1)
y = df['result']

# Train model
model = LogisticRegression()
model.fit(X, y)

# UI
st.title("Student Pass/Fail Predictor")

gender = st.selectbox("Gender", ["Male", "Female"])
reading = st.slider("Reading Score", 0, 100, 50)
writing = st.slider("Writing Score", 0, 100, 50)

# Convert input
gender_val = 0 if gender == "Male" else 1

# Predict
if st.button("Predict"):
    prediction = model.predict([[gender_val, reading, writing]])
    
    if prediction[0] == 1:
        st.success("✅ Student will PASS")
    else:
        st.error("❌ Student may FAIL")