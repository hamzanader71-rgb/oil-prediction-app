import streamlit as st
import pandas as pd

# إعدادات الواجهة الاحترافية
st.set_page_config(page_title="Oil Master Pro 20", page_icon="💎", layout="centered")

# تنسيق الألوان الفخم (الوضع الليلي مع الأخضر البترولي)
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .stButton>button { width: 100%; border-radius: 15px; height: 4em; background-color: #2ecc71; color: white; font-weight: bold; font-size: 20px; border: none; box-shadow: 0px 4px 10px rgba(46, 204, 113, 0.3); }
    .stNumberInput label { color: #3498db !important; font-size: 14px; }
    h1 { color: #2ecc71; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("⛽ نظام التحليل المتكامل (20 معامل)")
st.write("مرحباً مهندس حمزة. يرجى إدخال كافة البيانات الفنية العشرين:")

# تقسيم الـ 20 معامل لمجموعات
col1, col2 = st.columns(2)

with col1:
    st.info("🏗️ بيانات البئر والصخر")
    v1 = st.number_input("1. العمق الإجمالي (ft)", value=7000)
    v2 = st.number_input("2. الضغط الطبقي (psi)", value=2500)
    v3 = st.number_input("3. درجة الحرارة (F)", value=190)
    v4 = st.number_input("4. المسامية (%)", value=18.5)
    v5 = st.number_input("5. النفاذية (md)", value=120)
    v6 = st.number_input("6. تشبع الماء (%)", value=30)
    v7 = st.number_input("7. معامل الضرر (Skin)", value=0.5)
    v8 = st.number_input("8. سمك الطبقة (ft)", value=45)
    v9 = st.number_input("9. قطر البئر (in)", value=8.5)
    v10 = st.number_input("10. زاوية الميل (deg)", value=0)

with col2:
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
