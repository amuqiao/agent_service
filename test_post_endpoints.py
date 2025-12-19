import requests
import time

# 等待服务启动
print("等待服务启动...")
time.sleep(2)

# 测试检索接口 POST /api/v1/retrieval/query
print("\n=== 测试检索接口 POST /api/v1/retrieval/query ===")
try:
    # 使用示例请求体
    payload = {
        "retriever_name": "langchain_rag",
        "query": "什么是向量数据库？",
        "kwargs": {}
    }
    r = requests.post('http://localhost:8000/api/v1/retrieval/query', json=payload, timeout=10)
    print(f"状态码: {r.status_code}")
    if r.status_code == 200:
        print(f"✓ 成功！响应: {r.json()}")
    else:
        print(f"✗ 失败！状态码: {r.status_code}, 响应: {r.text}")
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
    r = requests.post('http://localhost:8000/api/v1/agent/query', json=payload, timeout=10)
    print(f"状态码: {r.status_code}")
    if r.status_code == 200:
        print(f"✓ 成功！响应: {r.json()}")
    else:
        print(f"✗ 失败！状态码: {r.status_code}, 响应: {r.text}")
except Exception as e:
    print(f"✗ 错误: {e}")

print("\n=== 所有POST接口测试完成 ===")
