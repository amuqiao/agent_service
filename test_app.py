from run import app
import asyncio

async def test_root_route():
    """测试根路径路由"""
    # 创建一个模拟请求
    from fastapi.testclient import TestClient
    client = TestClient(app)
    
    # 发送GET请求到根路径
    response = client.get("/")
    
    # 打印结果
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # 验证结果
    assert response.status_code == 200
    assert "message" in response.json()
    print("测试通过！")

if __name__ == "__main__":
    # 运行测试
    asyncio.run(test_root_route())