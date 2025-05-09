import streamlit as st
import pandas as pd
import numpy as np
import os

# Ensure Streamlit uses the correct port on Render
PORT = os.environ.get("PORT", 8501)

st.set_page_config(page_title="Sample App")

st.title("🎈 Welcome to My Streamlit App!")
st.write("This is a simple example deployed on Render.")

# Example data
df = pd.DataFrame({
    "Column A": np.random.rand(10),
    "Column B": np.random.rand(10)
})

st.line_chart(df)