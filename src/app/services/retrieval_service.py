from typing import Dict, Any
from app.models.retrieval import RetrievalInterface, LangChainRetriever
from app.utils.config import get_retrieval_config

class RetrievalService:
    """检索服务，管理不同的检索器"""
    
    def __init__(self):
        self.retrievers: Dict[str, RetrievalInterface] = {}
        self._init_retrievers()
    
    def _init_retrievers(self):
        """初始化所有配置的检索器"""
        config = get_retrieval_config()
        
        # 初始化LangChain RAG检索器
        if config.langchain_rag.enabled:
            self.retrievers["langchain_rag"] = LangChainRetriever(config.langchain_rag.config)
        
        # 初始化GraphRAG检索器（待实现）
        # if config.graphrag.enabled:
        #     from app.models.retrieval import GraphRAGRetriever
        #     self.retrievers["graphrag"] = GraphRAGRetriever(config.graphrag.config)
    
    def get_retriever(self, retriever_name: str) -> RetrievalInterface:
        """获取指定名称的检索器"""
        if retriever_name not in self.retrievers:
            raise ValueError(f"Retriever {retriever_name} not found")
        return self.retrievers[retriever_name]
    
    def retrieve(self, retriever_name: str, query: str, **kwargs) -> Dict[str, Any]:
        """调用指定检索器执行检索"""
        retriever = self.get_retriever(retriever_name)
        return retriever.retrieve(query, **kwargs)
    
    def list_retrievers(self) -> Dict[str, str]:
        """列出所有可用的检索器"""
        return {
            name: retriever.get_name()
            for name, retriever in self.retrievers.items()
        }
