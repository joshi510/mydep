
#uvicorn app:app --reload

#github - create repo- setting-
#https://github.com/joshi510/mydep/settings
from fastapi import FastAPI
import pickle

app = FastAPI()

# load model
with open("Salary_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Salary Prediction API Running"}

@app.post("/predict")
def predict(data: dict):
    exp = data.get("YearsExperience")

    if exp is None:
        return {"error": "YearsExperience required"}

    result = model.predict([[exp]])

    return {
        "YearsExperience": exp,
        "Salary": int(result[0])
    }