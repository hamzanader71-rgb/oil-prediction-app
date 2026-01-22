import streamlit as st
from streamlit_mic_recorder import mic_recorder
import time

# --- إعدادات النظام السيادي الفائق V4.0 ---
st.set_page_config(page_title="JARVIS SOVEREIGN V4", layout="wide", page_icon="🎙️")

# --- محرك الصوت (الترحيب الصوتي باسمك) ---
def speak(text):
    b64_text = text.replace("'", "\\'")
    js = f"""
    <script>
        var msg = new SpeechSynthesisUtterance('{b64_text}');
        msg.lang = 'ar-SA';
        window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js, height=0)

# --- محرك التصميم السينمائي (Iron Man UI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: radial-gradient(circle, #0a192f 0%, #000000 100%); color: #00f2ff; font-family: 'Segoe UI', sans-serif; }
    .auth-box { background: rgba(0, 242, 255, 0.05); border: 2px solid #00f2ff; border-radius: 20px; padding: 40px; box-shadow: 0 0 30px rgba(0, 242, 255, 0.2); text-align: center; }
    .stButton>button { border-radius: 10px; background: transparent; border: 1px solid #00f2ff; color: #00f2ff; font-size: 18px; transition: 0.5s; width: 100%; font-family: 'Orbitron'; }
    .stButton>button:hover { background: #00f2ff; color: #000; box-shadow: 0 0 50px #00f2ff; transform: translateY(-3px); }
    [data-testid="stSidebar"] { background-color: #0a1016 !important; border-right: 1px solid #00f2ff; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; letter-spacing: 3px; text-shadow: 0 0 10px #00f2ff; }
    .jarvis-circle { border: 4px solid #00f2ff; border-radius: 50%; width: 180px; height: 180px; margin: auto; 
                    box-shadow: 0 0 40px #00f2ff; animation: pulse 2s infinite; display: flex; align-items: center; justify-content: center; }
    @keyframes pulse { 0% { transform: scale(1); opacity: 0.8; } 50% { transform: scale(1.05); opacity: 1; box-shadow: 0 0 60px #00f2ff; } 100% { transform: scale(1); opacity: 0.8; } }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة الحالة والذاكرة ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'greeted' not in st.session_state: st.session_state.greeted = False

# نظام اللغات
DICT = {
    "English": {"scan": "BIOMETRIC SCAN", "secure": "SECURITY LEVEL: MAX", "voice": "JARVIS CORE"},
    "العربية": {"scan": "المسح البيومتري", "secure": "مستوى الأمان: أقصى", "voice": "مركز جارفيس"},
    "Français": {"scan": "SCAN BIOMÉTRIQUE", "secure": "SÉCURITÉ: MAX", "voice": "NOYAU VOCAL"},
    "Italiano": {"scan": "SCANSIONE BIOMETRICA", "secure": "SICUREZZA: MAX", "voice": "NUCLEO VOCALE"},
    "Deutsch": {"scan": "BIOMETRISCHER SCAN", "secure": "SICHERHEIT: MAX", "voice": "SPRACHKERN"}
}

st.sidebar.title("⚙️ SYSTEM CORE")
lang_choice = st.sidebar.selectbox("Language / اللغة", list(DICT.keys()))
TXT = DICT[lang_choice]

# --- بوابة الدخول (الاسم + الباسورد + البصمة) ---
if not st.session_state.auth:
    st.markdown("<br><h1 style='text-align: center;'>JARVIS PROTOCOL</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="auth-box">', unsafe_allow_html=True)
        name = st.text_input("ENTER YOUR NAME / اسم المستخدم")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("👤 FACE ID"):
                if name:
                    st.session_state.current_user = name
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Please enter name first")
        with c2:
            if st.button("☝️ FINGERPRINT"):
                if name:
                    st.session_state.current_user = name
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Please enter name first")
        st.markdown('</div>', unsafe_allow_html=True)

# --- واجهة جارفيس الحية (بعد الدخول) ---
else:
    # الترحيب الصوتي التلقائي باسمك
    if not st.session_state.greeted:
        welcome_text = f"أهلاً بك يا {st.session_state.current_user}. تم تفعيل جميع الأنظمة. كيف يمكنني مساعدتك اليوم؟"
        speak(welcome_text)
        st.session_state.greeted = True

    # شريط الحالة
    st.markdown(f"<marquee style='background: #00f2ff; color: black; font-weight: bold; padding: 5px;'> SYSTEM ONLINE | USER: {st.session_state.current_user.upper()} | SECURITY: ENCRYPTED | AI CORE: ACTIVE </marquee>", unsafe_allow_html=True)

    # مركز التحكم الجانبي
    st.sidebar.subheader(f"🎙️ {TXT['voice']}")
    mic_data = mic_recorder(start_prompt="Speak to JARVIS", stop_prompt="Process Command", key='jarvis_mic')
    
    manual_cmd = st.sidebar.text_input("Manual Command (Voice Backup)")
    if manual_cmd:
        if "google" in manual_cmd.lower() or "بحث" in manual_cmd:
            speak(f"جاري البحث عن {manual_cmd} يا {st.session_state.current_user}")
            st.markdown(f'<meta http-equiv="refresh" content="2;url=https://www.google.com/search?q={manual_cmd}">', unsafe_allow_html=True)

    # روابط الذكاء الاصطناعي
    st.sidebar.markdown("---")
    st.sidebar.link_button("ChatGPT 4o", "https://chat.openai.com")
    st.sidebar.link_button("DeepSeek AI", "https://chat.deepseek.com")

    # قلب جارفيس النابض
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='jarvis-circle'><h1>JS</h1></div>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>JARVIS IS LISTENING, {st.session_state.current_user.upper()}</h2>", unsafe_allow_html=True)

    # التبويبات (Tabs)
    t1, t2, t3 = st.tabs(["🚀 Dashboard", "📊 Analytics", "🔐 Vault"])
    with t1:
        st.metric("System Health", "100%", delta="Secure")
        st.progress(100)
    with t2:
        st.info("نظام معالجة البيانات الضخمة جاهز.")
        st.file_uploader("Upload Data")
    with t3:
        st.warning("Secure Vault Active")

    if st.sidebar.button("🔴 SHUTDOWN"):
        st.session_state.auth = False
        st.session_state.greeted = False
        st.rerun()
