from abc import ABC, abstractmethod
from typing import Dict, Any

class RetrievalInterface(ABC):
    """检索器接口，定义检索器的基本方法"""
    
    @abstractmethod
    def retrieve(self, query: str, **kwargs) -> Dict[str, Any]:
        """执行检索操作"""
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """获取检索器名称"""
        pass

class LangChainRetriever(RetrievalInterface):
    """基于LangChain的RAG检索器"""
    
    def __init__(self, config):
        self.config = config
        from langchain_openai import ChatOpenAI
        from langchain_huggingface.embeddings import HuggingFaceEmbeddings
        from langchain_community.vectorstores import Chroma
        from langchain_classic.chains import RetrievalQA
        import os
        
        self.llm = ChatOpenAI(
            model=os.getenv("MODEL", "qwen-plus"),
            base_url=os.getenv("BASE_URL"),
            api_key=os.getenv("API_KEY")
        )
        self.embedding = HuggingFaceEmbeddings(
            model_name=os.getenv("EMBED_MODEL_PATH", "bge-large-zh-v1.5"),
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        self.vectorstore = Chroma(
            collection_name=self.config["collection_name"],
            embedding_function=self.embedding,
            persist_directory=self.config["persist_dir"]
        )
        self.retriever = self.vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": self.config.get("top_k", 5)}
        )
    
    def retrieve(self, query: str, **kwargs) -> Dict[str, Any]:
        """执行LangChain RAG检索"""
        from langchain_classic.chains import RetrievalQA
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.retriever,
            return_source_documents=True
        )
        result = qa_chain.invoke({"query": query})
        return {
            "answer": result["result"],
            "sources": [
                {
                    "source": doc.metadata.get("source", "unknown"),
                    "page": doc.metadata.get("page", "N/A")
                }
                for doc in result["source_documents"]
            ]
        }
    
    def get_name(self) -> str:
        return "langchain_rag"
