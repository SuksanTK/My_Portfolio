import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

def linebalance():
    st.header("📊 Line Balancing & Takt Time Analysis")
    st.write("เครื่องมือวิเคราะห์สมดุลสายการผลิต")
    data_path = "data/factory_data.csv"
        
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
            
            # --- 2. ส่วนคำนวณ Takt Time (ให้ User ลองปรับเล่นได้) ---
        with st.expander("⏱️ Takt Time Simulation Setting", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                demand = st.number_input("Customer Demand (pcs/Shift)", value=2750)
            with col2:
                    # ลองดึงค่า Working Time มาตรฐาน (เช่น 8 ชม. = 28,800 วินาที)
                takt_time = 3600 / (demand/8)
                st.metric("Target Takt Time", f"{round(takt_time, 2)} sec/pcs")
                
    with st.container():
        col1, col2 = st.columns([1, 1]) 

        # --- Column ซ้าย : Line Balancing Chart ---
        with col1:
            fig = go.Figure()

            # Bar Chart
            fig.add_trace(go.Bar(
                x=df['Process'],
                y=df['CycleTime'],
                name='Actual Cycle Time',
                marker_color=[
                    '#EF553B' if val > takt_time else '#00CC96'
                    for val in df['CycleTime']
                ],
                text=df['CycleTime'],
                textposition='auto',
            ))

            # Takt Time Line
            fig.add_shape(
                type="line",
                x0=-0.5, x1=len(df) - 0.5,
                y0=takt_time, y1=takt_time,
                line=dict(color="Red", width=3, dash="dash"),
            )

            fig.update_layout(
                title=f"Line Balancing Analysis (Sample Data: {os.path.basename(data_path)})",
                xaxis_title="Production Process",
                yaxis_title="Time (Seconds)",
                template="plotly_dark",
                width= 500,
                height= 500
            )

            st.plotly_chart(fig, use_container_width=True)

        # --- Column ขวา : Data Table ---
        with col2:
            st.subheader("📋 Process Data Details")
            st.dataframe(df, use_container_width=True)

            