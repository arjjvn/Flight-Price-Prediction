# ✈️ Flight Price Prediction System

A full-stack machine learning application designed to estimate flight ticket prices based on various travel parameters. The project features a RESTful API backend built with **FastAPI** and an interactive, stylized frontend developed with **Streamlit**.

## 🚀 Features

* **Real-time Predictions:** Instantly calculates estimated flight prices based on user inputs.
* **Interactive UI:** A clean, responsive Streamlit web interface with a custom background and distinct layout containers.
* **REST API Backend:** A dedicated FastAPI server that handles data processing, feature scaling, and model inference.
* **Machine Learning Pipeline:** Utilizes pre-trained Scikit-Learn models, label encoders, and standard scalers to process categorical and numerical data accurately.

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI, Pydantic
* **Machine Learning:** Scikit-Learn, Pandas
* **HTTP Client:** Requests

## 📂 Project Architecture

* `app.py`: Streamlit frontend application that captures user inputs and communicates with the backend.
* `main.py`: FastAPI backend that exposes the `/predict` endpoint.
* `model.sav`: Pre-trained machine learning model for price prediction.
* `encoder.sav`: Saved LabelEncoders for transforming categorical variables (airline, city, class, etc.).
* `scailer.sav`: Saved scaler for normalizing input features before prediction.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/flight-price-prediction.git](https://github.com/yourusername/flight-price-prediction.git)
   cd flight-price-prediction
