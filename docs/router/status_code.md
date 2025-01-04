在FastAPI中，你可以使用`APIRouter`类的`status_code`参数来指定路径操作函数的默认响应状态码。这样可以使代码更加清晰，并且自动生成的API文档也会更加准确。

以下是一个示例，展示了如何使用`APIRouter`类中的`status_code`参数：

### 示例代码

```python
from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

# 定义Pydantic模型
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = 0.0

# 创建FastAPI应用实例
app = FastAPI()

# 创建APIRouter实例
router = APIRouter()

# 定义一个路径操作函数，并指定status_code
@router.post("/items/", status_code=201)
async def create_item(item: Item):
    return item

# 定义另一个路径操作函数，返回404状态码
@router.get("/items/{item_id}", status_code=200)
async def read_item(item_id: int):
    if item_id != 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": "Sample Item"}

# 将router包含到FastAPI应用中
app.include_router(router)

# 运行应用程序
```

### 代码解释

1. **定义Pydantic模型**：
   - `Item`模型表示输入的数据结构，包括名称、描述、价格和税。

2. **创建FastAPI应用实例**：
   - 使用`FastAPI()`创建一个应用实例。

3. **创建APIRouter实例**：
   - 使用`APIRouter()`创建一个路由器实例。

4. **定义路径操作函数并指定`status_code`**：
   - 使用`@router.post("/items/", status_code=201)`装饰器定义一个路径操作函数`create_item`，并指定默认响应状态码为201（Created）。这个函数接收`Item`类型的输入数据，并返回该数据。
   - 使用`@router.get("/items/{item_id}", status_code=200)`装饰器定义另一个路径操作函数`read_item`，默认响应状态码为200（OK）。这个函数检查`item_id`是否为1，如果不是，则抛出404状态码的HTTP异常。

5. **将router包含到FastAPI应用中**：
   - 使用`app.include_router(router)`将路由器包含到FastAPI应用中。

### 运行示例

1. 运行FastAPI应用程序。
2. 发送一个`POST`请求到`http://127.0.0.1:8000/items/`，请求体如下：

```json
{
  "name": "Example Item",
  "description": "This is an example item",
  "price": 100.0,
  "tax": 20.0
}
```

响应头将包含状态码201，响应体为：

```json
{
  "name": "Example Item",
  "description": "This is an example item",
  "price": 100.0,
  "tax": 20.0
}
```

3. 发送一个`GET`请求到`http://127.0.0.1:8000/items/1`，响应状态码为200，响应体为：

```json
{
  "item_id": 1,
  "name": "Sample Item"
}
```

4. 发送一个`GET`请求到`http://127.0.0.1:8000/items/2`，响应状态码为404，响应体为：

```json
{
  "detail": "Item not found"
}
```

### 结论

通过使用`APIRouter`类的`status_code`参数，你可以指定路径操作函数的默认响应状态码，使代码更加清晰，并且确保自动生成的API文档准确反映端点的行为。