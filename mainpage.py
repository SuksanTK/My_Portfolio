# import streamlit as st
# from streamlit_option_menu import option_menu
# import base64
# import requests
# import json
# from pages import About_me,app,begining_code,dashboard,Exp,Projects
# import os
# import images

# logo_base64 = base64("images/Profile_2.jpg")
# logo_html = f"""
#     <style>
#     .logo-container {{
#         display: flex;
#         justify-content: center;
#         margin-bottom: 20px;
#     }}
#     .logo {{
#         width: 120px;
#         height: 120px;
#         border-radius: 50%;
#         object-fit: cover;
#         box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
#     }}
#     .sidebar-links a:hover {{
#         color: #6C63FF;
#         font-weight: bold;
#     }}
#     </style>
#     <div class="logo-container">
#         <img src="data:image/png;base64,{logo_base64}" class="logo">
#     </div>
# """
# st.sidebar.markdown(logo_html, unsafe_allow_html=True)
# with st.sidebar:
#     pages = ["About me", "Experience", "Begining code",  "Projects", "Contact"]
#     nav_tab_op = option_menu(
#         menu_title="Ayush",
#         options=pages,
#         icons=['person-fill', 'file-text', 'briefcase', 'folder', 'star', 'envelope'],
#         menu_icon="cast",
#         default_index=0,
#     )

# if nav_tab_op == "About me":
#     About_me.Aboutme()
# elif nav_tab_op == "Experience":
#     Exp.exp()
# elif nav_tab_op == "Begining code":
#     begining_code.sqlcode()
# elif nav_tab_op == "Projects":
#     Projects.Projectt()
# elif nav_tab_op == "Contact":
#     dashboard.linebalance()
    
    
# pg = st.navigation([
#     st.Page( "pages/1_About_me.py", title="About me", icon="🔥"),
#     st.Page( "pages/exp.py", title="My exp", icon="🔥"),
#     st.Page( "pages/2_Projects.py", title="My Project", icon="🔥"),
#     st.Page("pages/begining_code.py", title="Newbie code", icon="🔥"),
#     st.Page("pages/app.py", title="Web app project", icon="🔥"),
#     st.Page("pages/dashboard.py", title="Dashboard", icon="🔥")
# ])
# pg.run()

import streamlit as st
from streamlit_option_menu import option_menu
import base64
from pages import about_me,begining_code,dashboard,expjob,projects,app

st.set_page_config(
    page_title="Suksan Portfolio",
    layout="wide"
)

def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = get_base64_image("images/Profile_2.jpg")

logo_html = f"""
<style>
.logo-container {{
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}}
.logo {{
    width: 120px;
    height: 120px;
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
        options=["Aboutme", "Experience", "Project App", "Projectsz", "Linebalanceconcept"],
        icons=['person-fill', 'file-text', 'briefcase', 'folder', 'envelope'],
        default_index=0,
    )

if nav_tab_op == "Aboutme":
    about_me.detailperson()
elif nav_tab_op == "Experience":
    expjob.exp()
elif nav_tab_op == "Project App":
    app.appstreamlit()
elif nav_tab_op == "Projectsz":
    projects.otherprojects()
elif nav_tab_op == "Linebalanceconcept":
    dashboard.linebalance()

import pages.dashboard as d
st.write(dir(d))