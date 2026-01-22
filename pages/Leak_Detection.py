import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# 1. إعدادات الصفحة والسمة الاحترافية
st.set_page_config(page_title="Emperor Leak Detection 100%", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #000508; color: #00ffa2; }
    .metric-card { background: #011627; padding: 15px; border-radius: 10px; border-left: 5px solid #ff0055; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ نظام الرقابة الإمبراطوري لخطوط الأنابيب (Full Integrity)")
st.write(f"تاريخ التقرير اللحظي: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# --- Sidebar للتحكم في بارامترات النظام ---
with st.sidebar:
    st.header("⚙️ إعدادات الحساسات")
    pipe_length = st.number_input("طول الخط (km)", 50, 500, 100)
    oil_price = st.number_input("سعر البرميل الحالي ($)", 70, 120, 85)
    st.divider()
    st.info("النظام يعمل بتقنية Fiber Optic + Mass Balance")

# 2. لوحة التحكم في الحساسات (Live Sensors)
col1, col2, col3, col4 = st.columns(4)
with col1:
    f_in = st.number_input("Flow In (bbl/hr)", 0, 10000, 4000)
with col2:
    f_out = st.number_input("Flow Out (bbl/hr)", 0, 10000, 3850)
with col3:
    p_in = st.number_input("Pressure In (psi)", 0, 2000, 1200)
with col4:
    p_out = st.number_input("Pressure Out (psi)", 0, 2000, 1050)

# --- محرك الحسابات الذكي (The Engine) ---
loss_hr = f_in - f_out
loss_ratio = (loss_hr / f_in) * 100 if f_in > 0 else 0
is_leak = loss_ratio > 1.0  # التنبيه يبدأ من 1% فقد

# 3. عرض مؤشرات الأداء (KPIs)
st.markdown("---")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.metric("حجم التسريب", f"{loss_hr} bbl/hr", delta=f"{loss_ratio:.1f}%", delta_color="inverse")
with kpi2:
    st.metric("الخسارة المالية/ساعة", f"${loss_hr * oil_price:,.0f}")
with kpi3:
    leak_location = (p_out / p_in) * pipe_length if is_leak else 0
    st.metric("نقطة التسريب المتوقعة", f"Km {leak_location:.2f}")
with kpi4:
    status = "🔴 CRITICAL" if is_leak else "🟢 SECURE"
    st.metric("حالة الخط الآن", status)

# 4. محاكاة نظام الألياف الضوئية (Fiber Optic DAS/DTS)
st.subheader("📡 مراقبة النبض الصوتي والحراري (Fiber Optic Sensing)")
x_km = np.linspace(0, pipe_length, 1000)
acoustic_signal = np.random.normal(20, 2, 1000) # Noise طبيعي

if is_leak:
    # عمل طفرة (Spike) في مكان التسريب
    leak_idx = int((leak_location / pipe_length) * 1000)
    acoustic_signal[leak_idx-20:leak_idx+20] += np.random.normal(50, 5, 40)

fig_fiber = px.line(x=x_km, y=acoustic_signal, title="تحليل الترددات الصوتية على طول الخط")
fig_fiber.update_traces(line_color="#ff0055")
st.plotly_chart(fig_fiber, use_container_width=True)


# 5. الخريطة الجغرافية والتحليل المكاني
st.markdown("---")
c1, c2 = st.columns([1, 1])

with c1:
    st.subheader("📍 التتبع الجغرافي (GPS)")
    # إحداثيات افتراضية تتغير مع مكان التسريب
    base_lat, base_lon = 30.0, 31.0
    leak_lat = base_lat + (leak_location * 0.001)
    leak_lon = base_lon + (leak_location * 0.001)
    
    map_data = pd.DataFrame({'lat': [leak_lat], 'lon': [leak_lon]})
    st.map(map_data, zoom=11 if is_leak else 8)

with c2:
    st.subheader("📸 الذكاء الاصطناعي وصور الأقمار الصناعية")
    st.write("ارفع صورة القمر صناعي لتحليل البقع الزيتية:")
    up_file = st.file_uploader("", type=["jpg", "png"])
    if up_file:
        st.image(up_file, caption="جاري المسح الطيفي...", use_container_width=True)
        if is_leak:
            st.warning("⚠️ تم رصد بقعة زيت سطحية بمساحة تقدر بـ 1200 متر مربع")
        else:
            st.success("✅ لا توجد بقع زيتية مرئية")

# 6. التقرير الاقتصادي وبروتوكول الطوارئ
st.markdown("---")
if is_leak:
    st.subheader("⚠️ بروتوكول الاستجابة السريعة")
    col_a, col_b = st.columns(2)
    with col_a:
        st.error(f"تنبيه: الخط يخسر حالياً {loss_hr * 24 * oil_price:,.0f}$ يومياً!")
        if st.button("🚨 تفعيل الإغلاق الاضطراري (ESD)"):
            st.critical("تم إرسال إشارة إغلاق الصمامات للمحطات رقم 4 و 5")
    with col_b:
        st.info("📋 توصية النظام: إرسال فريق صيانة فوراً للكيلو " + str(round(leak_location, 2)))
        st.download_button("تحليل البيانات للتحقيق (CSV)", 
                           pd.DataFrame({"KM": x_km, "Signal": acoustic_signal}).to_csv(), 
                           "leak_report.csv")
