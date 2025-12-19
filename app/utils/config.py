from pydantic_settings import BaseSettings
from typing import Dict, Any

class LangChainRAGConfig(BaseSettings):
    """LangChain RAG检索器配置"""
    enabled: bool = True
    config: Dict[str, Any] = {
        "persist_dir": "./data/rag_db",
        "collection_name": "rag",
        "chunk_size": 500,
        "chunk_overlap": 50,
        "top_k": 5
    }

class GraphRAGConfig(BaseSettings):
    """GraphRAG检索器配置"""
    enabled: bool = False
    config: Dict[str, Any] = {
        "data_dir": "./data/graphrag",
        "lancedb_uri": "./data/graphrag/lancedb"
    }

class RetrievalConfig(BaseSettings):
    """检索器配置"""
    langchain_rag: LangChainRAGConfig = LangChainRAGConfig()
    graphrag: GraphRAGConfig = GraphRAGConfig()

# 全局配置实例
_retrieval_config = RetrievalConfig()

def get_retrieval_config() -> RetrievalConfig:
    """获取检索器配置"""
    return _retrieval_config
