from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo
from db import SessionDep
from models import CustomerCreate, Customer, Transaction, Invoice

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola Mundo y Jaziel!"}

country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = ZoneInfo(timezone_str)

    return {"time": datetime.now(tz)}

db_customers: list[Customer] = []

@app.post("/customers", response_model = Customer, session: SessionDep)
async def create_customer(customer_data: CustomerCreate):
    customer = Customer.model_validate(customer_data.model_dump())
    # Asumiendo que se  hace en la bd
    customer.id = len(db_customers)
    db_customers.append(customer)
    return customer

@app.get("/customers")
async def list_customer():
    return db_customers

@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int):
    for customer in db_customers:
        if customer.id == customer_id:
            return customer
    return {"error": "Customer not found"}

@app.post("/transactions")
async def create_transaction(transaction_data: Transaction):
    return transaction_data

@app.post("/invoices")
async def create_invoice(invoice_data: Invoice):
    return invoice_data