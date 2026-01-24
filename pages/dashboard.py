import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

def linebalance():
    st.header("📊 Line Balancing & Takt Time Analysis")
    st.write("เครื่องมือวิเคราะห์สมดุลสายการผลิต (ข้อมูลตัวอย่างจากฐานข้อมูลภายใน)")

    # --- 1. การดึงไฟล์อัตโนมัติจาก Folder ---
    # ใช้ Relative Path เพื่อให้รันได้ทุกที่ (ทั้งบนเครื่องและบน Cloud)
    data_path = "data/factory_data.csv"
        
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
            
            # --- 2. ส่วนคำนวณ Takt Time (ให้ User ลองปรับเล่นได้) ---
        with st.expander("⏱️ Takt Time Simulation Setting", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                demand = st.number_input("Customer Demand (pcs/Shift)", value=500)
            with col2:
                    # ลองดึงค่า Working Time มาตรฐาน (เช่น 8 ชม. = 28,800 วินาที)
                takt_time = 3600 / (demand/8)
                st.metric("Target Takt Time", f"{round(takt_time, 2)} sec/pcs")

            # --- 3. การสร้างกราฟ Line Balancing ---
        fig = go.Figure()

            # เพิ่ม Bar Chart
        fig.add_trace(go.Bar(
            x=df['Process'],
            y=df['CycleTime'],
            name='Actual Cycle Time',
            marker_color=['#EF553B' if val > takt_time else '#00CC96' for val in df['CycleTime']],
            text=df['CycleTime'],
            textposition='auto',
        ))

            # เพิ่มเส้น Takt Time
        fig.add_shape(
            type="line",
            x0=-0.5, x1=len(df)-0.5,
            y0=takt_time, y1=takt_time,
            line=dict(color="Red", width=3, dash="dash"),
        )

        fig.update_layout(
            title=f"Line Balancing Analysis (Sample Data: {os.path.basename(data_path)})",
            xaxis_title="Production Process",
            yaxis_title="Time (Seconds)",
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

            # --- 4. ตารางข้อมูลด้านล่าง ---
        st.subheader("📋 Process Data Details")
        st.dataframe(df, use_container_width=True)

    else:
        st.error(f"❌ ไม่พบไฟล์ข้อมูลที่: {data_path} กรุณาตรวจสอบโฟลเดอร์ data")
        