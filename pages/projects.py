import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_pdf_viewer import pdf_viewer
st.set_page_config(page_title="IE Project", layout="wide")
def project_ie():
    with st.expander("Happy Workplace Initiative"):
        st.subheader("Happy Workplace Initiative (Cross‑Functional Project)")
        st.markdown("""
        **Description:**
        A cross‑departmental initiative aimed at improving employee well‑being and workplace efficiency by addressing both physical environment and engagement.
        - **Happy Canteen:** Improved food quality, lighting, and seating layout to enhance comfort and hygiene.
        - **Happy Toilet:** Upgraded restroom cleanliness, facilities, and maintenance standards to improve usability and employee satisfaction.
        - **Happy Day:** Organized employee engagement activities such as running and wellness events to promote health and team bonding.
        **Impact:** Improved employee morale, engagement, and overall working atmosphere, supporting sustainable productivity.
   """)
    with st.expander("Kaizen Project: Bartack Process Improvement"):
        st.subheader("Kaizen Project: Bartack Process Improvement")
        st.markdown("""
        **Description:**
        Focused on improving operator efficiency in the Bartack sewing process through simple but effective Kaizen solutions.
        - Observed operators with performance below standard to identify root causes.
        - Identified lack of a consistent reference point before sewing as the main issue.
        - Implemented a low‑cost solution by installing a plastic strap with position markings on the machine as a visual guide.
        **Result:**  Reduced cycle time by approximately 2 minutes per piece, significantly improving operator efficiency and consistency.
   """)
    with st.expander("Production Improvement Project (Premium Product)"):
        st.subheader("Production Improvement Project (Premium Product)")
        st.markdown("""
        Led a comprehensive improvement project for a premium style with complex design and sewing methods, initially operating at only 50–60% efficiency.
        - Conducted **Root Cause Analysis** to systematically identify and prioritize issues.
        - **Material Issue:** Resolved inconsistent cut‑part dimensions that caused sewing instability, quality defects, and rework.
        - **Method Issue:** Addressed incorrect working methods by retraining operators with technicians, emphasizing pattern understanding and precision over speed.
        - **Line Balancing Issue:** Eliminated bottlenecks at early production stages by cross‑training downstream operators to support constrained processes.
        **Result:** Increased line efficiency to 80–90%, while significantly reducing defects, rework, and production cost.
   """)
    with st.expander("Kata Improvement Program"):
        st.subheader("Kata Improvement Program (Continuous Improvement)")
        st.markdown("""
        Implemented Kata methodology to drive small, continuous improvements through behavior change and team involvement.
        - Conducted weekly Gemba Walks to identify operational gaps and inefficiencies.
        - Held short, focused mid‑week follow‑up meetings (5–10 minutes per line) with relevant stakeholders to track progress and remove obstacles.
        - Reinforced correct working behaviors through repetition and standardization.
        - **Line Balancing Issue:** Eliminated bottlenecks at early production stages by cross‑training downstream operators to support constrained processes.
        **Outcome:** Created a culture of continuous improvement with faster problem resolution and stronger ownership at line level.
   """)
    with st.expander("Multiskill Development Project"):
        st.subheader("Multiskill Development Project")
        st.markdown("""
        Designed and executed a multiskill development program to improve workforce flexibility and stabilize line balance.
        - Collected and analyzed operator skill data and production style requirements.
        - Identified critical processes with limited skilled operators.
        - Increased workforce capability in phases:
            - Achieved 60%+ of operators with at least 2 skills in Phase 1.
            - Expanded 3‑skill operators to 25%+ in later phases.
        **Impact:** Improved line stability, reduced disruption from absenteeism, and enhanced responsiveness to production changes.
   """)
    with st.expander("AIoT Transformation Project"):
        st.subheader("AIoT Transformation Project")
        st.markdown("""
        Participated in a large‑scale project to transform factory operations using real‑time data and digital systems.
        - Defined new operational processes transitioning from manual to data‑driven workflows.
        - Analyzed process impact and risks, proposing mitigation and improvement actions.
        - Established new standard operating procedures aligned with digital workflows.
        **Result:** Enabled real‑time performance tracking, faster decision‑making, and a stronger data‑driven production culture.
   """)
    with st.expander("Model Line Balance Automation Project (with Analytics Team)"):
        st.subheader("Model Line Balance Automation Project (with Analytics Team)")
        st.markdown("""
        Collaborated with the Analytics team to automate and optimize the line balancing process using real‑time production data.
        - Translated IE line balancing logic into clear models and rules for analytics development.
        - Reviewed and refined system logic to align with real production constraints.  
        **Key Result**  
        - Reduced weekly line balance preparation time from 2–3 days to 1 day.
        - Reduced daily line balance adjustment time from ~2 hours to ~15 minutes.
        - Allowed IE teams to spend more time on on‑site improvement and problem‑solving.
   """)
    st.header("📜 My Certificates")

    # -------------------------------
    # Row 1
    # -------------------------------
    with st.container():
        col1, col2 = st.columns(2)

        # Certificate 1
        with col1.expander("Data Science Bootcamp – Datarockie", expanded=False):
            st.subheader("Data Science Bootcamp – Datarockie")
            pdf_viewer("certificate-of-completion-for-data-science-bootcamp-12.pdf")

        # Certificate 2
        with col2.expander("Data Science Bootcamp – Udemy", expanded=False):
            st.subheader("Data Science Bootcamp – Udemy")
            pdf_viewer("Data Science Course udemy.pdf")

    # -------------------------------
    # Row 2
    # -------------------------------
    with st.container():
        col1, col2 = st.columns(2)

        # Certificate 3
        with col1.expander("Basic Python Certificate", expanded=False):
            st.subheader("Basic Python Certificate")
            pdf_viewer("python-certificate.pdf")

        # Certificate 4 (Image)
        with col2.expander("Additional Certificate", expanded=False):
            st.subheader("Additional Certificate")
            st.image("Gsd certificate.jpg", use_container_width=True)