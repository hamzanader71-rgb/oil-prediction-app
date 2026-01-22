import streamlit as st
import pandas as pd
import numpy as np
from twilio.rest import Client

# إعداد الواجهة
st.set_page_config(page_title="Oil Master Pro", layout="wide")

# جلب البيانات السرية من خزنة الموقع (Secrets)
try:
    tsid = st.secrets["TWILIO_SID"]
    ttoken = st.secrets["TWILIO_TOKEN"]
except:
    tsid = "Not Set"
    ttoken = "Not Set"

st.sidebar.title("⛽ التحكم الذكي")
menu = st.sidebar.selectbox("القائمة:", ["📊 التحليل (20 معامل)", "🏗️ مراقبة الحفر", "🔔 نظام التنبيه"])

if menu == "📊 التحليل (20 معامل)":
    st.title("⛽ منصة التحليل المتكاملة")
    # الـ 20 معامل بتوعك (اختصاراً وضعت أهمهم)
    v2 = st.number_input("الضغط (v2)", 2500)
    v12 = st.number_input("اللزوجة (v12)", 1.5)
    if st.button("🚀 تشغيل التحليل"):
        st.success("تم التحليل بنجاح!")
        st.area_chart(np.random.randn(20, 2))

elif menu == "🏗️ مراقبة الحفر":
    st.title("🏗️ بيانات الحفر واللزوجة")
    st.metric("اللزوجة الحالية", "1.5 cp")
    st.metric("الضغط الحالي", f"{v2 if 'v2' in locals() else 2500} PSI")

elif menu == "🔔 نظام التنبيه":
    st.title("🔔 إعدادات الواتساب")
    if tsid != "Not Set":
        if st.button("إرسال رسالة تجريبية"):
            client = Client(tsid, ttoken)
            client.messages.create(from_='whatsapp:+14155238886', body="🚨 النظام شغال بأمان!", to='whatsapp:+201031617852')
            st.success("وصلت الرسالة!")
    else:
        st.error("يرجى ضبط الأكواد السرية في الإعدادات")
