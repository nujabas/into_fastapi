在FastAPI中，`APIRouter`类用于创建路由对象，并将多个路径操作函数（endpoint）组织在一起，从而简化应用程序的结构和管理。`APIRouter`类的一个重要组件是endpoint，它是一个处理特定HTTP请求的函数。

### 什么是endpoint？

在FastAPI中，endpoint是一个函数，它负责处理特定的HTTP请求并返回响应。每个endpoint与一个或多个HTTP方法（如GET、POST、PUT、DELETE等）和一个URL路径相关联。当FastAPI接收到一个匹配的请求时，它会调用相应的endpoint函数来处理请求。

### 为什么endpoint是Callable类型？

在Python中，`Callable`是一个类型提示，它表示对象是可调用的。也就是说，`Callable`可以是一个函数、方法或任何实现了`__call__`方法的对象。在FastAPI中，将endpoint定义为`Callable`类型是因为它们必须是可调用的，以便在收到HTTP请求时能够被调用。

### 示例

以下是一个使用`APIRouter`和endpoint的示例：

```python
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

# 定义一个endpoint
@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# 将router包含到FastAPI应用中
app.include_router(router)
```

在这个示例中：

1. 创建一个`FastAPI`应用实例。
2. 创建一个`APIRouter`实例。
3. 使用`@router.get("/items/{item_id}")`装饰器定义了一个endpoint函数`read_item`，它处理`GET`请求，并返回一个包含请求的`item_id`的JSON响应。
4. 使用`app.include_router(router)`将`APIRouter`实例包含到FastAPI应用中。

总之，endpoint是一个处理HTTP请求的函数，而将其定义为`Callable`类型是为了确保它们是可调用的，以便在接收到HTTP请求时能够正确处理并返回响应。