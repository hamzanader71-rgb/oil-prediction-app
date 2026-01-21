import streamlit as st
import pandas as pd
import numpy as np

# إعداد واجهة الموبايل
st.set_page_config(page_title="Oil Master Pro", page_icon="⛽", layout="centered")

# تنسيق الألوان
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #2ecc71; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("⛽ منصة التحليل المتكاملة")
st.write("أدخل الـ 20 معامل لتوليد الرسم البياني:")

# مدخلات البيانات (الـ 20 معامل) بنفس الترتيب
col1, col2 = st.columns(2)
with col1:
    v1=st.number_input("1. العمق", 7000); v2=st.number_input("2. الضغط", 2500); v3=st.number_input("3. الحرارة", 190); v4=st.number_input("4. المسامية", 18); v5=st.number_input("5. النفاذية", 120)
    v6=st.number_input("6. تشبع الماء", 30); v7=st.number_input("7. Skin", 0); v8=st.number_input("8. السمك", 50); v9=st.number_input("9. القطر", 8); v10=st.number_input("10. الميل", 0)
with col2:
    v11=st.number_input("11. API", 34); v12=st.number_input("12. اللزوجة", 1.5); v13=st.number_input("13. GOR", 400); v14=st.number_input("14. الماء", 10); v15=st.number_input("15. ضغط الرأس", 400)
    v16=st.number_input("16. ضغط القاع", 2000); v17=st.number_input("17. الخانق", 32); v18=st.number_input("18. كثافة الغاز", 0.6); v19=st.number_input("19. الملوحة", 40000); v20=st.number_input("20. الأيام", 30)

if st.button("🚀 تحليل البيانات ورسم المخطط"):
    res = (v2 - v16) * (v5 / v12) * (v20 / 30)
    st.markdown("---")
    st.success(f"### الإنتاج المتوقع: {max(0, res):.2f} STB/D")
    
    # --- قسم الرسم البياني المضمون ---
    st.subheader("📈 مخطط توزيع الضغوط والحرارة")
    
    # سنرسم منحنى يوضح العلاقة بين الضغط والعمق بشكل افتراضي
    chart_data = pd.DataFrame(
        np.random.randn(20, 2) + [v2/1000, v3/100], # بيانات مبنية على مدخلاتك
        columns=['الضغط الموزع', 'الحرارة النسبية']
    )
    st.area_chart(chart_data) # هذا النوع يظهر بوضوح فوراً على الموبايل
    
    # الجدول التفصيلي
    labels = ["العمق", "الضغط", "الحرارة", "المسامية", "النفاذية", "الماء", "Skin", "السمك", "القطر", "الميل", "API", "اللزوجة", "GOR", "الماء", "ضغط الرأس", "ضغط القاع", "الخانق", "كثافة الغاز", "الملوحة", "الأيام"]
    vals = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20]
    st.table(pd.DataFrame({"المعامل": labels, "القيمة": vals}))
    st.balloons()
