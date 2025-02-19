import re
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    document = loader.load()
    
    splitter = CharacterTextSplitter(chunk_overlap=0)
    chunks = splitter.split_documents(document)
    
    return chunks[-1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    document = loader.load()
    
    full_text = ""
    for page in document:
        full_text += page.page_content

    chapter_pattern = re.compile(r'(第\s*[一二三四五六七八九十]+\s*章[\s\S]*?)(?=(第\s*[一二三四五六七八九十]+\s*章|$))')
    article_pattern = re.compile(r'(第\s*\d+\s*條[\s\S]*?)(?=(第\s*\d+\s*條|$))')

    chapters = chapter_pattern.findall(full_text)
    chunks = []
    
    for chapter in chapters:
        articles = article_pattern.findall(chapter[0])
        chunks.extend(articles)
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=0,
        separators=["\n\n", "\n", " ", ""]
    )
    
    final_chunks = []
    for chunk in chunks:
        final_chunks.extend(text_splitter.split_text(chunk[0]))
    
    return len(final_chunks)

def test(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    document = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=0,
        separators=["\n第", "\n", "\r"]
    )
    
    chunks = splitter.split_documents(document)
    
    return len(chunks)