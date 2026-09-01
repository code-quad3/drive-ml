# Ride ETA Prediction Service
 
A machine learning microservice built with FastAPI that predicts ride ETA using a trained Random Forest model.
 
The trained model is serialized using Joblib and loaded by the FastAPI application when the service starts.
 
---
 
## 🛠️ Tech Stack
 
- Python
- FastAPI
- Scikit-learn
- Random Forest
- Pandas
- NumPy
- Docker
---
 
## 🚀 Run Locally
 
```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```
 
- **Service:** `http://localhost:8000`
- **Swagger:** `http://localhost:8000/docs`
---
 
## 🧠 Train Model
 
```bash
python train.py
```
 
The trained Random Forest model is saved as:
 
```
eta_model.pkl
```
 
---
 
## 📡 API
 
### Health Check
```
GET /
```
 
### Predict ETA
```
POST /predict-eta
```
 
> See `/docs` for the complete request and response schema.
 
---
 
## 🐳 Docker
 
```bash
docker build -t ride-eta-ml .
docker run -p 8000:8000 ride-eta-ml
```
