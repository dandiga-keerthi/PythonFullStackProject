from fastapi import FastAPI
from src.logic import generate_event

app = FastAPI()

@app.get("/event")
def get_event():
    return generate_event()
