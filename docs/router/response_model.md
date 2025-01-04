在FastAPI中，`APIRouter`类允许你定义路由和路径操作，同时可以使用`response_model`参数来指定返回的数据模型。这有助于确保API的响应符合预期的结构和类型，并自动生成文档。

以下是一个示例，展示了如何使用`APIRouter`类和`response_model`参数：

### 示例代码

```python
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import List

# 定义Pydantic模型
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = 0.0

class ItemResponseModel(BaseModel):
    name: str
    description: str
    price_with_tax: float

# 创建FastAPI应用实例
app = FastAPI()

# 创建APIRouter实例
router = APIRouter()

# 定义一个路径操作函数，并指定response_model
@router.post("/items/", response_model=ItemResponseModel)
async def create_item(item: Item):
    price_with_tax = item.price + item.tax
    return ItemResponseModel(
        name=item.name,
        description=item.description,
        price_with_tax=price_with_tax
    )

# 将router包含到FastAPI应用中
app.include_router(router)

# 运行应用程序
```

### 代码解释

1. **定义Pydantic模型**：
   - `Item`模型表示输入的数据结构，包括名称、描述、价格和税。
   - `ItemResponseModel`模型表示响应的数据结构，包括名称、描述和税后的价格。

2. **创建FastAPI应用实例**：
   - 使用`FastAPI()`创建一个应用实例。

3. **创建APIRouter实例**：
   - 使用`APIRouter()`创建一个路由器实例。

4. **定义路径操作函数**：
   - 使用`@router.post`装饰器定义一个路径操作函数`create_item`，并指定`response_model`为`ItemResponseModel`。
   - `create_item`函数接收`Item`类型的输入数据，计算税后的价格，并返回符合`ItemResponseModel`的数据。

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

3. 你将得到如下响应：

```json
{
  "name": "Example Item",
  "description": "This is an example item",
  "price_with_tax": 120.0
}
```

### 结论

通过使用`APIRouter`类和`response_model`参数，你可以轻松地定义和管理API的路由，并确保响应数据符合指定的模型。这不仅提高了代码的可维护性，还自动生成了详细的API文档。