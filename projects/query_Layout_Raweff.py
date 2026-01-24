import streamlit as st
import pandas as pd
def run():
# ==============================
# Page config (ต้องอยู่บนสุด)
# ==============================
    st.set_page_config(
    page_title="Data Processing Automation",
    layout="wide"
)
st.title("⚙️ Data Processing Automation")
st.markdown("อัปโหลดไฟล์ > เลือกแท็บ > กดปุ่มประมวลผล > ดาวน์โหลดผลลัพธ์")

# ==============================
# Helper function
# ==============================
def get_cell_count_info(df, name):
    rows = len(df)
    cols = len(df.columns)
    total_cells = rows * cols
    return f"💾 **{name}:** {rows:,} แถว x {cols:,} คอลัมน์ = **{total_cells:,}** เซลล์"


# ==============================
# Process 1
# ==============================
def process_layout_joiner(layout_file, stylelist_file):
    try:
        layout_master = pd.read_csv(layout_file, encoding="utf-8-sig")
        stylelistcode = pd.read_csv(stylelist_file, encoding="utf-8-sig")

        st.info(get_cell_count_info(layout_master, "Layout Master"))
        st.info(get_cell_count_info(stylelistcode, "Style List Code"))

        merged_df = pd.merge(
            layout_master,
            stylelistcode,
            how="inner",
            on="LINELAYOUT"
        )
        return merged_df

    except Exception as e:
        st.error(f"❌ Layout Joiner error: {e}")
        return None


# ==============================
# Process 2
# ==============================
def process_rawdata_model(rawdata_file, stylelist_file):
    try:
        rawdata_df = pd.read_csv(rawdata_file, encoding="utf-8-sig")
        stylelist_df = pd.read_csv(stylelist_file, encoding="utf-8-sig")

        st.info(get_cell_count_info(rawdata_df, "Raw Data ALL"))
        st.info(get_cell_count_info(stylelist_df, "Style List Code"))

        rawdata_df.columns = rawdata_df.columns.str.strip().str.lower()
        stylelist_df.columns = stylelist_df.columns.str.strip().str.lower()

        if "style" not in rawdata_df.columns or "style" not in stylelist_df.columns:
            st.error("❌ ไม่พบคอลัมน์ style")
            return None

        rawdata_df["style"] = rawdata_df["style"].astype(str).str.upper().str.strip()
        stylelist_df["style"] = stylelist_df["style"].astype(str).str.upper().str.strip()

        merged_df = pd.merge(
            rawdata_df,
            stylelist_df.drop(columns=["line"], errors="ignore"),
            on="style",
            how="inner"
        )

        required = ["line", "linkeff", "linkop", "id", "shift", "style", "jobtitle", "eff"]
        for col in required:
            if col not in merged_df.columns:
                st.error(f"❌ ไม่พบคอลัมน์ {col}")
                return None

        merged_df["eff"] = pd.to_numeric(merged_df["eff"], errors="coerce").fillna(0)
        merged_df["eff_adjusted"] = merged_df["eff"] * 1.05

        merged_df["rank"] = (
            merged_df
            .groupby(["id", "style", "jobtitle"])["eff_adjusted"]
            .rank(ascending=False, method="first")
        )

        filtered = merged_df[(merged_df["rank"] <= 2) & (merged_df["eff"] >= 35)]

        if filtered.empty:
            st.warning("⚠️ ไม่พบข้อมูลตามเงื่อนไข")
            return pd.DataFrame()

        st.info(get_cell_count_info(filtered, "ข้อมูลหลังกรอง"))

        result = (
            filtered
            .groupby(
                ["linkeff", "linkop", "id", "line", "shift", "style", "jobtitle"],
                as_index=False
            )["eff"]
            .mean()
            .rename(columns={"eff": "AvgEff"})
        )

        return result

    except Exception as e:
        st.error(f"❌ Raw Data Processor error: {e}")
        return None


# ==============================
# Upload section
# ==============================


st.header("📂 อัปโหลดไฟล์ CSV")

uploaded_layout_master = st.file_uploader("1. layout_master.csv", type="csv")
uploaded_stylelistcode = st.file_uploader("2. stylelistcode.csv", type="csv")
uploaded_rawdata_all = st.file_uploader("3. RawdataALL.csv", type="csv")


# ==============================
# Tabs
# ==============================
tab1, tab2 = st.tabs([
    "Process 1: Layout Joiner",
    "Process 2: Raw Data Model"
])

with tab1:
    if st.button("🚀 Run Layout Joiner"):
        if uploaded_layout_master and uploaded_stylelistcode:
            with st.spinner("Processing..."):
                df1 = process_layout_joiner(
                    uploaded_layout_master,
                    uploaded_stylelistcode
                )
            if df1 is not None:
                st.dataframe(df1)
                st.download_button(
                    "📥 Download CSV",
                    df1.to_csv(index=False).encode("utf-8-sig"),
                    "Layout_result.csv",
                    "text/csv"
                )
        else:
            st.warning("กรุณาอัปโหลดไฟล์ให้ครบ")

with tab2:
    if st.button("🚀 Run Raw Data Model"):
        if uploaded_rawdata_all and uploaded_stylelistcode:
            with st.spinner("Processing..."):
                df2 = process_rawdata_model(
                    uploaded_rawdata_all,
                    uploaded_stylelistcode
                )
            if df2 is not None:
                st.dataframe(df2)
                st.download_button(
                    "📥 Download CSV",
                    df2.to_csv(index=False).encode("utf-8-sig"),
                    "Rawdata_model.csv",
                    "text/csv"
                )
        else:
            st.warning("กรุณาอัปโหลดไฟล์ให้ครบ")