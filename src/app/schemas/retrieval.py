from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class RetrievalRequest(BaseModel):
    """检索请求模型"""
    retriever_name: str = Field(..., description="检索器名称")
    query: str = Field(..., description="检索查询语句")
    kwargs: Optional[Dict[str, Any]] = Field(default={}, description="额外参数")

class RetrievalResponse(BaseModel):
    """检索响应模型"""
    query: str = Field(..., description="检索查询语句")
    retriever: str = Field(..., description="使用的检索器名称")
    result: Dict[str, Any] = Field(..., description="检索结果")
