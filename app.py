import streamlit as st
import pandas as pd
import numpy as np
import sys
from io import StringIO

# --- إعدادات الهوية البصرية (Industrial Elite) ---
st.set_page_config(page_title="Hamza Petro-Systems", layout="wide", page_icon="🛢️")

st.markdown("""
    <style>
    .stApp { background-color: #030712; color: #f9fafb; }
    [data-testid="stSidebar"] { background-color: #0b0f1a !important; border-right: 1px solid #374151; }
    .stButton>button { background: #2563eb; color: white; border-radius: 8px; width: 100%; }
    .output-box { background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 10px; border: 1px solid #374151; }
    h1, h2 { color: #60a5fa; }
    </style>
    """, unsafe_allow_html=True)

# --- نظام الباسورد المرن (تعديل مباشر) ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'master_pwd' not in st.session_state: st.session_state.master_pwd = "root"

# --- دمج الأكواد السبعة (Functions) ---
# ملاحظة: ضع "كودك الحقيقي" مكان التعليقات داخل كل دالة
def code_production():
    st.markdown("### 📊 نتائج تحليل الإنتاج")
    # --- كود الوورد الخاص بالإنتاج يوضع هنا ---
    data = pd.DataFrame(np.random.randint(0,100,size=(10, 2)), columns=['Oil', 'Gas'])
    st.line_chart(data)
    print("نظام الإنتاج يعمل بكفاءة: 2400 bpd")

def code_reservoir():
    st.markdown("### 🛢️ محاكاة الخزانات")
    # --- كود الوورد الخاص بالخزانات يوضع هنا ---
    st.success("ضغط الخزان الحالي: 3200 psi")
    print("Reservoir analysis completed for Zone A.")

def code_drilling():
    st.markdown("### 🏗️ عمليات الحفر")
    # --- كود الوورد الخاص بالحفر يوضع هنا ---
    print("Drilling depth: 4500 ft - Bit Status: Normal")

def code_fluids():
    st.markdown("### 💧 ديناميكا السوائل")
    # --- كود الوورد الخاص بالسوائل يوضع هنا ---
    print("Viscosity: 1.2 cp - Density: 0.85 g/cm3")

def code_pressure():
    st.markdown("### ⚙️ التحكم في الضغط")
    # --- كود الوورد الخاص بالضغط يوضع هنا ---
    print("Wellhead Pressure: Stable at 1500 psi")

def code_hse():
    st.markdown("### 🛡️ الأمن والسلامة HSE")
    # --- كود الوورد الخاص بالسلامة يوضع هنا ---
    st.warning("تنبيه: راجع مستويات الغاز في المنطقة B")

def code_economy():
    st.markdown("### 💰 التقييم الاقتصادي")
    # --- كود الوورد الخاص بالاقتصاد يوضع هنا ---
    print("ROI: 15% - Payback Period: 3.2 Years")

# --- بوابة الدخول ---
if not st.session_state.auth:
    st.markdown("<br><br><h1>INDUSTRIAL CORE ACCESS</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        pwd_input = st.text_input("Security Key", type="password")
        if st.button("AUTHENTICATE"):
            if pwd_input == st.session_state.master_pwd:
                st.session_state.auth = True
                st.rerun()
            else: st.error("خطأ في المفتاح")
else:
    # --- القائمة الجانبية ---
    st.sidebar.title("MASTER CONTROL")
    pages = {
        "Production": ("تحليل الإنتاج", code_production),
        "Reservoir": ("محاكاة الخزانات", code_reservoir),
        "Drilling": ("عمليات الحفر", code_drilling),
        "Fluids": ("ديناميكا السوائل", code_fluids),
        "Pressure": ("التحكم بالضغط", code_pressure),
        "HSE": ("الأمن والسلامة", code_hse),
        "Economy": ("التقييم الاقتصادي", code_economy)
    }
    
    selection = st.sidebar.radio("NAVIGATE", list(pages.keys()), format_func=lambda x: pages[x][0])
    
    st.sidebar.markdown("---")
    with st.sidebar.expander("🔐 Change Password"):
        new_pwd = st.text_input("New Password", type="password")
        if st.button("Update"):
            st.session_state.master_pwd = new_pwd
            st.success("Updated!")

    if st.sidebar.button("🔒 LOGOUT"):
        st.session_state.auth = False
        st.rerun()

    # --- التنفيذ المدمج والمخفي ---
    st.markdown(f"<h2>{pages[selection][0]}</h2>", unsafe_allow_html=True)
    st.markdown("<div class='output-box'>", unsafe_allow_html=True)
    
    # تحويل مخرجات الكود (print) لتظهر في الشاشة
    output_capture = StringIO()
    sys.stdout = output_capture
    
    # تشغيل الدالة المدمجة الخاصة بالصفحة
    pages[selection][1]() 
    
    sys.stdout = sys.__stdout__
    if output_capture.getvalue():
        st.code(output_capture.getvalue())
    st.markdown("</div>", unsafe_allow_html=True)
