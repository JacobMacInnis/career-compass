from fastapi import APIRouter
import tensorflow as tf
import pandas as pd
import joblib
from src.schemas.user_profile import UserProfileBase

class UserProfile(UserProfileBase):
    pass


router = APIRouter()

# Load model and pre-processing objects
model = tf.keras.models.load_model('models/career_employability_predictor.keras')
scaler = joblib.load('models/scaler.pkl')
trained_columns = joblib.load('models/trained_columns.pkl')
numeric_cols = joblib.load('models/numeric_columns.pkl')

@router.post("/predict")
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
