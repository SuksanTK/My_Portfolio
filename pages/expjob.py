import streamlit as st


def exp():
    st.markdown('<p class="section-header">Experience</p><div class="section-divider"></div>', unsafe_allow_html=True)

    # ---- JOB 1: IE ----
    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <p class="timeline-date">April 2024 – April 2026</p>
        <p class="timeline-title">Industrial Engineer</p>
        <p class="timeline-company">HBI Manufacturing (Thailand) Co., Ltd.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("1 · Line Balancing & Production Setup", expanded=False):
        st.markdown("""
        <div class="card" style="margin-bottom:0;">
        <ul style="margin:0; padding-left:1.2rem; color:#374151; font-size:0.9rem; line-height:1.8;">
            <li>Conducted line balancing for new styles — construction analysis, method study, issue identification, and critical operation analysis in collaboration with the NSI team.</li>
            <li>Managed line balancing for existing styles — layout arrangement, headcount preparation, operator retraining, skill testing, and new operator training.</li>
            <li>Shared weekly line balance updates for new styles, line conversions, and critical styles with cross-functional teams (Production, IE, Planning).</li>
            <li>Performed daily efficiency (%Eff) tracking, monitored line performance, and identified improvement opportunities.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("2 · Manpower & Operator Management", expanded=False):
        st.markdown("""
        <div class="card" style="margin-bottom:0;">
        <ul style="margin:0; padding-left:1.2rem; color:#374151; font-size:0.9rem; line-height:1.8;">
            <li>Adjusted manpower levels for lines not meeting line balance targets, in coordination with supervisors and attendance control.</li>
            <li>Rebalanced production lines following manpower adjustments to ensure optimal capacity utilization.</li>
            <li>Maintained and updated Skill Matrix and Efficiency Matrix for operators.</li>
            <li>Focused on improving performance of low-efficiency operators through targeted analysis and support.</li>
            <li>Planned and executed multi-skill training programs, monitoring efficiency improvement and supporting new style training.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("3 · On-floor Problem Solving & Quality Support", expanded=False):
        st.markdown("""
        <div class="card" style="margin-bottom:0;">
        <ul style="margin:0; padding-left:1.2rem; color:#374151; font-size:0.9rem; line-height:1.8;">
            <li>Conducted time studies (T/T) on production lines with existing or potential performance issues.</li>
            <li>Performed Gemba walks to observe actual production conditions, identify root causes, and implement corrective actions.</li>
            <li>Supported quality problem analysis using 4M framework (Man, Machine, Method, Material).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("4 · Data-Driven IE & Analytics Support", expanded=False):
        st.markdown("""
        <div class="card" style="margin-bottom:0;">
        <ul style="margin:0; padding-left:1.2rem; color:#374151; font-size:0.9rem; line-height:1.8;">
            <li>Analyzed real-time production data to identify efficiency gaps, performance trends, and improvement opportunities.</li>
            <li>Processed and cleaned raw system data to generate structured reports and analytical summaries for management.</li>
            <li>Validated and monitored real-time data accuracy; communicated findings to development teams for system improvement.</li>
            <li>Collaborated with Analytics team to design a line balancing forecasting model, significantly reducing manual effort.</li>
            <li>Developed data extraction logic for: employee scan-in/scan-out vs. actual working time, non-productive time analysis, and downtime gap patterns.</li>
            <li>Began implementing <strong>Python and SQL</strong> solutions to automate data extraction, analysis, and IE reporting.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom:0.5rem;'></div>", unsafe_allow_html=True)

    # ---- JOB 2: Internship ----
    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <p class="timeline-date">November 2023 – March 2024</p>
        <p class="timeline-title">Industrial Engineering Intern</p>
        <p class="timeline-company">HBI Manufacturing (Thailand) Co., Ltd.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("Internship Responsibilities", expanded=False):
        st.markdown("""
        <div class="card" style="margin-bottom:0;">
        <p style="color:#374151; font-size:0.9rem; line-height:1.7; margin-bottom:0.75rem;">
        Supported IE projects with a focus on productivity improvement and data-driven analysis.
        Worked closely with senior IEs to apply IE principles in real production environments.
        </p>
        <ul style="margin:0; padding-left:1.2rem; color:#374151; font-size:0.9rem; line-height:1.8;">
            <li><strong>Auto Line Balance Support:</strong> Collected data for the auto line balance automation project.</li>
            <li><strong>Process Improvement:</strong> Took a project from senior IE to improve a small production line using IE logic.</li>
            <li><strong>Testing & Feedback:</strong> Brainstormed and tested logic for the auto line balance system.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom:0.5rem;'></div>", unsafe_allow_html=True)

    # ---- JOB 3: QC ----
    st.markdown("""
    <div class="timeline-item" style="border-left-color:#D1D5DB;">
        <div class="timeline-dot" style="background:#9CA3AF; box-shadow:0 0 0 2px #9CA3AF;"></div>
        <p class="timeline-date">May 2018 – May 2020</p>
        <p class="timeline-title">Quality Control</p>
        <p class="timeline-company">HBI Manufacturing (Thailand) Co., Ltd.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("QC Responsibilities", expanded=False):
        st.markdown("""
        <div class="card" style="margin-bottom:0;">
        <p style="color:#374151; font-size:0.9rem; line-height:1.7; margin-bottom:0.75rem;">
        Ensured product quality and compliance throughout the final stages of manufacturing.
        Built a strong foundation in quality awareness and process discipline.
        </p>
        <ul style="margin:0; padding-left:1.2rem; color:#374151; font-size:0.9rem; line-height:1.8;">
            <li><strong>End-Line QC:</strong> Inspected finished products at the end of the production line to identify defects.</li>
            <li><strong>Outgoing Quality Inspection (AQL):</strong> Performed lot-by-lot inspections per AQL standards prior to shipment.</li>
            <li><strong>Final Audit:</strong> Conducted final quality audits before container loading; prepared audit reports for internal departments.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # ---- KEY TOOLS ----
    st.markdown("<div style='margin-top:2rem;'></div>", unsafe_allow_html=True)
    st.markdown('<p class="section-header" style="font-size:1.1rem;">Tools Used</p>', unsafe_allow_html=True)
    st.markdown("""
    <div style="margin-top:0.5rem;">
        <span class="badge">Python</span>
        <span class="badge">SQL</span>
        <span class="badge">Streamlit</span>
        <span class="badge badge-gray">Excel</span>
        <span class="badge badge-gray">Power BI</span>
        <span class="badge badge-gray">Line Balancing Software</span>
        <span class="badge badge-gray">Time Study Tools</span>
    </div>
    """, unsafe_allow_html=True)
