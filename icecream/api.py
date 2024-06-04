from fastapi import FastAPI
from icecream.predict import predict_sales

app = FastAPI()


@app.get("/")
def root():
    return {"greeting": "Hellow World!!"}


@app.get("/predict")
def predict(temp: int, num_people: int):
    prediction = predict_sales(temp, num_people)
    return {"prediction": prediction}
