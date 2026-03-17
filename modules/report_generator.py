from llm.ollama_client import generate

def generate_report(summary, risks):

    prompt = f"""
Generate a consulting report:

Summary:
{summary}

Risks:
{risks}

Include:
- Insights
- Recommendations
"""

    return generate(prompt)