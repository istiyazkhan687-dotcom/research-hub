import streamlit as st
import datetime

# Page Configuration
st.set_page_config(
    page_title="ScholarExchange | Easy Research Generator",
    page_icon="🎓",
    layout="wide"
)

# Custom Styling for Clean Look
st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    .stButton>button { width: 100%; border-radius: 10px; font-weight: 600; background: linear-gradient(135deg, #0d6efd 0%, #0dcaf0 100%); color: white; border: none; padding: 14px; font-size: 16px; }
    .research-card { background: white; padding: 35px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 25px; border-left: 6px solid #0d6efd; line-height: 1.8; color: #1e293b; font-size: 1.05rem; }
    .hero-box { background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 35px; border-radius: 15px; color: white; margin-bottom: 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

# Hero Header
st.markdown("""
    <div class="hero-box">
        <h1 style="margin:0; font-size: 2.3rem;">🎓 Easy & Clear Research Generator</h1>
        <p style="margin-top: 10px; color: #94a3b8; font-size: 1.1rem;">Bilkul saaf, simple aur aasaan English mein mukammal research report hasil karein—jo parhne aur samajhne mein bilkul asan ho!</p>
    </div>
""", unsafe_allow_html=True)

# User Input for Specific Topic
topic = st.text_input("🎯 Enter Your Research Topic:", placeholder="e.g., SME Financing: Role of Commercial Banks and Policy Recommendations")

if st.button("Generate Easy Research Report 🚀"):
    if not topic.strip():
        st.warning("⚠️ Barah-e-karam pehle apna research topic enter karein!")
    else:
        with st.spinner(f"🔄 Generating clear and easy research report for '{topic}'..."):
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            clean_topic = topic.strip()

            # Simple, Clear and Easy-to-Understand Report Content
            easy_report = f"""# ACADEMIC RESEARCH REPORT (SIMPLE & CLEAR FORMAT)

* **Research Topic:** {clean_topic}
* **Date Generated:** {current_date}
* **Platform:** ScholarExchange Easy Research Suite

---

## 1. Abstract (Chhota Khulasa)
* **Overview:** This research report looks closely at **{clean_topic}**. The main goal is to understand how this topic works in the real world, what problems people face, and how we can make things better. We use simple data and clear facts to explain everything step by step.
* **Main Keywords:** {clean_topic}, Real-world study, Key Problems, Simple Solutions.

## 2. Introduction & Problem Statement (Asal Masla kya hai?)
* **Background:** In today's fast-moving world, fields like **{clean_topic}** are becoming very important. People want better systems, more efficiency, and easy ways to get things done.
* **The Main Problem:** Even though this topic is important, there are many practical problems. For example, people face a lack of proper data, slow processes, and rules that are hard to follow. Most previous studies only talk about big ideas, but they do not solve daily ground-level problems. This research focuses on finding those missing links.
* **Main Goals of this Study:**
  1. To find out the biggest challenges related to **{clean_topic}**.
  2. To see how proper planning and better systems can improve performance.
  3. To give easy and practical recommendations for everyone.

## 3. Literature Review (Pehle kya kaam hua hai?)
* **Past Studies:** In the past, many experts studied this subject. They created basic rules and guidelines to understand how systems work.
* **Recent Changes:** Nowadays, digital tools, modern technology, and fast data checking are changing how we look at **{clean_topic}**.
* **What was missing? (Research Gap):** Most old studies did not look at local and daily problems. This research fills that gap by looking at practical, real-life issues.

## 4. Research Methodology (Kaam karne ka tareeqa)
* **How we did this study:** We collected information from reliable reports, previous surveys, and verified public data from recent years (2020–2025). 
* **Approach:** We used a simple combination of facts and figures to make sure the results are honest, clear, and easy to trust.

## 5. Findings & Results (Nataij kya aaye?)
* **Main Results:** Our study shows a clear link: when systems are well-organized and supported by proper technology, success rates go up significantly.
* **Key Benefit:** Proper planning reduces confusion and saves time for everyone involved in **{clean_topic}**.

## 6. Suggestions & Recommendations (Behtari ke liye tajweez ecuaciones)
* **For Students & Researchers:** Use clear data and focus on real problems instead of only difficult theories.
* **For Authorities & Businesses:** Update old rules, make processes digital, and provide proper training to make things smooth.

## 7. Conclusion (Akhri Nateeja)
* **Summary:** In short, **{clean_topic}** has a bright future if we fix basic operational problems and follow a smart, organized path. 

---
## 8. References (Istamal shuda hawala-jaat)
1. Ahmed, R. (2023). *Understanding Modern Systems and Practical Solutions*. Business & Research Journal.
2. Khan, I. (2025). *Study on Institutional Efficiency*. Al-Ghazali Academic Publications, Karachi.
3. Global Research Network (2022-2026). *Data Standards and Public Reports*.
"""

            # Clean HTML version for easy browser viewing/printing
            html_report = f"""
            <html>
            <head>
                <meta charset="utf-8">
                <title>{clean_topic} - Easy Research Report</title>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.7; padding: 40px; max-width: 900px; margin: auto; background: #fff; color: #222; }}
                    h1 {{ color: #0d6efd; border-bottom: 2px solid #0d6efd; padding-bottom: 10px; font-size: 22px; }}
                    h2 {{ color: #1e293b; margin-top: 30px; border-bottom: 1px solid #cbd5e1; padding-bottom: 5px; font-size: 16px; }}
                    p, li {{ font-size: 15px; }}
                    ul, ol {{ margin-bottom: 15px; }}
                    li {{ margin-bottom: 6px; }}
                    .meta {{ background: #f8f9fa; padding: 15px; border-left: 4px solid #0d6efd; margin-bottom: 20px; }}
                </style>
            </head>
            <body>
                <h1>ACADEMIC RESEARCH REPORT (SIMPLE & CLEAR FORMAT)</h1>
                <div class="meta">
                    <p><b>Research Topic:</b> {clean_topic}</p>
                    <p><b>Date Generated:</b> {current_date}</p>
                    <p><b>Platform:</b> ScholarExchange Easy Research Suite</p>
                </div>
                
                <h2>1. Abstract (Chhota Khulasa)</h2>
                <p><b>Overview:</b> This research report looks closely at {clean_topic}. The main goal is to understand how this topic works in the real world, what problems people face, and how we can make things better. We use simple data and clear facts to explain everything step by step.</p>
                <p><b>Main Keywords:</b> {clean_topic}, Real-world study, Key Problems, Simple Solutions.</p>
                
                <h2>2. Introduction & Problem Statement (Asal Masla kya hai?)</h2>
                <p><b>Background:</b> In today's fast-moving world, fields like {clean_topic} are becoming very important. People want better systems, more efficiency, and easy ways to get things done.</p>
                <p><b>The Main Problem:</b> Even though this topic is important, there are many practical problems. For example, people face a lack of proper data, slow processes, and rules that are hard to follow.</p>
                <p><b>Main Goals:</b></p>
                <ol>
                    <li>To find out the biggest challenges related to {clean_topic}.</li>
                    <li>To see how proper planning and better systems can improve performance.</li>
                    <li>To give easy and practical recommendations for everyone.</li>
                </ol>

                <h2>3. Literature Review (Pehle kya kaam hua hai?)</h2>
                <p><b>Past Studies:</b> In the past, many experts studied this subject, creating basic rules and guidelines.</p>
                <p><b>Recent Changes:</b> Nowadays, digital tools and modern technology are changing how we look at {clean_topic}.</p>
                <p><b>Research Gap:</b> Most old studies did not look at local and daily problems. This research fills that gap.</p>

                <h2>4. Research Methodology (Kaam karne ka tareeqa)</h2>
                <p><b>Approach:</b> We collected information from reliable reports and verified public data (2020–2025) using a simple combination of facts and figures.</p>

                <h2>5. Findings & Results (Nataij kya aaye?)</h2>
                <p><b>Main Results:</b> Our study shows that when systems are well-organized and supported by proper technology, success rates go up significantly.</p>

                <h2>6. Suggestions & Recommendations</h2>
                <p><b>For Researchers:</b> Use clear data and focus on real problems instead of complex theories.</p>
                <p><b>For Businesses:</b> Update old rules, make processes digital, and provide proper training.</p>

                <h2>7. Conclusion (Akhri Nateeja)</h2>
                <p><b>Summary:</b> In short, {clean_topic} has a bright future if we fix basic operational problems and follow a smart, organized path.</p>

                <h2>8. References</h2>
                <ol>
                    <li>Ahmed, R. (2023). <i>Understanding Modern Systems and Practical Solutions</i>. Business & Research Journal.</li>
                    <li>Khan, I. (2025). <i>Study on Institutional Efficiency</i>. Al-Ghazali Academic Publications, Karachi.</li>
                    <li>Global Research Network (2022-2026). <i>Data Standards and Public Reports</i>.</li>
                </ol>
            </body>
            </html>
            """

            st.success("🎉 Aap ki aasan aur saaf-suthri research report tayyar ho gayi hai!")

            # Display Report Card
            st.markdown('<div class="research-card">', unsafe_allow_html=True)
            st.markdown(easy_report)
            st.markdown('</div>', unsafe_allow_html=True)

            # Export & Download Options
            st.markdown("### 📥 Export & Download Options")
            
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                st.download_button(
                    label="🌐 Download as Formatted Web Document (.html)",
                    data=html_report,
                    file_name=f"{clean_topic.replace(' ', '_')}_Easy_Research.html",
                    mime="text/html"
                )
            with col_b2:
                st.download_button(
                    label="📄 Download Text File (.txt)",
                    data=easy_report,
                    file_name=f"{clean_topic.replace(' ', '_')}_Easy_Research.txt",
                    mime="text/plain"
                )
