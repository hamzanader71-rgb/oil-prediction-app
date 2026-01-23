import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- إعدادات النسخة الألترا ---
st.set_page_config(page_title="Petro-Titan Maximum v6.0", layout="wide")

DRILLING_LOGO = "https://cdn-icons-png.flaticon.com/512/2906/2906233.png"

# ثيم الشركات الكبرى (Premium Corporate Dark Theme)
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    .stMetric { background: linear-gradient(135deg, #161b22 0%, #0d1117 100%); border: 1px solid #30363d; border-radius: 15px; }
    .price-ticker { background-color: #1f2937; padding: 10px; border-radius: 5px; text-align: center; color: #10b981; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state.auth = False

# --- بوابة الدخول ---
if not st.session_state.auth:
    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        st.image(DRILLING_LOGO, width=120)
        st.markdown("<h1 style='text-align:center; color:#58a6ff;'>PETRO-TITAN MAXIMUM</h1>", unsafe_allow_html=True)
        st.markdown("<div class='price-ticker'>LIVE MARKET: BRENT $84.25 ▲ | WTI $79.10 ▲ | GAS $2.42 ▼</div>", unsafe_allow_html=True)
        with st.form("MaxLogin"):
            pwd = st.text_input("Enterprise Security Key", type="password")
            if st.form_submit_button("LAUNCH ENTERPRISE SUITE", use_container_width=True):
                if pwd == "123":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Access Denied")
else:
    # --- القائمة الجانبية الذكية ---
    st.sidebar.image(DRILLING_LOGO, width=80)
    st.sidebar.markdown("### 🛰️ Global Asset Command")
    
    tabs = ["📊 Master Dashboard", "🏗️ Drilling Telemetry", "🔮 AI Forecasting", "💰 ROI & Finance", "🛡️ HSE & Risk", "📂 Export Reports"]
    choice = st.sidebar.selectbox("Select Module:", tabs)

    if choice == "📊 Master Dashboard":
        st.title("🌐 Operational Intelligence Center")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Field Production", "645K BPD", "+5.2%")
        c2.metric("Avg Oil Price", "$84.22", "+$0.45")
        c3.metric("Lifting Cost", "$11.20/Bbl", "-2%")
        c4.metric("Rig Uptime", "99.1%", "Optimal")
        
        # خريطة حرارية للإنتاج
        st.subheader("Regional Extraction Density")
        fig = px.density_heatmap(np.random.rand(10,10), color_continuous_scale='Viridis')
        st.plotly_chart(fig, use_container_width=True)

    elif choice == "🏗️ Drilling Telemetry":
        st.title("🏗️ Smart Rig Analysis")
        # عرض الـ 3D للمسار
        z = np.linspace(0, 20, 100)
        fig_3d = go.Figure(data=[go.Scatter3d(x=np.cos(z), y=np.sin(z), z=-z*500, mode='lines', line=dict(color='#58a6ff', width=8))])
        fig_3d.update_layout(title="Wellbore Directional Path", template="plotly_dark", height=600)
        st.plotly_chart(fig_3d, use_container_width=True)
        

    elif choice == "💰 ROI & Finance":
        st.title("💰 Investment & Profitability Hub")
        col_in, col_out = st.columns(2)
        with col_in:
            capex = st.number_input("Well Cost (Million $)", value=15.0)
            daily_prod = st.number_input("Daily Output (Bbl)", value=5000)
            oil_price = 84
            daily_revenue = daily_prod * oil_price
            st.success(f"### Daily Revenue: ${daily_revenue:,.2f}")
            st.info(f"Estimated Payback Period: {capex*1000000 / daily_revenue:.1f} Days")
        with col_out:
            st.write("### Cash Flow Projection")
            st.plotly_chart(px.bar(x=["Year 1", "Year 2", "Year 3"], y=[capex*-0.5, capex*0.8, capex*2.1], title="ROI Forecast"))

    elif choice == "📂 Export Reports":
        st.title("📂 Data Export Center")
        st.write("استخراج التقارير بصيغ احترافية للشركاء.")
        st.button("📥 Export Production Data (CSV)")
        st.button("📥 Generate Geological Report (PDF)")
        st.button("📥 Financial Audit (Excel)")

# الخروج
st.sidebar.divider()
if st.sidebar.button("🔒 LOGOUT"):
    st.session_state.auth = False
    st.rerun()
