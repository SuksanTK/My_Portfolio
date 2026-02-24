import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(page_title="My Resume", layout="wide")

def resume():

    # resume english
    with open("Suksan Tuaklang IE Resume.pdf", "rb") as pdf_file:
        document_full = pdf_file.read()

    # Resume ไทย
    with open("Suksan Tuaklang IE Resume2.pdf", "rb") as pdf_file:
        document_short = pdf_file.read()

    st.markdown("""
        <style>
        .stDownloadButton button {
            background-color: #1E9E35 !important;
            color: white !important;
        }
        </style>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # resume english
    with col1:
        st.download_button(
            label="Download Resume(Eng)",
            key="download_Eng",
            file_name="Suksan Tuaklang IE Resume.pdf",
            data=document_full,
            help="Download Eng version.",
        )

    #Resume ไทย
    with col2:
        st.download_button(
            label="Download Resume(thai)",
            key="download_thai",
            file_name="Suksan Tuaklang IE Resume2.pdf",
            data=document_short,
            help="Download Thai version.",
        )

    # แสดง preview ไฟล์หลัก
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