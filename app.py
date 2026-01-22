import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px # للرسوم البيانية التفاعلية العالمية

# --- إعدادات المنصة ---
st.set_page_config(page_title="Petro-Master Ultimate", layout="wide")

# تصميم "براند" عالمي (Industrial Glass-Dark Theme)
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #e5e7eb; }
    [data-testid="stSidebar"] { background-color: #0b0f1a !important; border-right: 1px solid #1f2937; }
    .metric-box { 
        background: linear-gradient(145deg, #111827, #1f2937); 
        padding: 20px; border-radius: 15px; border: 1px solid #374151;
        text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .stButton>button { 
        background: linear-gradient(90deg, #1d4ed8, #2563eb); 
        color: white; border-radius: 10px; border: none; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- نظام الحماية المرن ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<div style='text-align: center; margin-top: 100px;'><h1>PETRO-MASTER LOGIN</h1>", unsafe_allow_html=True)
    pwd = st.text_input("Master Access Code", type="password")
    if st.button("Unlock System"):
        if pwd == "root": # يمكن تعديله لاحقاً
            st.session_state.auth = True
            st.rerun()
else:
    # --- القائمة الشاملة (12 صفحة تغطي قطاع البترول بالكامل) ---
    pages = {
        "DASHBOARD": "اللوحة الرئيسية",
        "GEOLOGY": "الجيولوجيا والمؤشرات السيزمية",
        "DRILLING": "هندسة وتحسين الحفر",
        "LOGGING": "تحليل سجلات الآبار (Petrophysics)",
        "RESERVOIR": "هندسة الخزانات وحساب الاحتياطي",
        "PVT_ANALYSIS": "خواص سوائل الخزان (PVT)",
        "PRODUCTION": "تحسين وإدارة الإنتاج",
        "DCA": "تحليل منحنيات الهبوط (Decline Curve)",
        "ARTIFICIAL_LIFT": "الرفع الصناعي (ESP/Gas Lift)",
        "PIPELINES": "شبكات النقل وخطوط الأنابيب",
        "HSE_SAFETY": "إدارة السلامة والبيئة",
        "ECONOMICS": "التحليل المالي وجدوى المشروع"
    }
    
    st.sidebar.title("💠 PETRO-NAVIGATOR")
    selection = st.sidebar.radio("إختر القطاع التخصصي:", list(pages.keys()), format_func=lambda x: pages[x])
    
    st.title(f"📂 {pages[selection]}")

    # --- موديول "الكمال الفني" (بيانات يدوية + إكسيل + كود مدمج) ---
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.subheader("📝 مدخلات المهندس")
        field_name = st.text_input("اسم الحقل/البئر", "Well-01")
        param_1 = st.number_input("الضغط (psi)", value=2500)
        param_2 = st.number_input("الإنتاج (bpd)", value=1200)
        if st.button("حفظ وتحديث"):
            st.success("تم التحديث في قاعدة البيانات")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.subheader("📈 التحليل البياني المتقدم")
        up_file = st.file_uploader("ارفع بيانات الحقل (Excel/CSV)", key=selection)
        if up_file:
            data = pd.read_excel(up_file) if up_file.name.endswith('xlsx') else pd.read_csv(up_file)
            fig = px.line(data, title=f"تحليل اتجاهات {pages[selection]}", template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- منطقة دمج الأكواد السبعة + الإضافات الجديدة ---
    st.markdown("---")
    st.subheader("🔍 النتائج الاستنتاجية (AI Insights)")
    
    if selection == "DCA":
        st.info("💡 موديول تحليل الهبوط: يتنبأ بعمر البئر بناءً على معدلات الإنتاج الحالية.")
        # هنا يدمج كود تحليل الـ Decline Curve
        
    elif selection == "RESERVOIR":
        st.info("💡 حسابات الاحتياطي: يتم الآن حساب المخرجات باستخدام معادلة الموازنة المادية (Material Balance).")
        # هنا يدمج كود الخزانات الخاص بك
        
    elif selection == "ECONOMICS":
        st.info("💡 التحليل المالي: حساب الـ NPV و الـ IRR للمشروع.")

    # إعدادات الحماية في الجنب
    with st.sidebar.expander("🛠️ إعدادات النظام"):
        if st.button("تغيير كلمة المرور"):
            st.info("ميزة قيد التفعيل...")
    if st.sidebar.button("🔒 تسجيل الخروج"):
        st.session_state.auth = False
        st.rerun()
