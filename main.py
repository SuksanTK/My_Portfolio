import streamlit as st
from streamlit_option_menu import option_menu
import base64
from pages import about_me, expjob, projects, app, resume_Page
from projects import begining_code

st.set_page_config(
    page_title="Suksan Portfolio",
    page_icon="🗂️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---- GLOBAL CSS: Minimalist Theme ----
st.markdown("""
<style>
/* ===== IMPORT FONT ===== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ===== BASE ===== */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #111827;
}

/* ===== FORCE LIGHT BACKGROUND ===== */
.stApp {
    background-color: #FFFFFF !important;
}
[data-testid="stAppViewContainer"] {
    background-color: #FFFFFF !important;
}
[data-testid="stHeader"] {
    background-color: #FFFFFF !important;
}
.main .block-container {
    background-color: #FFFFFF !important;
}

/* ===== FORCE TEXT COLORS ===== */
p, span, div, li, ul, ol, h1, h2, h3, h4, h5, h6, label {
    color: inherit;
}
.stMarkdown, .stMarkdown p, .stMarkdown span {
    color: #374151 !important;
}
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    color: #111827 !important;
}

/* ===== STREAMLIT NATIVE ELEMENTS ===== */
.stSelectbox label, .stTextInput label, .stTextArea label,
.stNumberInput label, .stSlider label, .stCheckbox label,
.stRadio label, .stMultiSelect label {
    color: #374151 !important;
    font-weight: 500 !important;
}
.stSelectbox [data-testid="stWidgetLabel"] > p,
.stTextInput [data-testid="stWidgetLabel"] > p {
    color: #374151 !important;
}

/* ===== EXPANDER ===== */
[data-testid="stExpander"] {
    border: 1px solid #E5E7EB !important;
    border-radius: 8px !important;
    background: #FFFFFF !important;
}
[data-testid="stExpander"] summary {
    color: #111827 !important;
    background: #FFFFFF !important;
}
[data-testid="stExpander"] summary:hover {
    background: #F9FAFB !important;
}
[data-testid="stExpander"] > div > div {
    background: #FFFFFF !important;
}

/* ===== DATAFRAME / TABLE ===== */
[data-testid="stDataFrame"] {
    background: #FFFFFF !important;
}

/* ===== INPUT WIDGETS ===== */
.stTextInput input, .stTextArea textarea, .stNumberInput input {
    background-color: #F9FAFB !important;
    color: #111827 !important;
    border: 1px solid #D1D5DB !important;
    border-radius: 8px !important;
}
.stSelectbox [data-baseweb="select"] > div {
    background-color: #F9FAFB !important;
    border: 1px solid #D1D5DB !important;
    color: #111827 !important;
}

/* ===== TABS ===== */
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    background-color: #FFFFFF !important;
}
[data-testid="stTabs"] [data-baseweb="tab"] {
    color: #6B7280 !important;
}
[data-testid="stTabs"] [aria-selected="true"] {
    color: #2563EB !important;
}

/* ===== INFO / SUCCESS / WARNING / ERROR BOXES ===== */
[data-testid="stAlert"] {
    background-color: #F9FAFB !important;
    color: #374151 !important;
}

/* ===== METRIC ===== */
[data-testid="stMetric"] label {
    color: #6B7280 !important;
}
[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #111827 !important;
}

/* ===== HIDE DEFAULT STREAMLIT NAV ===== */
[data-testid="stSidebarNav"] { display: none; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* ===== SIDEBAR ===== */
[data-testid="stSidebar"] {
    background-color: #FAFAFA;
    border-right: 1px solid #EBEBEB;
}
[data-testid="stSidebar"] .stMarkdown p {
    font-size: 0.82rem;
    color: #6B7280;
}

/* ===== MAIN CONTENT ===== */
.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 1100px;
}

/* ===== SECTION HEADER ===== */
.section-header {
    font-size: 1.75rem;
    font-weight: 700;
    color: #111827;
    letter-spacing: -0.5px;
    margin-bottom: 0.25rem;
}
.section-divider {
    width: 40px;
    height: 3px;
    background: #2563EB;
    border-radius: 2px;
    margin-bottom: 2rem;
}

/* ===== CARD ===== */
.card {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: box-shadow 0.2s ease;
}
.card:hover {
    box-shadow: 0 4px 20px rgba(0,0,0,0.07);
}

/* ===== BADGE / TAG ===== */
.badge {
    display: inline-block;
    background: #EFF6FF;
    color: #1D4ED8;
    border: 1px solid #BFDBFE;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 500;
    margin: 3px 2px;
}
.badge-gray {
    background: #F3F4F6;
    color: #374151;
    border: 1px solid #D1D5DB;
}
.badge-green {
    background: #F0FDF4;
    color: #16A34A;
    border: 1px solid #BBF7D0;
}

/* ===== TIMELINE ===== */
.timeline-item {
    position: relative;
    padding-left: 1.5rem;
    border-left: 2px solid #E5E7EB;
    margin-bottom: 2rem;
    padding-bottom: 0.5rem;
}
.timeline-dot {
    position: absolute;
    left: -6px;
    top: 6px;
    width: 10px;
    height: 10px;
    background: #2563EB;
    border-radius: 50%;
    border: 2px solid white;
    box-shadow: 0 0 0 2px #2563EB;
}
.timeline-date {
    font-size: 0.78rem;
    color: #6B7280;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.25rem;
}
.timeline-title {
    font-size: 1.05rem;
    font-weight: 600;
    color: #111827;
    margin-bottom: 0.15rem;
}
.timeline-company {
    font-size: 0.88rem;
    color: #2563EB;
    font-weight: 500;
    margin-bottom: 0.75rem;
}

/* ===== PROJECT CARD ===== */
.project-card {
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 0.75rem;
    border-left: 3px solid #2563EB;
}
.project-title {
    font-size: 0.98rem;
    font-weight: 600;
    color: #111827;
    margin-bottom: 0.5rem;
}
.project-desc {
    font-size: 0.85rem;
    color: #6B7280;
    line-height: 1.6;
}

/* ===== STAT BOX ===== */
.stat-box {
    text-align: center;
    padding: 1.25rem;
    background: #F9FAFB;
    border-radius: 10px;
    border: 1px solid #E5E7EB;
}
.stat-number {
    font-size: 1.8rem;
    font-weight: 700;
    color: #2563EB;
    line-height: 1;
}
.stat-label {
    font-size: 0.78rem;
    color: #6B7280;
    margin-top: 0.35rem;
    font-weight: 500;
}

/* ===== SOCIAL LINK ===== */
.social-links a {
    color: #6B7280;
    text-decoration: none;
    font-size: 0.82rem;
    margin-right: 8px;
    transition: color 0.2s;
}
.social-links a:hover { color: #2563EB; }

/* ===== DOWNLOAD BUTTON ===== */
.stDownloadButton button {
    background-color: #2563EB !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
    padding: 0.5rem 1.5rem !important;
}
.stDownloadButton button:hover {
    background-color: #1D4ED8 !important;
}

/* ===== EXPANDER STYLE ===== */
.streamlit-expanderHeader {
    font-weight: 600 !important;
    color: #111827 !important;
    font-size: 0.95rem !important;
}
</style>
""", unsafe_allow_html=True)


def get_base64_image(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None


logo_base64 = get_base64_image("profilenormal.png")

if logo_base64:
    logo_html = f"""
    <div style="display:flex; justify-content:center; margin-bottom:1rem;">
        <img src="data:image/png;base64,{logo_base64}"
             style="width:110px; height:110px; border-radius:50%; object-fit:cover;
                    border: 3px solid #E5E7EB; box-shadow: 0 2px 12px rgba(0,0,0,0.1);">
    </div>
    """
else:
    logo_html = ""

with st.sidebar:
    st.markdown(logo_html, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin-bottom:1.25rem;">
        <p style="font-size:1rem; font-weight:700; color:#111827; margin:0;">Suksan Tuaklang</p>
        <p style="font-size:0.78rem; color:#6B7280; margin:0; margin-top:2px;">Industrial Engineer · Data Driven</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border:none; border-top:1px solid #E5E7EB; margin:0 0 1rem 0;'>", unsafe_allow_html=True)

    nav_tab_op = option_menu(
        menu_title=None,
        options=["About Me", "Resume", "Experience", "Web App & Model", "Project & Certificate"],
        icons=["person", "file-text", "briefcase", "grid", "folder2-open"],
        default_index=0,
        styles={
            "container": {"padding": "0", "background-color": "transparent"},
            "icon": {"color": "#6B7280", "font-size": "14px"},
            "nav-link": {
                "font-size": "0.88rem",
                "font-weight": "500",
                "color": "#374151",
                "padding": "0.55rem 1rem",
                "border-radius": "8px",
                "margin-bottom": "2px",
            },
            "nav-link-selected": {
                "background-color": "#EFF6FF",
                "color": "#2563EB",
                "font-weight": "600",
            },
            "menu-title": {"display": "none"},
        },
    )

    st.markdown("<hr style='border:none; border-top:1px solid #E5E7EB; margin:1rem 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div class="social-links" style="text-align:center; padding: 0 0.5rem;">
        <a href="https://www.linkedin.com/in/suksantk/" target="_blank">LinkedIn</a> ·
        <a href="https://github.com/SuksanTK" target="_blank">GitHub</a> ·
        <a href="mailto:flukzaza1551@gmail.com">Email</a>
    </div>
    <p style="text-align:center; font-size:0.78rem; color:#9CA3AF; margin-top:0.5rem;">📞 083-736-5492</p>
    """, unsafe_allow_html=True)


# ---- PAGE ROUTER ----
if nav_tab_op == "About Me":
    about_me.detailperson()
elif nav_tab_op == "Resume":
    resume_Page.resume()
elif nav_tab_op == "Experience":
    expjob.exp()
elif nav_tab_op == "Web App & Model":
    app.appstreamlit()
elif nav_tab_op == "Project & Certificate":
    projects.project_ie()
