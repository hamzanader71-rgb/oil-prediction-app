import streamlit as st
import sys
import os
from io import StringIO

# --- 1. الإعدادات العالمية (تصميم DELFI العالمي) ---
st.set_page_config(page_title="Hamza Petro-Systems", layout="wide", page_icon="🛢️")

# ستايل النيون الزجاجي الاحترافي
st.markdown("""
    <style>
    .stApp { background-color: #030712; color: #f9fafb; }
    [data-testid="stSidebar"] { background-color: #0b0f1a !important; border-right: 1px solid #1f2937; }
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white; border-radius: 8px; font-weight: 600; height: 3em;
    }
    .status-box {
        background: rgba(31, 41, 55, 0.4); border: 1px solid #374151;
        padding: 20px; border-radius: 12px; text-align: center;
    }
    h1, h2 { color: #60a5fa; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. نظام الباسورد المرن (إنت اللي بتحدده) ---
if 'auth' not in st.session_state: st.session_state.auth = False

# ملف حفظ الباسورد
PWD_FILE = "config_secret.txt"
def get_pwd():
    if os.path.exists(PWD_FILE):
        with open(PWD_FILE, "r") as f: return f.read().strip()
    return "root" # الباسورد الافتراضي

if not st.session_state.auth:
    st.markdown("<br><br><h1>INDUSTRIAL ACCESS</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        pwd_input = st.text_input("Security Key", type="password")
        if st.button("AUTHENTICATE"):
            if pwd_input == get_pwd():
                st.session_state.auth = True
                st.rerun()
            else: st.error("Access Denied")
else:
    # --- 3. الهيكل التنظيمي (7 صفحات مدمجة) ---
    st.sidebar.markdown("<h2 style='color:#60a5fa;'>MASTER CONTROL</h2>", unsafe_allow_html=True)
    
    # أسماء الصفحات بناءً على تخصصاتك
    pages = {
        "Production": "تحليل الإنتاج الشامل",
        "Reservoir": "محاكاة الخزانات",
        "Drilling": "عمليات الحفر الميداني",
        "Fluids": "ديناميكا السوائل",
        "Pressure": "التحكم في الضغط",
        "HSE": "الأمن والسلامة المهنية",
        "Economy": "التقييم الاقتصادي"
    }
    
    selection = st.sidebar.radio("NAVIGATE", list(pages.keys()), format_func=lambda x: pages[x])
    
    st.sidebar.markdown("---")
    # ميزة تغيير الباسورد من جوه البرنامج
    with st.sidebar.expander("🔐 Change System Key"):
        new_pwd = st.text_input("New Key", type="password")
        if st.button("Update Key"):
            with open(PWD_FILE, "w") as f: f.write(new_pwd)
            st.success("Key Updated!")

    if st.sidebar.button("🔒 LOGOUT"):
        st.session_state.auth = False
        st.rerun()

    # --- 4. محرك تشغيل الأكواد السبعة (مخفي ومثبت) ---
    st.markdown(f"<h2>{pages[selection]} Module</h2>", unsafe_allow_html=True)
    
    # وظيفة لجلب الكود الخاص بكل صفحة (اللي إنت ثبتته من ملف الوورد)
    def execute_fixed_code(module_name):
        code_path = f"fixed_{module_name}.txt"
        if os.path.exists(code_path):
            with open(code_path, "r", encoding="utf-8") as f:
                fixed_code = f.read()
            try:
                # تنفيذ الكود وعرض المخرجات فقط بدون ظهور الكود
                output = StringIO()
                sys.stdout = output
                exec(fixed_code)
                sys.stdout = sys.__stdout__
                st.markdown("<div class='status-box'>", unsafe_allow_html=True)
                st.code(output.getvalue())
                st.markdown("</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Execution Error: {e}")
        else:
            st.warning("⚠️ هذا الموديول بانتظار دمج الكود البرمجي.")

    # تشغيل الكود فور فتح الصفحة
    execute_fixed_code(selection)

    # إضافة خيار لإدارة الملفات أو الملاحظات لكل قسم
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("📂 Project Records"):
        st.file_uploader("Upload Daily Reports", key=f"file_{selection}")
        st.text_area("Engineer Notes", key=f"note_{selection}")
