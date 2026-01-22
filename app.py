import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. إعدادات المنصة (تغطية كاملة 100%)
st.set_page_config(page_title="Hamza Petroleum 100% AI Hub", layout="wide")

# تصميم UI عالي التقنية
st.markdown("""
    <style>
    .stApp { background: #00050a; color: #00ffcc; }
    .stMetric { background: #0a1420; padding: 20px; border-radius: 15px; border-top: 4px solid #00ffcc; box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
    [data-testid="stSidebar"] { background-color: #050a15 !important; border-right: 2px solid #00ffcc; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #0a1420; border-radius: 10px 10px 0 0; color: #00ffcc; padding: 10px 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية (مركز التحكم الشامل)
with st.sidebar:
    st.title("🛡️ Hamza OS v10.0")
    menu = st.sidebar.selectbox("المحرك الذكي:", [
        "📉 تحليل العقد (Nodal Analysis)",
        "📊 قاعدة البيانات الشاملة والـ Skin",
        "🔮 التنبؤ بالإنتاج والمالية",
        "🏗️ مركز أمان الحفر (Well Control)",
        "🧪 البتروفيزياء (Archie's Law)",
        "⚡ أداء الطلمبات (ESP)",
        "📍 الخرائط والـ GPS",
        "🌱 ميزان الكربون (ESG)"
    ])
    st.sidebar.markdown("---")
    st.sidebar.info("الحالة: تغطية هندسية 100% ✅")

# --- 1. تحليل العقد (IPR vs VLP) ---
if menu == "📉 تحليل العقد (Nodal Analysis)":
    st.title("📉 System Analysis (IPR vs VLP)")
    q = np.linspace(10, 6000, 100)
    pr = st.sidebar.slider("Reservoir Pressure (psi)", 2000, 6000, 4000)
    ipr = pr * (1 - 0.2*(q/6000) - 0.8*(q/6000)**2)
    vlp = 800 + 0.00015 * q**2
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=q, y=ipr, name="IPR", line=dict(color='#00ffcc', width=4)))
    fig.add_trace(go.Scatter(x=q, y=vlp, name="VLP", line=dict(color='#ff4b4b', width=4)))
    st.plotly_chart(fig, use_container_width=True)

# --- 2. قاعدة البيانات الشاملة وحساب الـ Skin Factor ---
elif menu == "📊 قاعدة البيانات الشاملة والـ Skin":
    st.title("📊 Master Data & Formation Damage (Skin)")
    tab1, tab2, tab3 = st.tabs(["بيانات المكمن", "بيانات PVT", "حساب الـ Skin Factor"])
    
    with tab1:
        c1, c2 = st.columns(2)
        h = c1.number_input("السمك (h) ft", 50.0)
        phi = c1.number_input("المسامية (Φ)", 0.2)
        k = c2.number_input("النفاذية (k) mD", 150.0)
        re = c2.number_input("نصف قطر التصريف (re) ft", 1490.0)
        
    with tab2:
        c1, c2 = st.columns(2)
        api = c1.number_input("API Gravity", 35.0)
        mu = c2.number_input("اللزوجة (cp)", 1.5)
        
    with tab3:
        st.subheader("تحليل تضرر التكوين (Skin Factor)")
        pwf = st.number_input("ضغط القاع (Pwf) psi", 2500.0)
        q_prod = st.number_input("الإنتاج الحالي (q) bpd", 1200.0)
        rw = st.number_input("نصف قطر البئر (rw) ft", 0.328)
        
        if st.button("احسب الـ Skin Factor"):
            # معادلة تقريبية للـ Skin Factor
            skin = ((k * h * (4000 - pwf)) / (141.2 * q_prod * mu * 1.1)) - np.log(re/rw)
            st.metric("Skin Factor (s)", f"{skin:.2f}")
            if skin > 0: st.error("🚨 الطبقة متضررة (Damaged)")
            else: st.success("🟢 الطبقة ممتازة (Stimulated/Clean)")

# --- 3. التنبؤ بالإنتاج والمالية ---
elif menu == "🔮 التنبؤ بالإنتاج والمالية":
    st.title("💰 Production Economics")
    qi = st.number_input("Initial Rate", 3500)
    t = np.arange(0, 60)
    qt = qi * np.exp(-(0.15/12) * t)
    st.metric("Daily Revenue ($)", f"{qi * 85:,.0f}")
    st.area_chart(qt)

# --- 4. مركز أمان الحفر (Well Control) ---
elif menu == "🏗️ مركز أمان الحفر (Well Control)":
    st.title("🏗️ Kill Sheet & Safety")
    sidpp = st.number_input("SIDPP (psi)", 500)
    tvd = st.number_input("TVD (ft)", 10000)
    omw = st.number_input("Old Mud Weight (ppg)", 10.0)
    kmw = omw + (sidpp / (0.052 * tvd))
    st.metric("Kill Mud Weight", f"{kmw:.2f} ppg")

# --- 5. البتروفيزياء (Archie's Law) ---
elif menu == "🧪 البتروفيزياء (Archie's Law)":
    st.title("🧪 Sw Calculation")
    rw = st.number_input("Rw", 0.05); rt = st.number_input("Rt", 10.0); phi_p = st.slider("Phi", 0.01, 0.4, 0.2)
    sw = np.sqrt((1 * rw) / (phi_p**2 * rt))
    st.metric("Water Saturation (Sw)", f"{sw*100:.2f} %")

# --- 6. أداء الطلمبات (ESP) ---
elif menu == "⚡ أداء الطلمبات (ESP)":
    st.title("⚡ ESP Performance Hub")
    q_esp = np.linspace(0, 4000, 100); head = 3500 - 0.0002 * q_esp**2
    fig = px.line(x=q_esp, y=head, title="Pump Performance Curve"); st.plotly_chart(fig)

# --- 7. الخرائط والـ GPS ---
elif menu == "📍 الخرائط والـ GPS":
    st.title("📍 Field Assets")
    st.map(pd.DataFrame({'lat': [28.2, 29.8], 'lon': [33.1, 31.3]}))

# --- 8. ميزان الكربون (ESG) ---
else:
    st.title("🌱 Carbon Tracking")
    diesel = st.number_input("Diesel (Gal/Day)", 600)
    st.metric("CO2 (Tons)", f"{(diesel * 10.18)/1000:.2f}")
