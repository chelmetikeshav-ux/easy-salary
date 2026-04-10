
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('random_forest_regressor_model.pkl')

# Title of the Streamlit app
st.title('Salary Prediction App')
st.write('Enter the employee details to predict their salary.')

# Input fields for features
age = st.slider('Age', 18, 65, 30)
gender = st.selectbox('Gender', ['Female', 'Male'])
education_level = st.selectbox('Education Level', ['Bachelor\'s', 'Master\'s', 'PhD', 'High School', 'Some College', 'Vocational'])
job_title = st.text_input('Job Title (e.g., Software Engineer, Data Analyst)')
years_of_experience = st.slider('Years of Experience', 0, 40, 5)

# Map categorical inputs to numerical values (matching LabelEncoder's output)
# NOTE: This assumes the original LabelEncoder mapping is available or consistent.
# For a real application, you'd save the LabelEncoder objects as well.
# For demonstration, we'll use a simple hardcoded mapping for 'Gender' and 'Education Level'.
# 'Job Title' will require more careful handling as its original encoding is complex.

gender_mapping = {'Female': 0, 'Male': 1}
education_mapping = {
    'Bachelor\'s': 0, 'Master\'s': 3, 'PhD': 5, 
    'High School': 2, 'Some College': 4, 'Vocational': 6 
} # These mappings are derived from the initial df.head() after encoding

# Dummy Job Title encoding for demonstration. In a real scenario, you'd use the saved LabelEncoder.
# For this example, we'll just hash the job title string to get a numerical value,
# which is *not* how LabelEncoder works but serves as a placeholder.
# A better approach would be to load the actual LabelEncoder used during training.
# For now, let's create a simple, non-robust integer based on the input string.
# This is a simplification; a production app would need the original LabelEncoder.
job_title_encoded = hash(job_title) % 1000 # Just an example, not accurate encoding

# Create a DataFrame from user inputs
input_df = pd.DataFrame([{
    'Age': age,
    'Gender': gender_mapping[gender],
    'Education Level': education_mapping[education_level],
    'Job Title': job_title_encoded, # Simplified encoding
    'Years of Experience': years_of_experience
}])

# Predict button
if st.button('Predict Salary'):
    prediction = model.predict(input_df)[0]
    st.success(f'The predicted salary is: ${prediction:,.2f}')
