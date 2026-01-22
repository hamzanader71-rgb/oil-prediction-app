import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import datetime

# --- 1. الحماية والتدمير (يومين) ---
EXPIRY_DATE = datetime.date(2026, 1, 24)
if datetime.date.today() > EXPIRY_DATE:
    st.error("🚨 انتهت صلاحية النسخة! تواصل مع المهندس حمزة لتجديد الاشتراك.")
    st.stop()

# كلمات السر
GUEST_PWD = "123"
ADMIN_PWD = "root"

if 'auth' not in st.session_state: st.session_state.auth = None

# --- 2. بوابة الدخول ---
if not st.session_state.auth:
    st.title("🛡️ Petro-Titan Secure Gateway")
    p = st.text_input("كود الدخول الموحد", type="password")
    if st.button("دخول"):
        if p == ADMIN_PWD: st.session_state.auth = "ADMIN"; st.rerun()
        elif p == GUEST_PWD: st.session_state.auth = "GUEST"; st.rerun()
        else: st.error("الكود غير صحيح")
else:
    # --- 3. إدارة القائمة (7 مفتوحين + 63 محجوبين) ---
    unlocked = ["🔮 توقعات الإنتاج", "🚨 فحص التسريب", "💰 حساب الأرباح", "🏗️ حسابات الحفر", "📈 كفاءة البئر", "🛡️ تقييم الأمان", "🌍 اللوحة العامة"]
    locked = [f"🔒 موديول محجوب {i}" for i in range(8, 71)]
    
    st.sidebar.header("🛰️ نظام التحكم")
    selection = st.sidebar.radio("اختر القسم:", unlocked + locked if st.session_state.auth == "GUEST" else unlocked + [l.replace("🔒 ", "") for l in locked])

    if "🔒" in selection:
        st.warning(f"### 🛑 {selection}")
        st.info("عذراً، هذا الموديول متاح فقط في النسخة المدفوعة (Enterprise).")
        st.image("https://cdn-icons-png.flaticon.com/512/2550/2550260.png", width=100)
    else:
        st.title(f"🚀 {selection}")
        st.divider()

        # --- 4. محرك الحسابات التفاعلي (الـ 7 صفحات) ---
        
        if selection == "🔮 توقعات الإنتاج":
            st.subheader("حساب التنبؤ بالشهر القادم")
            prod = st.number_input("الإنتاج الحالي (برميل/يوم)", value=1000)
            decline = st.slider("نسبة التراجع الطبيعي (%)", 0, 10, 2)
            # الحسبة النهائية
            result = prod * (1 - (decline/100))
            st.success(f"### 📊 الإنتاج المتوقع: {result:,.2f} برميل/يوم")
            
        elif selection == "🚨 فحص التسريب":
            st.subheader("اختبار هبوط الضغط")
            p_in = st.number_input("ضغط الدخول (PSI)", value=1500)
            p_out = st.number_input("ضغط الخروج (PSI)", value=1450)
            loss = p_in - p_out
            st.metric("الفقد في الضغط", f"{loss} PSI")
            if loss > 50:
                st.error("🚨 تنبيه: هبوط ضغط حاد! يوجد تسريب محتمل.")
            else:
                st.success("✅ حالة الأنبوب: مستقرة")

        elif selection == "💰 حساب الأرباح":
            st.subheader("حاسبة العائد المالي")
            qty = st.number_input("الكمية المباعة (برميل)", value=50000)
            price = st.number_input("سعر البرميل اليوم ($)", value=80)
            cost = st.number_input("تكلفة الاستخراج للبرميل ($)", value=25)
            # الحسبة النهائية
            profit = qty * (price - cost)
            st.info(f"### 💸 صافي الربح المتوقع: ${profit:,.2f}")

        elif selection == "🏗️ حسابات الحفر":
            st.subheader("حساب معدل الاختراق (ROP)")
            dist = st.number_input("المسافة المقطوعة (قدم)", value=500)
            time = st.number_input("الوقت المستغرق (ساعة)", value=10)
            if time > 0:
                rop = dist / time
                st.success(f"### ⚙️ معدل الاختراق: {rop:.2f} قدم/ساعة")

        elif selection == "📈 كفاءة البئر":
            st.subheader("حساب مؤشر الإنتاجية (PI)")
            q = st.number_input("معدل التدفق (STB/D)", value=500)
            p_drop = st.number_input("هبوط الضغط (Drawdown) PSI", value=200)
            if p_drop > 0:
                pi = q / p_drop
                st.metric("مؤشر الإنتاجية (PI)", f"{pi:.2f}")

        elif selection == "🛡️ تقييم الأمان":
            st.subheader("مؤشر السلامة المهنية")
            hours = st.number_input("إجمالي ساعات العمل بدون حوادث", value=10000)
            st.progress(min(hours/20000, 1.0))
            st.write(f"الموقع يعمل بأمان بنسبة {min(hours/200, 100):.1f}%")

        elif selection == "🌍 اللوحة العامة":
            st.write("ملخص البيانات التي تم إدخالها في الأقسام الأخرى...")
            st.info("هذه اللوحة تجمع لك النتائج النهائية لاتخاذ القرار.")

# خروج
st.sidebar.divider()
if st.sidebar.button("🔒 تسجيل الخروج"):
    st.session_state.auth = None
    st.rerun()
