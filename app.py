import streamlit as st
import pandas as pd

# 1. إعدادات الواجهة
st.set_page_config(page_title="Oil Master 20", page_icon="⛽", layout="centered")

# 2. تنسيق الألوان
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background-color: #2ecc71; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("⛽ منصة التحليل المتكاملة")
st.write("أهلاً مهندس حمزة. يرجى إدخال الـ 20 معامل:")

# 3. تقسيم الـ 20 مدخل
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
    v12 = st.number_input("12. اللزوجة (cp)", value=1.5)
    v13 = st.number_input("13. نسبة GOR", value=400)
    v14 = st.number_input("14. القطع المائي", value=10)
    v15 = st.number_input("15. ضغط الرأس", value=400)
    v16 = st.number_input("16. ضغط القاع", value=2000)
    v17 = st.number_input("17. حجم الخانق", value=32)
    v18 = st.number_input("18. كثافة الغاز", value=0.6)
    v19 = st.number_input("19. الملوحة", value=40000)
    v20 = st.number_input("20. أيام الإنتاج", value=30)

# 4. زر التحليل
if st.button("🚀 تحليل البيانات الـ 20"):
    # عملية حسابية بسيطة
    total = (v2 - v16) * (v5 / v12)
    st.markdown("---")
    st.success(f"### الإنتاج المتوقع: {max(0, total):.2f} برميل/يوم")
    
    # 5. عرض الجدول (تم إصلاح اسم المتغير هنا)
    labels = ["العمق", "الضغط", "الحرارة", "المسامية", "النفاذية", "تشبع الماء", "Skin", "السمك", "القطر", "الميل", "API", "اللزوجة", "GOR", "الماء", "ضغط الرأس", "ضغط القاع", "الخانق", "كثافة الغاز", "الملوحة", "الأيام"]
    values = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20]
    
    final_df = pd.DataFrame({"المعامل": labels, "القيمة": values})
    st.table(final_df) # هنا تم التأكد من مطابقة الأسماء
    st.balloons()
    st.info("💧 خصائص السوائل والإنتاج")
    v11 = st.number_input("11. كثافة الزيت (API)", value=34.0)
    v12 = st.number_input("12. لزوجة الزيت (cp)", value=1.8)
    v13 = st.number_input("13. نسبة الغاز/زيت (GOR)", value=450)
    v14 = st.number_input("14. القطع المائي (WC %)", value=12.0)
    v15 = st.number_input("15. ضغط رأس البئر (psi)", value=450)
    v16 = st.number_input("16. ضغط القاع (psi)", value=1800)
    v17 = st.number_input("17. حجم الخانق (1/64 in)", value=28)
    v18 = st.number_input("18. كثافة الغاز (sp gr)", value=0.65)
    v19 = st.number_input("19. ملوحة الماء (ppm)", value=50000)
    v20 = st.number_input("20. أيام الإنتاج للشهر", value=30)

st.markdown("---")

if st.button("🚀 تحليل الـ 20 معامل وإصدار النتيجة"):
    # معادلة حسابية شاملة افتراضية
    base_prod = (v2 - v16) * (v5 * v8) / (v12 * 500)
    final_res = base_prod * (1 - (v14/100))
    
    st.success(f"### الإنتاج المتوقع: {max(0, final_res):.2f} STB/Day")
    
    # عرض الجدول الشامل لـ 20 معلومة
    st.write("📋 التقرير الفني المجمع:")
    labels = [
        "العمق", "الضغط الطبقي", "الحرارة", "المسامية", "النفاذية", 
        "تشبع الماء", "Skin", "سمك الطبقة", "قطر البئر", "زاوية الميل",
        "API", "اللزوجة", "GOR", "القطع المائي", "ضغط الرأس", 
        "ضغط القاع", "الخانق", "كثافة الغاز", "الملوحة", "أيام الإنتاج"
    ]
    values = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20]
    
    df = pd.DataFrame({"المعامل الفني": labels, "القيمة": values})
    st.table(df)
    st.balloons()
    st.table(pd.DataFrame(data))
