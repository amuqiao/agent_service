import requests
import time

# 等待服务启动
print("等待服务启动...")
time.sleep(2)

# 测试根路径
print("\n=== 测试根路径 ===")
try:
    r = requests.get('http://localhost:8000', timeout=5)
    print(f"状态码: {r.status_code}")
    print(f"响应: {r.json()}")
except Exception as e:
    print(f"错误: {e}")

# 测试API文档
print("\n=== 测试API文档 (/docs) ===")
try:
    r = requests.get('http://localhost:8000/docs', timeout=5)
    print(f"状态码: {r.status_code}")
    if r.status_code == 200:
        print("✓ 成功！Swagger UI 可访问")
    else:
        print(f"✗ 失败！状态码: {r.status_code}")
except Exception as e:
    print(f"✗ 错误: {e}")

# 测试API接口
print("\n=== 测试API接口 (/api/v1/retrieval/retrievers) ===")
try:
    r = requests.get('http://localhost:8000/api/v1/retrieval/retrievers', timeout=5)
    print(f"状态码: {r.status_code}")
    if r.status_code == 200:
        print(f"✓ 成功！响应: {r.json()}")
    else:
        print(f"✗ 失败！状态码: {r.status_code}")
except Exception as e:
    print(f"✗ 错误: {e}")

# 测试Agent API接口
print("\n=== 测试Agent API接口 (/api/v1/agent) ===")
try:
    r = requests.get('http://localhost:8000/api/v1/agent', timeout=5)
    print(f"状态码: {r.status_code}")
    print(f"响应: {r.text[:100]}...")
except Exception as e:
    print(f"错误: {e}")

print("\n=== 测试完成 ===")
