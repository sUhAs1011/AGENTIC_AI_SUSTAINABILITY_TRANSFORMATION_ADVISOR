import streamlit as st
from ingestion.pipeline import process_pdf
from modules.qa import answer_question

st.title("AI Document Intelligence Platform")

st.write("App Loaded Successfully ✅")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:
    try:
        with open("data/temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        st.write("Processing PDF...")

        process_pdf("data/temp.pdf")

        st.success("PDF processed successfully!")

    except Exception as e:
        st.error(f"Error during processing: {e}")

query = st.text_input("Ask a question")

if query:
    try:
        response = answer_question(query)
        st.write(response)

    except Exception as e:
        st.error(f"Error during query: {e}")