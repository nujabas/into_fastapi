在FastAPI中，`Query` 的 `alias_priority` 参数用于控制请求参数别名的优先级。它允许你指定当请求中同时存在原始参数名和别名参数名时，哪个应该被优先使用。

`alias_priority` 参数接受一个整数值，默认值为 2。这个值越高，别名的优先级越高。

以下是一个示例，展示了如何使用 `alias_priority` 参数：

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    item_id: str = Query(..., alias="item-id", alias_priority=1),
    user_id: str = Query(None, alias="user-id", alias_priority=2)
):
    return {"item_id": item_id, "user_id": user_id}
```

在这个示例中：

- `item_id` 参数的别名是 `item-id`，并且 `alias_priority` 设置为 1。
- `user_id` 参数的别名是 `user-id`，并且 `alias_priority` 设置为 2。

如果请求中同时包含 `item_id` 和 `item-id` 参数，由于 `alias_priority=1` 的设置，`item-id` 会被优先使用。同理，`user-id` 因为 `alias_priority=2` 设置为较高的优先级，当请求中同时包含 `user_id` 和 `user-id` 时，`user-id` 会被优先使用。

这种方式让你能够更细粒度地控制请求参数的解析和优先级，避免冲突。