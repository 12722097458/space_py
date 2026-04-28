from fastapi import APIRouter

from app.schemas.demo import (
    AddResponse,
    ApiResponse,
    DemoPostResponse,
    DemoRequest,
    MessageResponse,
)
from app.services.demo_service import add_numbers, build_echo_message
from app.utils.response import success_response

router = APIRouter()


@router.get("/", response_model=ApiResponse[MessageResponse])
def read_root() -> ApiResponse[MessageResponse]:
    return ApiResponse[MessageResponse](
        **success_response(MessageResponse(message="Hello from FastAPI").model_dump())
    )


@router.get("/add", response_model=ApiResponse[AddResponse])
def add(a: int, b: int) -> ApiResponse[AddResponse]:
    return ApiResponse[AddResponse](**success_response(AddResponse(result=add_numbers(a, b)).model_dump()))


@router.post("/echo", response_model=ApiResponse[DemoPostResponse])
def echo(payload: DemoRequest) -> ApiResponse[DemoPostResponse]:
    return ApiResponse[DemoPostResponse](
        **success_response(
            DemoPostResponse(
                name=payload.name,
                age=payload.age,
                message=build_echo_message(payload.name, payload.age),
            ).model_dump()
        )
    )
