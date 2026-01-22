import streamlit as st
from streamlit_mic_recorder import mic_recorder
import time

# --- إعدادات نظام جارفيس التفاعلي V8.0 ---
st.set_page_config(page_title="JARVIS v8 - LIVE INTERACTION", layout="wide", page_icon="🎙️")

# --- محرك الصوت المصري (The Voice of Jarvis) ---
def jarvis_speak(text):
    b64_text = text.replace("'", "\\'")
    js = f"""
    <script>
        var msg = new SpeechSynthesisUtterance('{b64_text}');
        msg.lang = 'ar-EG'; 
        msg.pitch = 0.9; 
        msg.rate = 1.0; 
        window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js, height=0)

# --- محرك التفاعل والرد الذكي (Automation Core) ---
def handle_action(command, user):
    cmd = command.lower()
    
    # 1. أوامر البحث الذكي
    if any(x in cmd for x in ["بحث", "جوجل", "google", "search"]):
        target = cmd.replace("google", "").replace("ابحث عن", "").replace("بحث", "").strip()
        jarvis_speak(f"تمام يا مستر {user}، هجيبلك قرار {target} من على جوجل حالا.")
        with st.spinner(f"جاري تنفيذ طلبك يا {user}..."):
            time.sleep(3) # وقت كافي عشان تسمع الرد وتستعد
            st.markdown(f'<meta http-equiv="refresh" content="0;url=https://www.google.com/search?q={target}">', unsafe_allow_html=True)
    
    # 2. أوامر الذكاء الاصطناعي
    elif any(x in cmd for x in ["شات", "chat", "ذكاء"]):
        jarvis_speak(f"من عيوني يا ريس، بفتحلك واجهة الذكاء الاصطناعي دلوقت.")
        with st.spinner("Loading AI Core..."):
            time.sleep(3)
            st.markdown(f'<meta http-equiv="refresh" content="0;url=https://chat.openai.com">', unsafe_allow_html=True)

    # 3. الدردشة التفاعلية
    elif any(x in cmd for x in ["يا جارفيس", "إزيك", "عامل إيه", "مين"]):
        jarvis_speak(f"أنا زي الفل يا ريس طول ما إنت تمام. أنا جارفيس، دراعك اليمين ومستعد لأي مأمورية.")

# --- التصميم السينمائي HUD (Neon Orb) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: radial-gradient(circle, #001529 0%, #000 100%); color: #00f2ff; font-family: 'Segoe UI', sans-serif; }
    [data-testid="stSidebar"] { background-color: #0a1016 !important; border-right: 1px solid #00f2ff; }
    .jarvis-orb { 
        border: 10px double #00f2ff; border-radius: 50%; width: 200px; height: 200px; 
        margin: auto; box-shadow: 0 0 50px #00f2ff;
        background: url('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndnB3ZzRyeGZ6ZzRyeGZ6ZzRyeGZ6ZzRyeGZ6ZzRyeGZ6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9iYyZjdD1n/3o7TKVUn7iM8FMEU24/giphy.gif');
        background-size: cover; background-position: center;
        animation: pulse 2s infinite alternate;
    }
    @keyframes pulse { from { transform: scale(1); box-shadow: 0 0 20px #00f2ff; } to { transform: scale(1.05); box-shadow: 0 0 80px #00f2ff; } }
    h1, h2 { font-family: 'Orbitron', sans-serif; text-shadow: 0 0 15px #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة الذاكرة (حمزة مسجل دائم) ---
if 'current_user' not in st.session_state:
    st.session_state.current_user = "حمزة"
if 'greeted' not in st.session_state:
    st.session_state.greeted = False

# الترحيب التلقائي عند التشغيل
if not st.session_state.greeted:
    jarvis_speak(f"أحلى مسا عليك يا مستر {st.session_state.current_user}. كل الأنظمة تحت أمرك، اؤمرني أعملك إيه؟")
    st.session_state.greeted = True

# الواجهة الرئيسية
st.markdown("<br><div class='jarvis-orb'></div>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center;'>JARVIS V8: {st.session_state.current_user.upper()}</h1>", unsafe_allow_html=True)

# مركز الأوامر الجانبي
st.sidebar.title("🎙️ مركز التحكم")
audio = mic_recorder(start_prompt="اتكلم يا ريس", stop_prompt="إنهاء", key='jarvis_engine')

st.sidebar.markdown("---")
manual_input = st.sidebar.text_input("اكتب أمرك هنا وجارفيس هيرد عليك")
if manual_input:
    handle_action(manual_input, st.session_state.current_user)

# روابط الوصول السريع
st.sidebar.subheader("🚀 Quick Access")
st.sidebar.link_button("Open ChatGPT", "https://chat.openai.com")
st.sidebar.link_button("Google Search", "https://www.google.com")

# لوحة البيانات
t1, t2, t3 = st.tabs(["🚀 Command Center", "📊 Analytics", "🔐 Vault"])
with t1:
    st.info(f"مرحباً يا مستر {st.session_state.current_user}.. أنا في وضع الاستعداد الدائم.")
    st.metric("الحالة الصحية للنظام", "100%", delta="Secure")

if st.sidebar.button("Restart JARVIS"):
    st.session_state.greeted = False
    st.rerun()
