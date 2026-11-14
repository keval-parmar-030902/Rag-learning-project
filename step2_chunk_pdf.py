from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

PDF_PATH = "documents/sample.pdf"

# 1. Loader the pdf pages (from step1)
loader = PyPDFLoader(PDF_PATH)
pages = loader.load()

# 2. Configure the RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 800, # Maximum Character per chunk
    chunk_overlap = 150, # Sliding Window overlap between consecutive chunks
    length_function = len, # Measure chunk size by character count
    add_start_index=True, # Adds start_index to metadata (exact char position on the page)
)

# 3. Split the pages Documents into smaller chunks Documents
chunks = text_splitter.split_documents(pages)
print(f"Total pages loaded: {len(pages)}")
print(f"Total chunks created: {len(chunks)}\n") 

# 4. Inspect Chunk 0 and Chunk 1 to see the sliding window overlap in action
print(f"=== CHUNK {0} ===\n")
print(f"Metadata: {chunks[0].metadata}\n")
print(f"Length: {len(chunks[0].page_content)} characters\n")
print(f"End of Chunk 0 sentences... :\n{chunks[0].page_content}\n\n\n\n")

# with open("documents/chunks.md", "w") as f:
#     for chunk in range(len(chunks)):
#         f.write(f"=== CHUNK {chunk} ===\n")
#         f.write(f"Metadata: {chunks[chunk].metadata}\n")
#         f.write(f"Length: {len(chunks[chunk].page_content)} characters\n")
#         f.write(f"End of Chunk {chunk} sentences... :\n{chunks[chunk].page_content}\n\n\n\n")
        
        
        