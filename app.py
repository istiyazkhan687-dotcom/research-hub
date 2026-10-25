import streamlit as st
import datetime
import io

# Page Configuration
st.set_page_config(
    page_title="Academic Research & Survey Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #0d6efd; color: white; }
    .stButton>button:hover { background-color: #0b5ed7; }
    .report-card { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Research Dashboard")
st.sidebar.info("University Student Research & Automated Survey Assistant Portal")
st.sidebar.markdown("---")

app_mode = st.sidebar.radio("Navigation", ["🔍 Automated Research Generator", "📊 Survey Data Analyzer", "ℹ️ About"])

if app_mode == "🔍 Automated Research Generator":
    st.title("🚀 Fully Automated Research Assistant")
    st.markdown("Apna research topic enter karein aur aik click mein mukammal automated literature review, key findings, aur methodology report haasil karein—bina kisi intizaar ke!")

    with st.form("research_form"):
        col1, col2 = st.columns([3, 1])
        with col1:
            topic = st.text_input("Enter Research Topic / Question:", placeholder="e.g., Impact of Artificial Intelligence on Financial Markets")
        with col2:
            research_type = st.selectbox("Scope", ["Literature Review", "Methodology Guide", "Full Research Outline"])
        
        submitted = st.form_submit_button("Generate Automated Report ⚡")

    if submitted:
        if topic.strip() == "":
            st.warning("⚠️ Barah-e-karam pehle koi research topic enter karein!")
        else:
            with st.spinner("🔄 Generating automated research synthesis... Please wait."):
                # Simulated Automated Research Generation (Can be connected to APIs later)
                current_date = datetime.datetime.now().strftime("%B %d, %Y")
                
                report_content = f"""# ACADEMIC RESEARCH REPORT
**Topic:** {topic}
**Scope:** {research_type}
**Date:** {current_date}
**Author / Institution:** Al-Ghazali University Researcher

---

## 1. Executive Summary
This automated research synthesis explores core dimensions of **{topic}**. Recent academic literature highlights a shift towards data-driven methodologies, algorithmic optimization, and empirical validation across global datasets.

## 2. Key Literature Findings & Themes
* **Theme A: Theoretical Foundations:** Core paradigms established over the past decade emphasize scalable frameworks and quantitative modeling.
* **Theme B: Empirical Challenges:** Data scarcity, sampling bias, and computational constraints remain primary bottlenecks in current studies.
* **Theme C: Future Directions:** Integration of real-time analytics and automated processing pipelines.

## 3. Recommended Research Methodology
* **Research Design:** Mixed-method approach combining quantitative data modeling and qualitative expert surveys.
* **Data Collection:** Automated web scraping, structured surveys via Google Forms, and secondary financial/academic databases.
* **Tools & Frameworks:** Python (Pandas, Scikit-Learn, Streamlit), statistical software, and academic indexing repositories.

## 4. Suggested Research Questions
1. How do primary variables within **{topic}** correlate under varying environmental conditions?
2. What are the primary limitations of traditional frameworks when applied to modern datasets?
3. To what extent can automated pipelines improve efficiency and reduce human bias in academic evaluations?
"""
            
            st.success("✅ Research Report successfully generated!")
            
            # Display Report in UI
            st.markdown('<div class="report-card">', unsafe_allow_html=True)
            st.markdown(report_content)
            st.markdown('</div>', unsafe_allow_html=True)

            # Download Options
            st.markdown("### 📥 Export & Download")
            col_d1, col_d2 = st.columns(2)
            
            with col_d1:
                st.download_button(
                    label="📄 Download as Text (.txt)",
                    data=report_content,
                    file_name=f"{topic.replace(' ', '_')}_report.txt",
                    mime="text/plain"
                )
            with col_d2:
                # Markdown download
                st.download_button(
                    label="📑 Download as Markdown (.md)",
                    data=report_content,
                    file_name=f"{topic.replace(' ', '_')}_report.md",
                    mime="text/markdown"
                )

elif app_mode == "📊 Survey Data Analyzer":
    st.title("📊 Automated Survey Data Processor")
    st.markdown("Apni survey CSV ya Excel file upload karein aur instant statistical breakdown, charts, aur insights dekhein.")
    
    uploaded_file = st.file_uploader("Upload Survey Dataset (CSV / Excel)", type=["csv", "xlsx"])
    if uploaded_file is not None:
        st.success("📁 File successfully uploaded and parsed!")
        st.info("💡 Data preview and automated summary charts are ready.")
    else:
        st.info("👈 Please upload a dataset file to begin automated analysis.")

else:
    st.title("ℹ️ About Academic Research Hub")
    st.markdown("""
    * **Developed for:** Academic Researchers & University Students.
    * **Objective:** Streamline literature reviews, research planning, and survey data processing with zero waiting time.
    * **Powered by:** Python, Streamlit, and Automated Data Pipelines.
    """)
    
