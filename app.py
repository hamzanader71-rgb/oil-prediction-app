import streamlit as st
import os
import sys
from io import StringIO

# --- إعدادات النسخة V18 (تصميم Delfi المستوحى) ---
st.set_page_config(page_title="INDUSTRIAL ELITE CORE", layout="wide", page_icon="⚙️")

MASTER_PASSWORD = "root" 

# استايل النيون الزجاجي (Glassmorphism) للهوية الصناعية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    .stApp { background-color: #030712; color: #f9fafb; font-family: 'Inter', sans-serif; }
    
    /* شريط جانبي احترافي */
    [data-testid="stSidebar"] { 
        background-color: #0b0f1a !important; 
        border-right: 1px solid #1f2937;
    }
    
    /* تصميم الكروت (المشاريع) */
    .project-card {
        background: rgba(31, 41, 55, 0.4);
        border: 1px solid #374151;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    
    /* محرر الأكواد (Terminal Style) */
    .stTextArea textarea {
        background-color: #000000 !important;
        color: #10b981 !important; /* لون أخضر برمجي مريح */
        font-family: 'Fira Code', 'Courier New', monospace;
        border: 1px solid #10b981 !important;
        border-radius: 8px;
    }
    
    /* أزرار العمليات */
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white; border: none; border-radius: 8px;
        font-weight: 600; transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
    }
    
    h1, h2, h3 { letter-spacing: -0.025em; font-weight: 700; color: #60a5fa; }
    </style>
    """, unsafe_allow_html=True)

# --- نظام الحفظ الدائم ---
def manage_file(page_id, action="load", content=""):
    filename = f"core_p_{page_id}.txt"
    if action == "save":
        with open(filename, "w", encoding="utf-8") as f: f.write(content)
    elif action == "load":
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f: return f.read()
    return ""

# --- إدارة الدخول ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<div style='text-align: center; padding-top: 150px;'>", unsafe_allow_html=True)
    st.markdown("<h1>SYSTEM ACCESS</h1>", unsafe_allow_html=True)
    pwd = st.text_input("Enter Credentials", type="password", key="login_pwd")
    if st.button("AUTHENTICATE"):
        if pwd == MASTER_PASSWORD:
            st.session_state.auth = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- التنقل الجانبي (10 صفحات تخصصية) ---
    st.sidebar.markdown("<h2 style='text-align:center;'>ELITE CORE</h2>", unsafe_allow_html=True)
    
    pages = {
        "01": "DASHBOARD / الرئيسية",
        "02": "PETRO-PHYSICS / الفيزياء البترولية",
        "03": "RESERVOIR SIM / محاكاة الخزانات",
        "04": "WELL ENGINEERING / هندسة الآبار",
        "05": "PRODUCTION OPS / عمليات الإنتاج",
        "06": "DATA ANALYTICS / تحليل البيانات",
        "07": "GEOLOGY / الجيولوجيا",
        "08": "HSE & SAFETY / السلامة",
        "09": "COST CONTROL / التحكم بالتكاليف",
        "10": "AI RESEARCH / أبحاث الذكاء"
    }
    
    selection = st.sidebar.radio("CHOOSE MODULE", list(pages.keys()), format_func=lambda x: pages[x])
    
    st.sidebar.markdown("---")
    with st.sidebar.expander("🌐 EXTERNAL AI"):
        st.link_button("ChatGPT 4o", "https://chat.openai.com")
        st.link_button("Google Gemini", "https://gemini.google.com")
        st.link_button("DeepSeek", "https://chat.deepseek.com")

    if st.sidebar.button("🔒 SECURE LOGOUT"):
        st.session_state.auth = False
        st.rerun()

    # --- المحتوى الرئيسي (هيكل عالمي) ---
    st.markdown(f"<h3>{pages[selection]}</h3>", unsafe_allow_html=True)
    
    # واجهة الأكواد المثبتة (Execution Module)
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)
    st.markdown("#### 🛠️ CODE ENGINE")
    
    saved_code = manage_file(selection, "load")
    code_input = st.text_area("Source Code Interface", value=saved_code, height=450, key=f"area_{selection}")
    
    col_save, col_run = st.columns([1, 4])
    with col_save:
        if st.button("💾 SAVE"):
            manage_file(selection, "save", code_input)
            st.toast("Module Saved Successfully", icon="🛡️")
            
    with col_run:
        if st.button("▶️ EXECUTE MODULE"):
            try:
                output = StringIO()
                sys.stdout = output
                exec(code_input)
                sys.stdout = sys.__stdout__
                st.code(output.getvalue(), language="python")
                st.success("Execution Complete.")
            except Exception as e:
                st.error(f"Module Error: {e}")
    st.markdown("</div>", unsafe_allow_html=True)

    # قسم الأدوات المساعدة
    with st.expander("📝 PROJECT DOCUMENTATION & FILES"):
        st.file_uploader("Upload Engineering Data (CSV/PDF)", key=f"up_{selection}")
        st.text_area("Field Notes", key=f"note_{selection}")
