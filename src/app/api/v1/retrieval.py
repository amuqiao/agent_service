from fastapi import APIRouter, Depends, HTTPException
from typing import Dict
from app.services.retrieval_service import RetrievalService
from app.schemas.retrieval import RetrievalRequest, RetrievalResponse

router = APIRouter(prefix="/retrieval", tags=["retrieval"])

@router.post("/query", response_model=RetrievalResponse)
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
