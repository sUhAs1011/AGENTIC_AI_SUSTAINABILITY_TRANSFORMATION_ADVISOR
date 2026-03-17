from retrieval.retriever import retrieve_context
from llm.ollama_client import generate

def answer_question(query):
    context = "\n".join(retrieve_context(query))

    prompt = f"""
Context:
{context}

Question:
{query}

Answer clearly.
"""

    return generate(prompt)