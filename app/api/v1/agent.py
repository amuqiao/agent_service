from fastapi import APIRouter, Depends, HTTPException
from app.services.retrieval_service import RetrievalService
from app.schemas.agent import AgentRequest, AgentResponse

router = APIRouter(prefix="/agent", tags=["agent"])

@router.post("/query", response_model=AgentResponse)
async def agent_query(
    request: AgentRequest,
    retrieval_service: RetrievalService = Depends()
):
    """执行Agent查询请求"""
    try:
        # 执行检索
        retrieval_result = retrieval_service.retrieve(
            retriever_name=request.retriever_name,
            query=request.query,
            **request.kwargs
        )
        
        # 这里可以添加LLM调用逻辑，整合检索结果生成最终回答
        # 目前简单返回检索结果
        return AgentResponse(
            query=request.query,
            retriever=request.retriever_name,
            result=retrieval_result
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent查询失败: {str(e)}")
