import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="ScholarExchange | Academic Research Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تیز رفتار اسٹائلنگ اور واضح ٹیکسٹ کلرز
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .hero-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%);
        padding: 30px 25px;
        border-radius: 14px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 8px;
        color: #ffffff;
    }
    .hero-subtitle {
        font-size: 1rem;
        color: #cbd5e1;
        max-width: 850px;
        line-height: 1.6;
    }

    .academic-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .card-title {
        color: #ffffff !important;
        font-size: 1.35rem;
        font-weight: 700;
        margin-top: 6px;
        margin-bottom: 6px;
    }
    .badge-field {
        background-color: #2563eb;
        color: #ffffff;
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
    }
    .badge-active {
        background-color: #10b981;
        color: #ffffff;
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .badge-closed {
        background-color: #ef4444;
        color: #ffffff;
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 0.8rem;
        font-weight: 600;
    }

    .footer {
        text-align: center;
        padding: 30px 0 15px 0;
        color: #94a3b8;
        font-size: 0.85rem;
        border-top: 1px solid #334155;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_db_connection():
    conn = sqlite3.connect("research.db", check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS surveys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        researcher_name TEXT,
        target_field TEXT,
        form_link TEXT,
        target_responses INTEGER DEFAULT 50,
        credits_offered INTEGER DEFAULT 10,
        responses_collected INTEGER DEFAULT 0,
        is_active INTEGER DEFAULT 1
    )
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS survey_responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        survey_id INTEGER,
        respondent_name TEXT,
        respondent_university TEXT,
        submitted_at TEXT
    )
    """)
    conn.execute("UPDATE surveys SET responses_collected = 0 WHERE responses_collected IS NULL;")
    conn.commit()
    return conn

conn = get_db_connection()

# ہیرو سیکشن
st.markdown("""
<div class="hero-container">
    <div class="hero-title">🎓 ScholarExchange</div>
    <div class="hero-subtitle">
        یونیورسٹی ریسرچرز، ایم ایس اور پی ایچ ڈی اسکالرز کے لیے مستند سروے شیئرنگ اور حقیقی ڈیٹا کلیکشن کا نیشنل پورٹل۔
    </div>
</div>
""", unsafe_allow_html=True)

# میٹرکس (فوری کیشڈ کیلکولیشن)
cur = conn.cursor()
cur.execute("SELECT COUNT(*), SUM(COALESCE(responses_collected, 0)), SUM(COALESCE(credits_offered, 0)) FROM surveys")
total_surveys, total_resp, total_credits = cur.fetchone()
total_surveys = total_surveys or 0
total_resp = total_resp or 0
total_credits = total_credits or 0

stat_c1, stat_c2, stat_c3, stat_c4 = st.columns(4)
stat_c1.metric("کل فعال سرویز", f"{total_surveys}")
stat_c2.metric("جمع شدہ رسپانسز", f"{total_resp}")
stat_c3.metric("مجموعی کریڈٹس پول", f"{total_credits} Pts")
stat_c4.metric("کامیابی کا تناسب", f"{(total_resp / (total_surveys * 50) * 100) if total_surveys else 100:.1f}%")

st.write("")

main_tab, publish_tab, resources_tab = st.tabs([
    "🌐 ایکسپلور سرویز (Surveys Directory)", 
    "➕ نیا سروے شائع کریں (Submit Survey)", 
    "📚 ڈیٹا سیٹس و اکیڈمک ٹولز (Resources)"
])

# ----------------- ٹیب 1: سرویز ڈائرکٹری -----------------
with main_tab:
    f1, f2 = st.columns([3, 1])
    with f1:
        search_query = st.text_input("🔍 عنوان یا محقق کے نام سے سرچ کریں...", "")
    with f2:
        field_filter = st.selectbox(
            "شعبہ منتخب کریں:", 
            ["تمام شعبہ جات", "Finance & Banking", "Economics", "Management Sciences", "Data Science & IT", "Social Sciences"]
        )

    query = "SELECT id, title, researcher_name, target_field, form_link, target_responses, credits_offered, responses_collected, is_active FROM surveys WHERE 1=1"
    params = []
    
    if search_query:
        query += " AND (title LIKE ? OR researcher_name LIKE ?)"
        params.extend([f"%{search_query}%", f"%{search_query}%"])
    if field_filter != "تمام شعبہ جات":
        query += " AND target_field = ?"
        params.append(field_filter)
        
    query += " ORDER BY is_active DESC, id DESC"
    cur.execute(query, params)
    surveys = cur.fetchall()

    if not surveys:
        st.info("اس تلاش کے مطابق فی الحال کوئی ریسرچ سروے دستیاب نہیں۔")
    else:
        for s in surveys:
            s_id, s_title, s_res, s_field, s_link, s_target, s_cred, s_collected, s_active = s
            s_collected = s_collected or 0
            s_target = s_target or 1
            s_cred = s_cred or 0
            
            with st.container():
                st.markdown(f"""
                <div class="academic-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="badge-field">{s_field}</span>
                        <span class="{'badge-active' if s_active else 'badge-closed'}">{'🟢 فعال' if s_active else '🔴 مکمل شدہ'}</span>
                    </div>
                    <div class="card-title">{s_title}</div>
                    <div style="color: #cbd5e1; font-size: 0.95rem;">
                        👤 محقق: <strong style="color: #ffffff;">{s_res}</strong> | 🪙 پیش کردہ کریڈٹس: <strong style="color: #f59e0b;">{s_cred} Points</strong>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                p_col1, p_col2 = st.columns([3, 1])
                with p_col1:
                    progress_val = min(float(s_collected) / float(s_target), 1.0)
                    st.progress(progress_val)
                    st.caption(f"ہدف پیش رفت: {s_collected} از {s_target} مستند رسپانسز مکمل")
                with p_col2:
                    st.link_button("🔗 سروے فارم پر جائیں", s_link, use_container_width=True)

                # رسپانس اندراج
                if s_active:
                    with st.expander("✍️ سروے فل کر لیا ہے؟ کریڈٹ کلیم کے لیے اپنا اندراج کریں"):
                        rc1, rc2 = st.columns(2)
                        with rc1:
                            r_name = st.text_input("آپ کا مکمل نام", key=f"name_{s_id}")
                        with rc2:
                            r_uni = st.text_input("آپ کا تعلیمی ادارہ / یونیورسٹی", key=f"uni_{s_id}")
                        
                        btn_col1, btn_col2 = st.columns([2, 1])
                        with btn_col1:
                            if st.button("تصدیقی اندراج جمع کریں", key=f"btn_{s_id}", type="primary"):
                                if r_name and r_uni:
                                    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
                                    cur.execute("INSERT INTO survey_responses (survey_id, respondent_name, respondent_university, submitted_at) VALUES (?, ?, ?, ?)",
                                                (s_id, r_name, r_uni, now_str))
                                    new_count = s_collected + 1
                                    new_active = 0 if new_count >= s_target else 1
                                    cur.execute("UPDATE surveys SET responses_collected = ?, is_active = ? WHERE id = ?", (new_count, new_active, s_id))
                                    conn.commit()
                                    st.success("آپ کا اندراج ریکارڈ ہو گیا!")
                                    st.rerun()
                                else:
                                    st.warning("براہ کرم نام اور ادارے کا نام درج کریں۔")
                        
                        # ڈیمانڈ پر CSV ایکسپورٹ (صرف کلک کرنے پر کوئری چلے گی)
                        with btn_col2:
                            cur.execute("SELECT COUNT(*) FROM survey_responses WHERE survey_id = ?", (s_id,))
                            count_r = cur.fetchone()[0]
                            if count_r > 0:
                                cur.execute("SELECT respondent_name, respondent_university, submitted_at FROM survey_responses WHERE survey_id = ?", (s_id,))
                                raw_rows = cur.fetchall()
                                df_temp = pd.DataFrame(raw_rows, columns=["اسم_محقق", "ادارہ_یونیورسٹی", "وقت_اندراج"])
                                st.download_button(
                                    label="📥 ڈاؤن لوڈ CSV",
                                    data=df_temp.to_csv(index=False).encode('utf-8-sig'),
                                    file_name=f"survey_{s_id}_data.csv",
                                    mime="text/csv",
                                    key=f"dl_{s_id}"
                                )
                st.write("")

# ----------------- ٹیب 2: نیا سروے شائع کریں -----------------
with publish_tab:
    st.subheader("اپنا ریسرچ سروے پورٹل پر درج کروائیں")
    with st.form("new_survey_web_form", clear_on_submit=True):
        f_title = st.text_input("مقالے / ریسرچ کا مکمل عنوان (Title)")
        f_name = st.text_input("پرنسپل انویسٹی گیٹر / محقق کا نام")
        f_field = st.selectbox(
            "تحقیقی فیلڈ", 
            ["Finance & Banking", "Economics", "Management Sciences", "Data Science & IT", "Social Sciences"]
        )
        f_url = st.text_input("گوگل فارم کا لنک (URL)")
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            f_target = st.number_input("مطلوبہ سیمپل سائز", min_value=10, max_value=2000, value=50, step=5)
        with col_t2:
            f_credits = st.number_input("پیش کردہ کریڈٹس", min_value=5, max_value=100, value=15, step=5)
            
        submit_btn = st.form_submit_button("🚀 سروے شائع کریں", type="primary")

    if submit_btn:
        if f_title and f_name and f_url:
            cur.execute("""
                INSERT INTO surveys (title, researcher_name, target_field, form_link, target_responses, credits_offered, responses_collected, is_active)
                VALUES (?, ?, ?, ?, ?, ?, 0, 1)
            """, (f_title, f_name, f_field, f_url, f_target, f_credits))
            conn.commit()
            st.success("سروے شائع ہو گیا!")
            st.rerun()
        else:
            st.error("تمام ضروری معلومات فراہم کریں۔")

# ----------------- ٹیب 3: اکیڈمک وسائل -----------------
with resources_tab:
    st.subheader("تحقیقی ٹولز اور معاون ریفرنسز")
    st.markdown("""
    * **State Bank of Pakistan (SBP) Data Portal:** ملکی میکرو اور مائیکرو اکنامک اشاریے
    * **Likert Scale Reliability Guidelines:** کرونبیک الفا اور اسکیل تصدیق
    * **SPSS & SmartPLS Clean Templates:** پرائمری ڈیٹا کے لیے تجزیاتی ٹیمپلیٹس
    """)

# فوٹر
st.markdown("""
<div class="footer">
    ScholarExchange &copy; 2026 | Academic Research & Survey Portal
</div>
""", unsafe_allow_html=True)
