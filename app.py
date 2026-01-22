import streamlit as st
import pandas as pd
import numpy as np
from twilio.rest import Client

# 1. إعدادات النظام الفائق
st.set_page_config(page_title="Hamza AI Ultimate", page_icon="⚡", layout="wide")

# تصميم واجهة "المستقبل"
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #050a10 0%, #000000 100%); color: #00ffcc; }
    .stSidebar { background-color: #0a1420 !important; border-right: 2px solid #00ffcc; }
    .stMetric { background-color: #0e1621; padding: 10px; border-radius: 15px; border: 1px solid #00ffcc; }
    .stButton>button { 
        background: linear-gradient(90deg, #00ffcc, #0088ff); 
        color: black; font-weight: bold; border-radius: 20px;
        box-shadow: 0px 0px 15px #00ffcc; transition: 0.5s; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# جلب بيانات تويليو السرية من إعدادات Streamlit (Secrets)
try:
    TWILIO_SID = st.secrets["TWILIO_SID"]
    TWILIO_TOKEN = st.secrets["TWILIO_TOKEN"]
except:
    TWILIO_SID = "None"
    TWILIO_TOKEN = "None"

# 2. هيكلة الأقسام الذكية
st.sidebar.title("🤖 مركز التحكم الذكي")
menu = st.sidebar.selectbox("اختر المحرك الفني:", [
    "📊 منصة التحليل (20 معامل)",
    "🏗️ مراقبة الحفر واللزوجة",
    "📈 توقع الإنتاج (AI Forecast)",
    "🚨 نظام الإنذار المبكر (Alerts)",
    "📊 تصدير التقارير"
])

# ---------------------------------------------------------
# القسم 1: الـ 20 معامل (تعديلك الأساسي)
if menu == "📊 منصة التحليل (20 معامل)":
    st.title("⛽ منصة التحليل (20 Parameter Analysis)")
    
    col1, col2 = st.columns(2)
    with col1:
        v1=st.number_input("1. العمق", 7000); v2=st.number_input("2. الضغط (PSI)", 2500)
        v3=st.number_input("3. الحرارة", 190); v4=st.number_input("4. المسامية", 18)
        v5=st.number_input("5. النفاذية", 120); v6=st.number_input("6. تشبع الماء", 30)
    with col2:
        v12=st.number_input("12. اللزوجة (cp)", 1.5); v16=st.number_input("16. ضغط القاع", 2000)
        v20=st.number_input("20. الأيام", 30)
        # (باقي المعاملات تضاف هنا بنفس الطريقة)

    if st.button("🚀 تشغيل المحاكاة الذكية"):
        res = (v2 - v16) * (v5 / v12) * (v20 / 30)
        st.success(f"### الإنتاج المتوقع: {max(0, res):.2f} STB/D")
        st.area_chart(np.random.randn(20, 2) + [v2/1000, 2])
        st.balloons()

# ---------------------------------------------------------
# القسم 2: مراقبة الحفر (اللزوجة والضغوط)
elif menu == "🏗️ مراقبة الحفر والضغوط":
    st.title("🏗️ مراقبة بارامترات الحفر المباشرة")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Viscosity (اللزوجة)", "45 cp", "+2")
    c2.metric("Mud Weight", "9.8 ppg")
    c3.metric("ROP (سرعة الحفر)", "110 ft/hr", "-5")
    
    st.subheader("📈 مخطط الضغط أثناء الحفر")
    st.line_chart(np.random.randint(2400, 2600, 24))

# ---------------------------------------------------------
# القسم 3: نظام التنبيهات (الواتساب التلقائي)
elif menu == "🚨 نظام الإنذار المبكر (Alerts)":
    st.title("🚨 مركز تنبيهات الطوارئ الذكي")
    current_p = st.number_input("أدخل الضغط الحالي للمراقبة", value=2500)
    
    if st.button("تفعيل الرصد والإرسال"):
        if current_p > 3000:
            st.error(f"🚨 خطر! الضغط وصل لـ {current_p}. جاري إرسال واتساب...")
            if TWILIO_SID != "None":
                try:
                    client = Client(TWILIO_SID, TWILIO_TOKEN)
                    client.messages.create(
                        from_='whatsapp:+14155238886',
                        body=f"⚠️ تنبيه من منصة حمزة: الضغط مرتفع جداً ({current_p} PSI) في بئر رقم 1",
                        to='whatsapp:+201031617852'
                    )
                    st.success("✅ تم إرسال رسالة الواتساب بنجاح!")
                except Exception as e:
                    st.warning(f"فشل الإرسال التلقائي: {e}")
            else:
                st.info("يرجى ضبط SID و Token في إعدادات Secrets")
        else:
            st.success("✅ الضغط في الحدود الآمنة.")

# ---------------------------------------------------------
else:
    st.title("📊 مركز التقارير")
    st.write("إصدار تقرير شامل بصيغة Excel")
    st.button("تحميل التقرير النهائي")
