# Project Initialization and Structure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure the learning project into a clearer FastAPI layout, archive practice scripts under `scripts/`, and add essential dependency files and documentation.

**Architecture:** Keep the app lightweight while splitting responsibilities into `main`, `api`, `services`, and `schemas`. Preserve the existing API behavior so tests stay simple, then move ad-hoc practice files into a dedicated `scripts` folder and document the structure.

**Tech Stack:** Python, FastAPI, Uvicorn, Pytest, HTTPX, Black, Ruff

---

### Task 1: Refactor API layout without changing behavior

**Files:**
- Create: `app/api/__init__.py`
- Create: `app/api/demo.py`
- Create: `app/services/__init__.py`
- Create: `app/services/demo_service.py`
- Create: `app/schemas/__init__.py`
- Create: `app/schemas/demo.py`
- Modify: `app/main.py`
- Test: `tests/test_app.py`

- [ ] **Step 1: Write the failing test**

```python
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_welcome_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI"}


def test_add_returns_sum():
    response = client.get("/add", params={"a": 3, "b": 4})

    assert response.status_code == 200
    assert response.json() == {"result": 7}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_app.py -v`
Expected: FAIL after refactor starts and before route wiring is restored.

- [ ] **Step 3: Write minimal implementation**

```python
from pydantic import BaseModel


class MessageResponse(BaseModel):
    message: str


class AddResponse(BaseModel):
    result: int
```

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

```python
from fastapi import APIRouter

from app.schemas.demo import AddResponse, MessageResponse
from app.services.demo_service import add_numbers

router = APIRouter()


@router.get("/", response_model=MessageResponse)
def read_root() -> MessageResponse:
    return MessageResponse(message="Hello from FastAPI")


@router.get("/add", response_model=AddResponse)
def add(a: int, b: int) -> AddResponse:
    return AddResponse(result=add_numbers(a, b))
```

```python
from fastapi import FastAPI

from app.api.demo import router as demo_router

app = FastAPI()
app.include_router(demo_router)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_app.py -v`
Expected: PASS

### Task 2: Add dependency files and archive practice scripts

**Files:**
- Create: `requirements-dev.txt`
- Create: `scripts/HelloWorld.py`
- Create: `scripts/Test2.py`
- Create: `scripts/Test3.py`
- Create: `scripts/Test4.py`
- Create: `scripts/Test5.py`
- Create: `scripts/Test6.py`
- Create: `scripts/Test7.py`
- Modify: `requirements.txt`

- [ ] **Step 1: Add dependency files**

```text
fastapi
uvicorn
```

```text
-r requirements.txt
pytest
httpx
black
ruff
```

- [ ] **Step 2: Move root practice scripts into `scripts/`**

Preserve the contents of `HelloWorld.py`, `Test2.py`, `Test3.py`, `Test4.py`, `Test5.py`, `Test6.py`, and `Test7.py` by moving them under `scripts/`.

- [ ] **Step 3: Verify test suite still passes**

Run: `python -m pytest tests/test_app.py -v`
Expected: PASS

### Task 3: Update README to explain structure and workflow

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Document structure and commands**

```markdown
# space_py

A beginner-friendly Python study project with a minimal FastAPI demo.

## Project structure

- `app/main.py`: FastAPI app entrypoint
- `app/api/`: route handlers
- `app/services/`: business logic
- `app/schemas/`: response models
- `tests/`: API tests
- `scripts/`: archived learning scripts
- `tools/`: utility scripts

## Install runtime dependencies

```bash
pip install -r requirements.txt
```

## Install development dependencies

```bash
pip install -r requirements-dev.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

## Run tests

```bash
python -m pytest tests/test_app.py -v
```
```

- [ ] **Step 2: Verify README commands match the project**

Run: `python -m pytest tests/test_app.py -v`
Expected: PASS
