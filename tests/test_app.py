from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_welcome_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "code": 0,
        "message": "success",
        "data": {"message": "Hello from FastAPI"},
    }


def test_add_returns_sum():
    response = client.get("/add", params={"a": 3, "b": 4})

    assert response.status_code == 200
    assert response.json() == {
        "code": 0,
        "message": "success",
        "data": {"result": 7},
    }


def test_echo_returns_request_data_and_message():
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
