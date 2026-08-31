from fastapi import FastAPI
import joblib

app = FastAPI()

# Load trained model once when the server starts
model = joblib.load("eta_model.pkl")


@app.get("/")
def home():
    return {"message": "ETA ML service is running"}


@app.post("/predict-eta")
def predict_eta(data: dict):

    distance_km = data["distanceKm"]
    hour = data["hour"]
    day_of_week = data["dayOfWeek"]

    prediction = model.predict([
        [distance_km, hour, day_of_week]
    ])

    return {
        "predicted_eta_minutes": round(float(prediction[0]), 2)
    }