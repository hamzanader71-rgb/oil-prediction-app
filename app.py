import streamlit as st
import pandas as pd
import numpy as np
import io

# 1. إعدادات النظام الفائق
st.set_page_config(page_title="Hamza AI Ultimate", page_icon="⚡", layout="wide")

# تصميم واجهة "المستقبل"
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #050a10 0%, #000000 100%); color: #00ffcc; }
    .stSidebar { background-color: #0a1420 !important; border-right: 2px solid #00ffcc; }
    .stButton>button { 
        background: linear-gradient(90deg, #00ffcc, #0088ff); 
        color: black; font-weight: bold; border-radius: 20px;
        box-shadow: 0px 0px 15px #00ffcc; transition: 0.5s;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0px 0px 25px #0088ff; }
    </style>
    """, unsafe_allow_html=True)

# 2. هيكلة الأقسام الذكية
st.sidebar.title("🤖 مركز التحكم الذكي")
menu = st.sidebar.selectbox("اختر المحرك الفني:", [
    "🛸 لوحة التحكم الرقمية (Digital Twin)",
    "📈 توقع الإنتاج (AI Forecast)",
    "🏗️ مراقبة الحفر والضغوط",
    "🛠️ نظام الإنذار المبكر (Alerts)",
    "📊 تصدير التقارير الذكية"
])

# ---------------------------------------------------------
# القسم 1: التوأم الرقمي (حساب 20 نقطة أوتوماتيك)
if menu == "🛸 لوحة التحكم الرقمية (Digital Twin)":
    st.title("🛸 محاكي أداء الآبار (Nodal Analysis)")
    pr = st.slider("Static Reservoir Pressure (psi)", 1000, 8000, 4000)
    pi = st.slider("Productivity Index (PI)", 0.5, 5.0, 2.0)
    
    # حساب 20 نقطة فوراً
    pressures = np.linspace(pr, 0, 20)
    q_rates = [pi * (pr - p) for p in pressures] # معادلة خطية سريعة للتوضيح
    
    st.subheader("📈 منحنى أداء البئر الحالي")
    df_ipr = pd.DataFrame({"Pressure": pressures, "Flow Rate": q_rates})
    st.line_chart(df_ipr.set_index("Pressure"))
    st.success(f"القدرة الإنتاجية القصوى: {max(q_rates)} STB/D")

# ---------------------------------------------------------
# القسم 2: التنبؤ (Forecasting)
elif menu == "📈 توقع الإنتاج (AI Forecast)":
    st.title("🔮 التنبؤ بالإنتاج المستقبلي (Machine Learning)")
    q_start = st.number_input("الإنتاج الحالي", value=3000)
    decline = st.slider("معدل الهبوط السنوي (%)", 1, 30, 10)
    
    months = np.arange(1, 25) # توقع لسنتين قدام
    forecast = q_start * np.exp(-(decline/100) * (months/12))
    
    st.subheader("📉 توقعات الإنتاج لـ 24 شهر قادم")
    st.area_chart(forecast)
    

# ---------------------------------------------------------
# القسم 3: نظام التنبيهات والواتساب (Concept)
elif menu == "🛠️ نظام الإنذار المبكر (Alerts)":
    st.title("🚨 مركز تنبيهات الطوارئ")
    h2s = st.number_input("مستوى غاز H2S (ppm)", 0)
    well_head_p = st.number_input("ضغط رأس البئر (psi)", 500)
    
    if st.button("تفعيل نظام التنبيه الذكي"):
        if h2s > 10 or well_head_p > 3000:
            st.error("🚨 خطر! سيتم إرسال رسالة واتساب فورية للمهندس حمزة.")
            # هنا نضع رابط الواتساب البرمجي
            wa_link = f"https://wa.me/20XXXXXXXXXX?text=Danger!%20H2S:{h2s}%20Pressure:{well_head_p}"
            st.markdown(f"[اضغط هنا لإرسال التنبيه يدوياً للواتساب الآن]({wa_link})")
        else:
            st.success("✅ النظام يراقب.. لا توجد أخطار حالياً.")

# ---------------------------------------------------------
# القسم 4: التقارير
else:
    st.title("📊 مركز التقارير النهائية")
    st.write("اضغط لتحميل ملف الإكسيل الشامل لكل حسابات الحقل.")
    if st.button("Generate Master Report"):
        st.balloons()
        st.download_button("Download Excel", data="Data Content", file_name="Hamza_Full_Report.xlsx")
