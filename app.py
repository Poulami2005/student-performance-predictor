from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    sleep_hours = float(request.form["sleep_hours"])
    previous_marks = float(request.form["previous_marks"])
    assignments = float(request.form["assignments"])

    sample_data = pd.DataFrame([[study_hours, attendance, sleep_hours,
                                 previous_marks, assignments]],
    columns=["StudyHours", "Attendance", "SleepHours",
             "PreviousMarks", "AssignmentsCompleted"])

    prediction = model.predict(sample_data)

    result = round(prediction[0], 2)

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)