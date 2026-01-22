import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. الإعدادات الأساسية ---
st.set_page_config(page_title="Petro-Oracle Pro V25", layout="wide")

# ستايل احترافي لمنع التشتت
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #adbac7; }
    .module-container { border: 1px solid #444c56; padding: 20px; border-radius: 10px; background: #1c2128; }
    .stButton>button { width: 100%; background-color: #347d39; color: white; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. إدارة الصفحات (30 موديول) ---
pages_list = [
    "الرئيسية", "الاستكشاف", "المسح السيزمي", "تقييم الطبقات", "هندسة الحفر", 
    "سوائل الحفر", "السمتة", "إكمال الآبار", "البتوفيزياء", "تحليل السجلات",
    "هندسة الخزانات", "نمذجة الخزانات", "اختبارات الآبار", "توقعات الإنتاج", "تحليل الهبوط DCA",
    "الرفع الصناعي ESP", "الرفع بالغاز", "المضخات", "كشف التسريب", "سلامة الأنابيب",
    "معالجة الخام", "معالجة الغاز", "فصل المياه", "التخزين والشحن", "المبيعات",
    "التحليل المالي", "إدارة المخاطر", "الأمن والسلامة", "الذكاء الاصطناعي", "الإعدادات"
]

# محرك البحث
st.sidebar.title("🔍 البحث السريع")
search = st.sidebar.text_input("ابحث عن موديول...")
filtered_pages = [p for p in pages_list if search.lower() in p.lower()]

selection = st.sidebar.radio("القائمة التقنية", filtered_pages)

# --- 3. نظام الحماية الذكي ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<h1 style='text-align:center;'>PETRO-SYSTEM LOCK</h1>", unsafe_allow_html=True)
    if st.text_input("Password", type="password") == "root":
        if st.button("دخول"): 
            st.session_state.auth = True
            st.rerun()
else:
    st.title(f"🚀 {selection}")
    
    # --- 4. فصل البيانات (Unique Session State) ---
    # بنستخدم الـ selection كجزء من اسم المتغير عشان م يحصلش تداخل
    st.markdown("<div class='module-container'>", unsafe_allow_html=True)
    col_in, col_res = st.columns([1, 1.5])

    with col_in:
        st.subheader("📥 مدخلات البيانات")
        # كل مدخل له مفتاح (key) فريد بناءً على اسم الصفحة
        p_val = st.number_input(f"الضغط في {selection} (psi)", key=f"p_{selection}")
        q_val = st.number_input(f"المعدل في {selection} (bpd)", key=f"q_{selection}")
        up_file = st.file_uploader("رفع إكسيل", type=['xlsx', 'csv'], key=f"file_{selection}")
        
        run_engine = st.button("تشغيل المعالجة الهندسية", key=f"btn_{selection}")

    with col_res:
        st.subheader("⚙️ النتائج والتحليل")
        if run_engine:
            # هنا بنفصل "المنطق البرمجي" لكل صفحة
            if selection == "كشف التسريب":
                if p_val < 500:
                    st.error("🚨 خطر: تسريب محتمل! الضغط منخفض جداً.")
                else:
                    st.success("✅ حالة الخط مستقرة.")
            
            elif selection == "المبيعات":
                total_sales = q_val * 75 # سعر برميل افتراضي
                st.metric("إجمالي مبيعات اليوم", f"${total_sales:,.0f}")
            
            elif selection == "توقعات الإنتاج":
                st.info("🔮 بناءً على الأرقام الحالية، الإنتاج سيستمر بمعدل ثابت لـ 6 أشهر.")
                st.line_chart(np.random.randn(20, 1)) # رسم بياني عشوائي للتوضيح

            else:
                st.write(f"تم تحليل بيانات {selection} بنجاح.")
                st.write(f"الضغط المسجل: {p_val} | المعدل: {q_val}")
        else:
            st.info("أدخل البيانات واضغط تشغيل للحصول على التحليل.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. زر الخروج ---
st.sidebar.markdown("---")
if st.sidebar.button("تسجيل الخروج"):
    st.session_state.auth = False
    st.rerun()
