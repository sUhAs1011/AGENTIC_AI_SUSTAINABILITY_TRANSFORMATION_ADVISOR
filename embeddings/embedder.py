from sentence_transformers import SentenceTransformer
from config.settings import MODEL_NAME

model = SentenceTransformer(MODEL_NAME)

def embed_texts(texts):
    return model.encode(texts)

def embed_query(query):
    return model.encode([query])[0]