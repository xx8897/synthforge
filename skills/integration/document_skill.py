"""
Document Skill - 集成 LangChain 的文件處理能力
===========================================

提供 PDF 加載、網頁爬取與文本切割功能。
"""

import os
from pathlib import Path
from typing import List, Optional
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class DocumentSkill:
    """整合 LangChain 的文件處理技能。"""

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len,
            is_separator_regex=False,
        )

    def load_pdf(self, file_path: str) -> List[Document]:
        """加載 PDF 檔案。"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF 檔案不存在: {file_path}")
        
        loader = PyPDFLoader(file_path)
        return loader.load()

    def load_url(self, url: str) -> List[Document]:
        """從網頁 URL 加載內容。"""
        loader = WebBaseLoader(url)
        return loader.load()

    def split_documents(self, documents: List[Document]) -> List[Document]:
        """將長文件切分成小塊。"""
        return self.splitter.split_documents(documents)

    def get_text_chunks(self, text: str) -> List[str]:
        """直接切割純文本。"""
        return self.splitter.split_text(text)

# Singleton instance
document_skill = DocumentSkill()
