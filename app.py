import streamlit as st

# --- إعدادات النسخة الأنيقة V12 ---
st.set_page_config(page_title="THE SLEEK BEAST", layout="wide", page_icon="🌑")

# --- التصميم الهادئ والمختصر (Minimalist Pro UI) ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #ffffff; }
    
    /* تصميم زرار فتح القائمة الجبار */
    .stButton>button { 
        border-radius: 50px; 
        background: linear-gradient(90deg, #1c2128, #3e4451);
        color: #00f2ff; border: 1px solid #00f2ff;
        padding: 10px 25px; font-weight: bold; transition: 0.4s;
    }
    .stButton>button:hover { 
        background: #00f2ff; color: #000; box-shadow: 0 0 20px #00f2ff;
    }
    
    /* ستايل الدوائر الصغيرة داخل القائمة */
    .ai-circle-small {
        width: 60px; height: 60px;
        border-radius: 50%; border: 1px solid #3e4451;
        display: flex; align-items: center; justify-content: center;
        margin: auto; background: #1c2128;
    }
    .ai-label { text-align: center; font-size: 11px; margin-top: 5px; color: #8b949e; }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة الدخول ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- شاشة تسجيل الدخول ---
if not st.session_state.auth:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown("<div style='text-align: center; background: #1c2128; padding: 40px; border-radius: 20px; border: 1px solid #3e4451;'>", unsafe_allow_html=True)
        st.image("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png", width=100)
        st.subheader("Login to System")
        if st.button("Sign in with Google"):
            st.session_state.auth = True
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- الواجهة الرئيسية الأنيقة ---
else:
    # هيدر بسيط جداً
    c1, c2 = st.columns([8, 1])
    with c2:
        if st.button("Exit"):
            st.session_state.auth = False
            st.rerun()

    # شاشة الترحيب الرئيسية (الفراغ الأنيق)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>BEAST SYSTEM</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8b949e;'>Welcome Master Hamza. Systems are idle.</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # الزرار السحري اللي بيفتح كل حاجة
    col_btn1, col_btn2, col_btn3 = st.columns([1.5, 1, 1.5])
    with col_btn2:
        show_menu = st.toggle("🚀 Open AI Command Center")

    # القائمة لا تظهر إلا عند تفعيل الزرار
    if show_menu:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div style='background: #1c2128; padding: 30px; border-radius: 20px; border: 1px solid #00f2ff;'>", unsafe_allow_html=True)
        
        cols = st.columns(5)
        
        with cols[0]:
            st.markdown("<div class='ai-circle-small'><img src='https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg' width='30'></div>", unsafe_allow_html=True)
            st.link_button("ChatGPT", "https://chat.openai.com", use_container_width=True)

        with cols[1]:
            st.markdown("<div class='ai-circle-small'><img src='https://www.gstatic.com/images/branding/product/2x/gemini_2023_logo_color_256dp.png' width='30'></div>", unsafe_allow_html=True)
            st.link_button("Gemini", "https://gemini.google.com", use_container_width=True)

        with cols[2]:
            st.markdown("<div class='ai-circle-small'><img src='https://static.deepseek.com/logo.png' width='30'></div>", unsafe_allow_html=True)
            st.link_button("DeepSeek", "https://chat.deepseek.com", use_container_width=True)

        with cols[3]:
            st.markdown("<div class='ai-circle-small'><img src='https://upload.wikimedia.org/wikipedia/commons/e/e1/Google_Chrome_icon_%28February_2022%29.svg' width='30'></div>", unsafe_allow_html=True)
            st.link_button("Chrome", "https://www.google.com", use_container_width=True)

        with cols[4]:
            st.markdown("<div class='ai-circle-small'><img src='https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg' width='40'></div>", unsafe_allow_html=True)
            st.link_button("YouTube", "https://www.youtube.com", use_container_width=True)
            
        st.markdown("</div>", unsafe_allow_html=True)

    # خانة البحث (مخفية برضه في tab)
    with st.expander("🔍 Quick Search"):
        search = st.text_input("Enter your search...")
        if search:
            st.link_button("Search Google", f"https://www.google.com/search?q={search}")
