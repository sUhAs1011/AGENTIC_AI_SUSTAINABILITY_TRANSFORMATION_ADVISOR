from llm.ollama_client import generate

def analyze_risk(text):
    prompt = f"""
Identify risks in the following content:

{text}

Focus on:
- compliance risks
- sustainability risks
- operational risks
"""
    return generate(prompt)