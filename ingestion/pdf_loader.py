from pypdf import PdfReader
from utils.helpers import clean_text   # ✅ ADD THIS


def load_pdf(file_path):

    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:

        content = page.extract_text()

        if content:
            # ✅ CLEAN TEXT BEFORE ADDING
            cleaned = clean_text(content)
            text += cleaned + "\n"

    return text