# Career Compass - Machine Learning Career Recommender API

Career Compass is a production-focused machine learning system that provides personalized career recommendations based on user profile attributes.  
It is built with modern MLOps principles in mind: modular code organization, containerized deployments, cloud-hosted infrastructure, and real SQL-backed feature storage.

---

## 📚 Project Overview

This project demonstrates a complete machine learning deployment workflow:

- Data ingestion and feature engineering from structured career and user datasets
- Supervised learning model training using TensorFlow/Keras
- Serving real-time predictions through a Dockerized FastAPI web service
- Cloud deployment on GCP Cloud Run with Artifact Registry and Cloud SQL (Postgres)

Career Compass is designed to simulate how scalable recommendation engines are built and served in real-world production environments.

---

## ⚙️ Technology Stack

- **Machine Learning**: TensorFlow/Keras (deep learning model for recommendations)
- **Backend API**: FastAPI (high-performance web server)
- **Database**: Postgres on GCP Cloud SQL (structured user and career metadata)
- **Containerization**: Docker
- **Cloud Infrastructure**: GCP Cloud Run, Artifact Registry
- **Data Processing**: Pandas, optional Scikit-learn for preprocessing

---

## 🏗️ Architecture

1. **Data Layer**: Raw career and user datasets stored locally, cleaned and processed.
2. **Model Layer**: Supervised ML model trained to predict suitable careers based on user profile features.
3. **API Layer**: FastAPI application exposes a `/recommendations` endpoint, loading the trained model for real-time inference.
4. **Infrastructure Layer**: Docker containerized app, pushed to Artifact Registry, deployed to Cloud Run.  
   Postgres database hosted on Cloud SQL holds user feature data.

---

## 🚀 Key Features

- Modular, production-ready Python codebase
- Clean separation of data preparation, model training, and API serving
- Scalable cloud deployment with minimal ops overhead
- SQL-backed user data management
- Lightweight, fast model for real-time responses

---

## 📦 Project Structure

```
career-compass/
├── data/ # Raw and processed datasets
│ ├── raw/ # Unmodified original data
│ └── processed/ # Cleaned and prepared data
├── docker/ # Dockerfile and container-related files
├── notebooks/ # Optional Jupyter exploration notebooks
├── src/ # Main application source code
│ ├── data_preparation.py # Data cleaning and feature engineering
│ ├── model_training.py # ML model definition and training
│ ├── model_serving.py # FastAPI app for inference serving
│ └── utils.py # Helper functions
├── deployment/ # Scripts for deploying to GCP Cloud Run
│ └── cloud_run_deploy.sh
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
├── LICENSE # MIT license
└── README.md # Project overview and instructions
```

---

## 🛠️ Setup and Deployment

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Train model locally:

   ```bash
   python src/model_training.py
   ```

3. Serve API locally (for testing):

   ```bash
   uvicorn src.model_serving:app --reload --host 0.0.0.0 --port 8000
   ```

4. Build Docker image:

   ```bash
   docker build -t career-compass .
   ```

5. Push to Artifact Registry and deploy to Cloud Run (via deploy script).

---

## 📣 Notes

This project is structured to emphasize clean production engineering, not research experimentation.  
It prioritizes simple, scalable, reproducible deployments — aligned with real-world ML engineering practices.

---
