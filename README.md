# Flight Price Prediction System

## Overview

An end-to-end machine learning application for predicting airline
ticket prices using flight and journey-related features.

## Architecture

Kaggle Dataset
      ↓
Google Colab
      ↓
ML Model Training
      ↓
Model + Encoder + Scaler
      ↓
FastAPI REST API
      ↓
Streamlit Frontend
      ↓
Predicted Flight Price

## Technologies

Python
Pandas
Scikit-learn
FastAPI
Pydantic
Streamlit
Pickle
Google Colab

## Features

- Flight price prediction
- Categorical feature encoding
- Feature scaling
- REST API prediction endpoint
- Interactive web interface
- Input validation
- API error handling

## API Endpoint

POST /predict

## How to Run

### FastAPI

uvicorn app:app --reload

### Streamlit

streamlit run streamlit_app.py
