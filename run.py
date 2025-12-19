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
    import argparse
    import os
    
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(
        description="Agent Service API Server",
        epilog="""
使用示例：

1. 默认方式运行（开启热重载）：
   python run.py

2. 关闭热重载模式运行：
   python run.py --no-reload

3. 指定主机和端口运行：
   python run.py --host 127.0.0.1 --port 8080

4. 使用环境变量配置：
   export UVICORN_RELOAD=false UVICORN_HOST=127.0.0.1 UVICORN_PORT=8080
   python run.py

5. 查看帮助信息：
   python run.py -h
   """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # 添加reload参数
    parser.add_argument(
        "--reload", 
        action="store_true", 
        default=os.getenv("UVICORN_RELOAD", "true").lower() == "true",
        help="Enable hot reload mode (default: true)"
    )
    
    # 添加host参数
    parser.add_argument(
        "--host", 
        type=str, 
        default=os.getenv("UVICORN_HOST", "0.0.0.0"),
        help="Host to bind (default: 0.0.0.0)"
    )
    
    # 添加port参数
    parser.add_argument(
        "--port", 
        type=int, 
        default=int(os.getenv("UVICORN_PORT", "8000")),
        help="Port to bind (default: 8000)"
    )
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 显示API文档访问地址
    # 如果是本地服务器，使用localhost而不是0.0.0.0或127.0.0.1
    display_host = args.host
    if args.host in ("0.0.0.0", "127.0.0.1"):
        display_host = "localhost"
    
    print("\nAgent Service API Server 已启动")
    print("=====================================")
    print(f"服务地址: http://{args.host}:{args.port}")
    print(f"Swagger UI: http://{display_host}:{args.port}/docs")
    print(f"ReDoc: http://{display_host}:{args.port}/redoc")
    print("=====================================")
    print("按 Ctrl+C 停止服务\n")
    
    # 运行uvicorn服务器
    if args.reload:
        # 当启用reload模式时，需要使用导入字符串
        uvicorn.run(
            "run:app", 
            host=args.host, 
            port=args.port, 
            reload=True
        )
    else:
        # 非reload模式可以直接传递应用对象
        uvicorn.run(
            app, 
            host=args.host, 
            port=args.port,
            reload=False
        )
