from llm.ollama_client import generate

def summarize(text):
    prompt = f"""
Summarize the following:

{text}

Give key points.
"""
    return generate(prompt)