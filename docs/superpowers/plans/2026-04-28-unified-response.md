# Unified Response Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Wrap all demo API responses in one consistent envelope for both success and validation error cases.

**Architecture:** Add simple response envelope schemas in `app/schemas/demo.py`, then update each route in `app/api/demo.py` to return `code`, `message`, and `data`. Keep validation in Pydantic and update the global validation exception handler in `app/main.py` to return the same top-level envelope plus an `errors` list.

**Tech Stack:** Python, FastAPI, Pydantic, Pytest

---

### Task 1: Add failing tests for unified response envelope

**Files:**
- Modify: `tests/test_app.py`
- Test: `tests/test_app.py`

- [ ] **Step 1: Write the failing tests**

```python
def test_root_returns_unified_response():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "code": 0,
        "message": "success",
        "data": {"message": "Hello from FastAPI"},
    }


def test_add_returns_unified_response():
    response = client.get("/add", params={"a": 3, "b": 4})

    assert response.status_code == 200
    assert response.json() == {
        "code": 0,
        "message": "success",
        "data": {"result": 7},
    }


def test_echo_returns_unified_response():
    response = client.post("/echo", json={"name": "Alice", "age": 18})

    assert response.status_code == 200
    assert response.json() == {
        "code": 0,
        "message": "success",
        "data": {
            "name": "Alice",
            "age": 18,
            "message": "你好，Alice，你今年 18 岁。",
        },
    }


def test_echo_returns_unified_validation_errors_in_chinese():
    response = client.post("/echo", json={"name": "", "age": -1})

    assert response.status_code == 422
    assert response.json() == {
        "code": 422,
        "message": "请求参数校验失败",
        "data": None,
        "errors": [
            "name 长度不能少于 2",
            "age 不能小于 0",
        ],
    }
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_app.py -v`
Expected: FAIL because the current API returns mixed response shapes.

- [ ] **Step 3: Write minimal implementation**

```python
class ResponseEnvelope(BaseModel):
    code: int
    message: str
    data: dict | None


class ErrorResponseEnvelope(ResponseEnvelope):
    errors: list[str]
```

```python
return ResponseEnvelope(
    code=0,
    message="success",
    data={"result": 7},
)
```

```python
return JSONResponse(
    status_code=422,
    content={
        "code": 422,
        "message": "请求参数校验失败",
        "data": None,
        "errors": [...],
    },
)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_app.py -v`
Expected: PASS

### Task 2: Update README unified examples

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update success and error examples**

```markdown
成功响应示例：

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "name": "Alice",
    "age": 18,
    "message": "你好，Alice，你今年 18 岁。"
  }
}
```

错误响应示例：

```json
{
  "code": 422,
  "message": "请求参数校验失败",
  "data": null,
  "errors": [
    "name 长度不能少于 2",
    "age 不能小于 0"
  ]
}
```
```

- [ ] **Step 2: Verify tests still pass**

Run: `python -m pytest tests/test_app.py -v`
Expected: PASS
