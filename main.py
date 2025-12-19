from fastapi import FastAPI
from app.api.v1 import agent_router, retrieval_router
from app.utils.config import get_retrieval_config
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

app = FastAPI(
    title="Agent Service API",
    description="基于FastAPI的MVC架构Agent服务",
    version="1.0.0"
)

# 注册路由
app.include_router(agent_router, prefix="/api/v1")
app.include_router(retrieval_router, prefix="/api/v1")

@app.get("/")
async def root():
    """根路径，返回服务状态"""
    return {
        "message": "Agent Service is running",
        "version": "1.0.0",
        "retrievers": list(get_retrieval_config().dict().keys())
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
