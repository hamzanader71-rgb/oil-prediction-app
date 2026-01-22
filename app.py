import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px # للمخططات التفاعلية

# 1. إعدادات المنصة الاحترافية
st.set_page_config(page_title="Hamza Oilfield AI", page_icon="🛢️", layout="wide")

# تصميم واجهة المستقبل (UI/UX)
st.markdown("""
    <style>
    .stApp { background: #050a10; color: #00ffcc; }
    .stSidebar { background-color: #0a1420 !important; border-right: 2px solid #00ffcc; }
    .stMetric { background-color: #0e1621; padding: 15px; border-radius: 15px; border: 1px solid #00ffcc; box-shadow: 0px 0px 10px #00ffcc; }
    .stButton>button { 
        background: linear-gradient(90deg, #00ffcc, #0088ff); 
        color: black; font-weight: bold; border-radius: 20px;
        box-shadow: 0px 0px 15px #00ffcc; width: 100%; transition: 0.5s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0px 0px 25px #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية المتكاملة
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2933/2933833.png", width=100)
    st.title("🤖 Hamza AI Center")
    menu = st.radio("انتقل إلى:", [
        "📊 منصة التحليل (20 معامل)",
        "🔮 التنبؤ بالإنتاج (AI Forecast)",
        "🏗️ مراقبة الحفر واللزوجة",
        "🌡️ توقع ضغط الطبقات (Pore Pressure)",
        "⚙️ محول الوحدات الهندسي",
        "📂 مركز التقارير الذكية"
    ])

# --- القسم 1: الـ 20 معامل ---
if menu == "📊 منصة التحليل (20 معامل)":
    st.title("⛽ منصة تحليل المكامن (Reservoir Analysis)")
    col1, col2 = st.columns(2)
    with col1:
        v1=st.number_input("العمق (ft)", 7000); v2=st.number_input("الضغط (psi)", 2500)
        v3=st.number_input("الحرارة (°F)", 190); v5=st.number_input("النفاذية (mD)", 120)
    with col2:
        v12=st.number_input("اللزوجة (cp)", 1.5); v16=st.number_input("ضغط القاع (BHP)", 2000)
        v20=st.number_input("عدد الأيام", 30)

    if st.button("🚀 تشغيل المحاكي الرقمي"):
        res = (v2 - v16) * (v5 / v12) * (v20 / 30)
        st.success(f"الإنتاج الحالي المحسوب: {max(0, res):.2f} STB/D")
        st.balloons()

# --- القسم 2: التنبؤ بالمستقبل (AI Forecast) ---
elif menu == "🔮 التنبؤ بالإنتاج (AI Forecast)":
    st.title("🔮 التنبؤ بمنحنى الإنتاج (Decline Curve)")
    qi = st.number_input("الإنتاج الابتدائي (Initial Production)", value=2000)
    decline_rate = st.slider("معدل الهبوط السنوي (%)", 1, 50, 15)
    years = st.slider("سنوات التوقع", 1, 10, 5)

    # معادلة التنبؤ (Exponential Decline)
    time_range = np.arange(0, years * 12)
    q_forecast = qi * np.exp(-(decline_rate/100) * (time_range/12))
    
    df_forecast = pd.DataFrame({"الشهر": time_range, "الإنتاج المتوقع": q_forecast})
    fig = px.area(df_forecast, x="الشهر", y="الإنتاج المتوقع", title="توقع إنتاج البئر للسنوات القادمة")
    st.plotly_chart(fig, use_container_width=True)
    st.info(f"إجمالي الإنتاج التراكمي المتوقع: {int(q_forecast.sum())} برميل")

# --- القسم 3: مراقبة الحفر واللزوجة ---
elif menu == "🏗️ مراقبة الحفر واللزوجة":
    st.title("🏗️ مراقبة بارامترات الحفر المباشرة")
    c1, c2, c3 = st.columns(3)
    c1.metric("Viscosity (اللزوجة)", "45 cp", "+2")
    c2.metric("Mud Weight", "9.8 ppg", "-0.1")
    c3.metric("ROP (سرعة الحفر)", "120 ft/hr")
    
    st.write("---")
    st.subheader("📊 مراقبة الضغط والاهتزاز")
    st.line_chart(np.random.randint(2400, 2600, 24))

# --- القسم 4: محول الوحدات الهندسي ---
elif menu == "⚙️ محول الوحدات الهندسي":
    st.title("⚙️ محول وحدات الحقل")
    val = st.number_input("أدخل القيمة:", value=1.0)
    unit_type = st.selectbox("من:", ["PSI to Bar", "Feet to Meter", "BBL to M3"])
    
    if unit_type == "PSI to Bar":
        st.write(f"النتيجة: {val * 0.0689:.4f} Bar")
    elif unit_type == "Feet to Meter":
        st.write(f"النتيجة: {val * 0.3048:.4f} Meter")
    elif unit_type == "BBL to M3":
        st.write(f"النتيجة: {val * 0.1589:.4f} M3")

# --- القسم 5: التقارير ---
else:
    st.title("📂 مركز التقارير الذكية")
    st.write("تجميع كافة البيانات الحالية في تقرير واحد.")
    if st.button("Generate Master PDF Report"):
        st.snow()
        st.success("جاري تصدير التقرير النهائي...")
