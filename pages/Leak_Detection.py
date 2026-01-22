import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# 1. إعدادات المنصة
st.set_page_config(page_title="Emperor Leak & Finance Hub", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #00080f; color: #00ffcc; }
    .stMetric { background: #011627; padding: 20px; border-radius: 15px; border-top: 4px solid #ff0055; box-shadow: 0 5px 15px rgba(255,0,85,0.2); }
    </style>
    """, unsafe_allow_html=True)

st.title("🚨 نظام مراقبة النزيف المالي وسلامة الأنابيب")
st.write(f"الحالة اللحظية للخط: {datetime.now().strftime('%H:%M:%S')}")

# 2. لوحة التحكم والحسابات المالية
with st.sidebar:
    st.header("💰 معايير الخسارة")
    oil_price = st.number_input("سعر البرميل الحالي ($)", 70.0, 120.0, 85.0)
    st.divider()
    st.header("⚙️ بيانات الحساسات")
    f_in = st.number_input("Inlet Flow (bbl/hr)", 4000)
    f_out = st.number_input("Outlet Flow (bbl/hr)", 3750)
    p_in = st.number_input("P-In (psi)", 1200)
    p_out = st.number_input("P-Out (psi)", 950)

# 3. المحرك المالي والهندسي
loss = f_in - f_out
loss_perc = (loss / f_in) * 100 if f_in > 0 else 0
financial_loss_hr = loss * oil_price
financial_loss_min = financial_loss_hr / 60
leak_loc = (p_out / p_in) * 100 if loss > 0 else 0

# 4. عرض مؤشرات الكارثة (Metrics)
st.markdown("---")
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("معدل التسريب", f"{loss} bbl/hr", delta=f"{loss_perc:.1f}%", delta_color="inverse")
with m2:
    st.metric("نزيف الأرباح/ساعة", f"${financial_loss_hr:,.2f}", delta="خسارة مادية", delta_color="inverse")
with m3:
    st.metric("خسارة كل دقيقة", f"${financial_loss_min:,.2f}")
with m4:
    status = "🔴 CRITICAL" if loss_perc > 2 else "🟢 STABLE"
    st.metric("الوضع الحالي", status)

# 5. التتبع الجغرافي والألياف الضوئية
st.markdown("---")
c1, c2 = st.columns([1, 1])

with c1:
    st.subheader("📍 الموقع الجغرافي الدقيق")
    # إحداثيات افتراضية تتغير مع حجم التسريب
    df_map = pd.DataFrame({'lat': [30.044 + (loss*0.0001)], 'lon': [31.235 + (loss*0.0001)]})
    st.map(df_map, zoom=12 if loss > 0 else 8)
    

with c2:
    st.subheader("📡 بصمة الصوت (Fiber Optic Sensing)")
    x = np.linspace(0, 100, 500)
    noise = np.random.normal(5, 1, 500)
    if loss > 50:
        noise[int(leak_loc * 5)] += 20  # ذروة الصوت عند التسريب
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=noise, name="Acoustic Signal", line=dict(color='#ff0055', width=2)))
    fig.update_layout(title="تحليل ضوضاء التسريب على طول 100 كم", template="plotly_dark", height=300)
    st.plotly_chart(fig, use_container_width=True)
    

# 6. نظام الاستجابة للطوارئ
if loss > 0:
    st.divider()
    col_a, col_b = st.columns(2)
    with col_a:
        st.warning(f"⚠️ تنبيه: إذا استمر التسريب لمدة 24 ساعة، ستصل الخسائر إلى ${financial_loss_hr * 24:,.2f}")
    with col_b:
        if st.button("🔴 تفعيل الإغلاق الاضطراري (ESD) فوراً"):
            st.error("🚨 تم إرسال إشارة إغلاق المحابس المركزية.. تم إبلاغ فرق الطوارئ.")
            st.balloons()
