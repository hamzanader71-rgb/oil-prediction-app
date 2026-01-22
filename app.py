import streamlit as st
from streamlit_mic_recorder import mic_recorder
import time

# --- إعدادات النظام السيادي V5.0 - JARVIS ACTIVE ---
st.set_page_config(page_title="JARVIS SOVEREIGN V5", layout="wide", page_icon="🎙️")

# --- محرك الصوت الفخم (Jarvis Cinematic Voice) ---
def jarvis_speak(text):
    b64_text = text.replace("'", "\\'")
    js = f"""
    <script>
        var msg = new SpeechSynthesisUtterance('{b64_text}');
        var voices = window.speechSynthesis.getVoices();
        msg.lang = 'ar-SA'; 
        msg.pitch = 0.75; // نبرة صوت عميقة وفخمة
        msg.rate = 0.85;  // سرعة متزنة لإعطاء هيبة
        window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js, height=0)

# --- محرك الأوامر التفاعلية (Automation Engine) ---
def handle_interaction(command, user):
    cmd = command.lower()
    if any(x in cmd for x in ["بحث", "جوجل", "google", "search"]):
        target = cmd.replace("google", "").replace("ابحث عن", "").replace("بحث", "").strip()
        jarvis_speak(f"بالتأكيد يا مستر {user}. جاري الولوج لقواعد البيانات والبحث عن {target}")
        time.sleep(2)
        st.markdown(f'<meta http-equiv="refresh" content="0;url=https://www.google.com/search?q={target}">', unsafe_allow_html=True)
    
    elif any(x in cmd for x in ["chat", "شات", "ذكاء"]):
        jarvis_speak(f"جاري تفعيل واجهة الذكاء الاصطناعي.. أهلاً بك في عالمك الخاص يا {user}")
        st.markdown(f'<meta http-equiv="refresh" content="0;url=https://chat.openai.com">', unsafe_allow_html=True)
        
    elif any(x in cmd for x in ["deep", "ديب"]):
        jarvis_speak("جاري الربط مع محرك ديب سيك..")
        st.markdown(f'<meta http-equiv="refresh" content="0;url=https://chat.deepseek.com">', unsafe_allow_html=True)

# --- التصميم المستقبلي (HUD Interface) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: #000; color: #00f2ff; font-family: 'Segoe UI', sans-serif; }
    .auth-box { background: rgba(0, 242, 255, 0.05); border: 2px solid #00f2ff; border-radius: 20px; padding: 40px; box-shadow: 0 0 30px rgba(0, 242, 255, 0.2); text-align: center; }
    .stButton>button { border-radius: 10px; background: transparent; border: 1px solid #00f2ff; color: #00f2ff; font-family: 'Orbitron'; transition: 0.5s; }
    .stButton>button:hover { background: #00f2ff; color: #000; box-shadow: 0 0 50px #00f2ff; }
    [data-testid="stSidebar"] { background-color: #0a1016 !important; border-right: 1px solid #00f2ff; }
    .jarvis-hud { border: 5px solid #00f2ff; border-radius: 50%; width: 220px; height: 220px; margin: auto; 
                   box-shadow: 0 0 40px #00f2ff, inset 0 0 20px #00f2ff; display: flex; align-items: center; 
                   justify-content: center; animation: pulse 3s infinite; }
    @keyframes pulse { 0% { box-shadow: 0 0 20px #00f2ff; } 50% { box-shadow: 0 0 60px #00f2ff; } 100% { box-shadow: 0 0 20px #00f2ff; } }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة الحالة ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'greeted' not in st.session_state: st.session_state.greeted = False

# --- بوابة الدخول ---
if not st.session_state.auth:
    st.markdown("<br><h1 style='text-align: center;'>SYSTEM PROTOCOL</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="auth-box">', unsafe_allow_html=True)
        name = st.text_input("IDENTIFY YOURSELF")
        if st.button("INITIATE BIOMETRIC SCAN"):
            if name:
                st.session_state.current_user = name
                st.session_state.auth = True
                st.rerun()
            else: st.error("Access Denied: Name Required")
        st.markdown('</div>', unsafe_allow_html=True)

# --- الواجهة الحية (بعد الدخول) ---
else:
    # الترحيب الفخم
    if not st.session_state.greeted:
        jarvis_speak(f"أهلاً بك يا مستر {st.session_state.current_user}. جارفيس نشط ومستعد لتلقي الأوامر.")
        st.session_state.greeted = True

    # الهيدر المتحرك
    st.markdown(f"<marquee style='color: #00f2ff; font-weight: bold;'> 🟢 ALL SYSTEMS GO | USER: {st.session_state.current_user.upper()} | ENCRYPTION: LEVEL 7 </marquee>", unsafe_allow_html=True)

    # شاشة جارفيس المركزية
    st.markdown("<div class='jarvis-hud'><h3>CORE</h3></div>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>ONLINE: {st.session_state.current_user.upper()}</h2>", unsafe_allow_html=True)

    # مركز الأوامر في الجنب
    st.sidebar.title("🎙️ VOICE COMMAND")
    audio = mic_recorder(start_prompt="تحدث الآن", stop_prompt="تحليل", key='jarvis_engine')
    
    st.sidebar.markdown("---")
    manual_in = st.sidebar.text_input("أمر يدوي (جارفيس سينفذه فوراً)")
    if manual_in:
        handle_interaction(manual_in, st.session_state.current_user)

    # روابط الذكاء الاصطناعي والبحث
    st.sidebar.subheader("🧠 Neural Links")
    st.sidebar.link_button("ChatGPT 4o", "https://chat.openai.com")
    st.sidebar.link_button("DeepSeek AI", "https://chat.deepseek.com")
    st.sidebar.link_button("Google Search", "https://www.google.com")

    # التبويبات للتوسع المستقبلي
    t1, t2, t3 = st.tabs(["🚀 Command", "📊 Analytics", "🔐 Vault"])
    with t1:
        st.info(f"مرحباً يا {st.session_state.current_user}، أنا أراقب جميع المدخلات الآن.")
        st.write("استخدم الميكروفون أو خانة الأوامر لفتح المواقع أو البحث.")
    
    if st.sidebar.button("SHUTDOWN"):
        jarvis_speak("إغلاق النظام.. إلى اللقاء يا مستر حمزة")
        time.sleep(2)
        st.session_state.auth = False
        st.session_state.greeted = False
        st.rerun()
