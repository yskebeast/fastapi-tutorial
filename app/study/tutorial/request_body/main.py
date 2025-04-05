from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


# Using BaseModel can define the data type
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/")
async def create_item(item: Item):
    return item


@app.post("/items/")
async def create_item2(item: Item):
    # Using dict() method to convert the model to a dictionary
    # Using dict() is recommended by FastAPI
    # dict() will copy the model to a dictionary
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@app.put("/items/{item_id}")
async def update_item2(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
