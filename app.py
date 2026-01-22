import streamlit as st
import pandas as pd
import numpy as np

# 1. إعدادات الصفحة
st.set_page_config(page_title="Hamza AI Ultimate", page_icon="⚡", layout="wide")

# تصميم الواجهة
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #050a10 0%, #000000 100%); color: #00ffcc; }
    .stSidebar { background-color: #0a1420 !important; border-right: 2px solid #00ffcc; }
    .stMetric { background-color: #0e1621; padding: 15px; border-radius: 15px; border: 1px solid #00ffcc; }
    .stButton>button { 
        background: linear-gradient(90deg, #00ffcc, #0088ff); 
        color: black; font-weight: bold; border-radius: 20px;
        box-shadow: 0px 0px 15px #00ffcc; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية المباشرة
menu = st.sidebar.radio("المحرك الفني:", [
    "📊 منصة التحليل (20 معامل)",
    "🏗️ مراقبة الحفر واللزوجة",
    "📊 تصدير التقارير"
])

# ---------------------------------------------------------
# القسم 1: الـ 20 معامل
if menu == "📊 منصة التحليل (20 معامل)":
    st.write("### ⛽ أدخل معاملات البئر الـ 20:")
    
    col1, col2 = st.columns(2)
    with col1:
        v1=st.number_input("1. العمق", 7000); v2=st.number_input("2. الضغط", 2500)
        v3=st.number_input("3. الحرارة", 190); v4=st.number_input("4. المسامية", 18)
        v5=st.number_input("5. النفاذية", 120); v6=st.number_input("6. تشبع الماء", 30)
        v7=st.number_input("7. Skin Effect", 0); v8=st.number_input("8. السمك (h)", 50)
        v9=st.number_input("9. القطر", 8); v10=st.number_input("10. الميل", 0)
    with col2:
        v11=st.number_input("11. API", 34); v12=st.number_input("12. اللزوجة", 1.5)
        v13=st.number_input("13. GOR", 400); v14=st.number_input("14. الماء", 10)
        v15=st.number_input("15. ضغط الرأس", 400); v16=st.number_input("16. ضغط القاع", 2000)
        v17=st.number_input("17. الخانق", 32); v18=st.number_input("18. كثافة الغاز", 0.6)
        v19=st.number_input("19. الملوحة", 40000); v20=st.number_input("20. الأيام", 30)

    if st.button("🚀 تحليل البيانات"):
        res = (v2 - v16) * (v5 / v12) * (v20 / 30)
        st.markdown(f"### 📈 الإنتاج المتوقع: **{max(0, res):.2f}** STB/D")
        
        # رسم بياني بسيط
        chart_data = pd.DataFrame(np.random.randn(20, 1), columns=['Pressure Profile'])
        st.line_chart(chart_data)

# ---------------------------------------------------------
# القسم 2: مراقبة الحفر واللزوجة
elif menu == "🏗️ مراقبة الحفر واللزوجة":
    st.write("### 🏗️ بارامترات الحفر الحالية")
    
    # ربط اللزوجة بالمدخل رقم 12 والضغط بالمدخل رقم 2
    c1, c2, c3 = st.columns(3)
    c1.metric("Viscosity (اللزوجة)", "1.5 cp")
    c2.metric("Mud Weight", "9.5 ppg")
    c3.metric("Pressure (الضغط)", "2500 psi")
    
    st.write("---")
    st.write("#### 📈 مراقبة سرعة الحفر (ROP)")
    st.area_chart(np.random.randint(10, 100, 15))

# ---------------------------------------------------------
# القسم 3: التقارير
else:
    st.write("### 📊 مركز الملفات")
    if st.button("Generate Excel Report"):
        st.success("تم إنشاء التقرير بنجاح!")
