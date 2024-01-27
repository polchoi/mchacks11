from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(): 
    return {"McHacks 11! By Cesar, Karma n, Oliver, Yoon Sun"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

students = {
    1: {
        "Name": "John",
        "Age": 17,
        "Id": 1
    }
}

@app.get("/get-student/{Id}")
def get_studetn(Id: int):
    return students[Id]