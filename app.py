import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- 1. الإعدادات العالمية الفائقة ---
st.set_page_config(page_title="Petro-Titan Enterprise | Full Suite", layout="wide")

# لوجو البريمة المعتمد
DRILLING_LOGO = "https://cdn-icons-png.flaticon.com/512/2906/2906233.png"

# تصميم عصري (Global Corporate Theme)
st.markdown("""
    <style>
    .main { background-color: #0b0e11; color: #e6edf3; }
    .stMetric { border: 1px solid #30363d; border-radius: 12px; padding: 20px; background: #161b22; box-shadow: 2px 2px 10px rgba(0,0,0,0.5); }
    .stSidebar { background-color: #0d1117; }
    div.stButton > button { width: 100%; border-radius: 8px; background-color: #238636; color: white; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. بوابة الدخول الذكية ---
if not st.session_state.auth:
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with col2 := c2:
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
    # --- 3. القائمة الجانبية (كل الموديولات تلقائياً) ---
    st.sidebar.image(DRILLING_LOGO, width=60)
    st.sidebar.title("Enterprise Hub")
    
    # قائمة الموديولات الشاملة
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

    # --- 4. محتوى الموديولات (كاملة المواصفات تلقائياً) ---

    # موديول لوحة التحكم
    if "Dashboard" in selection:
        st.title("🌐 Operational Intelligence Dashboard")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Production Rate", "645,200 BPD", "+4.8%")
        m2.metric("Efficiency Index", "98.2%", "Optimal")
        m3.metric("Opex/Bbl", "$11.40", "-1.2%")
        m4.metric("Active Assets", "62 Rigs", "+2")
        
        # رسم بياني للإنتاج التاريخي
        df = pd.DataFrame({'Date': pd.date_range(start='2025-01-01', periods=30), 'Output': np.random.randint(600, 650, 30)})
        st.plotly_chart(px.line(df, x='Date', y='Output', title="Monthly Production Performance (BPD/k)"))

    # موديول الحفر
    elif "Drilling" in selection:
        st.title("🏗️ Precision Drilling Telemetry")
        c1, c2 = st.columns([2, 1])
        with c1:
            # مسار البئر 3D
            st.write("### 3D Trajectory Visualization")
            z = np.linspace(0, 15, 100)
            x, y = np.sin(z), np.cos(z)
            fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=-z*1000, mode='lines', line=dict(color='gold', width=6))])
            fig.update_layout(template="plotly_dark", height=600)
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            st.metric("Total Vertical Depth", "18,450 ft")
            st.metric("Hook Load", "310 klbs")
            st.metric("ROP", "115 ft/hr")
            st.progress(0.85)

    # موديول المكامن والذكاء الاصطناعي
    elif "Reservoir" in selection:
        st.title("🔮 AI Reservoir Forecasting")
        # خريطة حرارية للضغط
        st.write("### Pressure Distribution Heatmap")
        heat_data = np.random.rand(10, 10)
        st.plotly_chart(px.imshow(heat_data, color_continuous_scale='Turbo', title="Reservoir Energy State"))
        st.success("AI Prediction: Field life extended by 14% based on current injection rates.")

    # موديول المالية
    elif "Financial" in selection:
        st.title("💰 Enterprise Financial Hub")
        f1, f2 = st.columns(2)
        with f1:
            qty = st.number_input("Sold Volume (Bbl)", value=1000000)
            rev = qty * 84.5
            st.metric("Gross Revenue", f"${rev:,.2f}")
            st.plotly_chart(px.pie(values=[70, 20, 10], names=['Net Profit', 'Operational Cost', 'Tax']))
        with f2:
            st.write("### Market Feed")
            st.info("Brent Crude: $84.50 | WTI: $79.20 | Natural Gas: $2.45")

    # موديول الخرائط
    elif "Maps" in selection:
        st.title("🗺️ Asset Geo-Location")
        locs = pd.DataFrame({
            'lat': [30.0, 29.5, 28.8, 30.2], 'lon': [31.0, 32.1, 33.5, 30.8],
            'Well': ['Rig-Alpha', 'Rig-Beta', 'Rig-Gamma', 'Rig-Delta']
        })
        st.map(locs)

    # موديول السلامة
    elif "HSE" in selection:
        st.title("🛡️ Safety & Risk Command")
        st.error("Alert: High Pressure detected in Section-A4. Automated valves engaged.")
        st.metric("Safe Work Days", "1,240 Days", "Excellent")

    # مركز التقارير
    elif "Reports" in selection:
        st.title("📂 Documentation Center")
        st.file_uploader("Upload Daily Rig Reports")
        st.button("📥 Export Full Enterprise Report (PDF)")
        st.button("📥 Download Financial Audit (Excel)")

# --- 5. التذييل التلقائي ---
st.sidebar.divider()
st.sidebar.caption(f"Status: Fully Synchronized 🟢")
st.sidebar.caption(f"Version: 5.0.1 Global Enterprise")
if st.sidebar.button("🔒 EXIT SYSTEM"):
    st.session_state.auth = False
    st.rerun()
