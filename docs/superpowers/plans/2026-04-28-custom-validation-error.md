# Custom Validation Error Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a global Chinese validation error response for request body failures while keeping existing FastAPI endpoints unchanged.

**Architecture:** Keep request validation in Pydantic and intercept FastAPI's validation exception globally in `app/main.py`. Translate the small set of current demo validation failures into beginner-friendly Chinese messages, then update tests and README to reflect the custom response shape.

**Tech Stack:** Python, FastAPI, Pydantic, Pytest

---

### Task 1: Add failing test for custom validation response

**Files:**
- Modify: `tests/test_app.py`
- Test: `tests/test_app.py`

- [ ] **Step 1: Write the failing test**

```python
def test_echo_returns_custom_validation_errors_in_chinese():
    response = client.post("/echo", json={"name": "", "age": -1})

    assert response.status_code == 422
    assert response.json() == {
        "message": "请求参数校验失败",
        "errors": [
            "name 长度不能少于 2",
            "age 不能小于 0",
        ],
    }
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_app.py -v`
Expected: FAIL because the current app returns the default FastAPI validation payload.

- [ ] **Step 3: Write minimal implementation**

```python
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def build_validation_message(error: dict) -> str:
    field_name = error["loc"][-1]
    error_type = error["type"]

    if field_name == "name" and error_type == "string_too_short":
        return "name 长度不能少于 2"
    if field_name == "age" and error_type == "greater_than_equal":
        return "age 不能小于 0"
    return f"{field_name} 参数不合法"


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "message": "请求参数校验失败",
            "errors": [build_validation_message(error) for error in exc.errors()],
        },
    )
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_app.py -v`
Expected: PASS

### Task 2: Update Chinese README examples

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add custom Chinese validation response example**

```markdown
自定义错误返回示例：

```json
{
  "message": "请求参数校验失败",
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
