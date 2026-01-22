import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- 1. الإعدادات العالمية والبحث ---
st.set_page_config(page_title="Petro-Oracle Ultimate", layout="wide", page_icon="🌐")

# ستايل "المستقبل" (Deep Space & Neon UI)
st.markdown("""
    <style>
    .stApp { background-color: #010409; color: #e6edf3; }
    [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 2px solid #30363d; }
    .main-card { background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 15px; margin-bottom: 20px; }
    .prediction-box { border-left: 5px solid #238636; background: #0d1117; padding: 15px; margin: 10px 0; }
    .leak-alert { border-left: 5px solid #da3633; background: #1b1111; padding: 15px; }
    .search-bar { background: #000; color: #58a6ff; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. محرك البحث ونظام التنقل (30 صفحة) ---
sections = {
    "الرئيسية": "DASHBOARD",
    "الاستكشاف الجيوفيزيائي": "GEOPHYSICS",
    "المسح السيزمي": "SEISMIC",
    "تقييم الطبقات": "FORMATION_EVAL",
    "هندسة الحفر": "DRILLING_ENG",
    "سوائل الحفر (الطفلة)": "MUD_ENG",
    "سمتة الآبار": "CEMENTING",
    "إكمال الآبار": "WELL_COMPLETION",
    "البتوفيزياء المتقدمة": "PETROPHYSICS_ADV",
    "تحليل سجلات الآبار": "WELL_LOGGING",
    "هندسة الخزانات": "RESERVOIR_ENG",
    "نمذجة الخزانات (3D)": "RESERVOIR_MODELING",
    "اختبارات الآبار": "WELL_TESTING",
    "توقعات الإنتاج": "PRODUCTION_FORECAST",
    "تحليل منحنيات الهبوط": "DCA_ANALYSIS",
    "الرفع الصناعي (ESP)": "ARTIFICIAL_LIFT_ESP",
    "الرفع بالغاز": "GAS_LIFT",
    "المضخات السطحية": "SURFACE_PUMPS",
    "كشف التسريب (Leak Detection)": "LEAK_DETECTION",
    "سلامة الأنابيب": "PIPELINE_INTEGRITY",
    "معالجة النفط الخام": "OIL_TREATMENT",
    "معالجة الغاز الطبيعي": "GAS_PROCESSING",
    "فصل المياه": "WATER_HANDLING",
    "التخزين والشحن": "STORAGE_SHIPPING",
    "المبيعات والعقود": "SALES_CONTRACTS",
    "التحليل المالي (ROI)": "ECONOMICS_ROI",
    "إدارة المخاطر": "RISK_MANAGEMENT",
    "الأمن والسلامة (HSE)": "HSE_SYSTEM",
    "الذكاء الاصطناعي (AI Predict)": "AI_PREDICTION",
    "إعدادات النظام": "SYSTEM_SETTINGS"
}

# شريط البحث العلوي
st.sidebar.markdown("### 🔍 محرك البحث السريع")
search_query = st.sidebar.text_input("ابحث عن قسم أو معادلة...", placeholder="مثال: تسريب، إنتاج...")

# فلترة القائمة بناءً على البحث
filtered_sections = {k: v for k, v in sections.items() if search_query.lower() in k.lower() or search_query.lower() in v.lower()}

st.sidebar.markdown("---")
selection = st.sidebar.radio("القوائم التخصصية", list(filtered_sections.keys()))

# --- 3. بوابة الدخول الذكية ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'pwd' not in st.session_state: st.session_state.pwd = "root"

if not st.session_state.auth:
    st.markdown("<div style='text-align:center; padding-top:100px;'><h1>PETRO-ORACLE LOGIN</h1>", unsafe_allow_html=True)
    if st.text_input("Master Key", type="password") == st.session_state.pwd:
        if st.button("Unlock System"): 
            st.session_state.auth = True
            st.rerun()
else:
    # --- 4. محتوى الصفحات (المحرك الحسابي) ---
    st.title(f"🚀 {selection}")

    col_input, col_output = st.columns([1, 1.5])

    with col_input:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("📝 المدخلات التشغيلية")
        
        # مدخلات عالمية تظهر في كل الصفحات لضمان التسجيل اليدوي
        u_press = st.number_input("الضغط الحالي (psi)", value=1500.0)
        u_temp = st.number_input("درجة الحرارة (F)", value=180.0)
        u_flow = st.number_input("معدل التدفق (bpd)", value=2400.0)
        
        uploaded_file = st.file_uploader("رفع بيانات الإكسيل المتقدمة", type=['xlsx', 'csv'], key=f"file_{selection}")
        
        run_btn = st.button("تشغيل التحليل الشامل")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_output:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("⚙️ مخرجات النظام الذكي")

        if run_btn:
            # --- موديول التنبؤ (Prediction) ---
            st.markdown("<div class='prediction-box'>", unsafe_allow_html=True)
            prediction_val = u_flow * 0.95 # مثال لمعادلة تنبؤ بالإنتاج القادم
            st.write(f"🔮 **التنبؤ بالإنتاج للشهر القادم:** {prediction_val:,.2f} bpd")
            st.markdown("</div>", unsafe_allow_html=True)

            # --- موديول كشف التسريب (Leak Detection) ---
            if selection == "كشف التسريب (Leak Detection)" or selection == "سلامة الأنابيب":
                if u_press < 1000: # لو الضغط نزل فجأة
                    st.markdown("<div class='leak-alert'>", unsafe_allow_html=True)
                    st.error("🚨 تحذير: هبوط حاد في الضغط! احتمال وجود تسريب في الخط الناقل.")
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.success("✅ حالة الأنابيب: مستقرة ولا يوجد تسريب مكتشف.")

            # --- موديول المبيعات (Sales) ---
            if selection == "المبيعات والعقود":
                revenue = u_flow * 75 # سعر البرميل الافتراضي
                st.write(f"💰 **إجمالي المبيعات المتوقعة اليوم:** ${revenue:,.2f}")

            # رسم بياني تفاعلي يظهر فوراً
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=[1,2,3,4], y=[u_flow, u_flow*0.9, u_flow*1.1, u_flow], mode='lines+markers', name='Trend'))
            fig.update_layout(title="تحليل الاتجاهات اللحظي", template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("في انتظار إدخال البيانات لبدء التحليل الهندسي...")
        st.markdown("</div>", unsafe_allow_html=True)

    # --- إدارة النظام والخروج ---
    if st.sidebar.button("🔒 خروج آمن"):
        st.session_state.auth = False
        st.rerun()
