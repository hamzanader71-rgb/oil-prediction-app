import streamlit as st
import sys
import os
from io import StringIO

# --- إعدادات النسخة V15 ---
st.set_page_config(page_title="BEAST PERSISTENT", layout="wide", page_icon="💾")

MASTER_PASSWORD = "root" 

# --- وظائف حفظ واسترجاع الأكواد من ملفات ---
def save_code(page_name, code):
    with open(f"{page_name}_code.txt", "w", encoding="utf-8") as f:
        f.write(code)

def load_code(page_name):
    filename = f"{page_name}_code.txt"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# --- التصميم الاحترافي ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #3e4451; }
    .project-header { color: #00f2ff; border-bottom: 2px solid #3e4451; padding-bottom: 10px; font-family: 'Orbitron'; }
    .stTextArea textarea { background-color: #000000 !important; color: #00ff00 !important; font-family: 'Courier New', monospace; border: 1px solid #00f2ff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- نظام الدخول ---
if 'authenticated' not in st.session_state: st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown("<div style='text-align: center; background: #1c2128; padding: 40px; border-radius: 20px; border: 1px solid #3e4451;'>", unsafe_allow_html=True)
        st.header("Master Access")
        pwd_input = st.text_input("Security Code", type="password")
        if st.button("Unlock"):
            if pwd_input == MASTER_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else: st.error("Access Denied")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- القائمة الجانبية (10 صفحات) ---
    st.sidebar.title("🎮 Command Center")
    page = st.sidebar.selectbox("Go to Page:", 
                               ["Home"] + [f"Project_{i}" for i in range(1, 11)])

    with st.sidebar.expander("🤖 AI & Tools"):
        st.link_button("ChatGPT", "https://chat.openai.com")
        st.link_button("Gemini", "https://gemini.google.com")
        st.link_button("DeepSeek", "https://chat.deepseek.com")

    if st.sidebar.button("🔴 Lock"):
        st.session_state.authenticated = False
        st.rerun()

    # --- محتوى الصفحات ---
    if page == "Home":
        st.markdown("<h1 class='project-header'>Main Dashboard</h1>", unsafe_allow_html=True)
        st.info(f"مرحباً يا مستر حمزة. الكود اللي هتكتبه في أي مشروع هيفضل محفوظ باسم الصفحة.")
    
    else:
        st.markdown(f"<h1 class='project-header'>{page} Environment</h1>", unsafe_allow_html=True)
        
        # تحميل الكود المحفوظ سابقاً
        saved_code = load_code(page)
        
        st.subheader("🚀 Code Editor (Auto-Saved)")
        code_input = st.text_area("أكتب الكود هنا (سيتم حفظه أوتوماتيكياً لهذا المشروع)", 
                                  value=saved_code, height=300, key=f"editor_{page}")
        
        col_btn1, col_btn2 = st.columns([1, 5])
        with col_btn1:
            if st.button("💾 حفظ الكود"):
                save_code(page, code_input)
                st.toast(f"تم حفظ كود {page} بنجاح!", icon="✅")
        
        with col_btn2:
            if st.button(f"▶️ تشغيل كود {page}"):
                if code_input:
                    st.markdown("---")
                    st.subheader("⚙️ Execution Output:")
                    try:
                        old_stdout = sys.stdout
                        redirected_output = sys.stdout = StringIO()
                        exec(code_input)
                        sys.stdout = old_stdout
                        result = redirected_output.getvalue()
                        if result: st.code(result, language='python')
                        else: st.success("تم التنفيذ بنجاح (لا يوجد مخرجات نصية).")
                    except Exception as e:
                        st.error(f"Error in Code: {e}")

        st.markdown("---")
        with st.expander("📝 ملاحظات المشروع"):
            st.text_area("اكتب أي ملاحظات إضافية هنا...", key=f"notes_{page}")
