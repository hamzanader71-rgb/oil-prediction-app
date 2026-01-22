import streamlit as st
import datetime

# --- إعدادات النسخة الجبارة الكونية V1.0 ---
st.set_page_config(page_title="THE BEAST COSMIC V1.0", layout="wide", page_icon="🌌")

# --- التصميم الكوني (Cosmic UI & Animation) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp { 
        background: url('https://i.imgur.com/3Y1N0k5.gif') no-repeat center center fixed; 
        background-size: cover;
        color: #E0E0E0; /* لون نص فاتح للوضوح */
        font-family: 'Orbitron', sans-serif;
    }

    /* تأثيرات النيون والتوهج */
    h1, h2, h3, .stButton>button, .stTextInput>div>div>input, .stSelectbox>div>div {
        color: #00f2ff;
        text-shadow: 0 0 10px rgba(0, 242, 255, 0.7), 0 0 20px rgba(0, 242, 255, 0.5);
    }
    
    /* كروت الذكاء الاصطناعي المتوهجة */
    .ai-module-card { 
        background: rgba(10, 20, 40, 0.7); /* خلفية داكنة شفافة */
        border: 2px solid #00f2ff; /* حدود نيون */
        border-radius: 15px; 
        padding: 30px; 
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 242, 255, 0.2); /* توهج خفيف */
        transition: all 0.5s ease-in-out;
        margin-bottom: 20px;
    }
    .ai-module-card:hover { 
        transform: scale(1.03); 
        box-shadow: 0 0 60px rgba(0, 242, 255, 0.5), 0 0 30px rgba(255, 0, 255, 0.4); /* توهج مزدوج */
    }

    /* أزرار التحكم الكوني */
    .stButton>button { 
        background: linear-gradient(90deg, #00f2ff, #2a00ff); 
        color: white; border: none; border-radius: 10px; 
        font-family: 'Orbitron'; font-weight: bold; height: 3.5em; width: 100%;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.5);
        transition: all 0.3s ease;
    }
    .stButton>button:hover { 
        background: linear-gradient(90deg, #2a00ff, #00f2ff); 
        transform: translateY(-3px); 
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.8), 0 0 20px rgba(255, 0, 255, 0.6);
    }

    /* الشريط الجانبي الفضائي */
    [data-testid="stSidebar"] { 
        background: linear-gradient(180deg, #000510 0%, #001525 100%); 
        border-right: 3px solid #00f2ff;
        box-shadow: 5px 0 20px rgba(0, 242, 255, 0.3);
    }

    /* شريط الحالة العلوي المتحرك */
    .cosmic-status-bar {
        background: linear-gradient(90deg, rgba(0,242,255,0.2) 0%, rgba(255,0,255,0.2) 50%, rgba(0,242,255,0.2) 100%);
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 30px;
        border: 1px solid #00f2ff;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.4);
        animation: status-glow 4s infinite alternate;
    }
    @keyframes status-glow {
        from { box-shadow: 0 0 10px rgba(0, 242, 255, 0.4); }
        to { box-shadow: 0 0 25px rgba(255, 0, 255, 0.6); }
    }

    /* تغيير لون النصوص في الـ metrics */
    [data-testid="stMetricValue"] { color: #00f2ff !important; text-shadow: 0 0 10px #00f2ff; }
    [data-testid="stMetricLabel"] { color: #88EEFF !important; }

    </style>
    """, unsafe_allow_html=True)

# --- نظام الذاكرة السيادي ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'username' not in st.session_state: st.session_state.username = "Master Hamza" # اسم افتراضي

# --- بوابة الدخول الكونية ---
if not st.session_state.auth:
    st.markdown("<br><h1 style='text-align: center; color:#00f2ff;'>ACCESS COSMIC CORE</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<div class='ai-module-card'>", unsafe_allow_html=True)
        st.subheader("INITIATE BIOMETRIC SCAN")
        access_code = st.text_input("Enter Master Key", type="password")
        if st.button("AUTHENTICATE CORE"):
            if access_code == "root": # الكود السري بتاعك يا مستر حمزة
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("ACCESS DENIED: Unauthorized Signature Detected")
        st.markdown("</div>", unsafe_allow_html=True)

# --- واجهة التحكم الكونية (بعد الدخول) ---
else:
    st.markdown(f"<h1 style='text-align: center;'>{st.session_state.username}'s COSMIC CONTROL</h1>", unsafe_allow_html=True)
    
    # شريط الحالة العلوي المتحرك
    st.markdown(f"""
        <div class="cosmic-status-bar">
            <span style="color:#00f2ff;">[SYSTEM STATUS: ONLINE]</span> 
            <span style="float:right; color:#FF00FF;">[TIME: {datetime.datetime.now().strftime("%H:%M:%S")} EET]</span>
        </div>
        """, unsafe_allow_html=True)

    # --- الشريط الجانبي للتحكم ---
    st.sidebar.title("🌌 NAVIGATION & UTILITIES")
    
    # البحث الكوني المباشر
    search_query = st.sidebar.text_input("Global Data Search")
    if search_query:
        st.sidebar.info(f"Initiating search protocol for: {search_query}...")
        webbrowser.open_new_tab(f"https://www.google.com/search?q={search_query}")
        
    st.sidebar.markdown("---")
    
    # زرار الإغلاق الكوني
    if st.sidebar.button("🔴 SHUTDOWN COSMIC CORE"):
        st.session_state.auth = False
        st.rerun()

    # --- محركات الذكاء الاصطناعي المركزية ---
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_ai1, col_ai2, col_ai3 = st.columns(3)
    
    with col_ai1:
        st.markdown("<div class='ai-module-card'>", unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg", width=60)
        st.subheader("ChatGPT 4o")
        st.write("Premier AI for Advanced Dialogue & Analysis.")
        st.link_button("Engage Neural Network", "https://chat.openai.com")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_ai2:
        st.markdown("<div class='ai-module-card'>", unsafe_allow_html=True)
        st.image("https://static.deepseek.com/logo.png", width=60) 
        st.subheader("DeepSeek AI")
        st.write("Next-Gen Reasoning & Creative Synthesis.")
        st.link_button("Activate Deep Cognition", "https://chat.deepseek.com")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_ai3:
        st.markdown("<div class='ai-module-card'>", unsafe_allow_html=True)
        st.image("https://www.gstatic.com/images/branding/product/2x/gemini_2023_logo_color_256dp.png", width=60) # لوجو Gemini
        st.subheader("Google Gemini")
        st.write("Multimodal Intelligence & Data Fusion.")
        st.link_button("Access Gemini Labs", "https://gemini.google.com")
        st.markdown("</div>", unsafe_allow_html=True)
        
    # --- وحدات تحكم إضافية (Tabs) ---
    st.markdown("<br>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["🚀 System Overview", "📊 Data Streams", "⚙️ Configuration"])
    
    with tab1:
        st.write("Welcome to your personal Cosmic Control Center. All systems are operating at peak efficiency.")
        st.metric("Core Processing Units", "99.9%", "Optimal")
        st.progress(100, text="Neural Network Stability: COMPLETE")
        
    with tab2:
        st.subheader("实时数据流 / REAL-TIME DATA STREAMS")
        st.info("Monitoring galactic data traffic. No anomalies detected.")
        
    with tab3:
        st.subheader("SYSTEM SETTINGS")
        st.warning("Warning: Unauthorized changes may lead to system instability.")
        # هنا ممكن تضيف خيارات تعديل مستقبلية
