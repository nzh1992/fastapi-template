from typing import Optional, Union
from pydantic import BaseModel

from app.schemas.base import BaseResponse


def make_response(code: int = 0,
                  message: str = "ok",
                  data: Union[BaseModel, None]=None) -> BaseResponse:
    if isinstance(data, BaseResponse):
        data = data.model_dump()

    base_response = BaseResponse(code=code, message=message, data=data)
    return base_response
