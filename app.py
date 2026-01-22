import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- 1. الإعدادات والستايل ---
st.set_page_config(page_title="Petro-Oracle Live V27", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .status-card { background: #161b22; border-radius: 10px; padding: 15px; border-left: 5px solid #58a6ff; margin-bottom: 20px; }
    .metric-text { font-size: 20px; font-weight: bold; color: #58a6ff; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. إدارة الـ 30 صفحة (المنظومة الكاملة) ---
sections = [
    "الرئيسية", "الاستكشاف", "المسح السيزمي", "تقييم الطبقات", "هندسة الحفر", 
    "سوائل الحفر", "السمتة", "إكمال الآبار", "البتوفيزياء", "تحليل السجلات",
    "هندسة الخزانات", "نمذجة الخزانات", "اختبارات الآبار", "توقعات الإنتاج", "تحليل الهبوط DCA",
    "الرفع الصناعي ESP", "الرفع بالغاز", "المضخات", "كشف التسريب", "سلامة الأنابيب",
    "معالجة الخام", "معالجة الغاز", "فصل المياه", "التخزين والشحن", "المبيعات",
    "التحليل المالي", "إدارة المخاطر", "الأمن والسلامة", "الذكاء الاصطناعي", "الإعدادات"
]

selection = st.sidebar.selectbox("🚀 انتقل إلى القسم التخصصي:", sections)

# --- 3. بوابة الدخول ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<h2 style='text-align:center;'>🔑 نظام الوصول العالمي</h2>", unsafe_allow_html=True)
    if st.text_input("Security Key", type="password") == "root":
        if st.button("دخول"): 
            st.session_state.auth = True
            st.rerun()
else:
    st.title(f"🛠️ وحدة: {selection}")
    
    # --- 4. محرك البيانات المتقدم (إدخال يدوي + معالجة فورية) ---
    col_input, col_graph = st.columns([1, 2])

    with col_input:
        st.markdown("<div class='status-card'>", unsafe_allow_html=True)
        st.subheader("📥 إدخال البيانات الحية")
        
        # أرقام حقيقية يدخلها المستخدم
        p_val = st.number_input("الضغط الفعلي (PSI)", min_value=0.0, key=f"p_{selection}")
        q_val = st.number_input("الإنتاج/المعدل الفعلي (BPD)", min_value=0.0, key=f"q_{selection}")
        temp_val = st.number_input("درجة الحرارة (F)", min_value=0.0, key=f"t_{selection}")
        
        run = st.button("🔥 تحليل وعرض النتائج", key=f"run_{selection}")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # إضافات في كل الصفحات (الحالة العامة)
        st.info(f"🛡️ حالة السلامة في {selection}: مؤمن")
        st.warning(f"💰 التكلفة التشغيلية التقديرية: ${(p_val * 0.5 + q_val * 0.1):,.2f}")

    with col_graph:
        st.markdown("<div class='status-card'>", unsafe_allow_html=True)
        if run and (p_val > 0 or q_val > 0):
            st.subheader("📊 الرسم البياني التحليلي (بناءً على أرقامك)")
            
            # رسم بياني تفاعلي باستخدام Plotly يظهر أرقامك بدقة
            fig = go.Figure()
            fig.add_trace(go.Bar(name='الضغط (PSI)', x=[selection], y=[p_val], marker_color='#58a6ff'))
            fig.add_trace(go.Bar(name='الإنتاج (BPD)', x=[selection], y=[q_val], marker_color='#238636'))
            
            fig.update_layout(
                title=f"تحليل أداء وحدة {selection}",
                template="plotly_dark",
                barmode='group',
                yaxis_title="القيمة العددية"
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # عرض الأرقام في شكل كروت واضحة (Metrics)
            m1, m2, m3 = st.columns(3)
            m1.metric("الضغط المسجل", f"{p_val} psi")
            m2.metric("المعدل المسجل", f"{q_val} bpd")
            m3.metric("الكفاءة", f"{min(100.0, (q_val/5000)*100):.1f}%")
            
        else:
            st.info("💡 أدخل الأرقام في الخانات الجانبية واضغط 'تحليل' لعرض الرسم البياني الحي.")
        st.markdown("</div>", unsafe_allow_html=True)

    # --- 5. نظام التنبؤ وكشف التسريب المدمج في كل الصفحات ---
    if selection == "كشف التسريب" or selection == "سلامة الأنابيب":
        if p_val < 200 and p_val > 0:
            st.error("🚨 ALERT: انخفاض حاد في الضغط! احتمال تسريب كبير.")
        elif p_val >= 200:
            st.success("✅ الضغط ضمن النطاق الآمن للتشغيل.")

    # ميزة البحث (Search Dashboard)
    with st.sidebar.expander("🔍 محرك البحث السريع"):
        st.text_input("اكتب اسم الموديول للوصول السريع...")

# زر الخروج
st.sidebar.markdown("---")
if st.sidebar.button("🔒 تسجيل الخروج"):
    st.session_state.auth = False
    st.rerun()
