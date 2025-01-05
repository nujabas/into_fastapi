在FastAPI中，`Query` 的 `default_factory` 参数用于生成默认值。它是一个可调用对象（通常是函数），在请求时调用以生成默认值。这在需要动态生成默认值的情况下非常有用，例如根据当前时间生成一个默认值。

以下是一个使用 `default_factory` 的示例：

```python
from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI()

# 定义一个函数来生成默认值
def get_current_time():
    return datetime.now().isoformat()

@app.get("/items/")
async def read_items(timestamp: str = Query(default_factory=get_current_time)):
    return {"timestamp": timestamp}
```

在这个例子中，`get_current_time` 函数用于生成当前时间的默认值。如果请求中没有提供 `timestamp` 参数，FastAPI 会调用 `get_current_time` 函数并使用它的返回值作为默认值。

这种方式在需要动态计算默认值的情况下非常方便，而不是使用静态的默认值。