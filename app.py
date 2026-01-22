import streamlit as st
from streamlit_mic_recorder import mic_recorder
import time

# --- إعدادات نظام جارفيس المصري V6.0 ---
st.set_page_config(page_title="JARVIS EGYPT V6", layout="wide", page_icon="🎙️")

# --- محرك الصوت العامي الذكي (The Soul Engine) ---
def jarvis_speak(text):
    # كود جافا سكريبت متطور للنطق بالعامية المصرية ونبرة بشرية
    b64_text = text.replace("'", "\\'")
    js = f"""
    <script>
        var msg = new SpeechSynthesisUtterance('{b64_text}');
        var voices = window.speechSynthesis.getVoices();
        msg.lang = 'ar-EG'; 
        msg.pitch = 1.0;   // نبرة طبيعية مش روبوت
        msg.rate = 1.0;    // سرعة الكلام العادي
        window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js, height=0)

# --- محرك الأوامر والتفاعل (Automation Logic) ---
def handle_interaction(command, user):
    cmd = command.lower()
    if any(x in cmd for x in ["بحث", "جوجل", "google", "search"]):
        target = cmd.replace("google", "").replace("ابحث عن", "").replace("بحث", "").strip()
        jarvis_speak(f"من عيوني يا مستر {user}.. هجيبلك قرار {target} من على جوجل حالا")
        time.sleep(2)
        st.markdown(f'<meta http-equiv="refresh" content="0;url=https://www.google.com/search?q={target}">', unsafe_allow_html=True)
    
    elif any(x in cmd for x in ["شات", "chat", "ذكاء"]):
        jarvis_speak(f"حاضر يا باشا.. بفتحلك الذكاء الاصطناعي أهو، تؤمرني بحاجة تانية؟")
        st.markdown(f'<meta http-equiv="refresh" content="0;url=https://chat.openai.com">', unsafe_allow_html=True)
    
    elif any(x in cmd for x in ["اسمك", "إنت مين"]):
        jarvis_speak(f"أنا جارفيس يا مستر {user}.. دراعك اليمين، ورقبتي سدادة في أي مصلحة")

# --- التصميم السينمائي HUD (Iron Man Style) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: #000; color: #00f2ff; font-family: 'Segoe UI', sans-serif; }
    .auth-box { background: rgba(0, 242, 255, 0.05); border: 2px solid #00f2ff; border-radius: 20px; padding: 40px; box-shadow: 0 0 30px rgba(0, 242, 255, 0.2); text-align: center; }
    .stButton>button { border-radius: 10px; background: transparent; border: 1px solid #00f2ff; color: #00f2ff; font-family: 'Orbitron'; transition: 0.5s; }
    .stButton>button:hover { background: #00f2ff; color: #000; box-shadow: 0 0 50px #00f2ff; }
    [data-testid="stSidebar"] { background-color: #0a1016 !important; border-right: 1px solid #00f2ff; }
    .jarvis-core { 
        border: 8px double #00f2ff; border-radius: 50%; width: 200px; height: 200px; 
        margin: auto; box-shadow: 0 0 40px #00f2ff; display: flex; 
        align-items: center; justify-content: center; background: radial-gradient(circle, #003344 0%, #000 70%);
        animation: pulse 2s ease-in-out infinite alternate;
    }
    @keyframes pulse { from { box-shadow: 0 0 20px #00f2ff; transform: scale(1); } to { box-shadow: 0 0 60px #00f2ff; transform: scale(1.05); } }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة حالة النظام ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'greeted' not in st.session_state: st.session_state.greeted = False

# --- بوابة الدخول (Identification) ---
if not st.session_state.auth:
    st.markdown("<br><h1 style='text-align: center;'>JARVIS PROTOCOL</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="auth-box">', unsafe_allow_html=True)
        name = st.text_input("قولي اسمك إيه يا باشا؟")
        if st.button("افتح يا سمسم"):
            if name:
                st.session_state.current_user = name
                st.session_state.auth = True
                st.rerun()
            else: st.error("لازم تقولي اسمك الأول")
        st.markdown('</div>', unsafe_allow_html=True)

# --- واجهة جارفيس الحية ---
else:
    # الترحيب الشعبي الفخم
    if not st.session_state.greeted:
        jarvis_speak(f"أحلى مسا عليك يا مستر {st.session_state.current_user}.. أنا صحيت وجاهز، شبيك لبيك جارفيس بين ايديك")
        st.session_state.greeted = True

    # شريط التنبيهات
    st.markdown(f"<marquee style='color: #00f2ff; font-weight: bold;'> 🟢 النظام شغال بامتياز | الريس {st.session_state.current_user} منور الدنيا | الأمان: 100% </marquee>", unsafe_allow_html=True)

    # قلب جارفيس النابض
    st.markdown("<br><div class='jarvis-core'><h2>LIVE</h2></div>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>Ready for Action, {st.session_state.current_user}</h2>", unsafe_allow_html=True)

    # مركز الأوامر الجانبي
    st.sidebar.title("🎙️ جارفيس سامعك")
    mic_data = mic_recorder(start_prompt="اتكلم يا كبير", stop_prompt="فهمتك خلاص", key='jarvis_mic')
    
    st.sidebar.markdown("---")
    manual_in = st.sidebar.text_input("أو اكتب هنا اللي إنت عاوزه")
    if manual_in:
        handle_interaction(manual_in, st.session_state.current_user)

    # الروابط الذكية
    st.sidebar.subheader("🧠 Neural Links")
    st.sidebar.link_button("ChatGPT 4o", "https://chat.openai.com")
    st.sidebar.link_button("DeepSeek AI", "https://chat.deepseek.com")

    # التبويبات (Dashboard)
    t1, t2, t3 = st.tabs(["🚀 التحكم", "📊 البيانات", "🔐 الخزنة"])
    with t1:
        st.info(f"مرحباً يا {st.session_state.current_user}، جارفيس تحت أمرك في أي لحظة.")
        st.metric("حالة السيرفر", "زي الفل", delta="Stable")
    
    if st.sidebar.button("اقفل النظام"):
        jarvis_speak(f"ماشي يا مستر {st.session_state.current_user}.. هتوحشنا، أشوفك على خير")
        time.sleep(2)
        st.session_state.auth = False
        st.session_state.greeted = False
        st.rerun()
