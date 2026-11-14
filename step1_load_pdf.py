from langchain_community.document_loaders import PyPDFLoader
from llama_index.core import SimpleDirectoryReader

PDF_PATH = "documents/sample.pdf"

# PART:1 langchain Document Loading

# Instantiate PyPDFLoader with the path to your pdf
lc_loader = PyPDFLoader(PDF_PATH)

lc_pages = lc_loader.load()

print(f"[LANGCHAIN]")
print(f"Total pages loaded: {len(lc_pages)}")
print(f"Page 1 Metadata: {lc_pages[0].metadata}")
print(f"Page 1 text preview: \n{lc_pages[0].page_content}\n")
