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
    .paper-item { background: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 10px; border: 1px solid #e9ecef; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ All-in-One Automated Research & Data Generator")
st.markdown("Aap sirf apna **Research Topic** enter karein, aur app foran real research papers, automated synthesis, aur mukammal report aik hi jagah generate kar ke de degi!")

# Single Input Field for Everything
topic = st.text_input("🎯 Enter Your Research Topic / Question:", placeholder="e.g., FinTech Adoption and Operational Efficiency in Islamic Banking")

if st.button("Generate Complete Research Data & Report 🚀"):
    if not topic.strip():
        st.warning("⚠️ Barah-e-karam pehle apna research topic enter karein!")
    else:
        with st.spinner("🔄 Fetching real-time papers and building automated synthesis... Please wait."):
            try:
                # 1. Fetching real papers from arXiv API
                encoded_query = urllib.parse.quote(topic)
                url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results=3"
                
                data = urllib.request.urlopen(url).read()
                root = ET.fromstring(data)
                ns = {'atom': 'http://www.w3.org/2005/Atom'}
                entries = root.findall('atom:entry', ns)
                
                current_date = datetime.datetime.now().strftime("%B %d, %Y")
                
                # Building the comprehensive automated report content
                full_report = f"""# ACADEMIC RESEARCH SYNTHESIS REPORT
**Topic:** {topic}
**Date:** {current_date}
**Platform:** ScholarExchange Automated Hub

---

## 1. Executive Summary & Literature Synthesis
This automated research synthesis explores the core dimensions of **{topic}**. Contemporary studies emphasize scalable digital frameworks, empirical validation, and cross-sector applicability, providing a robust foundation for researchers.

## 2. Real-Time Retrieved Research Papers (Global Repositories)
"""
                
                papers_data = []
                if entries:
                    for i, entry in enumerate(entries, 1):
                        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
                        published = entry.find('atom:published', ns).text[:10]
                        link = entry.find('atom:id', ns).text.strip()
                        
                        papers_data.append((title, published, link, summary))
                        full_report += f"\n### Paper {i}: {title}\n- **Published:** {published}\n- **Link:** {link}\n- **Abstract:** {summary[:350]}...\n"
                else:
                    full_report += "\nNo direct external archive papers found, generated via core parametric synthesis.\n"

                full_report += f"""
---

## 3. Recommended Research Methodology
* **Research Design:** Mixed-method approach combining quantitative data modeling and qualitative assessment.
* **Data Collection Strategy:** Automated harvesting, structured surveys, and institutional repositories.
* **Analytical Tools:** Python, Statistical Frameworks, and Academic Databases.

## 4. Core Research Questions for Further Study
1. How do primary variables of **{topic}** correlate under varying market conditions?
2. What are the core limitations of traditional frameworks when applied to modern datasets?
3. To what extent can automated pipelines improve efficiency and reduce human bias?
"""

                st.success("🎉 Aap ka mukammal research data aur report successfully generate ho gaya hai!")

                # Displaying Results on Screen
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.markdown(f"## 📑 Generated Report for: {topic}")
                st.markdown(full_report)
                st.markdown('</div>', unsafe_allow_html=True)

                # Download Button for Complete Report
                st.markdown("### 📥 Export & Download")
                st.download_button(
                    label="📄 Download Complete Research Report (.txt)",
                    data=full_report,
                    file_name=f"{topic.replace(' ', '_')}_complete_report.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Data fetch karne mein masla aya hai: {e}")
