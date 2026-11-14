"""
Milestone 2: Interactive PDF RAG Chat App with Streamlit, LangChain, ChromaDB & Ollama
======================================================================================
Run this app locally with:
    pip install streamlit pypdf chromadb langchain langchain-community langchain-text-splitters langchain-ollama langchain-chroma
    streamlit run app.py

Architecture Overview (All 5 RAG Steps in One UI):
1. Document Loading: Saves uploaded PDF bytes to a temporary file so PyPDFLoader can parse pages + metadata.
2. Text Chunking:    Splits pages using RecursiveCharacterTextSplitter with live sidebar controls (chunk_size, chunk_overlap).
3. Embeddings:       Uses local OllamaEmbeddings ('nomic-embed-text') to convert chunks and queries into 768-D vectors.
4. Vector Store:     Indexes chunks into ChromaDB with deterministic IDs (hashed by file + chunk settings) to avoid duplicates.
5. Retrieval + Chat: Uses ChatOllama ('llama3.2') to answer questions and renders a side-by-side 'Retrieved Source Chunks'
                     inspector (Stretch Goal) showing exact Page numbers, Character Offsets, and Chroma Distance Scores.
"""

import hashlib
import os
import tempfile
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

# =====================================================================
# 1. STREAMLIT PAGE CONFIGURATION & SESSION STATE INITIALIZATION
# =====================================================================
st.set_page_config(
    page_title="Local PDF RAG Studio (LangChain + Ollama)",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Chat with Your PDF — Local RAG Studio")
st.caption(
    "Built from scratch with **LangChain**, **ChromaDB**, and **Ollama** (`nomic-embed-text` + `llama3.2`)."
)

# Why st.session_state?
# Streamlit re-runs the entire Python script from top to bottom on every button click or chat input.
# Storing the vector store and chat history in st.session_state prevents re-indexing the PDF on every question!
if "messages" not in st.session_state:
    st.session_state.messages = []
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "active_index_key" not in st.session_state:
    st.session_state.active_index_key = None
if "index_stats" not in st.session_state:
    st.session_state.index_stats = {}


# =====================================================================
# 2. SIDEBAR: UPLOAD PDF & CONFIGURE RAG HYPERPARAMETERS
# =====================================================================
with st.sidebar:
    st.header("⚙️ 1. Upload & Ingestion Settings")
    uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

    st.subheader("Step 2: Chunking Controls")
    chunk_size = st.slider(
        "Chunk Size (characters)",
        min_value=300,
        max_value=2000,
        value=800,
        step=100,
        help="Maximum characters per chunk. Smaller = more granular retrieval; Larger = more surrounding context.",
    )
    chunk_overlap = st.slider(
        "Chunk Overlap (characters)",
        min_value=0,
        max_value=500,
        value=150,
        step=25,
        help="Sliding window overlap between consecutive chunks so sentences aren't cut in half.",
    )

    st.subheader("Step 3 & 5: Ollama Models & Retrieval")
    embed_model_name = st.text_input("Ollama Embedding Model", value="nomic-embed-text")
    llm_model_name = st.text_input("Ollama Chat LLM", value="llama3.2")
    top_k = st.slider(
        "Top-K Retrieved Chunks",
        min_value=1,
        max_value=8,
        value=3,
        help="Number of closest chunks retrieved from ChromaDB for every question.",
    )

    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# =====================================================================
# 3. PHASE 1 (STEPS 1–4): PDF INGESTION & CHROMADB INDEXING FUNCTION
# =====================================================================
def build_vector_store(
    pdf_bytes: bytes,
    filename: str,
    c_size: int,
    c_overlap: int,
    embed_model: str,
) -> tuple[Chroma, dict]:
    """
    Executes Steps 1 to 4 of our RAG pipeline:
    1. Saves uploaded PDF bytes to a temp file and loads pages via PyPDFLoader.
    2. Splits pages into overlapping chunks via RecursiveCharacterTextSplitter.
    3. Initializes OllamaEmbeddings.
    4. Stores vectors + metadata in a local persistent ChromaDB collection.
    """
    # Create a unique fingerprint for this PDF + chunk configuration
    file_hash = hashlib.md5(pdf_bytes).hexdigest()[:8]
    collection_name = f"pdf_{file_hash}_cs{c_size}_co{c_overlap}"
    persist_dir = "./chroma_streamlit_db"

    # Step 1: Write uploaded RAM bytes to a temporary file on disk for PyPDFLoader
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(pdf_bytes)
        tmp_pdf_path = tmp_file.name

    try:
        loader = PyPDFLoader(tmp_pdf_path)
        pages = loader.load()

        # Replace the temporary file path in metadata with the real uploaded filename
        for page in pages:
            page.metadata["source"] = filename

        # Step 2: Split pages into overlapping chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=c_size,
            chunk_overlap=c_overlap,
            add_start_index=True,
        )
        chunks = splitter.split_documents(pages)

        # Step 3: Initialize local Ollama Embeddings
        embeddings = OllamaEmbeddings(model=embed_model)

        # Step 4: Index into ChromaDB with deterministic IDs to prevent duplicate insertions
        chunk_ids = [f"{collection_name}_chunk_{i}" for i in range(len(chunks))]
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            ids=chunk_ids,
            collection_name=collection_name,
            persist_directory=persist_dir,
        )

        stats = {
            "filename": filename,
            "total_pages": len(pages),
            "total_chunks": len(chunks),
            "collection_name": collection_name,
        }
        return vector_store, stats

    finally:
        # Clean up temporary PDF file from disk
        if os.path.exists(tmp_pdf_path):
            os.remove(tmp_pdf_path)


# Trigger indexing only when a new PDF is uploaded or chunking sliders change
if uploaded_file is not None:
    pdf_bytes = uploaded_file.getvalue()
    current_key = f"{uploaded_file.name}_{len(pdf_bytes)}_{chunk_size}_{chunk_overlap}_{embed_model_name}"

    if st.session_state.active_index_key != current_key:
        with st.spinner(f"Indexing '{uploaded_file.name}' (Loading -> Chunking -> Embedding -> ChromaDB)..."):
            st.session_state.vector_store, st.session_state.index_stats = build_vector_store(
                pdf_bytes=pdf_bytes,
                filename=uploaded_file.name,
                c_size=chunk_size,
                c_overlap=chunk_overlap,
                embed_model=embed_model_name,
            )
            st.session_state.active_index_key = current_key

    # Display Ingestion Pipeline Metrics at the top of the app
    stats = st.session_state.index_stats
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📄 Loaded PDF", stats["filename"])
    col2.metric("📑 Pages Parsed (Step 1)", stats["total_pages"])
    col3.metric("🧩 Chunks Created (Step 2)", stats["total_chunks"])
    col4.metric("🔎 Top-K Retrieval (Step 5)", top_k)

else:
    st.info("👈 Upload a PDF in the sidebar to run Steps 1–4 (Ingestion) and start chatting!")


# =====================================================================
# 4. PHASE 2 (STEP 5): RETRIEVAL, GENERATION & SIDE-BY-SIDE CHUNK VIEW
# =====================================================================
PROMPT_TEMPLATE = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a precise research assistant. Answer the user's question using ONLY the provided context chunks.\n"
        "Always cite the page number in brackets like [Page X] for every fact you state. But Do no mention where you found the details not mention any page number or chunk number.\n Instead on mentioning the page number, you can just provide the answer directly without any citations. and whole text of chunk you want to reference. If the answer is not in the provided context, say: 'I cannot find the answer in the provided PDF.'",
    ),
    (
        "human",
        "Context Chunks:\n{context}\n\nQuestion: {question}",
    ),
])


def render_message_with_chunks(role: str, content: str, chunks: list[dict] | None = None):
    """Renders a chat message and, for assistant answers, displays the retrieved chunks side-by-side."""
    with st.chat_message(role):
        if role == "assistant" and chunks:
            ans_col, chunk_col = st.columns([1.15, 0.85], gap="large")
            with ans_col:
                st.markdown("#### 🤖 Grounded LLM Answer")
                st.markdown(content)
            # with chunk_col:
            #     st.markdown(f"#### 🔎 Retrieved Source Chunks (Top {len(chunks)})")
            #     for c in chunks:
            #         header = (
            #             f"Rank #{c['rank']} | Page {c['page']} "
            #             f"(offset {c['start_index']}) | Distance: {c['distance']:.4f}"
            #         )
            #         with st.expander(header, expanded=(c["rank"] == 1)):
            #             st.caption(f"Source: `{c['source']}` — Lower distance means closer semantic match")
            #             st.text(c["text"])
        else:
            st.markdown(content)


# Render existing conversation history from session state
for msg in st.session_state.messages:
    render_message_with_chunks(
        role=msg["role"],
        content=msg["content"],
        chunks=msg.get("chunks"),
    )

# Handle new user question
if user_question := st.chat_input("Ask a question about your uploaded PDF..."):
    if st.session_state.vector_store is None:
        st.warning("Please upload a PDF in the sidebar first!")
    else:
        # 1. Display and save user question
        st.session_state.messages.append({"role": "user", "content": user_question})
        render_message_with_chunks("user", user_question)

        # 2. Retrieve Top-K chunks with distance scores from ChromaDB
        with st.spinner("Retrieving top chunks from ChromaDB & generating answer with Ollama..."):
            retrieved_pairs = st.session_state.vector_store.similarity_search_with_score(
                user_question, k=top_k
            )

            serialized_chunks = []
            formatted_context_parts = []

            for rank, (doc, distance_score) in enumerate(retrieved_pairs, start=1):
                page_num = doc.metadata.get("page", 0) + 1  # Convert 0-indexed page to 1-indexed
                start_idx = doc.metadata.get("start_index", "?")
                source_name = doc.metadata.get("source", "PDF")

                serialized_chunks.append({
                    "rank": rank,
                    "page": page_num,
                    "start_index": start_idx,
                    "distance": float(distance_score),
                    "source": source_name,
                    "text": doc.page_content.strip(),
                })
                formatted_context_parts.append(
                    f"--- Chunk {rank} [Page {page_num}] ---\n{doc.page_content}"
                )

            context_text = "\n\n".join(formatted_context_parts)

            # 3. Generate grounded answer using ChatOllama (temperature=0)
            llm = ChatOllama(model=llm_model_name, temperature=0)
            rag_chain = PROMPT_TEMPLATE | llm
            response = rag_chain.invoke({
                "context": context_text,
                "question": user_question,
            })
            answer_text = response.content

        # 4. Save assistant answer + retrieved chunks to session state and display side-by-side
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer_text,
            "chunks": serialized_chunks,
        })
        render_message_with_chunks("assistant", answer_text, serialized_chunks)