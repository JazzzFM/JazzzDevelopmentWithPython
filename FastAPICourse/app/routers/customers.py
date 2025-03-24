from models import CustomerCreate, Customer, CustomerUpdate
from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from db import SessionDep

router = APIRouter(tags = ["customers"])

@router.post("/customers", response_model = Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    # Asumiendo que se  hace en la bd
    return customer

@router.get("/customers/{customer_id}", response_model = Customer)
async def read_customer(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        return HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                detail = "Customer does not exist")
                             
    return customer_db

@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        return HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                detail = "Customer does not exist")
    session.delete(customer_db)
    session.commit()                      
    return {"detail": "OK"}


@router.put("/customers/{id}")
async def update_customer(id: int, CustomerData: CustomerCreate, 
                          session: SessionDep):
    
    customer_id = session.get(Customer, id)
    
    if not customer_id:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = "Customer does not exist")
    
    if customer_id:
        if CustomerData.name:
            customer_id.name = CustomerData.name
        if CustomerData.description:
            customer_id.description = CustomerData.description
        if CustomerData.email:
            customer_id.email = CustomerData.email
        if CustomerData.age:
            customer_id.age = CustomerData.age
            
        session.add(customer_id)
        session.commit()
        session.refresh(customer_id)
    return {"detail": "ok, updated"}

@router.get("/customers", response_model = list[Customer])
async def list_customer(session: SessionDep):
    return session.exec(select(Customer)).all()

@router.get("/customers/{customer_id}", response_model = Customer)
async def get_customer(customer_id: int):
    db_customers: list[Customer] = []
    for customer in db_customers:
        if customer.id == customer_id:
            return customer
    return {"error": "Customer not found"}