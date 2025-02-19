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
        full_text += page.page_content + "\n"
    
    reg = r"第 (?:.*) (?:條|章)(?: |\n)"
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10,
        chunk_overlap=0,
        separators=[reg],
        # separators=[
        #     r"第\s*.+?\s*章",
        #     r"第\s*\d+(-\d+)?\s*條"
        # ],
        is_separator_regex=True
    )

    final_chunks = text_splitter.split_text(full_text);
    
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

num_chunks = hw02_2(q2_pdf)
print(num_chunks)