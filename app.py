import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- الإعدادات العالمية ---
st.set_page_config(page_title="Petro-Titan Ultimate", layout="wide")

# لوجو الحفر
DRILLING_LOGO = "https://cdn-icons-png.flaticon.com/512/2906/2906233.png"

if 'auth' not in st.session_state: st.session_state.auth = False

# --- بوابة الدخول ---
if not st.session_state.auth:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.image(DRILLING_LOGO, width=100)
        st.title("PETRO-TITAN GLOBAL")
        with st.form("Login"):
            pwd = st.text_input("Security Key", type="password")
            if st.form_submit_button("UNLOCK SYSTEM"):
                if pwd == "123":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Wrong Key")
else:
    # --- القائمة الجانبية ---
    st.sidebar.image(DRILLING_LOGO, width=60)
    selection = st.sidebar.selectbox("Navigate:", ["📊 Dashboard", "🏗️ Drilling", "💰 Financials"])

    if selection == "📊 Dashboard":
        st.title("🌐 Field Overview")
        st.metric("Daily Production", "645K BPD", "+5%")
        # رسم بياني ذكي
        df = pd.DataFrame({'Days': range(10), 'Output': np.random.randint(600, 700, 10)})
        st.plotly_chart(px.area(df, x='Days', y='Output', title="Production Flow"))

    elif selection == "🏗️ Drilling":
        st.title("🏗️ Rig Telemetry")
        z = np.linspace(0, 10, 50)
        fig = go.Figure(data=[go.Scatter3d(x=np.sin(z), y=np.cos(z), z=-z*100, mode='lines')])
        fig.update_layout(template="plotly_dark")
        st.plotly_chart(fig)

    elif selection == "💰 Financials":
        st.title("💰 Market Analysis")
        st.metric("Revenue", "$84.5M", "+1.2M")
        st.plotly_chart(px.pie(values=[70, 30], names=['Profit', 'Cost']))

st.sidebar.button("🔒 Logout", on_click=lambda: st.session_state.update({"auth": False}))
