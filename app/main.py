from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.demo import router as demo_router
from app.utils.response import error_response


def build_validation_message(error: dict) -> str:
    field_name = error["loc"][-1]
    error_type = error["type"]

    if field_name == "name" and error_type == "string_too_short":
        return "name 长度不能少于 2"
    if field_name == "age" and error_type == "greater_than_equal":
        return "age 不能小于 0"

    return f"{field_name} 参数不合法"


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content=error_response(
            code=422,
            message="请求参数校验失败",
            data=None,
            errors=[build_validation_message(error) for error in exc.errors()],
        ),
    )


app.include_router(demo_router)
