import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. إعدادات المنصة النهائية
st.set_page_config(page_title="Hamza Petroleum 100% AI", layout="wide")

# تصميم UI عالي التقنية (The Oilfield Dashboard)
st.markdown("""
    <style>
    .stApp { background: #000205; color: #00ffcc; }
    .stMetric { background: #050a10; padding: 25px; border-radius: 15px; border-top: 5px solid #00ffcc; box-shadow: 0px 10px 20px rgba(0,0,0,0.8); }
    [data-testid="stSidebar"] { background-color: #020508 !important; border-right: 1px solid #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية (الموسوعة الشاملة)
with st.sidebar:
    st.title("🛰️ Hamza OS v100%")
    menu = st.sidebar.selectbox("المحرك الذكي:", [
        "📉 تحليل العقد (Nodal Analysis)",
        "🔮 التنبؤ بالإنتاج (DCA)",
        "🏗️ أمان الحفر والـ Kill Sheet",
        "🧪 البتروفيزياء (Archie's Law)",
        "⚡ أداء الطلمبات (ESP Analysis)",
        "📊 منصة الـ 20 معامل",
        "🧭 خريطة المواقع (GPS)",
        "⚖️ ميزان الكربون والمالية"
    ])
    st.sidebar.markdown("---")
    st.sidebar.info("الحالة: تغطية هندسية كاملة 100% ✅")

# --- 1. تحليل العقد (IPR vs VLP) ---
if menu == "📉 تحليل العقد (Nodal Analysis)":
    st.title("📉 Inflow vs Outflow Performance")
    q = np.linspace(10, 6000, 100)
    pr = st.slider("Reservoir Pressure (psi)", 2000, 6000, 4500)
    ipr = pr * (1 - 0.2*(q/6000) - 0.8*(q/6000)**2)
    vlp = 1000 + 0.00015 * q**2
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=q, y=ipr, name="IPR", line=dict(color='#00ffcc', width=4)))
    fig.add_trace(go.Scatter(x=q, y=vlp, name="VLP", line=dict(color='#ff4b4b', width=4)))
    st.plotly_chart(fig, use_container_width=True)
    

# --- 2. البتروفيزياء (Archie's Law) ---
elif menu == "🧪 البتروفيزياء (Archie's Law)":
    st.title("🧪 Petrophysical Analysis (Water Saturation)")
    st.write("احسب نسبة المياه والزيت داخل الصخور:")
    rw = st.number_input("Formation Water Resistivity (Rw)", 0.05)
    phi = st.slider("Porosity (Φ)", 0.01, 0.40, 0.20)
    rt = st.number_input("True Formation Resistivity (Rt)", 10.0)
    
    # Archie's Equation: Sw = ( (a * Rw) / (Phi^m * Rt) )^(1/n)
    sw = np.sqrt((1 * rw) / (phi**2 * rt))
    so = 1 - sw
    
    c1, c2 = st.columns(2)
    c1.metric("Water Saturation ($S_w$)", f"{sw*100:.2f} %")
    c2.metric("Oil Saturation ($S_o$)", f"{so*100:.2f} %")
    

# --- 3. أداء الطلمبات (ESP Analysis) ---
elif menu == "⚡ أداء الطلمبات (ESP Analysis)":
    st.title("⚡ ESP Pump Performance Curve")
    q_pump = np.linspace(0, 5000, 100)
    head = 4000 - 0.0001 * q_pump**2 # محاكاة لمنحنى الـ Head
    
    fig = px.line(x=q_pump, y=head, title="Pump Head vs Flow Rate")
    fig.add_hline(y=2500, line_dash="dash", line_color="red", annotation_text="Required Head")
    st.plotly_chart(fig, use_container_width=True)
    

# --- 4. أمان الحفر والـ Kill Sheet ---
elif menu == "🏗️ أمان الحفر والـ Kill Sheet":
    st.title("🏗️ Well Control Center")
    sidpp = st.number_input("SIDPP (psi)", 500)
    tvd = st.number_input("Depth (ft)", 10000)
    omw = st.number_input("OMW (ppg)", 10.5)
    kmw = omw + (sidpp / (0.052 * tvd))
    st.metric("Kill Mud Weight (KMW)", f"{kmw:.2f} ppg")
    

# --- 5. التنبؤ بالإنتاج والمالية ---
elif menu == "🔮 التنبؤ بالإنتاج (DCA)":
    st.title("💰 Production & Financial Forecast")
    qi = st.number_input("Initial Rate", 4000)
    t = np.arange(0, 60)
    qt = qi * np.exp(-(0.12/12) * t)
    st.area_chart(qt)
    st.metric("Daily Revenue ($)", f"{qi * 85:,.0f}")

# --- 6. منصة الـ 20 معامل ---
elif menu == "📊 منصة الـ 20 معامل":
    st.title("📊 100% Data Coverage")
    cols = st.columns(5)
    for i in range(1, 21):
        cols[i%5].text_input(f"Parameter {i}", "Value")

# --- 7. خريطة المواقع (GPS) ---
elif menu == "🧭 خريطة المواقع (GPS)":
    st.title("📍 GPS Asset Tracking")
    st.map(pd.DataFrame({'lat': [28.2, 29.5], 'lon': [33.1, 31.2]}))

# --- 8. ميزان الكربون (ESG) ---
else:
    st.title("🌱 Environmental Impact")
    diesel = st.number_input("Diesel Used (Gal/Day)", 500)
    st.metric("Carbon Emissions ($CO_2$)", f"{(diesel * 10.18)/1000:.2f} Tons")
