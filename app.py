import streamlit as st
from streamlit_mic_recorder import mic_recorder
import datetime
import webbrowser
import time

# --- إعدادات النسخة الجبارة V9 ---
st.set_page_config(page_title="JARVIS SYSTEM - HAMZA", layout="wide")

# --- محرك الصوت (المصري المحسن) ---
def speak(text):
    b64_text = text.replace("'", "\\'")
    js = f"""
    <script>
        var msg = new SpeechSynthesisUtterance('{b64_text}');
        msg.lang = 'ar-EG'; msg.pitch = 1.0; msg.rate = 1.0;
        window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js, height=0)

# --- معالجة الأوامر (المنطق اللي إنت بعته) ---
def process_hamza_logic(command):
    cmd = command.lower()
    user = st.session_state.current_user

    # 1. الوقت والتاريخ
    if "الوقت" in cmd:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"الوقت دلوقتي {now} يا مستر {user}")
    
    elif "التاريخ" in cmd:
        today = datetime.date.today()
        speak(f"النهارده {today} يا ريس")

    # 2. يوتيوب (pywhatkit logic)
    elif "شغل" in cmd:
        query = cmd.replace("شغل", "").strip()
        speak(f"من عيوني، هشغلك {query} على يوتيوب حالا")
        time.sleep(2)
        st.markdown(f'<meta http-equiv="refresh" content="0;url=https://www.youtube.com/results?search_query={query}">', unsafe_allow_html=True)

    # 3. ويكيبيديا والبحث
    elif "بحث" in cmd or "معلومات عن" in cmd:
        query = cmd.replace("بحث", "").replace("عن", "").strip()
        speak(f"بدوّرلك على {query} في الموسوعة يا مستر {user}")
        time.sleep(2)
        st.markdown(f'<meta http-equiv="refresh" content="0;url=https://ar.wikipedia.org/wiki/{query}">', unsafe_allow_html=True)

    # 4. فتح المواقع
    elif "افتح" in cmd:
        if "جوجل" in cmd:
            speak("بفتحلك جوجل يا باشا")
            st.markdown('<meta http-equiv="refresh" content="0;url=https://www.google.com">', unsafe_allow_html=True)
        elif "فيسبوك" in cmd:
            speak("حاضر، بفتح الفيسبوك")
            st.markdown('<meta http-equiv="refresh" content="0;url=https://www.facebook.com">', unsafe_allow_html=True)

    # 5. الملاحظات
    elif "ملاحظة" in cmd or "اكتب" in cmd:
        speak("أنا سجلت الملاحظة دي عندي في الذاكرة يا ريس")
        st.session_state.notes.append(f"{datetime.datetime.now()}: {cmd}")

# --- التصميم (HUD Interface) ---
st.markdown("""
    <style>
    .stApp { background: #000; color: #00f2ff; }
    .core-node { 
        border: 5px solid #00f2ff; border-radius: 50%; width: 180px; height: 180px; 
        margin: auto; box-shadow: 0 0 40px #00f2ff; 
        background: radial-gradient(circle, #005566 0%, #000 80%);
        animation: rotate 5s linear infinite;
    }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

# --- إدارة الذاكرة ---
if 'current_user' not in st.session_state: st.session_state.current_user = "حمزة"
if 'notes' not in st.session_state: st.session_state.notes = []
if 'greeted' not in st.session_state: st.session_state.greeted = False

# الترحيب
if not st.session_state.greeted:
    speak(f"النظام في الخدمة. أهلاً بك يا مستر حمزة")
    st.session_state.greeted = True

# الواجهة
st.markdown("<div class='core-node'></div>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center;'>HAMZA COMMAND CENTER</h2>", unsafe_allow_html=True)

# الميكروفون (الاستماع)
st.sidebar.title("🎙️ LIVE MICROPHONE")
audio_data = mic_recorder(start_prompt="اتكلم يا ريس", stop_prompt="فهمت خلاص", key='main_mic')

# تنفيذ الأوامر (لو كتبت أو اتكلمت)
manual_cmd = st.sidebar.text_input("أمر يدوي (زي الكود اللي بعته)")
if manual_cmd:
    process_hamza_logic(manual_cmd)

# عرض الملاحظات (زي خاصية الملاحظات في كودك)
if st.session_state.notes:
    with st.expander("📝 الملاحظات المسجلة"):
        for n in st.session_state.notes:
            st.write(n)
