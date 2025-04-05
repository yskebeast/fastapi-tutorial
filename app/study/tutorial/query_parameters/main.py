from typing import Union
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/params/")
async def params_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/params/{params_id}")
async def params_items(params_id: str, q: Union[str, None] = None):
    if q:
        return {"params_id": params_id, "q": q}
    return {"params_id": params_id}


@app.get("/params2/{params_id}")
async def params2_item(params_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": params_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item
