import streamlit as st
from streamlit_mic_recorder import mic_recorder
import time

# --- إعدادات نظام جارفيس السيادي ---
st.set_page_config(page_title="JARVIS SOVEREIGN V3.0", layout="wide", page_icon="🎙️")

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
    /* أنيميشن الميكروفون */
    .mic-pulse { border-radius: 50%; background: rgba(0, 242, 255, 0.2); animation: pulse 2s infinite; }
    @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(0, 242, 255, 0.7); } 70% { box-shadow: 0 0 0 15px rgba(0, 242, 255, 0); } 100% { box-shadow: 0 0 0 0 rgba(0, 242, 255, 0); } }
    </style>
    """, unsafe_allow_html=True)

# --- نظام اللغات العالمي ---
DICT = {
    "English": {"greet": "SYSTEM ACTIVE", "scan": "BIOMETRIC SCAN", "secure": "SECURITY LEVEL: MAX", "voice": "JARVIS VOICE CORE"},
    "العربية": {"greet": "النظام نشط", "scan": "المسح البيومتري", "secure": "مستوى الأمان: أقصى", "voice": "مركز جارفيس الصوتي"},
    "Français": {"greet": "SYSTÈME ACTIF", "scan": "SCAN BIOMÉTRIQUE", "secure": "SÉCURITÉ: MAX", "voice": "NOYAU VOCAL"},
    "Italiano": {"greet": "SISTEMA ATTIVO", "scan": "SCANSIONE BIOMETRICA", "secure": "SICUREZZA: MAX", "voice": "NUCLEO VOCALE"},
    "Deutsch": {"greet": "SYSTEM AKTIV", "scan": "BIOMETRISCHER SCAN", "secure": "SICHERHEIT: MAX", "voice": "SPRACHKERN"}
}

if 'auth' not in st.session_state: st.session_state.auth = False

# القائمة الجانبية (Settings & Languages)
st.sidebar.title("⚙️ SYSTEM CORE")
lang_choice = st.sidebar.selectbox("Language / اللغة", list(DICT.keys()))
TXT = DICT[lang_choice]

# --- منطق الأوامر الصوتية (Voice Command Processor) ---
def execute_voice_command(command):
    cmd = command.lower()
    if "google" in cmd:
        term = cmd.replace("google", "").strip()
        st.sidebar.warning(f"JARVIS: Searching for {term}...")
        time.sleep(1)
        st.markdown(f'<meta http-equiv="refresh" content="0;url=https://www.google.com/search?q={term.replace(" ", "+")}">', unsafe_allow_html=True)
    elif "chat" in cmd:
        st.sidebar.info("JARVIS: Deploying AI Hub...")
        st.markdown('<meta http-equiv="refresh" content="0;url=https://chat.openai.com">', unsafe_allow_html=True)
    elif "deep" in cmd:
        st.sidebar.info("JARVIS: Syncing with DeepSeek...")
        st.markdown('<meta http-equiv="refresh" content="0;url=https://chat.deepseek.com">', unsafe_allow_html=True)
    elif "exit" in cmd or "lock" in cmd:
        st.session_state.auth = False
        st.rerun()

# --- واجهة الدخول (The Secure Gate) ---
if not st.session_state.auth:
    st.markdown("<br><br><h1 style='text-align: center;'>JARVIS PROTOCOL</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="auth-box">', unsafe_allow_html=True)
        st.write(f"### {TXT['scan']}")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("👤 FACE ID"):
                with st.spinner("Scanning..."):
                    time.sleep(2)
                    st.session_state.auth = True
                    st.rerun()
        with c2:
            if st.button("☝️ FINGERPRINT"):
                with st.spinner("Verifying..."):
                    time.sleep(2)
                    st.session_state.auth = True
                    st.rerun()
        st.markdown("---")
        u = st.text_input("ROOT USER")
        p = st.text_input("ACCESS CODE", type="password")
        if st.button("EXECUTE LOGIN"):
            if u == "admin" and p == "root":
                st.session_state.auth = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- واجهة التحكم الرئيسية (The Dashboard) ---
else:
    # شريط الحالة العلوي
    st.markdown(f"<marquee style='background: #00f2ff; color: black; font-weight: bold; padding: 5px;'> {TXT['greet']} | 🔓 {TXT['secure']} | VOICE COMMANDS: STANDBY | AI CORE: 100% </marquee>", unsafe_allow_html=True)

    # --- ميكروفون جارفيس في الجنب ---
    st.sidebar.markdown("---")
    st.sidebar.subheader(f"🎙️ {TXT['voice']}")
    
    # أداة تسجيل الصوت
    voice_data = mic_recorder(start_prompt="Speak to JARVIS", stop_prompt="Process", key='jarvis_engine')
    
    # محاكاة الأمر الصوتي (Text Backup)
    manual_cmd = st.sidebar.text_input("Command Input (Voice Backup)")
    if manual_cmd:
        execute_voice_command(manual_cmd)

    # روابط الذكاء الاصطناعي
    st.sidebar.markdown("---")
    st.sidebar.subheader("🧠 AI LINK")
    st.sidebar.link_button("ChatGPT 4o", "https://chat.openai.com")
    st.sidebar.link_button("DeepSeek AI", "https://chat.deepseek.com")

    # لوحة التحكم الرئيسية
    st.title("🎛️ GLOBAL COMMAND CENTER")
    t1, t2, t3 = st.tabs(["🚀 Control", "📊 Big Data", "🔐 Secure Vault"])
    
    with t1:
        st.subheader("System Performance")
        st.progress(98, text="AI Neural Network Stability")
        st.metric("Global Sync", "Active", "0.001ms Latency")
        
    with t2:
        st.info("نظام معالجة البيانات الضخمة جاهز. جارفيس في انتظار ملفاتك.")
        st.file_uploader("Upload Encrypted Data")

    with t3:
        st.error("Level 7 Encryption - Classified Data Only")
        st.text_area("Encrypted Notes Area")

    if st.sidebar.button("🔴 SHUTDOWN SYSTEM"):
        st.session_state.auth = False
        st.rerun()
