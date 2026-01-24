import streamlit as st
from streamlit_option_menu import option_menu

def appstreamlit():
    # ✅ ต้องอยู่บรรทัดแรกของ Streamlit app
    st.set_page_config(page_title="IE Portfolio", layout="wide")

    # --- HEADER UI ---
    st.markdown("""
    <div style="background-color: #AF7AC5; padding: 20px; border-radius: 5px; color: white; text-align: center;">
        <h1>Industrial Engineering Portfolio</h1>
        <p>Advanced Production & Quality Solutions</p>
    </div>
    """, unsafe_allow_html=True)

    # --- NAVIGATION MENU ---
    selected = option_menu(
        menu_title=None,
        options=["Home", "Check Efficiency", "Capacity Calc", "QueryData", "PDF-CSV"],
        icons=["house", "bar-chart", "calculator", "search", "file-pdf"],
        orientation="horizontal"
    )

    # --- IMPORT PROJECTS ---
    from projects import (
        home,
        efficiency_Checking,
        final_calculation,
        query_Layout_Raweff,
        pdf_to_csv
    )

    # --- ROUTER ---
    if selected == "Home":
        home.run()  # แนะนำให้ Home เป็น function ด้วย

    elif selected == "Check Efficiency":
        efficiency_Checking.run()

    elif selected == "Capacity Calc":
        final_calculation.run()

    elif selected == "QueryData":
        query_Layout_Raweff.run()

    elif selected == "PDF-CSV":
        pdf_to_csv.main()
