import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# إعدادات المنصة (صفحة التنبؤ الرئيسية)
st.set_page_config(page_title="Hamza Production Forecasting", layout="wide")

# تصميم UI عالي التقنية
st.markdown("""
    <style>
    .stApp { background: #00050a; color: #00ffcc; }
    .stMetric { background: #0a1420; padding: 20px; border-radius: 15px; border-top: 4px solid #00ffcc; box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 محرك التنبؤ والتحليل الفني (Forecasting Hub)")

# القائمة الجانبية للتنبؤ فقط
with st.sidebar:
    st.title("🛡️ Hamza Forecast")
    forecast_menu = st.radio("اختر نوع التحليل:", [
        "📉 تحليل العقد (Nodal Analysis)",
        "🔮 التنبؤ بالإنتاج والمالية"
    ])

# --- 1. تحليل العقد (IPR vs VLP) ---
if forecast_menu == "📉 تحليل العقد (Nodal Analysis)":
    st.subheader("📉 System Analysis (IPR vs VLP)")
    q = np.linspace(10, 6000, 100)
    pr = st.slider("Reservoir Pressure (psi)", 2000, 6000, 4000)
    ipr = pr * (1 - 0.2*(q/6000) - 0.8*(q/6000)**2)
    vlp = 800 + 0.00015 * q**2
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=q, y=ipr, name="IPR (Inflow)", line=dict(color='#00ffcc', width=4)))
    fig.add_trace(go.Scatter(x=q, y=vlp, name="VLP (Outflow)", line=dict(color='#ff4b4b', width=4)))
    st.plotly_chart(fig, use_container_width=True)
    

# --- 2. التنبؤ بالإنتاج والمالية ---
else:
    st.subheader("💰 Production Economics & Decline Curve")
    col1, col2 = st.columns([1, 2])
    with col1:
        qi = st.number_input("الإنتاج الابتدائي (bpd)", 3500)
        di = st.slider("معدل الهبوط سنوي (%)", 1, 40, 15)
        st.metric("Daily Revenue ($)", f"{qi * 85:,.0f}")
    
    with col2:
        t = np.arange(0, 60)
        qt = qi * np.exp(-(di/100/12) * t)
        st.area_chart(qt)
