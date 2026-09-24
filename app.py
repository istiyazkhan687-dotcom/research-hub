import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Academic Resource & Survey Vault",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# اسٹائلنگ
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&display=swap');
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .value-box {
        background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%);
        border: 2px solid #6366f1;
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        margin-bottom: 25px;
    }
    .lock-card {
        background-color: #1e293b;
        border: 1px dashed #64748b;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;
    }
    .unlocked-card {
        background-color: #064e3b;
        border: 2px solid #10b981;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ڈیٹا بیس
@st.cache_resource
def get_db():
    conn = sqlite3.connect("research.db", check_same_thread=False)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS auto_responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        university TEXT,
        submitted_at TEXT
    )
    """)
    conn.commit()
    return conn

conn = get_db()
cur = conn.cursor()

# ہیرو پیشکش (Incentive Offer)
st.markdown("""
<div class="value-box">
    <h1 style="color: #ffffff; margin-bottom: 10px;">🎁 ایم ایس و پی ایچ ڈی ریسرچ پیک (مفت رسائی)</h1>
    <p style="color: #cbd5e1; font-size: 1.15rem; max-width: 800px; margin: auto;">
        ہمارا مختصر 2 منٹ کا ریسرچ سروے مکمل کریں اور فوری طور پر اکیڈمک تھیسز ٹیمپلیٹس، SPSS/SmartPLS گائیڈز اور تصدیق شدہ اسکیلز تک مفت رسائی حاصل کریں۔
    </p>
</div>
""", unsafe_allow_html=True)

# اسٹیٹس چیک
if "survey_done" not in st.session_state:
    st.session_state.survey_done = False

col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.subheader("📋 مرحلہ 1: ریسرچ سروے مکمل کریں")
    st.info("سروے کو یہیں نیچے مکمل کریں یا الگ ونڈو میں کھولنے کے لیے بٹن دبائیں۔")
    
    # اپنا اصل گوگل فارم لنک یہاں لگائیں
    survey_url = "https://docs.google.com/forms/d/e/1FAIpQLSe-YOUR_FORM_ID/viewform?embedded=true"
    
    # ایمبیڈڈ گوگل فارم فریم
    st.markdown(f"""
    <iframe src="{survey_url}" width="100%" height="520" frameborder="0" marginheight="0" marginwidth="0">لوڈ ہو رہا ہے…</iframe>
    """, unsafe_allow_html=True)

with col_right:
    st.subheader("🔓 مرحلہ 2: اپنا ریسرچ مٹیریل انلاک کریں")
    
    if not st.session_state.survey_done:
        st.markdown("""
        <div class="lock-card">
            <h3 style="color: #94a3b8;">🔒 ڈاؤن لوڈز فی الحال لاک ہیں</h3>
            <p style="color: #64748b; font-size: 0.9rem;">
                فارم سبمٹ کرنے کے بعد نیچے اپنا نام درج کر کے انلاک کا بٹن دبائیں۔
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("unlock_form"):
            user_name = st.text_input("آپ کا نام")
            user_uni = st.text_input("یونیورسٹی / ادارہ")
            confirm_box = st.checkbox("میں تصدیق کرتا ہوں کہ میں نے سروے فارم مکمل کر لیا ہے")
            unlock_btn = st.form_submit_button("🚀 میٹریل انلاک کریں", type="primary")

        if unlock_btn:
            if user_name and user_uni and confirm_box:
                now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
                cur.execute("INSERT INTO auto_responses (name, university, submitted_at) VALUES (?, ?, ?)", 
                            (user_name, user_uni, now_str))
                conn.commit()
                st.session_state.survey_done = True
                st.balloons()
                st.rerun()
            else:
                st.error("براہ کرم تمام معلومات درج کریں اور تصدیق پر نشان لگائیں۔")
    else:
        st.markdown("""
        <div class="unlocked-card">
            <h3 style="color: #34d399;">🎉 تمام ریسرچ وسائل انلاک ہو گئے ہیں!</h3>
            <p style="color: #d1fae5; font-size: 0.95rem;">
                تعاون کا بہت شکریہ۔ آپ کے لیے تیار کردہ میٹریل نیچے ڈاؤن لوڈ کے لیے دستیاب ہے:
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # فوری قیمتی مواد کے ڈاؤن لوڈز
        st.success("✅ تصدیق مکمل! فائلز پر کلک کر کے ڈاؤن لوڈ کریں:")
        
        st.download_button(
            label="📥 MS/MPhil تھیسز کا معیاری فارمیٹ (MS Word Template)",
            data="Sample MS Thesis Structure with APA 7th Referencing Guidelines and Chapter Divisions",
            file_name="MS_Thesis_Standard_Template.txt",
            mime="text/plain",
            use_container_width=True
        )
        
        st.download_button(
            label="📥 SmartPLS اور SPSS ڈیٹا کلیننگ چیک لسٹ (PDF/Doc)",
            data="Normality test, Multicollinearity (VIF), Cronbach Alpha and Composite Reliability guidelines",
            file_name="Data_Screening_Guidelines.txt",
            mime="text/plain",
            use_container_width=True
        )

        st.download_button(
            label="📥 بینکنگ و مالیاتی اشاریوں کا ڈیٹا سورس شیٹ (Excel)",
            data="Financial Ratios, CAMELS framework indicators and SBP statistical handbook references",
            file_name="Financial_Analysis_Sources.txt",
            mime="text/plain",
            use_container_width=True
        )

# ایڈمن کے لیے رسپانسز ڈاؤن لوڈ کرنا
st.divider()
with st.expander("🔐 محقق کا لاگ ان (ڈاؤن لوڈ رسپانسز)"):
    cur.execute("SELECT name as 'نام', university as 'یونیورسٹی', submitted_at as 'تاریخ' FROM auto_responses")
    rows = cur.fetchall()
    if rows:
        df_log = pd.DataFrame(rows, columns=["نام", "یونیورسٹی", "تاریخ"])
        st.write(f"مجموعی تصدیق شدہ شرکاء: **{len(df_log)}**")
        st.download_button(
            label="📥 تمام رسپانسز CSV میں ڈاؤن لوڈ کریں",
            data=df_log.to_csv(index=False).encode('utf-8-sig'),
            file_name="verified_responses.csv",
            mime="text/csv"
        )
    else:
        st.caption("ابھی تک کوئی نیا اندراج نہیں ہوا۔")
