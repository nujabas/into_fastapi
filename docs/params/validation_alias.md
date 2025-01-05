在FastAPI中，`Query` 的 `validation_alias` 参数用于指定一个别名，该别名仅在数据验证过程中使用。这在处理复杂的请求结构或需要兼容旧API时特别有用。通过使用 `validation_alias`，可以将请求参数映射到不同的变量名以用于数据验证，而不会影响实际代码中的参数名。

以下是一个示例，展示了如何使用 `validation_alias` 参数：

```python
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    item_id: str = Query(..., alias="item-id", validation_alias="item_id"),
    user_id: str = Query(None, alias="user-id", validation_alias="user_id")
):
    return {"item_id": item_id, "user_id": user_id}
```

在这个示例中：

- `item_id` 参数的别名是 `item-id`，并且 `validation_alias` 设置为 `item_id`。
- `user_id` 参数的别名是 `user-id`，并且 `validation_alias` 设置为 `user_id`。

当请求发送到 `/items/?item-id=123&user-id=456` 时，FastAPI 会使用 `item-id` 和 `user-id` 作为请求参数名进行匹配，但在数据验证过程中，会使用 `item_id` 和 `user_id` 进行验证。这样可以使数据验证逻辑与请求参数名分离，提供更大的灵活性。

这种方式特别适合需要兼容旧版API或需要在验证过程中使用不同参数名的情况。