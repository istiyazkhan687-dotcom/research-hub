import streamlit as st
import datetime

# Page Configuration
st.set_page_config(
    page_title="ScholarExchange | Ultimate Research Assistant",
    page_icon="🎓",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    .stButton>button { width: 100%; border-radius: 10px; font-weight: 600; background: linear-gradient(135deg, #0d6efd 0%, #0dcaf0 100%); color: white; border: none; padding: 12px; }
    .card { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; border-left: 5px solid #0d6efd; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation for Research Hurdles
st.sidebar.markdown("### 🎓 Research Assistance Hub")
st.sidebar.markdown("Apni research ke kisi bhi marhalay (stage) ke liye yahan se module select karein:")

nav = st.sidebar.radio("Navigation", [
    "🚀 1. All-in-One Complete Report", 
    "🎯 2. Topic & Problem Statement", 
    "📚 3. Literature Review & Gap", 
    "🧪 4. Methodology & Framework", 
    "📊 5. Research Questions & Analysis"
])

current_date = datetime.datetime.now().strftime("%B %d, %Y")

if nav == "🚀 1. All-in-One Complete Report":
    st.title("⚡ All-in-One Automated Research Generator")
    st.markdown("Aap apna research topic likhein, aur app mukammal research report (Executive Summary, Literature, Methodology, aur Questions ke sath) foran taiyar kar ke de degi!")

    topic = st.text_input("🎯 Enter Research Topic / Question:", placeholder="e.g., FinTech Adoption and Profitability in Islamic Banking")

    if st.button("Generate Complete Research Report 🚀"):
        if not topic.strip():
            st.warning("⚠️ Barah-e-karam pehle apna topic enter karein!")
        else:
            with st.spinner("🔄 Building comprehensive research synthesis..."):
                report = f"""# ACADEMIC RESEARCH REPORT
**Topic:** {topic}
**Date:** {current_date}
**Platform:** ScholarExchange Research Assistant

---

## 1. Executive Summary & Problem Statement
This research investigates **{topic}**. Modern academic discourse highlights significant gaps in empirical validation, operational efficiency, and regulatory compliance, establishing a pressing need for structured investigation.

## 2. Literature Review & Key Themes
* **Theoretical Framework:** Foundational studies emphasize structural evolution, technological integration, and risk-management paradigms.
* **Identified Research Gap:** While prior literature explores macro-level trends, micro-level empirical analysis remains limited, which this study intends to address.

## 3. Recommended Research Methodology
* **Research Design:** Mixed-method approach combining quantitative econometric/statistical modeling with qualitative expert insights.
* **Data Collection:** Secondary financial databases, structured surveys, and institutional reports.
* **Tools:** Python (Pandas, Statsmodels), SPSS, or specialized financial software.

## 4. Key Research Questions
1. To what extent do primary variables within **{topic}** impact overall institutional performance?
2. What are the primary regulatory and operational bottlenecks in current frameworks?
3. How can digital transformation optimize efficiency and decision-making processes?
"""
                st.success("🎉 Aap ki research report kamyabi ke sath generate ho gayi hai!")
                
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown(report)
                st.markdown('</div>', unsafe_allow_html=True)

                st.download_button(
                    label="📄 Download Complete Report (.txt)",
                    data=report,
                    file_name=f"{topic.replace(' ', '_')}_report.txt",
                    mime="text/plain"
                )

elif nav == "🎯 2. Topic & Problem Statement":
    st.title("🎯 Topic Selection & Problem Statement Builder")
    st.markdown("Agar aap ko naya topic select karne ya problem statement likhne mein madad chahiye, toh yahan details enter karein:")

    field = st.selectbox("Aap ki Field / Subject:", ["Islamic Banking & Finance", "Conventional Finance & Economics", "Computer Science & AI", "Education & Social Sciences", "Other"])
    keyword = st.text_input("Aap ka pasandeeda keyword ya area:", placeholder="e.g., Digital Banking, Sukuk, Risk Management")

    if st.button("Suggest Research Topics & Problem Statement 💡"):
        if not keyword.strip():
            st.warning("⚠️ Barah-e-karam koi keyword enter karein!")
        else:
            st.success("✅ Aap ki field ke mutabiq tajweez kardah topics aur problem statement:")
            
            suggestions = f"""### 📌 Suggested Research Titles in {field}
1. **An Empirical Analysis of {keyword}: Challenges and Prospects**
2. **The Impact of {keyword} on Operational Efficiency and Growth (2020-2025)**
3. **Evaluating the Framework of {keyword}: A Comparative Case Study**

### 📝 Sample Problem Statement
"Despite the rapid evolution of modern financial and technological sectors, the practical integration of **{keyword}** faces severe empirical bottlenecks, data constraints, and regulatory hurdles. Existing literature lacks a comprehensive evaluation of how these factors influence long-term efficiency, creating a critical research gap that this study aims to resolve."
"""
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(suggestions)
            st.markdown('</div>', unsafe_allow_html=True)

elif nav == "📚 3. Literature Review & Gap":
    st.title("📚 Literature Review & Research Gap Assistant")
    st.markdown("Apne topic ki literature review likhne aur 'Research Gap' nikalne mein madad lein.")

    lit_topic = st.text_input("Enter Topic for Literature Analysis:")
    if st.button("Generate Literature Synthesis 📑"):
        if lit_topic:
            lit_content = f"""### 📖 Structured Literature Synthesis for: {lit_topic}
* **Historical Context & Evolution:** Early studies established foundational models focusing on structural compliance and theoretical definitions.
* **Modern Shift:** Recent literature (2022-2026) highlights algorithmic optimization, digital transformation, and quantitative econometric validation.
* **🔍 Identified Research Gap:** Most prior studies overlook regional market dynamics and post-implementation constraints. Your research will bridge this gap by introducing empirical panel data analysis.
"""
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(lit_content)
            st.markdown('</div>', unsafe_allow_html=True)

elif nav == "🧪 4. Methodology & Framework":
    st.title("🧪 Research Methodology & Framework Guide")
    st.markdown("Apni research ke liye behtareen tareeqa-e-kaar (Methodology) muntakhib karein.")

    method_type = st.selectbox("Research Type:", ["Quantitative (Numerical / Financial Data)", "Qualitative (Interviews / Thematic Analysis)", "Mixed Methods"])
    
    if st.button("Generate Methodology Blueprint 📐"):
        blueprint = f"""### 📐 Recommended Methodology Blueprint ({method_type})
* **Research Design:** Explanatory and empirical framework suited for testing primary hypotheses.
* **Data Sources:** Primary surveys or secondary panel data from recognized institutional repositories.
* **Analytical Techniques:** Statistical testing, regression models, or thematic coding to ensure academic rigor and validity.
"""
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(blueprint)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.title("📊 Research Questions & Data Analysis Guide")
    st.markdown("Apni research ke liye core questions aur data analysis structure tayyar karein.")
    
    q_topic = st.text_input("Research Area / Variables:")
    if st.button("Generate Research Questions ❓"):
        q_content = f"""### ❓ Core Research Questions & Hypotheses
1. **RQ1:** What is the direct relationship between primary variables in **{q_topic}**?
2. **RQ2:** How do external regulatory factors moderate this relationship?
3. **Hypothesis ($H_1$):** There is a statistically significant positive impact of technological integration on operational efficiency.
"""
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(q_content)
        st.markdown('</div>', unsafe_allow_html=True)
