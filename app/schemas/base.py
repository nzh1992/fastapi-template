from typing import Optional, Generic, TypeVar

from pydantic import BaseModel


T = TypeVar('T')


class BaseResponse(BaseModel, Generic[T]):
    code: int = 0
    message: str = "ok"
    data: Optional[T] = None
