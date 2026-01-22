import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime

# --- 1. حماية وتدمير (يومين) ---
EXPIRY_DATE = datetime.date(2026, 1, 24)
if datetime.date.today() > EXPIRY_DATE:
    st.error("🚨 License Expired! Contact Eng. Hamza")
    st.stop()

# --- 2. الدخول والخصوصية ---
GUEST_PWD = "123"
ADMIN_PWD = "root"
if 'auth' not in st.session_state: st.session_state.auth = None

if not st.session_state.auth:
    st.title("🔐 Petro-Titan Gate")
    p = st.text_input("Security Key", type="password")
    if st.button("Access"):
        if p == ADMIN_PWD: st.session_state.auth = "ADMIN"; st.rerun()
        elif p == GUEST_PWD: st.session_state.auth = "GUEST"; st.rerun()
else:
    # --- 3. بناء القائمة ---
    main_7 = ["🌍 التحكم العام", "🔮 توقعات AI", "🚨 كشف التسريب", "💰 المالية", "🏗️ عمليات الحفر", "📈 تحليل الأداء", "🛡️ السلامة HSE"]
    selection = st.sidebar.radio("قائمة الموديولات:", main_7 if st.session_state.auth == "GUEST" else main_7 + [f"موديول {i}" for i in range(8, 71)])

    st.markdown(f"## 🚀 {selection}")
    st.divider()

    # --- 4. تخصيص "شكل" كل صفحة ---
    
    if selection == "🌍 التحكم العام":
        # شكل: كروت معلومات كبيرة ورسم بياني عريض
        c1, c2, c3 = st.columns(3)
        c1.metric("إجمالي الإنتاج", "150K bpd", "+2k")
        c2.metric("السعر العالمي", "$82.5", "-0.5")
        c3.metric("الآبار النشطة", "45", "Stable")
        fig = px.area(y=np.random.randint(100, 200, 20), title="إنتاج الحقل الكلي", color_discrete_sequence=['#58a6ff'])
        st.plotly_chart(fig, use_container_width=True)

    elif selection == "🔮 توقعات AI":
        # شكل: عداد دائري (Gauge) وتنبؤ مستقبلي
        col_a, col_b = st.columns([1, 1])
        with col_a:
            fig = go.Figure(go.Indicator(mode="gauge+number", value=85, title={'text': "دقة التنبؤ %"}, gauge={'bar':{'color':"purple"}}))
            st.plotly_chart(fig, use_container_width=True)
        with col_b:
            st.write("### 🤖 تقرير AI")
            st.info("بناءً على تحليلات الشهر الماضي، نتوقع زيادة الإنتاج بنسبة 8% في بئر رقم 4.")
            st.progress(85)

    elif selection == "🚨 كشف التسريب":
        # شكل: خريطة حرارية (Heatmap) بالألوان
        st.write("### 🌡️ خريطة ضغط الأنابيب اللحظية")
        data = np.random.rand(5, 10)
        fig = px.imshow(data, labels=dict(x="نقطة الفحص", y="الخط الرئيسي", color="الضغط"), color_continuous_scale='RdYlGn')
        st.plotly_chart(fig, use_container_width=True)
        if st.button("بدء فحص الحساسات"): st.warning("جاري المسح... لا يوجد تسريب.")

    elif selection == "💰 المالية":
        # شكل: ميزانية وجدول بيانات (Donut Chart)
        col1, col2 = st.columns([1, 2])
        with col1:
            fig = px.pie(names=['أرباح', 'تشغيل', 'صيانة'], values=[60, 25, 15], hole=0.5, title="توزيع الميزانية")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write("### 📝 سجل المبيعات")
            df = pd.DataFrame({'الشحنة': ['A', 'B', 'C'], 'القيمة': ['$1M', '$2.5M', '$0.8M'], 'الحالة': ['تمت', 'معلقة', 'تمت']})
            st.table(df)

    elif selection == "🏗️ عمليات الحفر":
        # شكل: أعمدة رأسية (Bar Chart) للأعماق
        st.write("### ⚙️ بيانات الحفر والطبقات")
        depths = pd.DataFrame({'الطبقة': ['Surface', 'Shale', 'Sand', 'Reservoir'], 'العمق (ft)': [2000, 5000, 9000, 13000]})
        fig = px.bar(depths, x='الطبقة', y='العمق (ft)', color='العمق (ft)', title="تصميم البئر الحالي")
        st.plotly_chart(fig, use_container_width=True)

    elif selection == "📈 تحليل الأداء":
        # شكل: نقط تفاعلية (Scatter Plot) لمقارنة الآبار
        st.write("### ⚖️ مقارنة أداء الآبار (الضغط مقابل التدفق)")
        wells = pd.DataFrame({'Press': np.random.randint(1000, 3000, 10), 'Flow': np.random.randint(100, 500, 10), 'Well': [f"Well {i}" for i in range(10)]})
        fig = px.scatter(wells, x='Press', y='Flow', text='Well', size='Flow', color='Well', title="مصفوفة الآبار")
        st.plotly_chart(fig, use_container_width=True)

    elif selection == "🛡️ السلامة HSE":
        # شكل: مؤشرات أداء (Progress Bars) ورسم راداري
        st.write("### 📋 مؤشرات السلامة والصحة المهنية")
        st.write("نظافة الموقع")
        st.progress(95)
        st.write("الالتزام بمهمات الوقاية")
        st.progress(100)
        st.write("سرعة الاستجابة للطوارئ")
        st.progress(80)
        st.success("✅ الموقع آمن تماماً اليوم")

# خروج
st.sidebar.divider()
if st.sidebar.button("🔒 خروج"): st.session_state.auth = None; st.rerun()
