from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

model = pickle.load(open("model.sav", "rb"))
encoders = pickle.load(open("encoder.sav", "rb"))
scaler = pickle.load(open("scailer.sav", "rb"))

class FlightDetails(BaseModel):
    airline: str
    flight: str
    source: str
    departure: str
    stop: str
    arrival: str
    destination: str
    travel: str
    duration: float
    days_left: int


@app.post("/predict")
def predict(flight:FlightDetails):
    data = pd.DataFrame([{"airline":flight.airline, "flight":flight.flight, "source_city":flight.source, "departure_time":flight.departure, "stops":flight.stop, "arrival_time":flight.arrival, "destination_city":flight.destination, "class":flight.travel, "duration":flight.duration, "days_left":flight.days_left}])
    colum=["airline", "flight", "source_city", "departure_time", "stops", "arrival_time", "destination_city", "class", "duration", "days_left"]
    catagorical_columns = ["airline", "flight", "source_city", "departure_time", "stops", "arrival_time", "destination_city", "class"]
    for i in catagorical_columns:
        data[i] = encoders[i].transform(data[i])
    input_data = data[colum]
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    return {"predicted_price": prediction}
