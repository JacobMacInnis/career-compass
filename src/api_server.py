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
    prediction_label = int(prediction >= 0.5)

    return {
        "employability_probability": float(prediction),
        "employability_label": prediction_label
    }

@app.get("/info")
def info():
    return {"model_version": "v1.0.0", "author": "Jacob MacInnis", "framework": "TensorFlow"}


# {
#   "Age": 47,
#   "Accessibility": 0,
#   "EdLevel": 'Undergraduate',
#   "Gender": "",
#   "MentalHealth": "string",
#   "MainBranch": "string",
#   "YearsCode": 0,
#   "YearsCodePro": 0,
#   "Country": "string",
#   "PreviousSalary": 0,
#   "ComputerSkills": 0,
#   "Skill_JavaScript": 0,
#   "Skill_Docker": 0,
#   "Skill_HTML_CSS": 0,
#   "Skill_SQL": 0,
#   "Skill_Git": 0,
#   "Skill_AWS": 0,
#   "Skill_Python": 0,
#   "Skill_PostgreSQL": 0,
#   "Skill_MySQL": 0,
#   "Skill_TypeScript": 0,
#   "Skill_Node_js": 0,
#   "Skill_React_js": 0,
#   "Skill_Java": 0,
#   "Skill_Bash_Shell": 0,
#   "Skill_CSharp": 0,
#   "Skill_Microsoft_SQL_Server": 0,
#   "Skill_SQLite": 0,
#   "Skill_jQuery": 0,
#   "Skill_Microsoft_Azure": 0,
#   "Skill_MongoDB": 0
# }
