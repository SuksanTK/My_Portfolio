import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


def project_ie():

    st.markdown('<p class="section-header">Projects</p><div class="section-divider"></div>', unsafe_allow_html=True)

    # ---- PROJECT DATA ----
    projects_data = [
        {
            "icon": "😊",
            "title": "Happy Workplace Initiative",
            "type": "Cross-Functional",
            "desc": "A cross-departmental initiative improving employee well-being and workplace efficiency — covering Happy Canteen, Happy Toilet, and Happy Day engagement activities.",
            "result": "Improved employee morale, engagement, and working atmosphere.",
            "tags": ["Cross-functional", "Employee Engagement", "Workplace"],
        },
        {
            "icon": "⚙️",
            "title": "Kaizen: Bartack Process Improvement",
            "type": "Kaizen",
            "desc": "Identified that operators lacked a consistent reference point before sewing. Implemented a low-cost plastic strap with position markings as a visual guide.",
            "result": "Reduced cycle time by ~2 minutes per piece, significantly improving operator efficiency.",
            "tags": ["Kaizen", "IE", "Time Reduction"],
        },
        {
            "icon": "📈",
            "title": "Production Improvement (Premium Product)",
            "type": "IE Improvement",
            "desc": "Led a comprehensive improvement project for a premium style initially operating at only 50–60% efficiency. Conducted root cause analysis across Material, Method, and Line Balancing dimensions.",
            "result": "Increased line efficiency to 80–90%, significantly reducing defects, rework, and cost.",
            "tags": ["Root Cause Analysis", "Line Balancing", "Efficiency"],
        },
        {
            "icon": "🔄",
            "title": "Kata Improvement Program",
            "type": "Continuous Improvement",
            "desc": "Implemented Kata methodology with weekly Gemba Walks and short mid-week follow-up meetings to drive continuous improvement through behavior change and team involvement.",
            "result": "Created a culture of continuous improvement with faster problem resolution.",
            "tags": ["Kata", "Gemba Walk", "CI"],
        },
        {
            "icon": "👥",
            "title": "Multiskill Development Project",
            "type": "Workforce Development",
            "desc": "Designed and executed a multiskill development program — collected and analyzed operator skill data, identified critical process gaps, and expanded capability in phases.",
            "result": "60%+ operators with 2+ skills (Phase 1), 25%+ with 3 skills (Phase 2).",
            "tags": ["Skill Matrix", "Workforce Flexibility", "Training"],
        },
        {
            "icon": "🤖",
            "title": "AIoT Transformation Project",
            "type": "Digital Transformation",
            "desc": "Participated in transforming factory operations using real-time data and digital systems. Defined new operational processes transitioning from manual to data-driven workflows.",
            "result": "Enabled real-time performance tracking and faster decision-making.",
            "tags": ["AIoT", "Digital Transformation", "Real-time Data"],
        },
        {
            "icon": "🧠",
            "title": "Line Balance Automation Model",
            "type": "Analytics Collaboration",
            "desc": "Collaborated with the Analytics team to automate the line balancing process using real-time production data. Translated IE logic into clear models and refined system rules.",
            "result": "Weekly prep time: 2–3 days → 1 day. Daily adjustment time: ~2 hours → ~15 minutes.",
            "tags": ["Automation", "Python", "Line Balancing", "Analytics"],
        },
    ]

    # ---- RENDER PROJECTS AS CARDS ----
    for p in projects_data:
        tags_html = " ".join([f'<span class="badge badge-gray">{t}</span>' for t in p["tags"]])
        with st.expander(f"{p['icon']}  {p['title']}", expanded=False):
            st.markdown(f"""
            <div style="padding:0.25rem 0;">
                <p style="font-size:0.78rem; color:#6B7280; font-weight:600; text-transform:uppercase;
                          letter-spacing:0.5px; margin:0 0 0.5rem 0;">{p['type']}</p>
                <p style="font-size:0.92rem; color:#374151; line-height:1.7; margin:0 0 0.75rem 0;">
                    {p['desc']}
                </p>
                <div style="background:#F0FDF4; border-left:3px solid #16A34A; border-radius:0 6px 6px 0;
                            padding:0.6rem 1rem; margin-bottom:1rem;">
                    <p style="font-size:0.85rem; color:#15803D; margin:0; font-weight:500;">
                        🎯 {p['result']}
                    </p>
                </div>
                <div>{tags_html}</div>
            </div>
            """, unsafe_allow_html=True)

    # ---- CERTIFICATES ----
    st.markdown("<div style='margin-top:2.5rem;'></div>", unsafe_allow_html=True)
    st.markdown('<p class="section-header">Certificates</p><div class="section-divider"></div>', unsafe_allow_html=True)

    cert_col1, cert_col2 = st.columns(2)

    with cert_col1:
        with st.expander("🎓  Data Science Bootcamp – Datarockie", expanded=False):
            st.markdown("""
            <p style="font-size:0.85rem; color:#6B7280; margin-bottom:0.75rem;">
            Completed a comprehensive Data Science Bootcamp covering Python, SQL, Machine Learning,
            Statistics, and Data Visualization.
            </p>
            """, unsafe_allow_html=True)
            try:
                pdf_viewer("certificate-of-completion-for-data-science-bootcamp-12.pdf")
            except Exception:
                st.info("PDF preview unavailable.")

        with st.expander("🎓  Basic Python Certificate", expanded=False):
            try:
                pdf_viewer("python-certificate.pdf")
            except Exception:
                st.info("PDF preview unavailable.")

    with cert_col2:
        with st.expander("🎓  Data Science Bootcamp – Udemy", expanded=False):
            try:
                pdf_viewer("Data Science Course udemy.pdf")
            except Exception:
                st.info("PDF preview unavailable.")

        with st.expander("🏅  GSD Certificate", expanded=False):
            try:
                st.image("Gsd certificate.jpg", use_container_width=True)
            except Exception:
                st.info("Image unavailable.")
