from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import pandas as pd
import joblib
from src.feature_engineering import scale_numerical_features

# Load model and pre-processing objects
model = tf.keras.models.load_model('models/career_employability_predictor.keras')
scaler = joblib.load('models/scaler.pkl')
trained_columns = joblib.load('models/trained_columns.pkl')
numeric_cols = joblib.load('models/numeric_columns.pkl')


# App Instance
app = FastAPI()

# Define input fields
class UserProfile(BaseModel):
    Age: str
    Accessibility: str
    EdLevel: str
    Gender: str
    MentalHealth: str
    MainBranch: str
    YearsCode: int
    YearsCodePro: int
    Country: str
    PreviousSalary: float
    ComputerSkills: int
    # Skill flags (0/1 if user knows these skills)
    Skill_JavaScript: int = 0
    Skill_Docker: int = 0
    Skill_HTML_CSS: int = 0
    Skill_SQL: int = 0
    Skill_Git: int = 0
    Skill_AWS: int = 0
    Skill_Python: int = 0
    Skill_PostgreSQL: int = 0
    Skill_MySQL: int = 0
    Skill_TypeScript: int = 0
    Skill_Node_js: int = 0
    Skill_React_js: int = 0
    Skill_Java: int = 0
    Skill_Bash_Shell: int = 0
    Skill_CSharp: int = 0
    Skill_Microsoft_SQL_Server: int = 0
    Skill_SQLite: int = 0
    Skill_jQuery: int = 0
    Skill_Microsoft_Azure: int = 0
    Skill_MongoDB: int = 0

@app.post("/predict")
def predict(user: UserProfile):
    input_dict = user.dict()
    df = pd.DataFrame([input_dict])

    # One-hot encode categorical features
    df = pd.get_dummies(df)

    # Fill missing columns
    for col in trained_columns:
        if col not in df.columns:
            df[col] = 0

    # Reorder columns to match training
    df = df[trained_columns]

    # Scale numeric columns
    df[numeric_cols] = scaler.transform(df[numeric_cols])

    # Predict
    prediction = model.predict(df)[0][0]
    probability = round(float(prediction), 4)
    prediction_label = int(prediction >= 0.5)

    # Add human-readable output
    label_meaning = "Likely Employed" if prediction_label == 1 else "Likely Unemployed"
    confidence = round(probability * 100, 2) if prediction_label == 1 else round((1 - probability) * 100, 2)

    return {
        "employability_probability": probability,
        "employability_label": prediction_label,
        "meaning": label_meaning,
        "confidence_percent": confidence
    }

@app.get("/info")
def info():
    return {"model_version": "v1.0.0", "author": "Jacob MacInnis", "framework": "TensorFlow"}
