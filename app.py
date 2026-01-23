import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- 1. الإعدادات العالمية الفائقة ---
st.set_page_config(page_title="Petro-Titan Enterprise | Full Suite", layout="wide")

DRILLING_LOGO = "https://cdn-icons-png.flaticon.com/512/2906/2906233.png"

st.markdown("""
    <style>
    .main { background-color: #0b0e11; color: #e6edf3; }
    .stMetric { border: 1px solid #30363d; border-radius: 12px; padding: 20px; background: #161b22; }
    div.stButton > button { width: 100%; border-radius: 8px; background-color: #238636; color: white; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. بوابة الدخول ---
if not st.session_state.auth:
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.image(DRILLING_LOGO, width=100)
        st.markdown("<h1 style='text-align:center;'>PETRO-TITAN GLOBAL</h1>", unsafe_allow_html=True)
        with st.form("AdvancedLogin"):
            pwd = st.text_input("Security Access Key", type="password")
            if st.form_submit_button("AUTHORIZE & LAUNCH"):
                if pwd == "123":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Invalid Key")
else:
    # --- 3. القائمة الجانبية ---
    st.sidebar.image(DRILLING_LOGO, width=60)
    st.sidebar.title("Enterprise Hub")
    
    menu = [
        "📊 Dashboard (التحكم العام)", 
        "🏗️ Drilling Engineering (الحفر)", 
        "🔮 Reservoir & AI (المكامن)", 
        "💰 Financial Suite (المالية)", 
        "🗺️ Geo-Spatial Maps (الخرائط)", 
        "🚨 HSE & Security (السلامة)",
        "📂 Reports & Documents (التقارير)"
    ]
    selection = st.sidebar.selectbox("Navigate Modules:", menu)

    # موديول لوحة التحكم
    if "Dashboard" in selection:
        st.title("🌐 Operational Intelligence Dashboard")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Production Rate", "645,200 BPD", "+4.8%")
        m2.metric("Efficiency Index", "98.2%", "Optimal")
        m3.metric("Opex/Bbl", "$11.40", "-1.2%")
        m4.metric("Active Assets", "62 Rigs", "+2")
        df = pd.DataFrame({'Date': pd.date_range(start='2025-01-01', periods=30), 'Output': np.random.randint(600, 650, 30)})
        st.plotly_chart(px.line(df, x='Date', y='Output', title="Production Performance"))

    # موديول الحفر
    elif "Drilling" in selection:
        st.title("🏗️ Precision Drilling Telemetry")
        c1, c2 = st.columns([2, 1])
        with c1:
            z = np.linspace(0, 15, 100)
            x, y = np.sin(z), np.cos(z)
            fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=-z*1000, mode='lines', line=dict(color='gold', width=6))])
            fig.update_layout(template="plotly_dark", height=600)
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            st.metric("Depth", "18,450 ft")
            st.metric("ROP", "115 ft/hr")
            st.progress(0.85)

    # موديول المكامن
    elif "Reservoir" in selection:
        st.title("🔮 AI Reservoir Forecasting")
        heat_data = np.random.rand(10, 10)
        st.plotly_chart(px.imshow(heat_data, color_continuous_scale='Turbo'))

    # موديول المالية
    elif "Financial" in selection:
        st.title("💰 Enterprise Financial Hub")
        qty = st.number_input("Sold Volume (Bbl)", value=1000000)
        st.metric("Gross Revenue", f"${qty * 84.5:,.2f}")
        st.plotly_chart(px.pie(values=[70, 30], names=['Profit', 'Cost']))

    # موديول الخرائط
    elif "Maps" in selection:
        st.title("🗺️ Asset Geo-Location")
        locs = pd.DataFrame({'lat': [30.0, 29.5], 'lon': [31.0, 32.1], 'Well': ['Rig-A', 'Rig-B']})
        st.map(locs)

    # موديول السلامة والتقارير
    elif "HSE" in selection:
        st.error("Alert: System Normal")
    elif "Reports" in selection:
        st.button("📥 Download Full Report")

# الخروج
st.sidebar.divider()
if st.sidebar.button("🔒 EXIT SYSTEM"):
    st.session_state.auth = False
    st.rerun()
