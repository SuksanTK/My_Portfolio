import streamlit as st
import os
import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(
    page_title="Suksan Tuaklang",
    page_icon=":briefcase:",
    layout="wide"
)
def detailperson():
# Set page configuration
    st.image("images/Profile_2.jpg")

# --- Define the path to your assets and images ---
ASSETS_DIR = "Profile_1.jpg"
IMAGES_DIR = "images"

# --- Main Page Content ---
with st.container():
    st.title("Hi, I'm Suksan Tuaklang (Fluke) 👋")
    st.subheader("Thank you for visit to my site")
    st.write("---")
    st.write(
    """
    As an Industrial Engineer, I'm always on the lookout for new challenges. I'm especially passionate about diving into new work processes and learning more about analytics to build a solid foundation for my future. 
    """
    )
    st.write("")


# --- Contact Section ---
with st.container():
    st.header("Contact Me")
# You can add a button to download your resume
    try:
        resume_path = os.path.join(ASSETS_DIR, "your_resume.pdf")
        if os.path.exists(resume_path):
            with open(resume_path, "rb") as pdf_file:
                st.download_button(
                    label="📥 Download My Resume",
                    data=pdf_file,
                    file_name="your_resume.pdf",
                    mime="application/pdf"
                )
    except FileNotFoundError:
        st.warning("Please add your resume file to the 'assets' folder.")
    st.markdown("""
    [LinkedIn](https://www.linkedin.com/in/suksantk/) | 
    [GitHub](https://github.com/SuksanTK) | 
    [Email](flukzaza1551@gmail.com)
    [Facebook](https://www.facebook.com/share/19aFS1dN5f/?mibextid=wwXIfr)
    [Instagram](https://www.instagram.com/suksantk?igsh=MXRrdmRoZzVubjg2Zw%3D%3D&utm_source=qr)
    """)
    st.write("- **Tell:** 0837365492")

st.title("About Me")
st.write("---")
col1, col2, col3 = st.columns(3)
col1.metric("Age", "29",border=True)
col2.metric("Status", "Single",border=True)
col3.metric("Gender", "Male",border=True)

# --- About Me Section ---
st.header("My Background")
st.write(
    """
    I completed my university degree in 2024. Right after, I joined HBI Manufacturing in Surin, where I'm currently working as an Industrial Engineer. My journey with the company actually started as an intern, and I was fortunate to continue on in a full-time role.
    """
)

st.write("---")

# --- Skills Section ---
st.header("My Skills")

st.write("## Hard Skills")
st.write("**Data Analysis:** The ability to collect, analyze, and interpret large datasets to make informed decisions.")
st.write("**Process Improvement:** Applying methods like Lean Manufacturing, Six Sigma, or Kaizen to enhance efficiency and reduce waste.")
st.write("**Project Management:** The ability to plan, execute, and oversee projects from start to finish.")
st.write("**Python/SQL:** Proficiency in programming and database languages for data manipulation and automation.")
st.write("**Supply Chain Management:** Understanding the flow of goods and services from production to delivery.")

st.write("## Soft Skills")
st.write("**Problem-Solving:** The ability to identify issues, analyze root causes, and develop effective solutions.")
st.write("**Teamwork:** Collaborating with colleagues and different departments to achieve common goals.")
st.write("**Adaptability:** The flexibility to adjust to new challenges, technologies, and work environments.")
st.write("**Attention to Detail:** Meticulousness in work to ensure accuracy and prevent errors.")




st.write("### Engineering Tool")
st.progress(80, text="improvement")
st.progress(80, text="Lean")
st.progress(80, text="PDCA")
st.progress(80, text="KATA")

st.write("### Programming Languages & Frameworks")
st.progress(50, text="Python")
st.progress(75, text="SQL")

st.write("### Tools & Platforms")
st.progress(90, text="Microsoft Excel")
st.progress(80, text="Power BI")
st.progress(80, text="Microsoft Word")
st.progress(80, text="Microsoft Powerpoint")
st.write("---")



st.header("English Language Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Reading", "80%")

with col2:
    st.metric("Speaking", "60%")

with col3:
    st.metric("Writing", "70%")

from streamlit_echarts import st_echarts

options = {
    "title": {"text": "English Language Skills", "left": "center"},
    "tooltip": {"trigger": "item"},
    "legend": {"orient": "vertical", "left": "left"},
    "series": [
        {
            "name": "Skill",
            "type": "pie",
            "radius": "50%",
            "data": [
                {"value": 80, "name": "Reading"},
                {"value": 60, "name": "Speaking"},
                {"value": 70, "name": "Writing"},
            ],
            "emphasis": {
                "itemStyle": {
                    "shadowBlur": 10,
                    "shadowOffsetX": 0,
                    "shadowColor": "rgba(0, 0, 0, 0.5)",
                }
            },
        }
    ],
}
st_echarts(options=options, height="200px")



st.title("Industrial Engineering Plant Self-Assessment")
st.write("---")

# --- 1. Prepare Data ---
# Create a DataFrame with your assessment data
# The 'Score' column represents the percentage (0-100)
# Make sure the 'Category' names match your assessment areas.
data = {
    'Category': [
        'Engineering Organization',
        'Technical Skill',
        'PDCA - Problem Solving Tools',
        'AMT Training',
        'Engineering Program/System',
        'Cost Savings',
        'New Style Introduction'
    ],
    'Score': [20, 20, 22, 25, 21, 27, 21] # ใส่คะแนนของคุณที่นี่ (0-100)
    # 'Score': [70, 76, 92, 35, 81, 67, 61] # ใส่คะแนนของคุณที่นี่ (0-100)
}
df = pd.DataFrame(data)

# --- 2. Create Radar Chart using Plotly Express ---
fig = px.line_polar(
    df,
    r='Score',              # ค่าที่จะแสดงบนรัศมี (คะแนน)
    theta='Category',       # หมวดหมู่ที่จะแสดงบนมุม
    line_close=True,        # ปิดเส้นกราฟให้เป็นรูปหลายเหลี่ยม
    # color_discrete_sequence=["#FF6347"], # สามารถเปลี่ยนสีได้
    # template="plotly_white" # เปลี่ยน theme ได้
)

# Optional: Customize the chart's appearance to match the image
fig.update_traces(
    fill='toself',          # เติมสีภายในรูปหลายเหลี่ยม
    line_color='blue',      # สีเส้นขอบ
    fillcolor='rgba(173, 216, 230, 0.6)' # สีเติมภายใน (ฟ้าอ่อน)
)
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100],  # กำหนดช่วงของแกนรัศมี 0-100%
            tickvals=[0, 20, 40, 60, 80, 100], # กำหนดจุดแสดงค่าบนแกน
            tickmode='array',
            ticktext=['0%', '20%', '40%', '60%', '80%', '100%'], # กำหนดข้อความบนแกน
            showline=True,
            linewidth=1,
            linecolor='gray'
        ),
        angularaxis=dict(
            rotation=90,  # หมุนเริ่มต้นให้เหมือนในรูป
            direction="clockwise" # ทิศทางการหมุน
        )
    ),
    showlegend=False, # ซ่อน legend ถ้าไม่ต้องการ
    title_text="Industrial Engineering Plant Self-Assessment", # หัวข้อกราฟ
    font_size=20
)

# --- 3. Display Chart in Streamlit ---
st.plotly_chart(fig, use_container_width=True)

st.write("---")

# --- My Certificates Section ---
st.header("My Certificates")
st.write("[Python Certificate >](https://skilllane-certificate.s3.ap-southeast-1.amazonaws.com/user-certificate/J903OMJ/user-certificate.pdf?AWSAccessKeyId=AKIATMDCMPRLJDDWINUC&Expires=1756371720&Signature=NaJMFJ4URRuteEebkRE90i706K8%3D)")
st.write("[Data Analytics Certificate >](https://udemy-certificate.s3.amazonaws.com/pdf/UC-ae583170-e45a-4cdb-a005-0eeae1720d95.pdf)")




