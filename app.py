import streamlit as st
import os

# --- الإعدادات الفنية (الاستايل الصناعي) ---
st.set_page_config(page_title="PETRO-LEADER CONTROL", layout="wide", page_icon="⛽")

MASTER_PASSWORD = "root" 

# استايل شركات البترول (Deep Space Gray & Safety Orange)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #111111 !important; border-right: 2px solid #f39c12; }
    
    /* كروت البيانات المهنية */
    .metric-card {
        background: #1a1a1a; border-left: 5px solid #f39c12;
        padding: 15px; border-radius: 5px; margin-bottom: 10px;
    }
    
    /* العناوين الاحترافية */
    .petro-header {
        color: #f39c12; font-family: 'Arial Black'; border-bottom: 1px solid #333;
        padding-bottom: 10px; text-transform: uppercase; letter-spacing: 2px;
    }
    
    /* محرر الأكواد (الهيكل التنفيذي) */
    .stTextArea textarea {
        background-color: #000 !important; color: #f39c12 !important;
        font-family: 'Consolas', monospace; border: 1px solid #333 !important;
    }
    
    .stButton>button {
        background-color: #f39c12; color: black; border-radius: 0px;
        font-weight: bold; width: 100%; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- نظام الذاكرة وحفظ الكود ---
def save_p_code(p_id, content):
    with open(f"p_{p_id}_source.txt", "w", encoding="utf-8") as f: f.write(content)

def load_p_code(p_id):
    if os.path.exists(f"p_{p_id}_source.txt"):
        with open(f"p_{p_id}_source.txt", "r", encoding="utf-8") as f: return f.read()
    return "# Start your Petro-Project code here..."

# --- نظام الدخول ---
if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<div style='text-align: center; margin-top: 150px;'>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2967/2967568.png", width=100)
    st.markdown("<h2 class='petro-header'>SYSTEM LOGIN</h2>", unsafe_allow_html=True)
    pwd = st.text_input("Enter Credentials", type="password")
    if st.button("LOG IN"):
        if pwd == MASTER_PASSWORD:
            st.session_state.auth = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # --- الهيكل العالمي (القائمة الجانبية الموزعة) ---
    st.sidebar.markdown("<h2 style='color:#f39c12;'>🛢️ PETRO-CORE</h2>", unsafe_allow_html=True)
    
    # توزيع الـ 10 صفحات بأسماء تخصصات البترول
    pages = {
        "DASHBOARD": "الرئيسية",
        "WELL_LOGS": "سجلات الآبار",
        "PRODUCTION": "بيانات الإنتاج",
        "DRILLING": "عمليات الحفر",
        "RESERVOIR": "الخزانات",
        "SEISMIC": "المسح السيزمي",
        "PIPELINES": "خطوط الأنابيب",
        "SAFETY_HSE": "الأمن والسلامة",
        "REFINING": "التكرير",
        "COST_ANALYSIS": "تحليل التكاليف"
    }
    
    selection = st.sidebar.radio("NAVIGATE SYSTEM", list(pages.keys()))
    
    st.sidebar.markdown("---")
    with st.sidebar.expander("🛠️ EXTERNAL AI"):
        st.link_button("ChatGPT", "https://chat.openai.com")
        st.link_button("Gemini", "https://gemini.google.com")

    if st.sidebar.button("🔒 EXIT SYSTEM"):
        st.session_state.auth = False
        st.rerun()

    # --- محتوى الصفحات (الهيكل العالمي) ---
    st.markdown(f"<h1 class='petro-header'>{selection} UNIT</h1>", unsafe_allow_html=True)
    
    # عرض الـ Metrics زي برامج البترول
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("<div class='metric-card'><b>Flow Rate:</b> 2,450 bpd</div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='metric-card'><b>Pressure:</b> 1,200 psi</div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='metric-card'><b>Status:</b> ACTIVE</div>", unsafe_allow_html=True)

    # محرك الأكواد المثبت (المحرك اللي بيشغل مشروعك)
    st.markdown("### ⚙️ PROJECT CODE EXECUTOR")
    current_code = load_p_code(selection)
    code_area = st.text_area("Source Code", value=current_code, height=350, key=f"code_{selection}")
    
    col_act1, col_act2 = st.columns([1, 4])
    with col_act1:
        if st.button("SAVE CODE"):
            save_p_code(selection, code_area)
            st.toast("Data Saved to Core", icon="💾")
    with col_act2:
        if st.button("RUN MODULE"):
            try:
                # تنفيذ الكود وعرض النتايج
                import sys
                from io import StringIO
                output = StringIO()
                sys.stdout = output
                exec(code_area)
                sys.stdout = sys.__stdout__
                st.code(output.getvalue(), language="python")
            except Exception as e:
                st.error(f"Execution Error: {e}")

    # مساحة الملاحظات والملفات لكل صفحة
    with st.expander("📂 PROJECT FILES & NOTES"):
        st.file_uploader("Upload Sector Data", key=f"file_{selection}")
        st.text_area("Engineering Notes", key=f"note_{selection}")
