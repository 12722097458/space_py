# Echo Validation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a beginner-friendly validation failure example to `POST /echo` and document the resulting `422` behavior.

**Architecture:** Keep the current layered structure unchanged and implement validation through Pydantic field constraints on the request schema. Add one focused failing test for invalid input, then document both the invalid request example and the expected validation failure behavior in Chinese.

**Tech Stack:** Python, FastAPI, Pydantic, Pytest, HTTPX

---

### Task 1: Add validation failure test first

**Files:**
- Modify: `tests/test_app.py`
- Test: `tests/test_app.py`

- [ ] **Step 1: Write the failing test**

```python
def test_echo_returns_422_for_invalid_payload():
    response = client.post("/echo", json={"name": "", "age": -1})

    assert response.status_code == 422
    detail = response.json()["detail"]
    assert len(detail) >= 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_app.py -v`
Expected: FAIL because the current schema accepts the invalid payload.

- [ ] **Step 3: Write minimal implementation**

```python
from pydantic import BaseModel, Field


class DemoRequest(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=0)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_app.py -v`
Expected: PASS

### Task 2: Document the validation failure example

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add invalid request example to README**

```markdown
`POST /echo` 参数校验失败示例：

```json
{
  "name": "",
  "age": -1
}
```

预期现象：
- 返回状态码 `422`
- 返回字段校验错误信息
```

- [ ] **Step 2: Verify tests still pass**

Run: `python -m pytest tests/test_app.py -v`
Expected: PASS
