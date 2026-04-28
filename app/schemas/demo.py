from typing import Generic, TypeVar

from pydantic import BaseModel, Field


class MessageResponse(BaseModel):
    message: str


class AddResponse(BaseModel):
    result: int


class DemoRequest(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=0)


class DemoPostResponse(BaseModel):
    name: str
    age: int
    message: str


ResponseDataT = TypeVar("ResponseDataT")


class ApiResponse(BaseModel, Generic[ResponseDataT]):
    code: int
    message: str
    data: ResponseDataT


class ErrorResponse(BaseModel):
    code: int
    message: str
    data: dict | None = None
    errors: list[str]
