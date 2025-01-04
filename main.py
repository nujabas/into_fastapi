from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel


# 定义Pydantic模型
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = 0.0


class ErrorResponse(BaseModel):
    detail: str


# 创建FastAPI应用实例
app = FastAPI()

# 创建APIRouter实例
router = APIRouter()


# 定义路径操作函数，并指定responses参数
@router.post("/items/",
             status_code=201,
             response_model=Item,
             responses={
                 201: {
                     "description": "Item created successfully"
                 },
                 204: {
                     "description": "No Content"
                 },
                 400: {
                     "description": "Validation Error",
                     "model": ErrorResponse
                 },
                 500: {
                     "description": "Internal Server Error",
                     "model": ErrorResponse
                 }
             })
async def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400,
                            detail="Price must be non-negative")
    # 模拟内部服务器错误
    if item.name == "error":
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return item


# 将router包含到FastAPI应用中
app.include_router(router)

# 运行应用程序

# 运行应用程序
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
