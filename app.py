import streamlit as st
import pandas as pd

# 1. إعداد واجهة الموبايل
st.set_page_config(page_title="Oil Master Pro", page_icon="⛽", layout="centered")

# 2. تنسيق الألوان
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #2ecc71; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("⛽ منصة التحليل المتكاملة")
st.write("مرحباً مهندس حمزة. أدخل الـ 20 معامل:")

# 3. مدخلات البيانات (20 معامل)
col1, col2 = st.columns(2)
with col1:
    v1 = st.number_input("1. العمق (ft)", value=7000)
    v2 = st.number_input("2. الضغط (psi)", value=2500)
    v3 = st.number_input("3. الحرارة (F)", value=190)
    v4 = st.number_input("4. المسامية (%)", value=18)
    v5 = st.number_input("5. النفاذية (md)", value=120)
    v6 = st.number_input("6. تشبع الماء", value=30)
    v7 = st.number_input("7. معامل Skin", value=0)
    v8 = st.number_input("8. سمك الطبقة", value=50)
    v9 = st.number_input("9. قطر البئر", value=8)
    v10 = st.number_input("10. زاوية الميل", value=0)
with col2:
    v11 = st.number_input("11. كثافة API", value=34)
    v12 = st.number_input("12. لزوجة الزيت", value=1.5)
    v13 = st.number_input("13. نسبة GOR", value=400)
    v14 = st.number_input("14. القطع المائي", value=10)
    v15 = st.number_input("15. ضغط الرأس", value=400)
    v16 = st.number_input("16. ضغط القاع", value=2000)
    v17 = st.number_input("17. حجم الخانق", value=32)
    v18 = st.number_input("18. كثافة الغاز", value=0.6)
    v19 = st.number_input("19. ملوحة الماء", value=40000)
    v20 = st.number_input("20. أيام الإنتاج", value=30)

if st.button("🚀 تحليل البيانات ورسم المخطط"):
    res = (v2 - v16) * (v5 / v12) * (v20 / 30)
    st.markdown("---")
    st.success(f"### الإنتاج المتوقع: {max(0, res):.2f} برميل/يوم")
    
    # 4. إضافة الرسم البياني (Bar Chart)
    st.write("📊 مخطط مقارنة أهم 5 معاملات:")
    # اخترنا أهم 5 معاملات عشان الرسمة تكون واضحة على الموبايل
    chart_data = pd.DataFrame({
        'المعامل': ['الضغط', 'الحرارة', 'المسامية', 'النفاذية', 'الماء'],
        'القيمة': [v2/100, v3, v4*5, v5, v6*2] # عملنا Scaling بسيط عشان الأعمدة تبان متناسقة
    }).set_index('المعامل')
    
    st.bar_chart(chart_data) # ده أمر الرسم البياني السريع والذكي

    # 5. الجدول التفصيلي
    labels = ["العمق", "الضغط", "الحرارة", "المسامية", "النفاذية", "تشبع الماء", "Skin", "السمك", "القطر", "الميل", "API", "اللزوجة", "GOR", "الماء", "ضغط الرأس", "ضغط القاع", "الخانق", "كثافة الغاز", "الملوحة", "الأيام"]
    vals = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20]
    st.table(pd.DataFrame({"المعامل": labels, "القيمة": vals}))
    st.balloons()
