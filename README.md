# 📄 Local PDF RAG Studio — Chat with Any PDF from Scratch

A 100% local, privacy-preserving **Retrieval-Augmented Generation (RAG)** system built from scratch in Python using **[LangChain](https://docs.langchain.com/oss/python/langchain/knowledge-base)**, **[ChromaDB](https://github.com/chroma-core/chroma)**, **[Ollama](https://docs.langchain.com/oss/python/integrations/providers/ollama)** (`nomic-embed-text` + `llama3.2`), and **[Streamlit](https://docs.streamlit.io/develop/api-reference)**.

This repository is structured both as a **step-by-step educational implementation** (`step1` through `step5` scripts) and a **full-featured interactive Streamlit web application** (`main.py`) that displays retrieved source chunks, page numbers, character offsets, and vector distance scores right next to every LLM response.

## ✨ Key Features & Engineering Highlights

* **100% Local & Zero API Cost:** Runs entirely on your local machine using [OllamaEmbeddings](https://reference.langchain.com/python/langchain-ollama/embeddings/OllamaEmbeddings) (`nomic-embed-text`, 768-dimensional vectors) and [ChatOllama](https://reference.langchain.com/python/langchain-ollama/chat_models/ChatOllama) (`llama3.2`).
* **Transparent Side-by-Side Retrieval Inspector:** Every answer displays the exact **Top-$K$ retrieved PDF chunks**, 1-indexed page citations, character start offsets, and ChromaDB distance scores alongside the generated response to make debugging retrieval vs. generation effortless.
* **Duplicate-Safe Persistent Vector Store:** Uses content-hashed collection names and deterministic chunk IDs in [LangChain Chroma](https://docs.langchain.com/oss/python/integrations/vectorstores/chroma) so re-running scripts or reloading the UI never creates duplicate embeddings on disk.
* **Live Hyperparameter Tuning in Streamlit:** Adjust `chunk_size`, `chunk_overlap`, and `top_k` live in the sidebar via [Streamlit Session State (`st.session_state`)](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state) to observe how chunking granularity impacts retrieval quality.
* **Modular 5-Step Learning Path:** Includes standalone scripts for each stage of the RAG pipeline so reviewers and learners can inspect and test every component in isolation.

## 🏗️ System Architecture & 5-Stage RAG Pipeline

| Stage | Script / Module | Core LangChain / Vector Class | What Happens Under the Hood |
| :--- | :--- | :--- | :--- |
| **Step 1: Document Loading** | `rag_learning.ipynb` | [`PyPDFLoader`](https://reference.langchain.com/python/langchain-community/document_loaders/pdf/PyPDFLoader) | Parses binary PDF files page-by-page into `Document` objects containing `page_content` and `metadata` (`source`, `page`). |
| **Step 2: Text Chunking** | `rag_learning.ipynb` | [`RecursiveCharacterTextSplitter`](https://reference.langchain.com/python/langchain-text-splitters/character/RecursiveCharacterTextSplitter) | Splits pages hierarchically (`\n\n` $\rightarrow$ `\n` $\rightarrow$ space) into 800-character chunks with a 150-character sliding window overlap and `start_index` tracking. |
| **Step 3: Embeddings & Math** | `rag_learning.ipynb` | [`OllamaEmbeddings`](https://reference.langchain.com/python/langchain-ollama/embeddings/OllamaEmbeddings) | Maps text chunks and queries into 768-float semantic vectors ($\vec{v} \in \mathbb{R}^{768}$) and verifies closeness via Cosine Similarity. |
| **Step 4: Vector Store Indexing** | `rag_learning.ipynb` | [`Chroma`](https://reference.langchain.com/python/langchain-chroma/vectorstores/Chroma) | Persists chunk vectors, raw text, and metadata into a local SQLite + HNSW graph index (`./chroma_db`) for millisecond nearest-neighbor search. |
| **Step 5: Augmented Generation** | `rag_learning.ipynb` | [`ChatPromptTemplate`](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate) + [`ChatOllama`](https://reference.langchain.com/python/langchain-ollama/chat_models/ChatOllama) | Retrieves the Top-$K$ chunks from ChromaDB, injects them into a strict system prompt (`temperature=0`), and prints the LLM answer alongside the source chunks. |
| **Milestone UI: Web Studio** | `main.py` | [`st.file_uploader`](https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader) + [`st.session_state`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state) | Combines Steps 1–5 into an interactive browser studio with PDF upload, live chunking sliders, metric cards, and expandable source chunk cards. |

## 📂 Repository Structure

```text
├── main.py                        # Complete Streamlit RAG Web Application (All 5 Steps + Chunk Inspector)
├── rag_learning.ipynb             # All steps of the learning is here.
├── requirements.txt              # Python package dependencies
└── README.md                     # Project documentation and setup guide
```

## 🛠️ Prerequisites & Local Setup Guide

### 1. Install Ollama & Pull Required Models

Download and install [Ollama](https://docs.langchain.com/oss/python/integrations/providers/ollama) on your local machine (Linux, Windows, or macOS), then pull the embedding model and chat LLM in your terminal:

```bash
# 1. Pull the 768-dimensional embedding model (used in Steps 3, 4, 5, and app.py)
ollama pull nomic-embed-text

# 2. Pull the chat LLM for grounded answer generation (used in Step 5 and app.py)
ollama pull llama3.2

# Verify both models are available locally
ollama list
```

### 2. Clone the Repository & Create a Virtual Environment

You can set up the Python environment (Python 3.10+ recommended) using either standard `pip` or `uv`:

#### Option A: Using `pip` and `venv`

```bash
git clone https://github.com/keval-parmar-030902/pdf-rag-from-scratch.git
cd pdf-rag-from-scratch

python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate

pip install --upgrade pip
pip install streamlit pypdf chromadb langchain langchain-core langchain-community langchain-text-splitters langchain-ollama langchain-chroma
```

#### Option B: Using `uv` (Fast Package Manager)

```bash
git clone https://github.com/keval-parmar-030902/pdf-rag-from-scratch.git
cd pdf-rag-from-scratch

uv venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
uv pip install streamlit pypdf chromadb langchain langchain-core langchain-community langchain-text-splitters langchain-ollama langchain-chroma
```

### 3. `requirements.txt` Reference

If you want to save a `requirements.txt` file in your repository root, include these packages:

```text
streamlit>=1.38.0
pypdf>=4.3.0
chromadb>=0.5.0
langchain>=0.3.0
langchain-core>=0.3.0
langchain-community>=0.3.0
langchain-text-splitters>=0.3.0
langchain-ollama>=0.2.0
langchain-chroma>=0.1.4
```

## 🚀 How to Run the Project

### 1. Run the Interactive Streamlit Web App (`app.py`)

Launch the full web interface in your browser:

```bash
streamlit run app.py
```

1. Open the local URL shown in your terminal (typically `http://localhost:8501`).
2. Upload any PDF file in the left sidebar using the file uploader.
3. Adjust **Chunk Size** (default `800`), **Chunk Overlap** (default `150`), and **Top-K Retrieved Chunks** (default `3`) as needed.
4. Type any question in the chat box at the bottom. The left column displays the **Grounded LLM Answer** with `[Page X]` citations, and the right column displays the **Retrieved Source Chunks** with their exact page numbers, character offsets, and vector distance scores.

### 2. Run the Jupyter Notebook

```bash
jupyter notebook
```

```bash
jupyter lab
```

#### OR
```bash
uv run jupyter notebook
```

```bash
uv run jupyter lab
```

## 🧠 Core Theory Quick-Reference (Why Each Parameter Matters)

* **Why `chunk_size=800` and `chunk_overlap=150`?** Embedding a full 3,000-character page into a single vector dilutes specific topics across the whole page. Splitting into 800-character chunks keeps each vector focused on a single concept, while the 150-character sliding window ensures sentences split at chunk boundaries retain their context.
* **Cosine Similarity vs. Chroma Distance Score:**
  * In `step3_embeddings.py`, **Cosine Similarity** ($\frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\| \|\vec{B}\|}$) ranges from `-1.0` to `+1.0` (**higher is better**).
  * In `step4`, `step5`, and `app.py`, ChromaDB's `similarity_search_with_score()` returns a **Distance Score** (**lower is better**, where `0.0` is an exact match).
* **Why `temperature=0` in `ChatOllama`?** Setting `temperature=0` makes token selection greedy/deterministic, minimizing creative extrapolation so the LLM sticks strictly to the retrieved PDF chunks.

## 🛠️ Troubleshooting Common Issues

| Issue / Error Message | Cause | Solution |
| :--- | :--- | :--- |
| **`ConnectionError: Failed to connect to Ollama`** | The local Ollama background service is not running. | Run `ollama serve` in a separate terminal window or launch the Ollama desktop app. |
| **`ollama._types.ResponseError: model 'nomic-embed-text' not found`** | The embedding or chat model hasn't been downloaded yet. | Run `ollama pull nomic-embed-text` and `ollama pull llama3.2`. |
| **`InvalidDimensionException` in ChromaDB** | Switching between embedding models with different vector dimensions inside the same collection. | Delete the `./chroma_db` or `./chroma_streamlit_db` directory so Chroma creates a fresh index matching the new model's dimension. |
| **Empty text extracted in Step 1** | The uploaded PDF is a scanned image without an embedded text layer. | Use a digital-native PDF or pre-process scanned PDFs with an OCR tool before loading with `PyPDFLoader`. |

## 👤 Author

**Keval Parmar**
* GitHub: [@keval-parmar-030902](https://github.com/keval-parmar-030902)
