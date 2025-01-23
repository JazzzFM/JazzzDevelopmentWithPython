from fastapi import FastAPI
from datetime import datetime

app =  FastAPI()

@app.get("/")
async def root():
    date = datetime.now()
    return {"datetime": date}