import streamlit as st
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

# Page Configuration
st.set_page_config(
    page_title="ScholarExchange | Real-Time Research Finder",
    page_icon="📚",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    .stButton>button { width: 100%; border-radius: 10px; font-weight: 600; background: linear-gradient(135deg, #0d6efd 0%, #0dcaf0 100%); color: white; border: none; padding: 10px; }
    .paper-card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 15px; border-left: 4px solid #0d6efd; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Real-Time Academic Research & Paper Finder")
st.markdown("Apna research topic enter karein, aur app foran internet se **asli research papers aur live data** fetch kar ke laye gi!")

topic = st.text_input("🎯 Enter Research Topic / Keyword:", placeholder="e.g., Artificial Intelligence in Banking, Machine Learning, Quantum Computing")

if st.button("Search Real Papers 🔍"):
    if not topic.strip():
        st.warning("⚠️ Barah-e-karam pehle koi topic enter karein!")
    else:
        with st.spinner("🔄 Fetching real-time research papers from global academic databases..."):
            try:
                # arXiv API Query for real papers
                encoded_query = urllib.parse.quote(topic)
                url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results=5"
                
                data = urllib.request.urlopen(url).read()
                root = ET.fromstring(data)
                
                ns = {'atom': 'http://www.w3.org/2005/Atom'}
                entries = root.findall('atom:entry', ns)
                
                if not entries:
                    st.info("Is topic ke mutabiq koi papers nahi mile. Koshish karein ke koi aur keyword ya English mein topic likhein.")
                else:
                    st.success(f"✅ Mukammal taur par {len(entries)} asli research papers mil gaye hain!")
                    
                    papers_text = f"# Real Research Papers for: {topic}\n\n"
                    
                    for i, entry in enumerate(entries, 1):
                        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
                        published = entry.find('atom:published', ns).text[:10]
                        link = entry.find('atom:id', ns).text.strip()
                        
                        papers_text += f"### {i}. {title}\n* **Published Date:** {published}\n* **Link:** {link}\n* **Abstract:** {summary}\n\n---\n"
                        
                        # Display card in UI
                        st.markdown(f"""
                            <div class="paper-card">
                                <h4>{i}. {title}</h4>
                                <p><b>Published:</b> {published} | <a href="{link}" target="_blank" style="color: #0d6efd; font-weight: bold;">View Original Paper Link 🔗</a></p>
                                <p><b>Abstract:</b> {summary[:350]}...</p>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    # Download Option
                    st.markdown("### 📥 Export Options")
                    st.download_button(
                        label="📄 Download Papers Summary (.txt)",
                        data=papers_text,
                        file_name=f"{topic.replace(' ', '_')}_real_papers.txt",
                        mime="text/plain"
                    )
            except Exception as e:
                st.error(f"Data fetch karne mein masla aya hai: {e}")
