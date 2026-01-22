import streamlit as st
from streamlit_mic_recorder import mic_recorder
import time

# --- إعدادات نظام مستر حمزة السيادي V7.0 ---
st.set_page_config(page_title="JARVIS - HAMZA EDITION", layout="wide", page_icon="🎙️")

# --- محرك الصوت المصري المحسن (HD Human-like Voice) ---
def jarvis_speak(text):
    # كود جافا سكريبت متطور للنطق بالعامية المصرية بوضوح عالي
    b64_text = text.replace("'", "\\'")
    js = f"""
    <script>
        var msg = new SpeechSynthesisUtterance('{b64_text}');
        msg.lang = 'ar-EG'; 
        msg.pitch = 1.0;   // نبرة طبيعية
        msg.rate = 1.0;    // سرعة بشرية
        msg.volume = 1.0;  // أعلى وضوح
        window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js, height=0)

# --- محرك الأوامر الذكي ---
def handle_interaction(command, user):
    cmd = command.lower()
    if any(x in cmd for x in ["بحث", "جوجل", "google", "search"]):
        target = cmd.replace("google", "").replace("ابحث عن", "").replace("بحث", "").strip()
        jarvis_speak(f"من عيوني يا ريس.. هجيبلك قرار {target} من على جوجل حالا")
        time.sleep(2)
        st.markdown(f'<meta http-equiv="refresh" content="0;url=https://www.google.com/search?q={target}">', unsafe_allow_html=True)
    
    elif any(x in cmd for x in ["شات", "chat", "ذكاء"]):
        jarvis_speak(f"حاضر يا مستر حمزة.. بفتحلك الـ AI أهو، تؤمرني بحاجة تانية؟")
        st.markdown(f'<meta http-equiv="refresh" content="0;url=https://chat.openai.com">', unsafe_allow_html=True)

# --- التصميم السينمائي (Iron Man HUD) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: #000; color: #00f2ff; font-family: 'Segoe UI', sans-serif; }
    [data-testid="stSidebar"] { background-color: #0a1016 !important; border-right: 1px solid #00f2ff; }
    .jarvis-core { 
        border: 10px double #00f2ff; border-radius: 50%; width: 220px; height: 220px; 
        margin: auto; box-shadow: 0 0 50px #00f2ff; display: flex; 
        align-items: center; justify-content: center; background: radial-gradient(circle, #003344 0%, #000 70%);
        animation: pulse 2s ease-in-out infinite alternate;
    }
    @keyframes pulse { from { box-shadow: 0 0 20px #00f2ff; transform: scale(1); } to { box-shadow: 0 0 70px #00f2ff; transform: scale(1.05); } }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; text-shadow: 0 0 10px #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة الذاكرة (حمزة مسجل مرة واحدة فقط) ---
if 'current_user' not in st.session_state:
    st.session_state.current_user = "حمزة"  # السيستم حفظك خلاص يا ريس
if 'greeted' not in st.session_state:
    st.session_state.greeted = False

# --- الواجهة الحية ---
# الترحيب بيحصل أوتوماتيك أول ما تفتح
if not st.session_state.greeted:
    jarvis_speak(f"أحلى مسا عليك يا مستر حمزة.. أنا صحيت وجاهز، شبيك لبيك جارفيس بين ايديك")
    st.session_state.greeted = True

# شريط التنبيهات
st.markdown(f"<marquee style='color: #00f2ff; font-weight: bold;'> 🟢 ALL SYSTEMS ACTIVE | MASTER: HAMZA | SECURE CONNECTION ESTABLISHED </marquee>", unsafe_allow_html=True)

# قلب جارفيس النابض
st.markdown("<br><div class='jarvis-core'><h1>CORE</h1></div>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center;'>READY FOR YOUR COMMANDS, MR. {st.session_state.current_user.upper()}</h2>", unsafe_allow_html=True)

# مركز الأوامر الجانبي
st.sidebar.title("🎙️ جارفيس سامعك")
mic_data = mic_recorder(start_prompt="اتكلم يا ريس", stop_prompt="فهمتك", key='jarvis_mic')

st.sidebar.markdown("---")
manual_in = st.sidebar.text_input("أو اكتب هنا اللي في بالك")
if manual_in:
    handle_interaction(manual_in, st.session_state.current_user)

# الروابط الذكية
st.sidebar.subheader("🧠 Neural Links")
st.sidebar.link_button("ChatGPT 4o", "https://chat.openai.com")
st.sidebar.link_button("DeepSeek AI", "https://chat.deepseek.com")

# لوحة التحكم
t1, t2, t3 = st.tabs(["🚀 Control", "📊 Analytics", "🔐 Vault"])
with t1:
    st.info(f"مرحباً يا {st.session_state.current_user}، أنا أراقب جميع المدخلات الآن.")
    st.metric("System Stability", "Perfect", delta="100%")

if st.sidebar.button("Log out / إعادة تشغيل"):
    st.session_state.greeted = False
    st.rerun()
