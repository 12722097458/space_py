# FastAPI Demo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a minimal FastAPI application with a demo function, tests, dependency file, and README usage instructions.

**Architecture:** Keep the project simple by adding a small `app/main.py` FastAPI entrypoint. Put behavior behind one small helper function and expose it through two GET routes. Add a focused test file using FastAPI's test client and document how to run the app.

**Tech Stack:** Python, FastAPI, Uvicorn, Pytest

---

### Task 1: Add failing API tests

**Files:**
- Create: `tests/test_app.py`
- Test: `tests/test_app.py`

- [ ] **Step 1: Write the failing test**

```python
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_welcome_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello from FastAPI"


def test_add_returns_sum():
    response = client.get("/add", params={"a": 3, "b": 4})

    assert response.status_code == 200
    assert response.json() == {"result": 7}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_app.py -v`
Expected: FAIL because `app.main` does not exist yet.

- [ ] **Step 3: Write minimal implementation**

```python
from fastapi import FastAPI

app = FastAPI()


def add_numbers(a: int, b: int) -> int:
    return a + b


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}


@app.get("/add")
def add(a: int, b: int) -> dict[str, int]:
    return {"result": add_numbers(a, b)}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_app.py -v`
Expected: PASS

### Task 2: Add dependency file and usage docs

**Files:**
- Create: `requirements.txt`
- Modify: `README.md`

- [ ] **Step 1: Add runtime and test dependencies**

```text
fastapi
uvicorn
pytest
httpx
```

- [ ] **Step 2: Update README with exact usage**

```markdown
# space_py

A beginner-friendly Python study project with a minimal FastAPI demo.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

## Open in browser

- API root: `http://127.0.0.1:8000/`
- Swagger UI: `http://127.0.0.1:8000/docs`
- Add demo: `http://127.0.0.1:8000/add?a=1&b=2`

## Run tests

```bash
pytest tests/test_app.py -v
```
```

- [ ] **Step 3: Verify docs match implementation**

Run: `uvicorn app.main:app --reload`
Expected: server starts and routes above are reachable.
