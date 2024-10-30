# Required Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load Data
@st.cache_data
def load_data():
    train_data = pd.read_csv("train.csv")
    test_data = pd.read_csv("test.csv")
    return train_data, test_data

train_data, test_data = load_data()

# Data Preparation
def prepare_data(data):
    # Fill missing values for 'Age' with median
    data['Age'].fillna(data['Age'].median(), inplace=True)
    # Fill missing values for 'Fare' in test data with median
    data['Fare'].fillna(data['Fare'].median(), inplace=True)
    # Fill missing values in 'Embarked' with the most common value
    data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
    
    # Drop 'Cabin' and 'Ticket' as they contain a lot of missing data or irrelevant info
    data.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'], inplace=True)
    
    # Convert categorical variables to numerical
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    
    return data

train_data = prepare_data(train_data)
test_data_prepared = prepare_data(test_data)

# Separate features and target
X = train_data.drop(columns=['Survived'])
y = train_data['Survived']

# Train-test split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluation on validation set
y_pred = model.predict(X_val)
conf_matrix = confusion_matrix(y_val, y_pred)
accuracy = accuracy_score(y_val, y_pred)

# Display results in Streamlit
st.title("Titanic Survival Prediction")
st.write("This application uses logistic regression to predict Titanic passenger survival.")

st.header("Confusion Matrix")
fig, ax = plt.subplots()
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", ax=ax)
st.pyplot(fig)

st.write(f"**Accuracy:** {accuracy * 100:.2f}%")

# Predict on Test Data
test_predictions = model.predict(test_data_prepared)

# Save predictions to CSV file
submission = pd.DataFrame({
    "PassengerId": range(892, 892 + len(test_predictions)),
    "Survived": test_predictions
})
submission.to_csv("submission.csv", index=False)

# Display confirmation message
st.header("Predictions on Test Data")
st.write("The predictions have been saved to `submission.csv`.")
st.write(submission)
