import streamlit as st
import pandas as pd
import numpy as np
import os
import PyPDF2

st.title("File Upload Example")

uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "pdf"])

if uploaded_file is not None:
    file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    st.write(file_details)

    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
        st.text(content)
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page_num, page in enumerate(pdf_reader.pages):
            st.text(page.extract_text())
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)