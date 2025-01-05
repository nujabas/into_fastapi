在FastAPI中，`Query` 的 `alias` 参数用于指定请求参数的别名。这在以下情况下非常有用：

1. **处理保留字或不合法的参数名称**：如果请求参数名称是Python保留字或不合法的Python变量名，可以使用别名来解决。
2. **提高参数可读性**：可以使用更简短或更具描述性的名称来提高API的可读性。

以下是一个示例，展示了如何使用 `alias` 参数：

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    item_id: str = Query(..., alias="item-id"),
    user_id: str = Query(None, alias="user-id")
):
    return {"item_id": item_id, "user_id": user_id}
```

在这个示例中：

- `item_id` 和 `user_id` 是函数参数的名称。
- 通过 `alias` 参数，将请求参数 `item-id` 和 `user-id` 映射到 `item_id` 和 `user_id` 变量。

当请求发送到 `/items/?item-id=123&user-id=456` 时，FastAPI 会将 `item-id` 和 `user-id` 的值分别传递给 `item_id` 和 `user_id` 参数。

这种方式使得API能够使用更友好的URL参数，同时保持代码中的变量名符合Python的命名规范。