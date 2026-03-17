from pinecone import Pinecone
from config.settings import PINECONE_API_KEY, INDEX_NAME
from utils.helpers import generate_id   # ✅ ADD THIS

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Connect to index
index = pc.Index(INDEX_NAME)


def upsert_embeddings(chunks, embeddings):

    vectors = []

    for chunk, emb in zip(chunks, embeddings):

        vectors.append({
            "id": generate_id(),   # ✅ UNIQUE ID
            "values": emb.tolist(),
            "metadata": {
                "text": chunk
            }
        })

    # Upsert to Pinecone
    index.upsert(vectors=vectors)


def query_embeddings(query_embedding, top_k=5):

    results = index.query(
        vector=query_embedding.tolist(),
        top_k=top_k,
        include_metadata=True
    )

    # Extract text from metadata
    return [match["metadata"]["text"] for match in results["matches"]]