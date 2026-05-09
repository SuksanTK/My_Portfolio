import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


def resume():

    st.markdown('<p class="section-header">Resume</p><div class="section-divider"></div>', unsafe_allow_html=True)

    st.markdown("""
    <p style="color:#6B7280; font-size:0.9rem; margin-bottom:1.5rem;">
    Download my resume in English or Thai, or preview it below.
    </p>
    """, unsafe_allow_html=True)

    # ---- DOWNLOAD BUTTONS ----
    try:
        with open("Suksan Tuaklang IE Resume.pdf", "rb") as f:
            doc_eng = f.read()
        with open("Suksan Tuaklang IE Resume2.pdf", "rb") as f:
            doc_thai = f.read()

        col1, col2, col_spacer = st.columns([1, 1, 3])
        with col1:
            st.download_button(
                label="⬇️  Download (English)",
                key="download_Eng",
                file_name="Suksan Tuaklang IE Resume.pdf",
                data=doc_eng,
                help="Download English version.",
            )
        with col2:
            st.download_button(
                label="⬇️  Download (Thai)",
                key="download_thai",
                file_name="Suksan Tuaklang IE Resume2.pdf",
                data=doc_thai,
                help="Download Thai version.",
            )
    except FileNotFoundError:
        st.warning("Resume files not found.")

    st.markdown("<div style='margin-top:1.5rem;'></div>", unsafe_allow_html=True)

    # ---- PDF PREVIEW ----
    st.markdown("""
    <p style="font-size:0.88rem; color:#9CA3AF; font-weight:500; text-transform:uppercase;
              letter-spacing:0.5px; margin-bottom:0.5rem;">Preview · English Version</p>
    """, unsafe_allow_html=True)

    try:
        pdf_viewer("Suksan Tuaklang IE Resume.pdf")
    except Exception:
        st.info("PDF preview unavailable.")
