import streamlit as st
from streamlit_option_menu import option_menu
import base64
from pages import about_me,expjob,projects,app,resume_Page
from projects import begining_code

st.set_page_config(
    page_title="Suksan Portfolio",
    page_icon="file-earmark-person-fill",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ใช้ CSS เพื่อซ่อนเมนูจัดการเพจพื้นฐานของ Streamlit
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = get_base64_image("profilenormal.png")

logo_html = f"""
<style>
.logo-container {{
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}}
.logo {{
    width: 180px;
    height: 180px;
    border-radius: 50%;
    object-fit: cover;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
}}
</style>
<div class="logo-container">
    <img src="data:image/png;base64,{logo_base64}" class="logo">
</div>
"""

with st.sidebar:
    st.markdown(logo_html, unsafe_allow_html=True)
    nav_tab_op = option_menu(
        menu_title="Suksan Tuaklang",
        options=["About Me","Resume","Experience","Web App & Model", "Project & Certificate"],
        icons=['person-fill', 'file-text', 'briefcase', 'archive', 'folder'],
        default_index=0,
    )

if nav_tab_op == "About Me":
    about_me.detailperson()
elif nav_tab_op == "Resume":
    resume_Page.resume()
elif nav_tab_op == "Experience":
    expjob.exp()
elif nav_tab_op == "Web App & Model":
    app.appstreamlit()
elif nav_tab_op == "Project & Certificate":
    projects.project_ie()
    
with st.sidebar:
    st.markdown("""
    [LinkedIn](https://www.linkedin.com/in/suksantk/) | 
    [GitHub](https://github.com/SuksanTK) | 
    [Email](flukzaza1551@gmail.com) |
    [Facebook](https://www.facebook.com/share/19aFS1dN5f/?mibextid=wwXIfr)|
    [Instagram](https://www.instagram.com/suksantk?igsh=MXRrdmRoZzVubjg2Zw%3D%3D&utm_source=qr)
    """)
    st.markdown("- **Tell:** 0837365492")