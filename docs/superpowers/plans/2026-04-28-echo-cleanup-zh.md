# Echo Cleanup Zh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a beginner-friendly `POST /echo` endpoint, remove archived practice scripts from the project root, and rewrite the README in Chinese.

**Architecture:** Reuse the existing layered FastAPI layout by extending `schemas`, `services`, and `api` with one POST example. Keep behavior simple and explicit, then remove only those root scripts that already exist under `scripts/`, and update documentation to match the new structure and endpoints.

**Tech Stack:** Python, FastAPI, Uvicorn, Pytest, HTTPX

---

### Task 1: Add POST /echo with TDD

**Files:**
- Modify: `tests/test_app.py`
- Modify: `app/schemas/demo.py`
- Modify: `app/services/demo_service.py`
- Modify: `app/api/demo.py`
- Test: `tests/test_app.py`

- [ ] **Step 1: Write the failing test**

```python
def test_echo_returns_request_data_and_message():
    response = client.post("/echo", json={"name": "Alice", "age": 18})

    assert response.status_code == 200
    assert response.json() == {
        "name": "Alice",
        "age": 18,
        "message": "你好，Alice，你今年 18 岁。",
    }
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_app.py -v`
Expected: FAIL because `/echo` does not exist yet.

- [ ] **Step 3: Write minimal implementation**

```python
from pydantic import BaseModel


class DemoRequest(BaseModel):
    name: str
    age: int


class DemoPostResponse(BaseModel):
    name: str
    age: int
    message: str
```

```python
def add_numbers(a: int, b: int) -> int:
    return a + b


def build_echo_message(name: str, age: int) -> str:
    return f"你好，{name}，你今年 {age} 岁。"
```

```python
@router.post("/echo", response_model=DemoPostResponse)
def echo(payload: DemoRequest) -> DemoPostResponse:
    return DemoPostResponse(
        name=payload.name,
        age=payload.age,
        message=build_echo_message(payload.name, payload.age),
    )
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_app.py -v`
Expected: PASS

### Task 2: Remove root-level archived scripts

**Files:**
- Delete: `HelloWorld.py`
- Delete: `Test2.py`
- Delete: `Test3.py`
- Delete: `Test4.py`
- Delete: `Test5.py`
- Delete: `Test6.py`
- Delete: `Test7.py`

- [ ] **Step 1: Verify script copies exist under `scripts/`**

Check that each root file has the corresponding file under `scripts/`.

- [ ] **Step 2: Delete only duplicated root-level scripts**

Remove `HelloWorld.py`, `Test2.py`, `Test3.py`, `Test4.py`, `Test5.py`, `Test6.py`, and `Test7.py` from the project root.

- [ ] **Step 3: Run tests after cleanup**

Run: `python -m pytest tests/test_app.py -v`
Expected: PASS

### Task 3: Rewrite README in Chinese

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Replace English README with Chinese project guide**

```markdown
# space_py

一个适合 Python 新手学习的项目，当前包含一个最小可运行的 FastAPI 示例。

## 项目结构

- `app/main.py`：FastAPI 应用入口
- `app/api/`：接口层，负责定义路由
- `app/services/`：业务逻辑层
- `app/schemas/`：数据模型层
- `tests/`：接口测试
- `scripts/`：练习脚本归档目录
- `tools/`：工具脚本

## 安装运行依赖

```bash
pip install -r requirements.txt
```

## 安装开发依赖

```bash
pip install -r requirements-dev.txt
```

## 启动项目

```bash
uvicorn app.main:app --reload
```

## 接口示例

- `GET /`
- `GET /add?a=1&b=2`
- `POST /echo`

请求体示例：

```json
{
  "name": "Alice",
  "age": 18
}
```

## 运行测试

```bash
python -m pytest tests/test_app.py -v
```
```

- [ ] **Step 2: Verify README matches implementation**

Run: `python -m pytest tests/test_app.py -v`
Expected: PASS
