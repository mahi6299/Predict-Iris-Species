import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Load the model
model = joblib.load("model.pkl")
class_names = ['Setosa', 'Versicolor', 'Virginica']

# Page configuration
st.set_page_config(page_title="Iris Classifier")
st.title("🌼 Iris Flower Species Predictor")

# Sidebar inputs
st.sidebar.header("🌿 Input Features")
sepal_length = st.sidebar.slider('Sepal Length (cm)', 4.0, 8.0, 5.8)
sepal_width  = st.sidebar.slider('Sepal Width (cm)', 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider('Petal Length (cm)', 1.0, 7.0, 4.3)
petal_width  = st.sidebar.slider('Petal Width (cm)', 0.1, 2.5, 1.3)

# Prepare input
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Predict
if st.button("🔍 Predict Species"):
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    st.subheader("🔎 Prediction Result")
    st.success(f"🌸 Predicted species: **{class_names[prediction]}**")

    st.subheader("📊 Prediction Probabilities")
    fig, ax = plt.subplots()
    ax.bar(class_names, probabilities, color=["#7FFFD4", "#FFD700", "#FF69B4"])
    ax.set_ylabel("Probability")
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("📘 Made with Streamlit")
