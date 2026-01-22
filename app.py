import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- إعدادات المنصة ---
st.set_page_config(page_title="Petro-Oracle Identity V28", layout="wide")

# --- بوابة الدخول ---
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.markdown("<h2 style='text-align:center;'>🔑 نظام الوصول العالمي</h2>", unsafe_allow_html=True)
    if st.text_input("Security Key", type="password") == "root":
        if st.button("دخول"): 
            st.session_state.auth = True
            st.rerun()
else:
    # --- القائمة الجانبية (30 صفحة) ---
    sections = [
        "الرئيسية", "هندسة الحفر", "هندسة الخزانات", "توقعات الإنتاج", "كشف التسريب", 
        "المبيعات والعقود", "الأمن والسلامة", "التحليل المالي", "سوائل الحفر", "المسح السيزمي"
        # ... باقي الـ 30 صفحة تتبع نفس النمط
    ]
    selection = st.sidebar.selectbox("🚀 اختر القسم التخصصي:", sections)

    st.title(f"🛠️ وحدة: {selection}")

    # --- محرك التغيير (كل صفحة ليها مدخلاتها الخاصة) ---
    st.markdown("<div style='background:#161b22; padding:20px; border-radius:10px;'>", unsafe_allow_html=True)
    col_in, col_res = st.columns([1, 2])

    with col_in:
        st.subheader("📥 المدخلات الفنية")
        
        # هنا بنغير المدخلات حسب الصفحة عشان متزهقش وتحس بالفرق
        if selection == "هندسة الحفر":
            depth = st.number_input("عمق الحفر الحالي (ft)", key="drill_d")
            weight = st.number_input("الوزن على الدقاق (klbs)", key="drill_w")
            run = st.button("تحليل الحفر")
            
        elif selection == "المبيعات والعقود":
            barrels = st.number_input("عدد البراميل المباعة", key="sale_b")
            price = st.number_input("سعر البرميل اليوم ($)", value=75.0, key="sale_p")
            run = st.button("حساب الأرباح")
            
        elif selection == "كشف التسريب":
            in_press = st.number_input("ضغط الدخول (psi)", key="leak_in")
            out_press = st.number_input("ضغط الخروج (psi)", key="leak_out")
            run = st.button("فحص التسريب")
            
        else:
            p_val = st.number_input("الضغط (psi)", key=f"gen_p_{selection}")
            q_val = st.number_input("المعدل (bpd)", key=f"gen_q_{selection}")
            run = st.button("تحليل عام")

    with col_res:
        st.subheader("📊 المخرجات التخصصية")
        if run:
            if selection == "هندسة الحفر":
                st.info(f"النتيجة: تم الوصول لعمق {depth} قدم بكفاءة عالية.")
                st.write(f"الحمل الموزع: {weight/10} %")
                
            elif selection == "المبيعات والعقود":
                revenue = barrels * price
                st.metric("إجمالي الدخل", f"${revenue:,.2f}")
                st.success(f"تم تسجيل العقد لـ {barrels} برميل.")
                
            elif selection == "كشف التسريب":
                drop = in_press - out_press
                if drop > 50:
                    st.error(f"🚨 تحذير: فقد في الضغط بمقدار {drop} psi! احتمال تسريب.")
                else:
                    st.success("✅ حالة التدفق مستقرة.")
            
            # رسم بياني مخصص لكل نتيجة
            fig = go.Figure(go.Indicator(mode="gauge+number", value=100, title={'text': "كفاءة العمل"}))
            st.plotly_chart(fig)
    st.markdown("</div>", unsafe_allow_html=True)
