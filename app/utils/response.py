def success_response(data: dict) -> dict:
    return {
        "code": 0,
        "message": "success",
        "data": data,
    }


def error_response(code: int, message: str, errors: list[str], data: dict | None = None) -> dict:
    return {
        "code": code,
        "message": message,
        "data": data,
        "errors": errors,
    }
