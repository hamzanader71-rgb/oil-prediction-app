import streamlit as st

# --- إعدادات النسخة البرو V11 ---
st.set_page_config(page_title="THE PRO BEAST", layout="wide", page_icon="🛡️")

# --- التصميم الهادئ (Pro Minimalist UI) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #e0e0e0; }
    
    /* ستايل الدوائر الصغيرة للذكاء الاصطناعي */
    .ai-circle {
        width: 80px; height: 80px;
        border-radius: 50%;
        border: 2px solid #3e4451;
        display: flex; align-items: center; justify-content: center;
        margin: auto; transition: 0.3s;
        background: #1c2128;
        cursor: pointer;
    }
    .ai-circle:hover { border-color: #00f2ff; transform: scale(1.1); box-shadow: 0 0 15px #00f2ff; }
    .ai-label { text-align: center; font-size: 12px; margin-top: 8px; color: #8b949e; }
    
    /* ستايل زرار جوجل */
    .google-btn {
        background-color: white; color: #757575; border-radius: 5px;
        padding: 10px 20px; text-align: center; font-weight: bold;
        cursor: pointer; border: 1px solid #ddd; display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- نظام الذاكرة والدخول ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- شاشة تسجيل الدخول بجوجل (محاكاة) ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown("<div style='text-align: center; background: #1c2128; padding: 40px; border-radius: 20px;'>", unsafe_allow_html=True)
        st.image("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png", width=120)
        st.subheader("تسجيل الدخول للنظام")
        st.write("استخدم حساب جوجل للوصول للنسخة الجبارة")
        if st.button("Sign in with Google"):
            st.session_state.auth = True
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- الواجهة الرئيسية (بعد الدخول) ---
else:
    # هيدر بسيط فيه اللغة والبحث
    col_h1, col_h2, col_h3 = st.columns([2, 4, 2])
    with col_h1:
        lang = st.selectbox("🌐 Language", ["Arabic", "English"])
    with col_h3:
        if st.button("Log out"):
            st.session_state.auth = False
            st.rerun()

    st.markdown("<hr style='border-color: #3e4451;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>مركز التحكم الذكي</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # صف الدوائر (AI & Browser)
    col_ai = st.columns(5)
    
    with col_ai[0]:
        st.markdown("<div class='ai-circle'><img src='https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg' width='40'></div>", unsafe_allow_html=True)
        st.markdown("<p class='ai-label'>ChatGPT</p>", unsafe_allow_html=True)
        st.link_button("Open", "https://chat.openai.com", use_container_width=True)

    with col_ai[1]:
        st.markdown("<div class='ai-circle'><img src='https://www.gstatic.com/images/branding/product/2x/gemini_2023_logo_color_256dp.png' width='40'></div>", unsafe_allow_html=True)
        st.markdown("<p class='ai-label'>Gemini</p>", unsafe_allow_html=True)
        st.link_button("Open", "https://gemini.google.com", use_container_width=True)

    with col_ai[2]:
        st.markdown("<div class='ai-circle'><img src='https://static.deepseek.com/logo.png' width='40'></div>", unsafe_allow_html=True)
        st.markdown("<p class='ai-label'>DeepSeek</p>", unsafe_allow_html=True)
        st.link_button("Open", "https://chat.deepseek.com", use_container_width=True)

    with col_ai[3]:
        # إضافة جوجل كروم
        st.markdown("<div class='ai-circle'><img src='https://upload.wikimedia.org/wikipedia/commons/e/e1/Google_Chrome_icon_%28February_2022%29.svg' width='40'></div>", unsafe_allow_html=True)
        st.markdown("<p class='ai-label'>Chrome</p>", unsafe_allow_html=True)
        st.link_button("Browse", "https://www.google.com", use_container_width=True)

    with col_ai[4]:
        st.markdown("<div class='ai-circle'><img src='https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg' width='50'></div>", unsafe_allow_html=True)
        st.markdown("<p class='ai-label'>YouTube</p>", unsafe_allow_html=True)
        st.link_button("Watch", "https://www.youtube.com", use_container_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # منطقة البحث السريع
    st.markdown("<div style='background: #1c2128; padding: 20px; border-radius: 15px;'>", unsafe_allow_html=True)
    st.subheader("🔍 بحث سريع")
    search = st.text_input("ابحث عن أي شيء في جوجل...")
    if search:
        st.link_button("اضغط للتنفيذ", f"https://www.google.com/search?q={search}")
    st.markdown("</div>", unsafe_allow_html=True)
