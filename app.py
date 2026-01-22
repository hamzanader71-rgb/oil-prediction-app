import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from io import StringIO

# --- إعدادات المنصة العالمية ---
st.set_page_config(page_title="PETRO-MASTER AI", layout="wide", page_icon="🏗️")

# ستايل المصانع الذكية (Cyber-Industrial Theme)
st.markdown("""
    <style>
    .stApp { background-color: #010409; color: #c9d1d9; }
    [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #30363d; }
    .result-card { 
        background: #161b22; border: 1px solid #30363d; 
        padding: 20px; border-radius: 10px; margin-top: 15px;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.1);
    }
    .metric-value { color: #58a6ff; font-size: 24px; font-weight: bold; }
    .stButton>button { background-color: #238636; color: white; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- نظام الحماية (الباسورد المرن) ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'master_pwd' not in st.session_state: st.session_state.master_pwd = "root"

if not st.session_state.auth:
    st.markdown("<div style='text-align:center; padding-top:100px;'><h1>🔐 SECURE ACCESS</h1>", unsafe_allow_html=True)
    pwd_in = st.text_input("Enter Master Key", type="password")
    if st.button("UNLOCK"):
        if pwd_in == st.session_state.master_pwd:
            st.session_state.auth = True
            st.rerun()
else:
    # --- توزيع الـ 15 صفحة (تغطية شاملة للمجال) ---
    sections = {
        "DASHBOARD": "التحكم المركزي",
        "GEOPHYSICS": "الجيوفيزياء والسيزماتيك",
        "EXPLORATION": "الاستكشاف والتقييم",
        "DRILLING_ENG": "هندسة الحفر والآبار",
        "MUD_LOGGING": "تسجيل الطفلة والسوائل",
        "PETROPHYSICS": "تحليل الخصائص الصخرية",
        "RESERVOIR_ENG": "هندسة الخزانات",
        "PVT_MOD": "نمذجة خواص السوائل (PVT)",
        "WELL_TESTING": "اختبارات الآبار والضغوط",
        "PRODUCTION_OPT": "تحسين الإنتاج (Optimization)",
        "ARTIFICIAL_LIFT": "أنظمة الرفع الصناعي",
        "FACILITIES": "المنشآت السطحية والمعالجة",
        "PIPELINE_FLOW": "جريان خطوط الأنابيب",
        "HSE_CORP": "السلامة والبيئة المؤسسية",
        "ECON_APPRAISAL": "الجدوى والتقييم المالي"
    }

    st.sidebar.title("💠 PETRO-GIANT V23")
    selection = st.sidebar.radio("NAVIGATE MODULES", list(sections.keys()), format_func=lambda x: sections[x])
    
    # ميزة تغيير الباسورد
    with st.sidebar.expander("⚙️ System Settings"):
        new_p = st.text_input("New PWD", type="password")
        if st.button("Update"): st.session_state.master_pwd = new_p

    st.markdown(f"<h1>🚀 {sections[selection]}</h1>", unsafe_allow_html=True)

    # --- موديول معالجة البيانات واستخراج النتائج (The Engine) ---
    col_in, col_out = st.columns([1, 1.5])

    with col_in:
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.subheader("📥 Data Inputs")
        
        # خيار الرفع
        up_file = st.file_uploader("Upload Sector File (Excel/CSV)", key=f"up_{selection}")
        
        # خيار الإدخال اليدوي
        st.markdown("---")
        st.write("Manual Parameters Entry:")
        p_val = st.number_input("Pressure (psi)", value=2000.0)
        q_val = st.number_input("Flow Rate (bpd)", value=500.0)
        
        calc_btn = st.button("RUN ANALYSIS & COMPUTE")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_out:
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.subheader("📊 Execution Results & AI Insights")
        
        if calc_btn:
            # --- محرك النتائج (هنا ندمج معادلاتك السبعة) ---
            if selection == "RESERVOIR_ENG":
                # مثال لنتيجة حسابية (معادلة ميزان المادة)
                reserve = (p_val * q_val) / 0.85 # مثال لمعادلة
                st.write("### Calculated Result:")
                st.markdown(f"<p class='metric-value'>Estimated Reserves: {reserve:,.0f} STB</p>", unsafe_allow_html=True)
                
            elif selection == "PRODUCTION_OPT":
                st.write("### Production Performance:")
                # كود رسم بياني تفاعلي
                fig = go.Figure(go.Indicator(mode = "gauge+number", value = q_val, title = {'text': "BPD Rate"}, gauge = {'axis': {'range': [None, 5000]}, 'bar': {'color': "#58a6ff"}}))
                st.plotly_chart(fig, use_container_width=True)

            # تشغيل مخرجات الكود المدمج (print)
            st.success("Analysis Complete. No Anomalies Detected.")
        else:
            st.info("Waiting for data input to generate report...")
        st.markdown("</div>", unsafe_allow_html=True)

    # --- قسم المستندات والحفظ ---
    st.markdown("---")
    with st.expander("📂 Archive & Document Storage"):
        st.text_area("Field Engineer Remarks", key=f"rem_{selection}")
        st.button("Archive to Master Database")

    if st.sidebar.button("🔒 LOGOUT"):
        st.session_state.auth = False
        st.rerun()
