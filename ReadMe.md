Project title: Student Result Prediction using Logistic Regression
Problem statement: This project aims to predict whether a student will pass or fail based on academic-related features. The goal is to build a classification model that can identify performance outcomes using available student data. 
Features used: Gender, Reading Score and Writing Score
Model used: Logistic Regression (For binary classification)
Result (accuracy): 
Initial model (including math score): 100% accuracy (due to data leakage)
Final model (excluding math score): 87.5% accuracy
After removing the math score to prevent data leakage, the model still achieved good accuracy. This indicates that reading and writing scores are correlated with overall student performance, allowing the model to make reliable predictions.