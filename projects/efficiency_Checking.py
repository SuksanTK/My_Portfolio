import streamlit as st
import pandas as pd
import os

# ---------------------------------------------------------
# 📂 FILE PATHS
# ---------------------------------------------------------
FILE_PATHS = {
    "manpower": "lb_uc3_in_template_manpow.csv",
    "stylelist": "lb_uc3_in_template_style_list.csv",
    "raweff": "Raw_Eff_All_Shift MCU.csv",
    "ind_eff": "Individual Efficiency.csv",
    "master_gwc": "Master_GWC.csv",
}

# ---------------------------------------------------------
#  Core Logic Function (Reusable)
# ---------------------------------------------------------
def process_efficiency_data():
    # 1️⃣ Load files
    for key, path in FILE_PATHS.items():
        if not os.path.exists(path):
            st.error(f"❌ ไม่พบไฟล์: {path}")
            return None

    manpower = pd.read_csv(FILE_PATHS["manpower"])
    stylelist = pd.read_csv(FILE_PATHS["stylelist"])
    raweff = pd.read_csv(FILE_PATHS["raweff"], low_memory=False)
    ind_eff = pd.read_csv(FILE_PATHS["ind_eff"], low_memory=False)
    master_gwc = pd.read_csv(FILE_PATHS["master_gwc"])

    # Normalize columns
    for df in [manpower, stylelist, raweff, ind_eff, master_gwc]:
        df.columns = df.columns.str.lower().str.strip()

    # Standardize keys
    for df in [manpower, raweff, ind_eff]:
        if "id" in df.columns:
            df["id"] = df["id"].astype(str).str.strip()

    for df in [stylelist, raweff, master_gwc]:
        if "style" in df.columns:
            df["style"] = df["style"].astype(str).str.strip()

    # Merge base table
    merged = pd.merge(manpower, stylelist, on="line", how="left")
    final_table = merged[["id", "line", "style", "jobtitle"]]

    final_table = pd.merge(final_table, master_gwc[["style", "gwc"]], on="style", how="left")

    eff_agg = raweff.groupby(["id", "style"], as_index=False)["eff"].mean()
    final_table = pd.merge(final_table, eff_agg, on=["id", "style"], how="left")

    missing = final_table[final_table["eff"].isna()].copy()

    # เติม jobtitle
    raweff["id_gwc"] = raweff["id"] + "_" + raweff["gwc"].astype(str)
    missing["id_gwc"] = missing["id"] + "_" + missing["gwc"].astype(str)

    missing = pd.merge(
        missing,
        raweff[["id_gwc", "jobtitle"]].drop_duplicates(),
        on="id_gwc",
        how="left",
        suffixes=("", "_from_raweff")
    )

    missing["jobtitle"] = missing["jobtitle"].fillna(missing["jobtitle_from_raweff"])
    missing.drop(columns=["jobtitle_from_raweff"], inplace=True)

    # เติม eff จาก individual efficiency
    ind_eff["eff %"] = pd.to_numeric(ind_eff["eff %"], errors="coerce")
    avg_ind = ind_eff.groupby("id", as_index=False)["eff %"].mean()

    missing = pd.merge(missing, avg_ind, on="id", how="left")
    missing["eff"] = missing["eff"].fillna(missing["eff %"])
    missing.drop(columns=["eff %"], inplace=True)

    return missing


# ---------------------------------------------------------
#  Streamlit ENTRY POINT
# ---------------------------------------------------------
def run():
    st.subheader("📊 Efficiency Checker")
    st.markdown("ตรวจสอบพนักงานที่ไม่มี Efficiency และเติมค่าอัตโนมัติ")
    mp_file = st.file_uploader("Upload manpower", type="csv")
    style_file = st.file_uploader("Upload style list", type="csv")
    raw_file = st.file_uploader("Upload raw eff", type="csv")
    ind_file = st.file_uploader("Upload individual eff", type="csv")
    gwc_file = st.file_uploader("Upload master GWC", type="csv")

    if all([mp_file, style_file, raw_file, ind_file, gwc_file]):
        manpower = pd.read_csv(mp_file)
        stylelist = pd.read_csv(style_file)
        raweff = pd.read_csv(raw_file, low_memory=False)
        ind_eff = pd.read_csv(ind_file, low_memory=False)
        master_gwc = pd.read_csv(gwc_file)
    if st.button("▶️ Run Efficiency Checker"):
        with st.spinner("กำลังประมวลผล..."):
            result = process_efficiency_data()

        if result is not None:
            st.success(f"✅ พบข้อมูลที่ต้องเติมทั้งหมด {len(result)} แถว")

            display = result[["id", "line", "style", "jobtitle", "gwc", "eff"]].copy()
            display["eff"] = display["eff"].round(2)
            display.columns = ["ID", "Line", "Style", "Job Title", "GWC", "Efficiency"]

            st.dataframe(display, use_container_width=True)

            csv = result.to_csv(index=False).encode("utf-8-sig")
            st.download_button(
                "💾 Download Result CSV",
                csv,
                "filled_eff_result.csv",
                "text/csv"
            )
