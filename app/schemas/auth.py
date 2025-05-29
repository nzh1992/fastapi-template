from pydantic import BaseModel

from .base import BaseResponse


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
