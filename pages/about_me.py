import streamlit as st
import os
import streamlit as st
import pandas as pd
import plotly.express as px
import images


st.set_page_config(
    page_title="Suksan Tuaklang",
    layout="wide"
)
def detailperson():
    # --- About Me Section ---
    st.header("About Me")
    with st.container():
        col1,col2 = st.columns([3,2])
        col1.markdown(
            """
            I am an Industrial Engineer with a strong passion for continuous improvement and data-driven manufacturing. My journey did not begin in a traditional engineering pathway—I hold a degree in Business Administration. However, through hands-on experience, ambition, and continuous self-development, I transitioned into the Industrial Engineering field and built my career from the factory floor upward.

    My professional background started in the Quality Control (QC) department at HBI Manufacturing, where I gained a solid foundation in quality standards, defect analysis, and production discipline. Driven by a desire for growth and deeper technical understanding, I made the decision to step away temporarily to further develop my skills and capabilities.

    I later returned to the organization through an Industrial Engineering internship, where I was given the opportunity to apply IE principles in real production environments. Through strong performance and dedication, I was selected to join the team as a full-time Industrial Engineer. I began working as a production-zone IE, focusing on line balancing, manpower planning, work measurement, and on-floor problem solving.

    Over time, my role evolved beyond traditional IE responsibilities into IE analysis and data-driven improvement. I now work extensively with real-time manufacturing data, transforming raw system data into insights, reports, and analytical models that support operational and management decision-making. I collaborate closely with production, analytics, and development teams to reduce manual IE work, improve system accuracy, and drive smarter manufacturing processes.

    I see myself as a bridge between operations and data—an Industrial Engineer who understands people, processes, and systems, and who believes that meaningful improvement comes from combining shop-floor experience with analytical thinking. My goal is to continue growing as a Data-Driven Industrial Engineer, contributing to smarter, more efficient, and sustainable manufacturing environments.
            """
        )
        # col2.image("images/P6.jpg", use_container_width=True)