from ingestion.pdf_loader import load_pdf
from ingestion.text_splitter import split_text
from embeddings.embedder import embed_texts
from vector_db.pinecone_db import upsert_embeddings
from utils.helpers import log   # ✅ ADD THIS


def process_pdf(file_path):

    log("Loading PDF...")

    text = load_pdf(file_path)

    log("Splitting text into chunks...")

    chunks = split_text(text)

    log(f"Generated {len(chunks)} chunks")

    log("Generating embeddings...")

    embeddings = embed_texts(chunks)

    log("Uploading embeddings to Pinecone...")

    upsert_embeddings(chunks, embeddings)

    log("PDF processing completed successfully")

    return chunks