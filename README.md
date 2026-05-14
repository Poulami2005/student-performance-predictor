# 🎓 AI-Based Student Performance Predictor

A Machine Learning web application that predicts student academic performance based on study habits, attendance, sleep hours, previous marks, and assignments completed.

---

## Features

- Predict student marks using Machine Learning
- Grade prediction system
- Responsive and modern UI
- Flask backend integration
- ML model using Linear Regression
- User-friendly web interface

---

## Tech Stack

### Frontend
- HTML
- CSS

### Backend
- Flask
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

---

## Machine Learning Model

This project uses **Linear Regression** to predict final student marks based on:
- Study Hours
- Attendance
- Sleep Hours
- Previous Marks
- Assignments Completed

---

## Project Structure

```plaintext
student-performance-predictor/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── dataset.csv
├── model.pkl
└── README.md
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/Poulami2005/student-performance-predictor.git
```

2. Install required libraries

```bash
pip install flask pandas numpy scikit-learn joblib
```

3. Run the application

```bash
python app.py
```

4. Open in browser

```plaintext
http://127.0.0.1:5000
```

---

## Future Improvements

- Dark mode
- Graph visualization
- User login system
- Subject-wise prediction
- AI study recommendations

---

## Author

Poulami Ghosh
