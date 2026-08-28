import joblib

# Load trained model
model = joblib.load("eta_model.pkl")

# Driver information
distance_km = 2.5
hour = 18
day_of_week = 5

# Predict ETA
prediction = model.predict([
    [distance_km, hour, day_of_week]
])

print("Predicted ETA:", round(prediction[0], 2), "minutes")