from typing import Dict, Any
from app.models.retrieval import RetrievalInterface, LangChainRetriever
from app.utils.config import get_retrieval_config

class RetrievalService:
    """检索服务，管理不同的检索器"""
    
    def __init__(self):
        self.retrievers: Dict[str, RetrievalInterface] = {}
        self.config = get_retrieval_config()
        # 延迟初始化检索器，只有在需要时才创建
    
    def _init_retrievers(self):
        """初始化所有配置的检索器"""
        if not self.retrievers:
            # 初始化LangChain RAG检索器
            if self.config.langchain_rag.enabled:
                self.retrievers["langchain_rag"] = LangChainRetriever(self.config.langchain_rag.config)
            
            # 初始化GraphRAG检索器（待实现）
            # if self.config.graphrag.enabled:
            #     from app.models.retrieval import GraphRAGRetriever
            #     self.retrievers["graphrag"] = GraphRAGRetriever(self.config.graphrag.config)
    
    def get_retriever(self, retriever_name: str) -> RetrievalInterface:
        """获取指定名称的检索器"""
        if retriever_name not in self.retrievers:
            # 延迟初始化所有检索器
            self._init_retrievers()
            if retriever_name not in self.retrievers:
                raise ValueError(f"Retriever {retriever_name} not found")
        return self.retrievers[retriever_name]
    
    def retrieve(self, retriever_name: str, query: str, **kwargs) -> Dict[str, Any]:
        """调用指定检索器执行检索"""
        retriever = self.get_retriever(retriever_name)
        return retriever.retrieve(query, **kwargs)
    
    def list_retrievers(self) -> Dict[str, str]:
        """列出所有可用的检索器"""
        # 基于配置返回可用检索器，不实际初始化
        available_retrievers = {}
        
        if self.config.langchain_rag.enabled:
            available_retrievers["langchain_rag"] = "langchain_rag"
        
        if self.config.graphrag.enabled:
            available_retrievers["graphrag"] = "graphrag"
        
        return available_retrievers
