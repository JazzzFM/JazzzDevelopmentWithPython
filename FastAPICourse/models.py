from pydantic import BaseModel # type: ignore
from sqlmodel import SQLModel

class CustomerBase(SQLModel):
    name: str
    descr: str | None
    email: str
    age: int

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase, table = True):
    id: int | None = None


class Transaction(BaseModel):
    id: int
    ammount: int
    description: str

class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int 

    def __init__(self, **data):
        super().__init__(**data)
        self.total = self.ammount_total


    @property
    def ammount_total(self):
        return sum(trans.ammount for trans in self.transactions)