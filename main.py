import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from app.api import api_router
from app.core.config import Settings
from app.utils.response import make_response
from app.core.config import get_settings


# 加载配置
settings = get_settings()

app = FastAPI(
    # API的标题
    title=settings.API_TITLE,
    # API简短描述。可以使用Markdown
    description=settings.API_DESCRIPTION,
    # API的简短摘要
    summary=settings.API_SUMMARY,
    # API的版本号
    version=settings.API_VERSION,
    # API的服务条款的URL。如果提供，必须是URL。
    terms_of_service=None,
    # 公开的API的联系信息，dict类型，可以包含多个字段
    contact={
        "name": settings.API_CONTACT_NAME,
        "url": settings.API_CONTACT_URL,
        "email": settings.API_CONTACT_EMAIL,
    },
    # 公开的API的许可证信息，dict类型，可以包含多个字段
    license_info={
        "name": settings.API_LICENSE_NAME,
        "url": settings.API_LICENSE_URL,
        "identifier": settings.API_LICENSE_IDENTIFIER,
    }
)


# 注册路由
app.include_router(api_router)


# 全局异常处理
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    err_resp = {
        "code": 1,
        "msg": exc.detail,
    }
    return JSONResponse(status_code=400, content=err_resp)


if __name__ == '__main__':
    uvicorn.run(app)