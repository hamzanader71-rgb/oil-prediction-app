import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import datetime

# --- 1. الحماية والتدمير (يومين) ---
EXPIRY_DATE = datetime.date(2026, 1, 24)
if datetime.date.today() > EXPIRY_DATE:
    st.error("🚨 License Expired! Contact Eng. Hamza")
    st.stop()

# --- 2. إعدادات الدخول ---
GUEST_PWD = "123"
ADMIN_PWD = "root"

if 'auth_level' not in st.session_state: st.session_state.auth_level = None

if not st.session_state.auth_level:
    st.title("🔒 Petro-Titan Login")
    pwd = st.text_input("Enter Key", type="password")
    if st.button("Unlock"):
        if pwd == ADMIN_PWD: st.session_state.auth_level = "ADMIN"; st.rerun()
        elif pwd == GUEST_PWD: st.session_state.auth_level = "GUEST"; st.rerun()
else:
    # --- 3. تصميم القائمة المتنوعة ---
    main_7 = ["🌍 لوحة التحكم", "🔮 تنبؤ AI", "🚨 مراقبة التسريب", "💰 مبيعات", "🏗️ حفر", "📈 أداء الإنتاج", "🛡️ أمان HSE"]
    selection = st.sidebar.selectbox("القسم العملياتي:", main_7 if st.session_state.auth_level == "GUEST" else main_7 + [f"موديول {i}" for i in range(8, 71)])

    st.title(f"🚀 {selection}")

    # --- 4. محرك البيانات المختلفة (هنا السر) ---
    col_data, col_viz = st.columns([1, 2])

    with col_data:
        st.markdown("### 🔢 قراءات حية")
        if selection == "🔮 تنبؤ AI":
            val = st.number_input("الإنتاج المستهدف (BPD)", 5000)
            st.metric("التوقع الدقيق", f"{val * 1.05:,.0f}", "+5%")
            st.write("**الحالة:** نمو مستمر")
            
        elif selection == "🚨 مراقبة التسريب":
            p1 = st.number_input("الضغط الرئيسي (psi)", 1500)
            p2 = st.number_input("الضغط الفرعي (psi)", 1480)
            st.metric("فقد الضغط", f"{p1-p2} psi", delta_color="inverse")
            st.write("**النتيجة:** خطوط سليمة")

        elif selection == "🏗️ حفر":
            depth = st.number_input("العمق الحالي (ft)", 12000)
            rpm = st.number_input("سرعة الدوران (RPM)", 120)
            st.write(f"**تآكل الدقاق:** {depth/2000:.1f}%")

        else:
            v = st.number_input("القيمة الأساسية", 100)
            st.metric("القراءة", v)

    with col_viz:
        st.markdown("### 📊 التحليل البصري")
        # كل صفحة ليها رسمة "شكلها" مختلف تماماً
        if selection == "🔮 تنبؤ AI":
            # رسمة "عداد" (Gauge)
            fig = go.Figure(go.Indicator(mode="gauge+number", value=92, title={'text': "دقة التنبؤ %"}, gauge={'bar': {'color': "#58a6ff"}}))
        
        elif selection == "🚨 مراقبة التسريب":
            # رسمة "حرارية" (Heatmap)
            fig = px.imshow([[1500, 1490, 1480], [1495, 1485, 1475]], title="خريطة ضغط الشبكة", color_continuous_scale="RdYlGn")
        
        elif selection == "🏗️ حفر":
            # رسمة "أعمدة" رأسية للأعماق
            fig = px.bar(x=["Surface", "Intermediate", "Production"], y=[3000, 8000, 12000], title="تصميم البئر")
            
        else:
            # رسمة "كيرف" عادي
            fig = px.line(y=np.random.randint(10, 100, 10), title="اتجاه البيانات العام")

        fig.update_layout(template="plotly_dark", height=350)
        st.plotly_chart(fig, use_container_width=True)

# زر الخروج
st.sidebar.markdown("---")
if st.sidebar.button("🔒 تسجيل الخروج"):
    st.session_state.auth_level = None; st.rerun()
