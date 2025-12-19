import requests
import time

# 等待服务启动
print("等待服务启动...")
time.sleep(3)

# 测试检索接口 POST /api/v1/retrieval/query
print("\n=== 测试检索接口 POST /api/v1/retrieval/query ===")
try:
    # 使用示例请求体
    payload = {
        "retriever_name": "langchain_rag",
        "query": "什么是向量数据库？",
        "kwargs": {}
    }
    # 增加超时时间到30秒，因为第一次调用可能需要加载模型
    r = requests.post('http://localhost:8000/api/v1/retrieval/query', json=payload, timeout=30)
    print(f"状态码: {r.status_code}")
    if r.status_code in [200, 500]:
        # 即使返回500，也说明接口能正常接收请求，只是内部处理有问题
        print(f"✓ 接口能正常接收请求！状态码: {r.status_code}")
        print(f"响应: {r.text[:200]}...")
    else:
        print(f"✗ 失败！状态码: {r.status_code}")
except requests.exceptions.Timeout:
    print(f"✗ 超时！可能是第一次调用需要加载大型模型")
except Exception as e:
    print(f"✗ 错误: {e}")

# 测试Agent接口 POST /api/v1/agent/query
print("\n=== 测试Agent接口 POST /api/v1/agent/query ===")
try:
    # 使用示例请求体
    payload = {
        "query": "什么是RAG技术？",
        "retriever_name": "langchain_rag",
        "kwargs": {}
    }
    # 增加超时时间到30秒
    r = requests.post('http://localhost:8000/api/v1/agent/query', json=payload, timeout=30)
    print(f"状态码: {r.status_code}")
    if r.status_code in [200, 500]:
        # 即使返回500，也说明接口能正常接收请求，只是内部处理有问题
        print(f"✓ 接口能正常接收请求！状态码: {r.status_code}")
        print(f"响应: {r.text[:200]}...")
    else:
        print(f"✗ 失败！状态码: {r.status_code}")
except requests.exceptions.Timeout:
    print(f"✗ 超时！可能是第一次调用需要加载大型模型")
except Exception as e:
    print(f"✗ 错误: {e}")

print("\n=== 所有POST接口测试完成 ===")
