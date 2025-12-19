from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class AgentRequest(BaseModel):
    """Agent查询请求模型"""
    query: str = Field(..., description="查询内容")
    retriever_name: Optional[str] = Field(default="langchain_rag", description="检索器名称")
    kwargs: Optional[Dict[str, Any]] = Field(default={}, description="额外参数")

class AgentResponse(BaseModel):
    """Agent查询响应模型"""
    query: str = Field(..., description="查询内容")
    retriever: str = Field(..., description="使用的检索器名称")
    result: Dict[str, Any] = Field(..., description="查询结果")
