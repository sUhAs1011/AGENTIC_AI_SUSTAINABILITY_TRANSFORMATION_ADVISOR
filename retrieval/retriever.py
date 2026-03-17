from embeddings.embedder import embed_query
from vector_db.pinecone_db import query_embeddings
from utils.helpers import format_context   # ✅ ADD THIS


def retrieve_chunks(query, top_k=5):
    """
    Returns raw retrieved chunks (list of strings)
    """
    query_emb = embed_query(query)
    return query_embeddings(query_emb, top_k=top_k)


def retrieve_context(query, top_k=5):
    """
    Returns formatted context string for LLM prompts
    """
    chunks = retrieve_chunks(query, top_k=top_k)

    # ✅ FORMAT CONTEXT CLEANLY
    context = format_context(chunks)

    return context