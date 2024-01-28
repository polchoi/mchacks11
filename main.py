from typing import Union

from fastapi import FastAPI

app = FastAPI()


# MINE
class CLIENT:
    def __init__(self, name: str):
        self.name = name
        self.expensesReport = []
        self.spent = 0


class EXPENSES:
    def __init__(self, Name: str, Price: float, Category: str, Date: str):
        self.Name = Name
        self.Price = Price
        self.Category = Category
        self.Date = Date


Clients = []


@app.get("/")
def read_root():
    return {"McHacks 11! By Cesar, Karman, Oliver, Yoon Sun"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items")
def new_client(name: str):
    Clients.append(CLIENT(name))
    return None


@app.get("/items/{item_id}")
def new_expense(exp: EXPENSES, cli: CLIENT):
    cli.expensesReport.append(exp)
    return None
