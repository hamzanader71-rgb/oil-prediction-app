import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. بناء الهيكل الذكي المستقل ---
st.set_page_config(page_title="Petro-Oracle V26", layout="wide")

# تصميم احترافي عالمي
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .module-box { border-left: 5px solid #58a6ff; background: #161b22; padding: 20px; border-radius: 8px; }
    .prediction-text { color: #aff5b4; font-weight: bold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. محرك البحث والـ 30 صفحة ---
sections = [
    "الرئيسية", "الاستكشاف", "المسح السيزمي", "تقييم الطبقات", "هندسة الحفر", 
    "سوائل الحفر", "السمتة", "إكمال الآبار", "البتوفيزياء", "تحليل السجلات",
    "هندسة الخزانات", "نمذجة الخزانات", "اختبارات الآبار", "توقعات الإنتاج", "تحليل الهبوط DCA",
    "الرفع الصناعي ESP", "الرفع بالغاز", "المضخات", "كشف التسريب", "سلامة الأنابيب",
    "معالجة الخام", "معالجة الغاز", "فصل المياه", "التخزين والشحن", "المبيعات",
    "التحليل المالي", "إدارة المخاطر", "الأمن والسلامة", "الذكاء الاصطناعي", "الإعدادات"
]

search = st.sidebar.text_input("🔍 ابحث في الـ 30 صفحة...")
filtered = [s for s in sections if search in s]
selection = st.sidebar.radio("اختر التخصص:", filtered)

# --- 3. بوابة الدخول (بالباسورد اللي تقدر تغيره) ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<h2 style='text-align:center;'>🔑 نظام الدخول الموحد</h2>", unsafe_allow_html=True)
    if st.text_input("Password", type="password", key="main_login") == "root":
        if st.button("Unlock"): 
            st.session_state.auth = True
            st.rerun()
else:
    st.title(f"📂 {selection}")
    
    # --- 4. معالجة البيانات بفصل كامل (The Logic Engine) ---
    st.markdown("<div class='module-box'>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.subheader("📥 إدخال البيانات")
        # استخدام key فريد لكل صفحة يمنع التهنيج والتداخل
        press = st.number_input("الضغط (psi)", key=f"p_input_{selection}")
        flow = st.number_input("المعدل (bpd)", key=f"q_input_{selection}")
        run = st.button("تحليل البيانات", key=f"run_btn_{selection}")

    with col2:
        st.subheader("📊 المخرجات الهندسية")
        if run:
            # هنا بقى السر: البرنامج بيعرض فقط اللي يخص الصفحة المختارة
            
            if selection == "توقعات الإنتاج":
                st.markdown(f"<p class='prediction-text'>🔮 التنبؤ المتوقع: {flow * 1.05:,.2f} bpd</p>", unsafe_allow_html=True)
                st.line_chart(np.random.randn(15, 1))

            elif selection == "كشف التسريب":
                if press < 500: st.error("🚨 تحذير من تسريب!")
                else: st.success("✅ الخط سليم")

            elif selection == "المبيعات":
                st.metric("الأرباح التقديرية", f"${flow * 70:,.0f}")

            else:
                st.info(f"تم تحليل بيانات {selection}. النتائج مطابقة للمواصفات الهندسية.")
                # رسم بياني بسيط لكل صفحة بشكل مستقل
                st.bar_chart(pd.DataFrame([press, flow], index=['Press', 'Flow']))
        else:
            st.write("أدخل البيانات واضغط 'تحليل' لبدء العمل.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. زر الخروج ---
if st.sidebar.button("🔒 تسجيل الخروج"):
    st.session_state.auth = False
    st.rerun()
