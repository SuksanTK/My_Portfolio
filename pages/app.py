import streamlit as st
from streamlit_option_menu import option_menu

from projects import model_linebalance
st.set_page_config(page_title="Web App & Model", layout="wide")
def appstreamlit():
    # --- HEADER UI ---
    st.markdown('<p class="section-header">Web App & Model</p><div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background: #F8FAFF; border: 1px solid #DBEAFE; border-radius: 10px;
                padding: 1.25rem 1.5rem; margin-bottom: 1.5rem;">
        <p style="color: #1D4ED8; font-size: 0.88rem; font-weight: 600; margin: 0 0 4px 0;
                  text-transform: uppercase; letter-spacing: 0.5px;">Industrial Engineering</p>
        <p style="color: #374151; font-size: 0.9rem; margin: 0;">
            Web App and data management tools for IE workflows
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- NAVIGATION MENU ---
    selected = option_menu(
        menu_title=None,
        options=[ "Check Efficiency", "Capacity Calc", "QueryData", "PDF-CSV","Linebalance Model","SQL Code"],
        icons=["bar-chart", "calculator", "search", "file-pdf"],
        orientation="horizontal"
    )

    # --- IMPORT PROJECTS ---
    from projects import (
        efficiency_Checking,
        final_calculation,
        query_Layout_Raweff,
        pdf_to_csv,
        model_linebalance,
        begining_code
    )

    # --- ROUTER ---
    if selected == "Check Efficiency":
        efficiency_Checking.run()

    elif selected == "Capacity Calc":
        final_calculation.run()

    elif selected == "QueryData":
        query_Layout_Raweff.run()

    elif selected == "PDF-CSV":
        pdf_to_csv.main()
        
    elif selected == "Linebalance Model":
        model_linebalance.linebalance()
        
    elif selected == "SQL Code":
        begining_code.sqlcode()

