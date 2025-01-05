from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class ItemResponseModel(BaseModel):
    item_id: str
    user_id: str


@app.get("/items/")
async def read_items(item_id: str = Query(..., serialization_alias="item-id"),
                     user_id: str = Query(..., serialization_alias="user-id")):
    return {"item_id": item_id, "user_id": user_id}


@app.get("/item/")
async def read_item(
        q: str = Query(
            default=None,
            alias="item-query",  # URL 中使用的名称
            serialization_alias="query_string"  # 序列化时使用的名称
        )):
    return {"query": q}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
