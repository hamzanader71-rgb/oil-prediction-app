import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. إعدادات المنصة الشاملة
st.set_page_config(page_title="Hamza Petroleum Full Intelligence", layout="wide")

# تصميم UI احترافي
st.markdown("""
    <style>
    .stApp { background: #000b14; color: #00ffcc; }
    [data-testid="stSidebar"] { background-color: #05101a !important; border-right: 2px solid #00ffcc; }
    .stMetric { background: #0a1e2d; padding: 20px; border-radius: 15px; border-top: 4px solid #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية (فهرس النظام)
with st.sidebar:
    st.title("🛡️ Hamza OS v12.0")
    menu = st.sidebar.radio("اختر النظام:", [
        "🔮 محرك التنبؤ الشامل (DCA & IPR)",
        "🧪 البتروفيزياء والـ Skin Factor",
        "🚨 نظام كشف التسريب والخرائط",
        "🏗️ أمان الحفر والـ Kill Sheet",
        "📊 منصة الـ 20 معامل"
    ])
    st.write("---")
    st.success("الحالة: تغطية كاملة 100% ✅")

# ==========================================
# 1. محرك التنبؤ الشامل (كل حسابات التنبؤ)
# ==========================================
if menu == "🔮 محرك التنبؤ الشامل (DCA & IPR)":
    st.title("🔮 Production Forecasting & Nodal Analysis")
    t1, t2 = st.tabs(["التنبؤ بالهبوط (DCA)", "تحليل القدرة (IPR vs VLP)"])
    
    with t1:
        qi = st.number_input("الإنتاج الابتدائي (bpd)", 4000)
        di = st.slider("معدل الهبوط سنوي (%)", 1, 40, 15)
        t = np.arange(0, 120)
        qt = qi * np.exp(-(di/100) * (t/12))
        st.area_chart(qt)
        st.metric("الدخل اليومي المتوقع ($)", f"{qi * 85:,.0f}")
        

    with t2:
        pr = st.slider("Reservoir Pressure (psi)", 2000, 6000, 4500)
        q = np.linspace(0, 6000, 100)
        ipr = pr * (1 - 0.2*(q/6000) - 0.8*(q/6000)**2)
        vlp = 1000 + 0.00015 * q**2
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=q, y=ipr, name="IPR", line=dict(color='#00ffcc', width=3)))
        fig.add_trace(go.Scatter(x=q, y=vlp, name="VLP", line=dict(color='#ff4b4b', width=3)))
        st.plotly_chart(fig, use_container_width=True)
        

# ==========================================
# 2. البتروفيزياء والـ Skin Factor (الحسابات المتقدمة)
# ==========================================
elif menu == "🧪 البتروفيزياء والـ Skin Factor":
    st.title("🧪 Advanced Formation Evaluation")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Archie's Law (Sw)")
        rw = st.number_input("Rw", 0.05); rt = st.number_input("Rt", 10.0); phi = st.slider("Porosity", 0.1, 0.4, 0.2)
        sw = np.sqrt((1 * rw) / (phi**2 * rt))
        st.metric("Water Saturation", f"{sw*100:.2f} %")
    with c2:
        st.subheader("Skin Factor Analysis")
        k = st.number_input("Permeability (k)", 150); h = st.number_input("Thickness (h)", 50)
        pwf = st.number_input("Pwf", 2500); q_prod = st.number_input("Production Rate", 1000)
        skin = ((k * h * (4000 - pwf)) / (141.2 * q_prod * 1.5 * 1.1)) - np.log(1490/0.328)
        st.metric("Skin Factor", f"{skin:.2f}")

# ==========================================
# 3. نظام كشف التسريب والخرائط (القسم الجديد)
# ==========================================
elif menu == "🚨 نظام كشف التسريب والخرائط":
    st.title("🚨 Leak Detection & GPS Tracking")
    col1, col2 = st.columns([1, 2])
    with col1:
        f_in = st.number_input("Flow In", 1000); f_out = st.number_input("Flow Out", 950)
        loss = f_in - f_out
        if (loss/f_in) > 0.02:
            st.error("🚨 Leak Detected!")
            lat, lon = 30.05, 31.25 # مكان التسريب المتوقع
        else:
            st.success("✅ Line Secure")
            lat, lon = 30.0, 31.2
    with col2:
        st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}), zoom=10)

# ==========================================
# 4. أمان الحفر (Kill Sheet)
# ==========================================
elif menu == "🏗️ أمان الحفر والـ Kill Sheet":
    st.title("🏗️ Well Control Center")
    sidpp = st.number_input("SIDPP", 500); tvd = st.number_input("TVD", 10000)
    kmw = 10.0 + (sidpp / (0.052 * tvd))
    st.metric("Kill Mud Weight", f"{kmw:.2f} ppg")

# ==========================================
# 5. منصة الـ 20 معامل
# ==========================================
else:
    st.title("📊 Master Data Entry")
    cols = st.columns(5)
    for i in range(1, 21):
        cols[i%5].text_input(f"Param {i}", "Value")
