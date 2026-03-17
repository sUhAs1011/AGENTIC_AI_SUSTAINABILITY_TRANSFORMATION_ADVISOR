import uuid
import re


# 🆔 Generate unique IDs for Pinecone vectors
def generate_id():
    return str(uuid.uuid4())


# 🧹 Clean extracted text
def clean_text(text):

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # remove weird characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    return text.strip()


# ✂️ Optional: truncate long text (for LLM safety)
def truncate_text(text, max_length=2000):
    return text[:max_length]


# 🧾 Format context nicely for prompts
def format_context(chunks):
    return "\n\n".join(chunks)


# 📊 Simple debug logger
def log(message):
    print(f"[DEBUG]: {message}")