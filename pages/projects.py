import streamlit as st
import os

st.set_page_config(page_title="My Projects", page_icon="🚀", layout="wide")
def Projectt():
    st.title("My Projects")
st.write("---")

# --- Project 1 ---
st.header("Project 1: Improvement JQ Operation")
st.write("`Industrial Engineer Tool`")
st.write(
    """
To enhance our production efficiency, we conducted a root cause analysis to identify the source of a quality issue. We began by observing our employees' work methods. When we determined that wasn't the problem, we continued our investigation and discovered that the root cause was the inconsistent quality of our raw materials.
    """
)

# You can add an image of your project
try:
    image_path = os.path.join("images", "project1_image.jpg")
    if os.path.exists(image_path):
        st.image(image_path, caption="[คำอธิบายภาพ]")
except FileNotFoundError:
    st.warning("Please add your project image file to the 'images' folder.")

st.write("[My Interm Project >](https://hanes-my.sharepoint.com/personal/suksan_tuaklang_hanes_com/Documents/Documents/Suksan_IE2024/00%20Old%20Data/01.IE%20Suksan%20Project/Internship%20Project.pdf)")

st.write("---")

# --- Project 2 ---
st.header("Project 2: Convert PDF to Excel")
st.write("`Python `")
st.write(
    """
    The need arose because I wanted to use data from PDFs, 
    but the files were too large to be imported with Power Query in Excel.
    As a solution, I wrote a script to convert the data from PDF into an Excel format.
    """
)
st.write("[Go to Wep App >](https://pdf-to-csv666.streamlit.app/)")

st.header("Project 3: Query Data With Python")
st.write("`Python `")
st.write(
    """
Developed a Python script to efficiently filter and analyze large Excel files, streamlining data extraction for key reports
    """
)
st.write("[Go to Wep App >](https://layout-raweff-model.streamlit.app/)")

st.write("---")
st.header("**Kaizen**")
st.write("[Kaizen project >](https://hanes-my.sharepoint.com/personal/suksan_tuaklang_hanes_com/Documents/Documents/Reduce%20batack%20time.pdf)")




st.write("---")

st.set_page_config(page_title="Show Code Checkbox", page_icon="📝")

st.title("My Code SQL")

show_code_checkbox = st.checkbox("Check_line_mcuVSmanpower")

if show_code_checkbox:
    code_to_show = """
WITH DailyEfficiencySummary AS (
    SELECT
        DATEPART(wk, [ShiftDate]) AS [Week],
        [ID],
        [Lines],
        SUM([Total Time]) AS [TotalTime]
    FROM [DailyData].[dbo].[tbl_RealTime_Efficiency] with (NOLOCK)
    WHERE
        [ShiftDate] BETWEEN '2025-06-30' AND '2025-07-05' AND [OPCode] IS NOT NULL
    GROUP BY
        DATEPART(wk, [ShiftDate]),
        [ID],
        [Lines]
),
FirstR_nameIE_Week_Data AS (
    SELECT
        rw.[IDemp],
        rw.[Week],
        rw.[Nameline],
        ROW_NUMBER() OVER (PARTITION BY rw.[IDemp], rw.[Week] ORDER BY rw.DateValue ASC) as rn
    FROM [RealTime].[dbo].[R_nameIE_Week] rw
    WHERE
        rw.Week = 27
),
FilteredR_nameIE_Week AS (
    SELECT
        [IDemp],
        [Week],
        [Nameline]
    FROM FirstR_nameIE_Week_Data
    WHERE
        rn = 1
),
CombinedAndCheckedData AS (
    SELECT
        des.[Week],
        des.[ID],
        des.[Lines],
        des.[TotalTime],
        frn.[Nameline],
        CASE
            WHEN LOWER(CAST(frn.[Nameline] AS NVARCHAR(MAX))) LIKE '%' + LOWER(CAST(des.Lines AS NVARCHAR(MAX))) + '%' THEN 1
            ELSE 0
        END AS [check]
    FROM DailyEfficiencySummary des
    LEFT JOIN FilteredR_nameIE_Week frn
        ON des.[ID] = frn.[IDemp]
),
RankedTotalTimePerID AS (
    SELECT
        ccd.*,
        ROW_NUMBER() OVER (PARTITION BY ccd.[ID] ORDER BY ccd.TotalTime DESC) as RankNum
    FROM CombinedAndCheckedData ccd
)
SELECT
    rtp.[Week],
    rtp.[ID],
    rtp.[Lines],
    rtp.[TotalTime],
    rtp.[Nameline],
    rtp.[check]
FROM RankedTotalTimePerID rtp
WHERE
    rtp.RankNum = 1 
ORDER BY
    rtp.[Week],
    rtp.[ID];
"""
    st.code(code_to_show, language='SQL')

st.set_page_config(page_title="Show Code Checkbox", page_icon="📝")

show_code_checkbox = st.checkbox("Incentive_by_week")

if show_code_checkbox:
    code_to_show = """
WITH IndividualIncentiveData AS (
    SELECT
        [ID],
        [Name],
        [Line],
        [Team] AS [Shift],
        [Reg_Hrs],
        [Overtime],
        [Hrs],
        [Output],
        [Rate],
        [SAH Earned],
        [Incentive],
        [Eff %],
        [Shift_Date] AS [date]
    FROM [DailyData].[dbo].[tbl_Individual_Incentive_Efficiency]
    WHERE [Shift_Date] BETWEEN '2025-07-07' AND '2025-07-12'
),
FirstR_nameIE_Week_Data AS (
    SELECT
        rw.[IDemp],
        rw.[Week],
        rw.[JobTitle],        
        rw.[GroupDescription], 
        rw.[Area],              
        -- rw.[Nameline],     
        ROW_NUMBER() OVER (PARTITION BY rw.[IDemp], rw.[Week] ORDER BY rw.DateValue ASC) as rn
    FROM [RealTime].[dbo].[R_nameIE_Week] rw
    WHERE
        rw.Week = 28
),
FilteredR_nameIE_Week AS (
    SELECT
        [IDemp],
        [Week],
        [Jobtitle],
        [GroupDescription],
        [Area]
    FROM FirstR_nameIE_Week_Data
    WHERE
        rn = 1
)
SELECT
    iid.[ID],
    iid.[Name],
    iid.[Line],
    iid.[Shift],
    iid.[Reg_Hrs],
    iid.[Overtime],
    iid.[Hrs],
    iid.[Output],
    iid.[Rate],
    iid.[SAH Earned],
    iid.[Incentive],
    iid.[Eff %],
    iid.[date],
    frn.JobTitle,         
    frn.GroupDescription,  
    frn.Area               
FROM IndividualIncentiveData iid
LEFT JOIN FilteredR_nameIE_Week frn
    ON iid.[ID] = frn.[IDemp]
ORDER BY
    iid.[ID],
    iid.[date];
"""
    st.code(code_to_show, language='SQL')
    








# file: pages/2_Project.py
import streamlit as st

# file: pages/2_Project.py
import streamlit as st

st.title("📂 Projects")

# เมนูเลือก Project ย่อย
project = st.sidebar.radio(
    "เลือกโปรเจ็คที่ต้องการดู",
    ["Project 1", "Project 2", "Project 3", "Project 4", "Project 5", "Project 6"]
)
# เนื้อหาของแต่ละโปรเจ็ค
if project == "Project 1":
    st.header("📊 Improvement JQ Operation")
    st.write("To enhance our production efficiency, we conducted a root cause analysis to identify the source of a quality issue. We began by observing our employees' work methods. When we determined that wasn't the problem, we continued our investigation and discovered that the root cause was the inconsistent quality of our raw materials.")
    st.success("[My Interm Project >](https://hanes-my.sharepoint.com/personal/suksan_tuaklang_hanes_com/Documents/Documents/Suksan_IE2024/00%20Old%20Data/01.IE%20Suksan%20Project/Internship%20Project.pdf)")

elif project == "Project 2":
    st.header("📈 Project 2")
    st.write("รายละเอียดของ Project 2")
    st.info("Demo: ผลลัพธ์/กราฟ/ตารางของ Project 2")

elif project == "Project 3":
    st.header("📉 Project 3")
    st.write("รายละเอียดของ Project 3")
    st.warning("Demo: ผลลัพธ์/กราฟ/ตารางของ Project 3")

elif project == "Project 4":
    st.header("🛠 Project 4")
    st.write("รายละเอียดของ Project 4")
    st.error("Demo: ผลลัพธ์/กราฟ/ตารางของ Project 4")

elif project == "Project 5":
    st.header("🚀 Project 5")
    st.write("รายละเอียดของ Project 5")
    st.success("Demo: ผลลัพธ์/กราฟ/ตารางของ Project 5")

elif project == "Project 6":
    st.header("🔍 Project 6")
    st.write("รายละเอียดของ Project 6")
    st.info("Demo: ผลลัพธ์/กราฟ/ตารางของ Project 6")
