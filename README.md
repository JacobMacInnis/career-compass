# Career Compass - Employment Prediction API

Career Compass is a production-grade machine learning system that predicts **whether a user is currently employed** based on structured profile attributes.
It follows modern MLOps principles: modular architecture, containerized deployments, continuous learning support, cloud SQL integration, and automated cloud hosting.

---

## 📚 Project Overview

This project demonstrates a real-world ML deployment pipeline:

- **Data ingestion**, feature engineering, and preprocessing from structured datasets
- **Supervised binary classification** model training using TensorFlow/Keras
- **Real-time prediction API** served via FastAPI inside a Docker container
- **Cloud deployment** on Google Cloud Run with Artifact Registry and Cloud SQL (PostgreSQL)
- **Continuous learning workflows** for model retraining as new data arrives
- **Data visualizations** for monitoring and understanding model behavior

---

## ⚙️ Technology Stack

- **Machine Learning**: TensorFlow/Keras (binary classification)
- **API Backend**: FastAPI (async high-performance server)
- **Database**: PostgreSQL (via Cloud SQL)
- **Containerization**: Docker
- **Cloud Infrastructure**: GCP Cloud Run + Artifact Registry
- **Data Processing**: Pandas, Scikit-learn
- **Visualization**: Matplotlib, Seaborn

---

## 🏗️ Architecture

1. **Data Layer**: Raw datasets → processed features → stored in PostgreSQL
2. **Model Layer**: Supervised ML model trained to classify users as employed or not employed
3. **API Layer**: FastAPI app exposes a `/predict` endpoint for employment prediction
4. **Deployment Layer**: Dockerized app deployed to Cloud Run
5. **Continuous Learning**: Scripts to retrain and redeploy updated models seamlessly

---

## 🚀 Key Features

- Modular, production-focused codebase
- SQL-backed feature storage (Postgres Cloud SQL)
- Real-time employment status predictions
- Continuous model retraining support
- Fully containerized and cloud-deployable
- Insightful model and dataset visualizations

---

## 📈 Visualizations

### Correlation Heatmap

![Correlation Heatmap](https://github.com/JacobMacInnis/career-compass/blob/main/plots/correlation_heatmap.png?raw=true)

- Shows correlations between numerical features, excluding country columns.
- Helps identify important relationships driving employment outcomes.

---

### Top Feature Correlations with Employment

![Top Employment Correlations](https://github.com/JacobMacInnis/career-compass/blob/main/plots/top_employment_correlations.png?raw=true)

- Highlights the features most correlated with being employed.
- Useful for feature selection and model explainability.

---

### Training vs Validation Loss Curve

![Loss Curve](https://github.com/JacobMacInnis/career-compass/blob/main/plots/loss_curve.png?raw=true)

- Displays training and validation loss across epochs.
- Helps monitor model convergence and detect overfitting.

---

## 📦 Project Structure

```
career-compass/
├── data/
│   ├── raw/
│   └── processed/
├── docker/
├── deployment/
│   └── cloud_run_deploy.sh
├── notebooks/
├── plots/
├── src/
│   ├── data_preparation.py
│   ├── model_training.py
│   ├── model_serving.py
│   ├── continuous_learning.py
│   ├── utils.py
│   └── data_visualization/
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛠️ Setup and Deployment

1. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model locally**:

   ```bash
   python src/model_training.py
   ```

3. **Serve the API locally**:

   ```bash
   uvicorn src.model_serving:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Build Docker image**:

   ```bash
   docker build -t career-compass .
   ```

5. **Deploy to GCP Cloud Run**:

   ```bash
   ./deployment/cloud_run_deploy.sh
   ```

---

## 🔄 Continuous Learning (Optional)

included in the deployment script

## 📤 Sample Prediction Example

**Sample curl command to test the API locally:**

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
        "Age": "25-34 years old",
        "Accessibility": "No",
        "EdLevel": "Bachelor’s degree",
        "Gender": "Man",
        "MentalHealth": "No",
        "MainBranch": "I am a developer by profession",
        "YearsCode": 5,
        "YearsCodePro": 3,
        "Country": "United States",
        "PreviousSalary": 85000.0,
        "ComputerSkills": 8,
        "Skill_JavaScript": 1,
        "Skill_Docker": 1,
        "Skill_HTML_CSS": 1,
        "Skill_SQL": 1,
        "Skill_Git": 1,
        "Skill_AWS": 0,
        "Skill_Python": 1,
        "Skill_PostgreSQL": 0,
        "Skill_MySQL": 0,
        "Skill_TypeScript": 1,
        "Skill_Node_js": 1,
        "Skill_React_js": 1,
        "Skill_Java": 0,
        "Skill_Bash_Shell": 0,
        "Skill_CSharp": 0,
        "Skill_Microsoft_SQL_Server": 0,
        "Skill_SQLite": 0,
        "Skill_jQuery": 0,
        "Skill_Microsoft_Azure": 0,
        "Skill_MongoDB": 0
      }'
```

**Expected Response:**

```json
{
  "employability_probability": 0.87,
  "employability_label": 1,
  "meaning": "Likely Employed",
  "confidence_percent": "87%"
}
```

---

## 🧠 Full Expected Input Fields

| Field            | Type  | Notes                                                 |
| :--------------- | :---- | :---------------------------------------------------- |
| Age              | str   | e.g., "25-34 years old"                               |
| Accessibility    | str   | "Yes" or "No"                                         |
| EdLevel          | str   | Highest education level                               |
| Gender           | str   | e.g., "Man", "Woman"                                  |
| MentalHealth     | str   | "Yes" or "No"                                         |
| MainBranch       | str   | Professional background                               |
| YearsCode        | int   | Total years coding experience                         |
| YearsCodePro     | int   | Professional coding years                             |
| Country          | str   | Country name                                          |
| PreviousSalary   | float | Most recent salary                                    |
| ComputerSkills   | int   | Self-rated number of skills known by applicant        |
| Skill\_\* fields | int   | 0 (no skill) or 1 (has skill) across 20+ technologies |

---

## 📣 Notes

Career Compass emphasizes **real-world MLOps practices**:

- Structured inputs
- Clear outputs
- Cloud-native scaling
- Continuous model refresh capabilities

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
