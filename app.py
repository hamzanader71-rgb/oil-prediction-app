import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hamza Oil Pro", page_icon="⛽", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .stButton>button { width: 100%; border-radius: 12px; background-color: #2ecc71; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ منصة المهندس حمزة المتكاملة")

# --- الخيار الأول: رفع ملف Excel ---
st.subheader("📊 أولاً: تحليل ملفات الإكسيل")
uploaded_file = st.file_uploader("ارفع ملف البيانات هنا", type=["xlsx", "csv"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith('.xlsx') else pd.read_csv(uploaded_file)
    st.success("✅ تم قراءة الملف")
    st.dataframe(df.head(5)) # عرض عينة من البيانات
    if st.button("تحليل بيانات الملف"):
        st.line_chart(df.iloc[:, 1]) # رسم بياني لأول عمود بيانات
        st.balloons()

st.markdown("---")

# --- الخيار الثاني: الإدخال اليدوي (موجود دائماً) ---
with st.expander("📝 ثانياً: الإدخال اليدوي (20 معامل)", expanded=False):
    st.write("أدخل البيانات يدوياً في حالة عدم توفر ملف:")
    col1, col2 = st.columns(2)
    with col1:
        v1=st.number_input("1. العمق", 7000); v2=st.number_input("2. الضغط", 2500)
        # ... (باقي المعاملات)
    with col2:
        v11=st.number_input("11. API", 34); v12=st.number_input("12. اللزوجة", 1.5)
        # ... (باقي المعاملات)
    
    if st.button("🚀 تحليل الإدخال اليدوي"):
        res = (v2 * 0.5) + (v11 * 2) # معادلة سريعة
        st.success(f"النتيجة اليدوية: {res:.2f}")
        st.balloons()
