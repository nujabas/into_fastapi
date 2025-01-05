在FastAPI中，`Query` 的 `serialization_alias` 参数用于指定在响应中序列化数据时使用的别名。这在以下情况下特别有用：

1. **一致性**：你可能希望在API请求和响应中使用不同的字段名称，以保持一致性或遵循特定的命名约定。
2. **兼容性**：当你需要与旧版API兼容时，可以使用不同的字段名称进行序列化。

以下是一个示例，展示了如何使用 `serialization_alias` 参数：

```python
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class ItemResponseModel(BaseModel):
    item_id: str = Field(serialization_alias="item-id")
    user_id: str = Field(serialization_alias="user-id")

@app.get("/items/", response_model=ItemResponseModel)
async def read_items(
    item_id: str = Query(..., serialization_alias="item-id"),
    user_id: str = Query(None, serialization_alias="user-id")
):
    return {"item_id": item_id, "user_id": user_id}
```

在这个示例中：

- `item_id` 和 `user_id` 是查询参数，它们在响应中会使用 `serialization_alias` 指定的别名，即 `item-id` 和 `user-id`。
- `ItemResponseModel` 是响应模型，`Config` 类中的 `fields` 配置指定了序列化时使用的别名。

当请求发送到 `/items/?item_id=123&user_id=456` 时，响应将会是：

```json
{
  "item-id": "123",
  "user-id": "456"
}
```

这样，你可以在请求中使用原始字段名称，同时在响应中使用指定的别名进行序列化。这在需要保持API的一致性或与旧版API兼容时非常有用。