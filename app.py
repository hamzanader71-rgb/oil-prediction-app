import streamlit as st
import pandas as pd

# 1. إعدادات المنصة الاحترافية
st.set_page_config(page_title="Hamza Global Oil & Gas Suite", page_icon="🌐", layout="wide")

# تصميم الواجهة بالألوان الموحدة
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .stSidebar { background-color: #1a1c24; border-right: 1px solid #2ecc71; }
    .stButton>button { width: 100%; border-radius: 12px; background-color: #2ecc71; color: white; font-weight: bold; }
    h1 { color: #2ecc71; font-family: 'Arial'; }
    .stSubheader { color: #3498db; }
    </style>
    """, unsafe_allow_html=True)

# 2. القائمة الجانبية الضخمة لـ 8 تخصصات
st.sidebar.title("🚀 لوحة التحكم الكبرى")
menu = st.sidebar.radio("اختر القسم الفني:", [
    "📌 1. التقييم الجيولوجي (Geology)",
    "🏗️ 2. هندسة الحفر (Drilling)",
    "🛢️ 3. خصائص الخزانات (Reservoir)",
    "💧 4. هندسة السوائل (PVT)",
    "⛽ 5. تحسين الإنتاج (Production)",
    "🛠️ 6. صيانة الآبار (Workover)",
    "📊 7. التحليل الاقتصادي (Economics)",
    "🛡️ 8. السلامة والبيئة (HSE)"
])

# ---------------------------------------------------------
# 1. الجيولوجيا
if "1" in menu:
    st.title("📌 التقييم الجيولوجي والجس (Logging)")
    col1, col2 = st.columns(2)
    with col1:
        v1 = st.number_input("نسبة الطفلة (V-Shale)", 0.2)
        v2 = st.number_input("المقاومة الكهربية (Resistivity)", 10.0)
    with col2:
        v3 = st.number_input("كثافة الصخر (Bulk Density)", 2.4)
    if st.button("حساب احتمالية وجود الهيدروكربون"):
        st.success("الاحتمالية: 85% - الطبقة واعدة!")

# 2. الحفر
elif "2" in menu:
    st.title("🏗️ هندسة الحفر والتبطين (Drilling & Casing)")
    col1, col2 = st.columns(2)
    with col1:
        v4 = st.number_input("وزن الطفلة (Mud Weight ppg)", 9.5)
        v5 = st.number_input("سرعة الدوران (RPM)", 120)
    with col2:
        v6 = st.number_input("عزم الدوران (Torque)", 1500)
    st.bar_chart([v4*10, v5, v6/10])

# 3. الخزانات
elif "3" in menu:
    st.title("🛢️ ميكانيكا الخزانات (Reservoir Engineering)")
    v7 = st.slider("المسامية (%)", 5, 35, 20)
    v8 = st.slider("النفاذية (md)", 1, 500, 150)
    st.write(f"النسبة الذهبية للخزان: {v8/v7:.2f}")

# 4. السوائل
elif "4" in menu:
    st.title("💧 تحليل الـ PVT والسوائل")
    v9 = st.selectbox("نوع الزيت المتوقع:", ["Light Oil", "Heavy Oil", "Gas Condensate"])
    v10 = st.number_input("API Gravity", 38.0)
    st.metric("تصنيف الجودة", "Excellent" if v10 > 35 else "Fair")

# 5. الإنتاج
elif "5" in menu:
    st.title("⛽ هندسة الإنتاج والرفع الصناعي")
    v11 = st.number_input("معدل التدفق (Flow Rate)", 200)
    v12 = st.selectbox("نوع الرفع:", ["Natural Flow", "ESP", "Gas Lift", "Sucker Rod"])
    st.line_chart([10, 25, 45, 80, 150, v11])

# 6. صيانة الآبار
elif "6" in menu:
    st.title("🛠️ صيانة الآبار والتدخل (Workover)")
    st.write("أدخل سجل الأعطال:")
    v13 = st.text_area("وصف المشكلة (مثلاً: سد رملي، تآكل مواسير)")
    if st.button("اقتراح الحل الفني"):
        st.warning("يوصى بعمل Acidizing (تحميض) أو Sand Control.")

# 7. التحليل الاقتصادي
elif "7" in menu:
    st.title("📊 التكاليف والأرباح (Economics)")
    v14 = st.number_input("سعر البرميل اليوم ($)", 80)
    v15 = st.number_input("تكلفة الإنتاج للبرميل ($)", 15)
    st.metric("صافي الربح المتوقع للبرميل", f"{v14-v15} $")

# 8. السلامة
else:
    st.title("🛡️ السلامة والصحة المهنية (HSE)")
    v16 = st.number_input("مستوى غاز H2S (ppm)", 0.0)
    if v16 > 10:
        st.error("🚨 خطر! مستوى الغاز مرتفع جداً. أخلِ المنطقة!")
    else:
        st.success("المنطقة آمنة للعمل.")
