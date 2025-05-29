from fastapi import APIRouter

from app.schemas.base import BaseResponse
from app.schemas.auth import LoginResponse
from app.utils.response import make_response

router = APIRouter()


@router.get('/login', response_model=BaseResponse)
def login():
    login_response = LoginResponse(access_token="aa", token_type="Bearer", expires_in=3600)
    return make_response(data=login_response)
