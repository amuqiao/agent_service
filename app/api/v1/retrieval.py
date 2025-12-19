from fastapi import APIRouter, Depends, HTTPException
from typing import Dict
from app.services.retrieval_service import RetrievalService
from app.schemas.retrieval import RetrievalRequest, RetrievalResponse

router = APIRouter(prefix="/retrieval", tags=["retrieval"])

@router.post("/query", response_model=RetrievalResponse, 
             openapi_extra={
                 "requestBody": {
                     "content": {
                         "application/json": {
                             "examples": {
                                 "默认示例": {
                                     "summary": "默认检索示例",
                                     "description": "使用默认配置执行检索",
                                     "value": {
                                         "retriever_name": "langchain_rag",
                                         "query": "什么是向量数据库？",
                                         "kwargs": {}
                                     }
                                 },
                                 "自定义参数示例": {
                                     "summary": "带自定义参数的检索示例",
                                     "description": "使用自定义参数执行检索",
                                     "value": {
                                         "retriever_name": "langchain_rag",
                                         "query": "介绍一下Chroma DB",
                                         "kwargs": {"top_k": 5}
                                     }
                                 }
                             }
                         }
                     }
                 }
             })
async def retrieve(
    request: RetrievalRequest,
    retrieval_service: RetrievalService = Depends()
):
    """执行检索请求"""
    try:
        result = retrieval_service.retrieve(
            retriever_name=request.retriever_name,
            query=request.query,
            **request.kwargs
        )
        return RetrievalResponse(
            query=request.query,
            retriever=request.retriever_name,
            result=result
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"检索失败: {str(e)}")

@router.get("/retrievers", response_model=Dict[str, str])
async def list_retrievers(
    retrieval_service: RetrievalService = Depends()
):
    """列出所有可用的检索器"""
    return retrieval_service.list_retrievers()
