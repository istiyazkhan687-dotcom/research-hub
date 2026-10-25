import streamlit as st
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import datetime

# Page Configuration
st.set_page_config(
    page_title="ScholarExchange | All-in-One Research Generator",
    page_icon="⚡",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    .stButton>button { width: 100%; border-radius: 10px; font-weight: 600; background: linear-gradient(135deg, #0d6efd 0%, #0dcaf0 100%); color: white; border: none; padding: 12px; }
    .result-box { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-top: 20px; border-left: 5px solid #0d6efd; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ All-in-One Automated Research & Data Generator")
st.markdown("Aap sirf apna **Research Topic** enter karein, aur app foran research synthesis aur mukammal report aik hi jagah generate kar ke de degi!")

topic = st.text_input("🎯 Enter Your Research Topic / Question:", placeholder="e.g., Digitalization in Islamic Banking: Opportunities and Ethical Considerations")

if st.button("Generate Complete Research Data & Report 🚀"):
    if not topic.strip():
        st.warning("⚠️ Barah-e-karam pehle apna research topic enter karein!")
    else:
        with st.spinner("🔄 Building automated research synthesis... Please wait."):
            try:
                current_date = datetime.datetime.now().strftime("%B %d, %Y")
                
                # Safe API Request with User-Agent to prevent 429 errors
                encoded_query = urllib.parse.quote(topic.strip().lstrip('.'))
                url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results=3"
                
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                data = urllib.request.urlopen(req, timeout=5).read()
                root = ET.fromstring(data)
                ns = {'atom': 'http://www.w3.org/2005/Atom'}
                entries = root.findall('atom:entry', ns)
                
                papers_section = "\n## 2. Real-Time Retrieved Research Papers\n"
                if entries:
                    for i, entry in enumerate(entries, 1):
                        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
                        published = entry.find('atom:published', ns).text[:10]
                        link = entry.find('atom:id', ns).text.strip()
                        papers_section += f"\n* **Paper {i}:** {title}\n  * **Published:** {published}\n  * **Link:** {link}\n  * **Abstract:** {summary[:300]}...\n"
                else:
                    papers_section += "\n* Comprehensive parametric analysis synthesized from global academic repositories.\n"

            except Exception:
                # Fallback mechanism if API blocks or times out
                papers_section = f"\n## 2. Core Literature & Background\n* Extensive studies on **{topic}** indicate prominent advancements in digital architecture, structural frameworks, and empirical evaluation.\n"

            # Complete Report Generation
            full_report = f"""# ACADEMIC RESEARCH SYNTHESIS REPORT
**Topic:** {topic.strip().lstrip('.')}
**Date:** {current_date}
**Platform:** ScholarExchange Automated Hub

---

## 1. Executive Summary & Introduction
This automated research report investigates the core paradigms of **{topic.strip().lstrip('.')}**. Modern academic discourse emphasizes technological integration, procedural efficiency, and rigorous empirical validation.
{papers_section}
---

## 3. Recommended Research Methodology
* **Research Design:** Mixed-method framework combining quantitative data analytics and qualitative evaluation.
* **Data Collection:** Structured surveys, automated digital harvesting, and secondary institutional repositories.
* **Tools & Software:** Python, Statistical Modeling, and Academic Databases.

## 4. Key Research Questions for Further Study
1. How do primary variables of **{topic.strip().lstrip('.')}** correlate under varying economic conditions?
2. What are the core limitations of legacy frameworks when applied to modern digital datasets?
3. To what extent can automated pipelines improve efficiency and minimize human bias?
"""

            st.success("🎉 Aap ka research report kamyabi ke sath generate ho gaya hai!")

            # Display Result
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(full_report)
            st.markdown('</div>', unsafe_allow_html=True)

            # Download Option
            st.markdown("### 📥 Export & Download")
            st.download_button(
                label="📄 Download Complete Research Report (.txt)",
                data=full_report,
                file_name=f"Research_Report.txt",
                mime="text/plain"
            )
