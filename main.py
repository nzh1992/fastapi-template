import uvicorn
from fastapi import FastAPI

from app.api import api_router


app = FastAPI()

# 注册路由
app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run(app)