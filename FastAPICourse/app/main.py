from fastapi import FastAPI, HTTPException, status
from datetime import datetime
from zoneinfo import ZoneInfo
from db import SessionDep, create_all_tables
from .routers import customers, transactions
from models import Transaction, Invoice

app = FastAPI(lifespan = create_all_tables)
app.include_router(customers.router)
app.include_router(transactions.router)

@app.get("/")
async def root():
    return {"message": "Hola Mundo y Jaziel!"}

country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima"
}


@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = ZoneInfo(timezone_str)

    return {"time": datetime.now(tz)}

@app.post("/invoices")
async def create_invoice(invoice_data: Invoice):
    return invoice_data
