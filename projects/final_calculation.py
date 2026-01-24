import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

# ------------------------------
# ฟังก์ชันสำหรับกรองข้อมูล
# ------------------------------
def filter_production_data(df):
    required_columns = ['ANET', 'QTY', 'Style', 'Asst', 'Zone']
    for col in required_columns:
        if col not in df.columns:
            st.error(f"❌ Production file ไม่มีคอลัมน์ {col}")
            return None

    df['ANET'] = pd.to_numeric(df['ANET'], errors='coerce')
    df['QTY'] = pd.to_numeric(df['QTY'], errors='coerce')

    df_filtered = df.dropna(subset=['QTY'])
    df_filtered = df_filtered[df_filtered['QTY'] != 0].copy()

    condition = (df_filtered['ANET'] == 0) | (df_filtered['ANET'] >= df_filtered['QTY'] / 3)
    df_filtered = df_filtered[condition]

    df_filtered['linkk'] = df_filtered['Zone'].astype(str) + df_filtered['Style'].astype(str)
    return df_filtered


# ------------------------------
# ฟังก์ชันคำนวณ capacity allocation
# ------------------------------
def calculate_capacity(df_production, df_capacity):
    df_merged = pd.merge(df_production, df_capacity, on='linkk', how='left')

    for col in ['Style_y', 'Zone_y']:
        if col in df_merged.columns:
            df_merged = df_merged.drop(columns=[col])

    df_merged = df_merged.rename(columns={'Style_x': 'Style', 'Zone_x': 'Zone'})
    df_merged['Capacity'] = pd.to_numeric(df_merged['Capacity'], errors='coerce')

    results_df = pd.DataFrame(columns=[
        'Zone', 'Asst', 'Style', 'Cap_per_shift', 'Day', 'Shift',
        'Allocated_QTY', 'linkk', 'Group', 'Color', 'Size', 'Original_QTY'
    ])

    for zone, group in df_merged.groupby('Zone'):
        current_day = 1
        remaining_A_capacity = 0
        remaining_B_capacity = 0
        group = group.sort_values(by='Issue date')

        for _, row in group.iterrows():
            QTY_to_allocate = row['QTY']
            cap_per_shift = row['Capacity']

            if pd.isna(cap_per_shift):
                continue

            if remaining_A_capacity == 0 and remaining_B_capacity == 0:
                remaining_A_capacity = cap_per_shift
                remaining_B_capacity = cap_per_shift

            while QTY_to_allocate > 0:
                for shift, remaining in [('A', remaining_A_capacity), ('B', remaining_B_capacity)]:
                    if QTY_to_allocate <= 0 or remaining <= 0:
                        continue

                    allocated = min(QTY_to_allocate, remaining)
                    results_df.loc[len(results_df)] = [
                        zone, row['Asst'], row['Style'], cap_per_shift,
                        current_day, shift, allocated, row['linkk'],
                        row.get('Group'), row.get('Color'),
                        row.get('Size'), row['QTY']
                    ]

                    QTY_to_allocate -= allocated
                    if shift == 'A':
                        remaining_A_capacity -= allocated
                    else:
                        remaining_B_capacity -= allocated

                if QTY_to_allocate > 0:
                    current_day += 1
                    remaining_A_capacity = cap_per_shift
                    remaining_B_capacity = cap_per_shift

    return results_df


# ------------------------------
# 🚀 Streamlit ENTRY POINT
# ------------------------------
def run():
    st.set_page_config(
        page_title="Production Capacity Calculator",
        page_icon="📊",
        layout="wide"
    )

    st.title("📦 Production Capacity Calculator")
    st.markdown(
        "อัปโหลดไฟล์ข้อมูลการผลิต และ capacity เพื่อคำนวณจัดสรรกำลังผลิตอัตโนมัติ"
    )

    # 📁 Upload CSV
    prod_file = st.file_uploader("📁 Upload Production File (CSV)", type="csv")
    cap_file = st.file_uploader("📁 Upload Capacity File (CSV)", type="csv")

    if prod_file and cap_file:
        df_prod = pd.read_csv(prod_file)
        df_cap = pd.read_csv(cap_file)

        st.subheader("📋 ข้อมูลการผลิต (ตัวอย่าง)")
        st.dataframe(df_prod.head(10), use_container_width=True)

        st.subheader("⚙️ ข้อมูล Capacity (ตัวอย่าง)")
        st.dataframe(df_cap.head(10), use_container_width=True)

        if st.button("▶️ Run Calculation"):
            with st.spinner("กำลังคำนวณ..."):
                df_filtered = filter_production_data(df_prod)

                if df_filtered is not None:
                    result = calculate_capacity(df_filtered, df_cap)

                    st.success("✅ คำนวณเสร็จเรียบร้อย!")
                    st.subheader("📊 ผลลัพธ์ตัวอย่าง")
                    st.dataframe(result.head(20), use_container_width=True)

                    csv_output = result.to_csv(index=False).encode("utf-8-sig")
                    st.download_button(
                        "💾 Download Result CSV",
                        csv_output,
                        "calculated_production_capacity.csv",
                        "text/csv"
                    )
    else:
        st.info("👆 กรุณาอัปโหลดไฟล์ทั้งสองก่อนเริ่มการคำนวณ")
