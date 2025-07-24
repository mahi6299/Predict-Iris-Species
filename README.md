# Predict-Iris-Species
Predict-Iris-Species is a machine learning web application built with Python, scikit-learn, and Streamlit. It predicts the species of an iris flower (Setosa, Versicolor, or Virginica) based on user-provided flower measurements (sepal length &amp; width, petal length &amp; width).
##Features
~ Trains a Random Forest classifier on the Iris dataset.

~ Uses joblib to save and load the trained model.

~ Clean, interactive Streamlit UI.

~ Shows prediction probabilities in a horizontal bar chart.

##Tech Stack
~ Python
~ scikit-learn
~ pandas
~ joblib
~ Streamlit

##Project Structure
Predict-Iris-Species/
├── app.py                # Streamlit web app script
├── iris.pkl              # Saved trained Random Forest model
├── requirements.txt      # List of Python dependencies
└── README.md             # Project description and instructions

##Model Details
~ Dataset: Iris (from scikit-learn)
~ Algorithm: Random Forest Classifier
~ Accuracy: ~97%
~ Exported using: joblib

##How to Run the App Locally:
git clone https://github.com/mahi6299/Predict-Iris-Species.git
cd Predict-Iris-Specie
pip install -r requirements.txt
streamlit run app.py
http://localhost:8501/
