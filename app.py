import streamlit as st
import pandas as pd

# إعدادات التطبيق الاحترافي
st.set_page_config(page_title="Oil Expert Pro", page_icon="⛽", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #28a745; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("⛽ نظام خبير البترول")
st.write("مرحباً مهندس حمزة، أدخل بيانات البئر:")

# مدخلات الموبايل
p = st.number_input("الضغط الحالي (PSI)", value=1200)
t = st.number_input("درجة الحرارة (F)", value=160)
d = st.slider("العمق الإجمالي (قدم)", 1000, 10000, 5000)

if st.button("🚀 ابدأ تحليل التوقع"):
    # معادلة التوقع
    res = (p * 0.45) + (t * 0.25) - (d * 0.02)
    
    st.markdown("---")
    st.success(f"### الإنتاج المقدر: {max(0, res):.2f} برميل/يوم")
    
    # إضافة جدول بيانات بسيط (ميزة احترافية)
    st.write("📊 ملخص البيانات الفنية:")
    df_result = pd.DataFrame({
        "المعامل": ["الضغط", "الحرارة", "العمق"],
        "القيمة": [p, t, d]
    })
    st.table(df_result)
    st.pyplot(fig)
