import streamlit as st

st.set_page_config(
    page_title="Test",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("SIDEBAR TEST")
st.sidebar.write("If you see this, sidebar works.")

st.write("Main area loaded.")