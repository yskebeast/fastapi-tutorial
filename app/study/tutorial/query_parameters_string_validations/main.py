from typing import Union, List

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})  # type: ignore
    return results


@app.get("/items2/")
async def read_items2(
    q: Union[str, None] = Query(default=None, min_length=3, max_length=50),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})  # type: ignore
    return results


@app.get("/items3/")
# When using List query, Query is required
async def read_items3(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items


@app.get("/item4/")
async def read_items4(
    q: Union[str, None] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})  # type: ignore
    return results
