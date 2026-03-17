from llm.ollama_client import generate

def detect_contradictions(text1, text2):
    prompt = f"""
Check if these contradict:

Text 1:
{text1}

Text 2:
{text2}
"""
    return generate(prompt)