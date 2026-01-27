import streamlit as st
from streamlit_option_menu import option_menu

from projects import model_linebalance
st.set_page_config(page_title="Web App & Model", layout="wide")
def appstreamlit():
    # --- HEADER UI ---
    st.markdown("""
    <div style="background-color: #919292; padding: 20px; border-radius: 5px; color: white; text-align: center;">
        <h1>Industrial Engineering Data Driven</h1>
        <p>Web App and data management</p>
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

