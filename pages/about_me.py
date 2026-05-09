import streamlit as st
import base64


def get_base64_image(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None


def detailperson():

    # ---- HERO SECTION ----
    profile_b64 = get_base64_image("profilesuit.png") or get_base64_image("profilenormal.png")
    img_tag = (
        f'<img src="data:image/png;base64,{profile_b64}" '
        'style="width:160px; height:160px; border-radius:50%; object-fit:cover; '
        'border:3px solid #E5E7EB; box-shadow:0 4px 20px rgba(0,0,0,0.1);">'
        if profile_b64
        else ""
    )

    st.markdown(f"""
    <div style="display:flex; align-items:center; gap:2rem; padding:2rem 0 1.5rem 0;
                border-bottom:1px solid #F3F4F6; margin-bottom:2rem;">
        {img_tag}
        <div>
            <p style="font-size:0.82rem; color:#6B7280; font-weight:500;
                      letter-spacing:1px; text-transform:uppercase; margin:0 0 4px 0;">
                Industrial Engineer
            </p>
            <h1 style="font-size:2.2rem; font-weight:700; color:#111827;
                       letter-spacing:-0.5px; margin:0 0 6px 0;">
                Suksan Tuaklang
            </h1>
            <p style="font-size:0.95rem; color:#6B7280; margin:0 0 1rem 0; max-width:520px; line-height:1.6;">
                Data-Driven IE bridging the gap between shop-floor operations
                and analytical decision-making.
            </p>
            <div>
                <span class="badge">Python</span>
                <span class="badge">SQL</span>
                <span class="badge">Streamlit</span>
                <span class="badge">Line Balancing</span>
                <span class="badge">Data Analysis</span>
                <span class="badge badge-green">Open to Work</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---- QUICK STATS ----
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""<div class="stat-box">
            <div class="stat-number">2+</div>
            <div class="stat-label">Years as IE</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="stat-box">
            <div class="stat-number">7+</div>
            <div class="stat-label">Projects</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="stat-box">
            <div class="stat-number">4</div>
            <div class="stat-label">Streamlit Apps</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="stat-box">
            <div class="stat-number">3</div>
            <div class="stat-label">Certificates</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='margin-top:2rem;'></div>", unsafe_allow_html=True)

    # ---- BIO + SKILLS ----
    col_bio, col_skills = st.columns([3, 2], gap="large")

    with col_bio:
        st.markdown('<p class="section-header">About Me</p><div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="color:#374151; font-size:0.93rem; line-height:1.85;">
        <p>
        I am an Industrial Engineer with a strong passion for continuous improvement and
        data-driven manufacturing. My journey did not begin in a traditional engineering
        pathway — I hold a degree in <strong>Business Administration</strong>. However,
        through hands-on experience, ambition, and continuous self-development, I
        transitioned into the Industrial Engineering field and built my career from
        the factory floor upward.
        </p>
        <p>
        My professional background started in the <strong>Quality Control</strong> department
        at HBI Manufacturing, where I gained a solid foundation in quality standards, defect
        analysis, and production discipline. I later joined as a full-time Industrial Engineer,
        focusing on <strong>line balancing</strong>, manpower planning, work measurement, and
        on-floor problem solving.
        </p>
        <p>
        Over time, my role evolved into <strong>IE analysis and data-driven improvement</strong>.
        I now work extensively with real-time manufacturing data, transforming raw system data
        into insights, reports, and analytical models. I see myself as a bridge between
        operations and data — combining shop-floor experience with analytical thinking.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col_skills:
        st.markdown('<p class="section-header">Skills</p><div class="section-divider"></div>', unsafe_allow_html=True)

        st.markdown("**Programming & Data**", unsafe_allow_html=False)
        st.markdown("""
        <div style="margin-bottom:1rem;">
            <span class="badge">Python</span>
            <span class="badge">SQL</span>
            <span class="badge">Pandas</span>
            <span class="badge">Plotly</span>
            <span class="badge">Streamlit</span>
            <span class="badge">Scikit-Learn</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**IE & Manufacturing**", unsafe_allow_html=False)
        st.markdown("""
        <div style="margin-bottom:1rem;">
            <span class="badge badge-gray">Line Balancing</span>
            <span class="badge badge-gray">Time Study</span>
            <span class="badge badge-gray">Manpower Planning</span>
            <span class="badge badge-gray">Kaizen</span>
            <span class="badge badge-gray">Gemba Walk</span>
            <span class="badge badge-gray">AQL</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Tools & Platforms**", unsafe_allow_html=False)
        st.markdown("""
        <div style="margin-bottom:1rem;">
            <span class="badge badge-gray">GitHub</span>
            <span class="badge badge-gray">Excel / Power BI</span>
            <span class="badge badge-gray">Jupyter Notebook</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Soft Skills**", unsafe_allow_html=False)
        st.markdown("""
        <div>
            <span class="badge badge-gray">Problem Solving</span>
            <span class="badge badge-gray">Cross-functional Collab</span>
            <span class="badge badge-gray">Data Storytelling</span>
        </div>
        """, unsafe_allow_html=True)
