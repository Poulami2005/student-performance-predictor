import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

# Features
X = data[["StudyHours", "Attendance", "SleepHours", "PreviousMarks", "AssignmentsCompleted"]]

# Target
y = data["FinalMarks"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")