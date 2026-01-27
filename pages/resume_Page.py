import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


st.set_page_config(page_title="My Resume", layout="wide")
def resume():
    with open("Suksan Tuaklang IE Resume.pdf", "rb") as pdf_file:
        document = pdf_file.read()

    st.markdown("""
            <style>
            .stDownloadButton button {
                background-color: #1E9E35 !important;
                color: white !important;
            }
            </style>
            """, unsafe_allow_html=True)


    st.download_button(
                label="Download Resume",
                key="download_button",
                file_name="Suksan Tuaklang IE Resume.pdf",
                data=document,
                help="Click to download.",
            )
    with st.container():
        st.markdown(
            """
            <style>
            .stContainer > div {
                width: 55%;
                margin: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        pdf_viewer("Suksan Tuaklang IE Resume.pdf")