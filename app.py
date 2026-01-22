import streamlit as st
import pandas as pd
import datetime
import plotly.graph_objects as go

# --- 1. نظام الحماية المزدوج والتدمير الذاتي ---
EXPIRY_DATE = datetime.date(2026, 1, 24)
TODAY = datetime.date.today()

# كلمات السر (غيرهم براحتك)
GUEST_PWD = "123"      # باسورد العميل (بيفتح 7 صفحات بس)
ADMIN_PWD = "root"     # باسورد الأدمن (بيفتح الـ 70 صفحة كاملين)

def secure_system():
    if TODAY > EXPIRY_DATE:
        st.markdown("<h1 style='text-align:center; color:red;'>🚨 SYSTEM LOCKED</h1>", unsafe_allow_html=True)
        st.error("انتهت صلاحية النسخة التجريبية. يرجى التواصل مع المهندس حمزة.")
        st.stop()

secure_system()

# --- 2. إعدادات المنصة ---
st.set_page_config(page_title="Petro-Titan Dual Lock", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #0d1117; color: #e6edf3; }
    .module-card { background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 12px; }
    .admin-badge { background: #238636; color: white; padding: 2px 8px; border-radius: 10px; font-size: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. إدارة الجلسة والدخول ---
if 'auth_level' not in st.session_state: st.session_state.auth_level = None

if not st.session_state.auth_level:
    st.markdown("<h2 style='text-align:center;'>🔑 بوابة الوصول الآمن</h2>", unsafe_allow_html=True)
    user_input = st.text_input("ادخل كود الوصول", type="password")
    if st.button("Unlock System"):
        if user_input == ADMIN_PWD:
            st.session_state.auth_level = "ADMIN"
            st.rerun()
        elif user_input == GUEST_PWD:
            st.session_state.auth_level = "GUEST"
            st.rerun()
        else:
            st.error("الكود غير صحيح!")
else:
    # --- 4. محرك الـ 70 موديول بنظام الحجب الذكي ---
    main_7_modules = [
        "🌐 التحكم الرئيسي", "🔮 توقعات الإنتاج (AI)", "🚨 مراقبة التسريب", 
        "💰 ميزان المبيعات", "🏗️ هندسة الحفر", "📈 تحليل الأداء", "🛡️ الأمن والسلامة"
    ]
    
    hidden_modules = [f"موديول تخصصي {i}" for i in range(8, 71)]
    
    # القائمة تظهر حسب مستوى الدخول
    if st.session_state.auth_level == "ADMIN":
        full_list = main_7_modules + hidden_modules
        st.sidebar.markdown("<span class='admin-badge'>ADMIN ACCESS</span>", unsafe_allow_html=True)
    else:
        full_list = main_7_modules + ["🔓 فك حجب باقي الموديولات"]
    
    selection = st.sidebar.selectbox("اختر الموديول:", full_list)

    # --- 5. منطق فك الحجب من الداخل ---
    if selection == "🔓 فك حجب باقي الموديولات":
        st.subheader("هذه الموديولات محجوبة في النسخة التجريبية")
        unlock_key = st.text_input("ادخل باسورد الأدمن لفك الحجب", type="password")
        if st.button("فك الحجب الآن"):
            if unlock_key == ADMIN_PWD:
                st.session_state.auth_level = "ADMIN"
                st.success("تم فك الحجب عن الـ 70 موديول!")
                st.rerun()
            else:
                st.error("باسورد الأدمن غلط!")
    else:
        # --- 6. تشغيل الموديولات المتاحة ---
        st.title(f"🚀 {selection}")
        
        col_in, col_out = st.columns([1, 1.5])
        with col_in:
            st.markdown("<div class='module-card'>", unsafe_allow_html=True)
            v1 = st.number_input("المدخل الأول", key=f"in1_{selection}")
            v2 = st.number_input("المدخل الثاني", key=f"in2_{selection}")
            run = st.button("بدء التحليل", key=f"btn_{selection}")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_out:
            st.markdown("<div class='module-card'>", unsafe_allow_html=True)
            if run:
                if selection == "🔮 توقعات الإنتاج (AI)":
                    st.metric("التوقع", f"{v1 * 1.12:,.2f} BPD")
                # ... باقي الأكواد السبعة هنا ...
                st.success("تمت المعالجة بنجاح.")
                fig = go.Figure(go.Scatter(y=[v1, v2, v1*1.5], mode='lines+markers', line=dict(color='#58a6ff')))
                st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

# زر الخروج
st.sidebar.markdown("---")
if st.sidebar.button("🔒 خروج"):
    st.session_state.auth_level = None; st.rerun()
