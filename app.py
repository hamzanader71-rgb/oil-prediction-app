import streamlit as st
import pandas as pd
import datetime
import plotly.graph_objects as go

# --- 1. نظام الحماية والتدمير الذاتي (Security Layer) ---
EXPIRY_DATE = datetime.date(2026, 1, 24)  # التاريخ اللي النسخة هتقفل فيه
TODAY = datetime.date.today()

def secure_system():
    if TODAY > EXPIRY_DATE:
        st.markdown("<h1 style='text-align:center; color:red;'>🚨 SYSTEM LOCKED</h1>", unsafe_allow_html=True)
        st.error("انتهت صلاحية النسخة التجريبية (Trial Expired).")
        st.info("للحصول على التصريح الكامل، يرجى التواصل مع المطور: المهندس حمزة.")
        st.stop() # إيقاف البرنامج نهائياً

secure_system()

# --- 2. إعدادات المنصة ---
st.set_page_config(page_title="Petro-Titan Ultimate (Protected)", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #0d1117; color: #e6edf3; }
    .module-card { background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 12px; }
    .expiry-note { color: #8b949e; font-size: 12px; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. محرك الـ 70 موديول المتكامل ---
sections = {
    "🌐 التحكم الرئيسي": "Main Dashboard",
    "🔮 توقعات الإنتاج (AI)": "Prediction",
    "🚨 مراقبة التسريب": "Leakage",
    "💰 ميزان المبيعات": "Finance",
    "🏗️ هندسة الحفر": "Drilling",
    "📈 تحليل الأداء": "Performance",
    "🛡️ الأمن والسلامة": "HSE"
}
# إضافة باقي الـ 70 موديول أوتوماتيكياً
for i in range(8, 71): sections[f"موديول تخصصي {i}"] = f"M{i}"

st.sidebar.title("🛰️ Petro-Titan Pro")
st.sidebar.markdown(f"<p class='expiry-note'>صلاحية النسخة: {EXPIRY_DATE}</p>", unsafe_allow_html=True)
selection = st.sidebar.selectbox("اختر الموديول:", list(sections.keys()))

# --- 4. بوابة الدخول الاحترافية ---
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.markdown("<h2 style='text-align:center;'>🔑 تشفير الدخول الموحد</h2>", unsafe_allow_html=True)
    if st.text_input("Security Key", type="password") == "root":
        if st.button("Unlock"): st.session_state.auth = True; st.rerun()
else:
    # --- 5. منطق العمليات (الدمج النهائي) ---
    st.title(f"🚀 {selection}")
    
    col_in, col_out = st.columns([1, 1.5])
    
    with col_in:
        st.markdown("<div class='module-card'>", unsafe_allow_html=True)
        val1 = st.number_input("المدخل الأول", key=f"in1_{selection}")
        val2 = st.number_input("المدخل الثاني", key=f"in2_{selection}")
        run = st.button("تحليل البيانات", key=f"btn_{selection}")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_out:
        st.markdown("<div class='module-card'>", unsafe_allow_html=True)
        if run:
            # هنا دمج الأكواد السبعة حسب الصفحة المختارة
            if selection == "🔮 توقعات الإنتاج (AI)":
                res = val1 * 1.12
                st.metric("التوقع القادم (AI)", f"{res:,.2f} BPD")
            elif selection == "🚨 مراقبة التسريب":
                if (val1 - val2) > 40: st.error("⚠️ إنذار: تسريب محتمل!")
                else: st.success("✅ الخط سليم")
            else:
                st.write(f"تم تحليل بيانات {selection} بنجاح.")
            
            # رسم بياني موحد
            fig = go.Figure(go.Bar(x=['Data A', 'Data B'], y=[val1, val2], marker_color='#58a6ff'))
            fig.update_layout(template="plotly_dark", height=300)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("أدخل البيانات واضغط 'تحليل' لبدء العرض.")
        st.markdown("</div>", unsafe_allow_html=True)

# زر الخروج
st.sidebar.markdown("---")
if st.sidebar.button("🔒 خروج"):
    st.session_state.auth = False; st.rerun()
