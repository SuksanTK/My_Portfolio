import streamlit as st
import os

st.set_page_config(page_title="My Code For working", page_icon="🚀", layout="wide")

st.title("My Code 101 ")
st.write("---")
st.set_page_config(page_title="Show Code Checkbox", page_icon="📝")

st.title("Code SQL")

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

st.set_page_config(page_title="Show Code Checkbox", page_icon="📝")

show_code_checkbox = st.checkbox("Time stamp working")

if show_code_checkbox:
    code_to_show = """
WITH T3_Latest AS (
    SELECT
        BOLSTY,
        BOLSEQ,
        BOLOP1,
        Start_date, -- รวมคอลัมน์ Start_date เพื่อใช้จัดอันดับ
        ROW_NUMBER() OVER (
            PARTITION BY BOLSTY, BOLSEQ 
            ORDER BY Start_date DESC
        ) AS rn
    FROM
        [DailyData].[dbo].tbl_BOLARC WITH (NOLOCK)
)
SELECT
    T1.EmpID,
    T1.Lines,
    T1.Operation,
    T1.shiftdate,
    T1.shift,
    T1.TimeSlot_Start_30Min,
    T1.TotalDozen,
	T1.style,
    T2.EmployeeName,
    T2.Shift,
    T2.JobTitle,
    T2.GroupDescription,
    T3.BOLOP1 -- ดึง BOLOP1 จาก T3_Latest ที่ถูกกรองแล้ว
FROM
    (
        -- Subquery (T1) : ข้อมูลการผลิตหลักที่ถูกจัดกลุ่ม 30 นาที (คงเดิม)
        SELECT
            EmpID,
            Lines,
            Operation,
            shiftdate,
			Style,
            shift,
            DATEADD(minute, DATEDIFF(minute, 0, Interval_start_Datetime) / 30 * 30, 0) AS TimeSlot_Start_30Min,
            SUM(Pieces) / 12.0 AS TotalDozen
        FROM
            [DailyData].[dbo].[tbl_Output_Gathered_Aggregated_Lowest] WITH (NOLOCK)
        WHERE
            ShiftDate = '2025-11-04'
        GROUP BY
            EmpID,
            Lines,
			Style,
            Operation,
            shiftdate,
            shift,
            DATEADD(minute, DATEDIFF(minute, 0, Interval_start_Datetime) / 30 * 30, 0)
    ) AS T1 -- ตารางหลัก (การผลิต)
LEFT JOIN
    [RealTime].[dbo].[R_nameIE_Week] AS T2 WITH (NOLOCK)
    ON T1.EmpID = T2.IDEmp
    AND T2.week = '45'
-- **Join กับ CTE ที่ถูกกรองแล้ว (T3_Latest)**
LEFT JOIN
    T3_Latest AS T3
    ON T1.Style = T3.BOLSTY
    AND T1.Operation = T3.BOLSEQ
    AND T3.rn = 1 -- **เงื่อนไขสำคัญ: เลือกเฉพาะแถวที่ใหม่ที่สุด**
ORDER BY
    T1.TimeSlot_Start_30Min ASC,
    T1.Lines ASC;
"""
    st.code(code_to_show, language='SQL')

st.set_page_config(page_title="Show Code Checkbox", page_icon="📝")

show_code_checkbox = st.checkbox("Agregress efficiency")

if show_code_checkbox:
    code_to_show = """
WITH Rankdata AS (
    SELECT 
          [ID]
        , [Operator Name]
        , [Shift]
        , [Locations]
        , [Area]
        , [SellStyle]
        , [OPCode]
        , [JobTitle]
        , [SAH Earned hours]
        , [Total Time]
        , [Efficiency]
        , [Pieces]
        , [Dozen]
        , ROW_NUMBER() OVER (
              PARTITION BY [ID], [SellStyle], [OPCode], [JobTitle] 
              ORDER BY [Efficiency] DESC
          ) AS RANK
    FROM 
        [DailyData].[dbo].[tbl_RealTime_Efficiency] WITH (NOLOCK)
    WHERE 
        [ShiftDate] BETWEEN '2025-09-22' AND '2025-09-27'
        AND [OPCode] IS NOT NULL 
        AND [Area] = 'Sew'
        AND [Pieces] >= '144'
        AND [Efficiency] <= '300'
        AND [Efficiency] >= '35'
        AND [SellStyle] IS NOT NULL
)
, FilteredData AS (
    SELECT 
          [ID]
        , [Operator Name]
        , [Shift]
        , [Locations]
        , [Area]
        , [SellStyle]
        , [OPCode]
        , [JobTitle]
        , [SAH Earned hours]
        , [Total Time]
    FROM 
        Rankdata
    WHERE 
        RANK <= 6
)
SELECT 
      [ID]
    , [Operator Name]
    , [Shift]
    , [Locations]
    , [Area]      
    , [SellStyle]
    , [OPCode]
    , [JobTitle]
    , SUM([SAH Earned hours]) AS TotalEarnedHours
    , SUM([Total Time]) AS TotalTime
    , CASE 
          WHEN SUM([Total Time]) > 0 THEN 
              SUM([SAH Earned hours]) * 1.0 / SUM([Total Time])*100
          ELSE 
              NULL 
      END AS AggregateEfficiency
FROM 
    FilteredData
GROUP BY 
      [ID]
    , [Operator Name]
    , [Shift]
    , [Locations]
    , [Area]      
    , [SellStyle]
    , [OPCode]
    , [JobTitle]
ORDER BY 
      [ID]
    , [SellStyle]
    , [OPCode];
"""
    st.code(code_to_show, language='SQL')

st.set_page_config(page_title="Show Code Checkbox", page_icon="📝")

show_code_checkbox = st.checkbox("Location Operator")

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
        [ShiftDate] = '2025-10-07' 
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
        -- ตรวจสอบให้แน่ใจว่า rw.DateValue เป็นชื่อคอลัมน์ที่ถูกต้องสำหรับเรียงลำดับ "อันแรกสุด"
        ROW_NUMBER() OVER (PARTITION BY rw.[IDemp], rw.[Week] ORDER BY rw.DateValue ASC) as rn
    FROM [RealTime].[dbo].[R_nameIE_Week] rw
    WHERE
        rw.Week = 40
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
CombinedAndCheckedData AS ( -- CTE ใหม่สำหรับผลลัพธ์ที่รวมและคำนวณ check แล้ว
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
RankedTotalTimePerID AS ( -- CTE สุดท้ายสำหรับจัดอันดับ TotalTime ของแต่ละ ID
    SELECT
        ccd.*, -- เลือกทุกคอลัมน์จาก CombinedAndCheckedData
        ROW_NUMBER() OVER (PARTITION BY ccd.[ID] ORDER BY ccd.TotalTime DESC) as RankNum
        -- ^^^ จัดอันดับ TotalTime ภายในแต่ละ ID จากมากไปน้อย
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
    rtp.RankNum = 1 -- กรองเอาเฉพาะแถวที่มี TotalTime สูงสุดสำหรับแต่ละ ID
ORDER BY
    rtp.[Week],
    rtp.[ID]; -- อาจจะเรียงตาม ID อย่างเดียว เพราะ Lines ถูกเลือกเฉพาะค่ามากสุดแล้ว
"""
    st.code(code_to_show, language='SQL')

st.set_page_config(page_title="Show Code Checkbox", page_icon="📝")

show_code_checkbox = st.checkbox("Agregress efficienc")

if show_code_checkbox:
    code_to_show = """
WITH DailyEfficiencySummary AS (
    SELECT
        DATEPART(wk, [ShiftDate]) AS [Week],
        [ID],
        -- เปลี่ยนเป็น Job Title แทน Lines
        [JobTitle], -- <<<<<<< สมมติว่านี่คือคอลัมน์สำหรับ Job Title
        SUM([Total Time]) AS [TotalTime]
    FROM [DailyData].[dbo].[tbl_RealTime_Efficiency] with (NOLOCK)
    WHERE
        [ShiftDate] BETWEEN '2025-09-22' AND '2025-09-27' AND [OPCode] IS NOT NULL
    GROUP BY
        DATEPART(wk, [ShiftDate]),
        [ID],
        -- Group By ด้วย JobTitle แทน Lines
        [JobTitle] -- <<<<<<< Group By ด้วย Job Title
),
FirstR_nameIE_Week_Data AS (
    SELECT
        rw.[IDemp],
        rw.[Week],
        rw.[Nameline],
        -- ตรวจสอบให้แน่ใจว่า rw.DateValue เป็นชื่อคอลัมน์ที่ถูกต้องสำหรับเรียงลำดับ "อันแรกสุด"
        ROW_NUMBER() OVER (PARTITION BY rw.[IDemp], rw.[Week] ORDER BY rw.DateValue ASC) as rn
    FROM [RealTime].[dbo].[R_nameIE_Week] rw
    WHERE
        rw.Week = 39
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
        -- ดึง JobTitle แทน Lines
        des.[JobTitle], -- <<<<<<< Job Title
        des.[TotalTime],
        frn.[Nameline],
        -- Note: การตรวจสอบ 'check' เดิมใช้ [Lines]
        -- ถ้า Nameline ควรเปรียบเทียบกับ JobTitle ให้เปลี่ยนบรรทัดถัดไป
        -- แต่ถ้ายังต้องการเปรียบเทียบกับ Lines เดิม (ซึ่งตอนนี้หายไปแล้ว)
        -- หรือไม่ต้องการการตรวจสอบนี้เลย อาจต้องพิจารณาใหม่
        CASE
            -- เนื่องจากไม่มี Lines แล้ว จึงไม่สามารถทำการ 'check' ตามเงื่อนไขเดิมได้
            -- ถ้า JobTitle มีความสัมพันธ์กับ Nameline ให้เปลี่ยนเป็น JobTitle
            -- แต่ถ้า 'check' ไม่เกี่ยวข้องแล้ว สามารถลบ CTE นี้ได้ หรือปรับให้เป็น 0/1 ตลอด
            -- เพื่อรักษาโครงสร้างเดิม ผมตั้งค่า 'check' ให้เป็น 1
            WHEN 1 = 1 THEN 1 -- เปลี่ยนเงื่อนไข เนื่องจากไม่มี des.Lines แล้ว
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
        -- จัดอันดับ TotalTime ภายในแต่ละ ID จากมากไปน้อย
    FROM CombinedAndCheckedData ccd
)
SELECT
    rtp.[Week],
    rtp.[ID],
    -- แสดง JobTitle แทน Lines
    rtp.[JobTitle] AS [JobTitle], -- <<<<<<< แสดง Job Title
    rtp.[TotalTime],
    rtp.[Nameline],
    rtp.[check]
FROM RankedTotalTimePerID rtp
WHERE
    rtp.RankNum = 1 -- กรองเอาเฉพาะแถวที่มี TotalTime สูงสุดสำหรับแต่ละ ID
ORDER BY
    rtp.[Week],
    rtp.[ID];
"""