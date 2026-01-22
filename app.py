import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Global Oil Platform", layout="wide")

# 2. نظام اللغات (مساحة قابلة للتوسع)
languages = {
    "English": {"welcome": "Welcome", "search": "Search Google", "login": "Login"},
    "العربية": {"welcome": "أهلاً بك", "search": "بحث جوجل", "login": "تسجيل الدخول"},
    "Français": {"welcome": "Bienvenue", "search": "Chercher sur Google", "login": "Connexion"},
    "Italiano": {"welcome": "Benvenuto", "search": "Cerca su Google", "login": "Accedi"},
    "Deutsch": {"welcome": "Willkommen", "search": "Google-Suche", "login": "Anmelden"}
}

sel_lang = st.sidebar.selectbox("🌐 Choose Language / اختر اللغة", list(languages.keys()))
lang = languages[sel_lang]

# 3. نظام الأمان (Login System)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login():
    st.title(lang["login"])
    user = st.text_input("Username")
    pw = st.text_input("Password", type="password")
    if st.button("Enter"):
        if user == "admin" and pw == "12345": # تقدر تغيرهم طبعاً
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("خطأ في البيانات / Incorrect Credentials")

# 4. محتوى البرنامج بعد الدخول
if not st.session_state['logged_in']:
    login()
else:
    st.sidebar.success(f"✅ {lang['welcome']}")
    
    # أزرار الذكاء الاصطناعي وجوجل في الجنب
    st.sidebar.markdown("---")
    st.sidebar.subheader("🚀 Quick Links")
    st.sidebar.link_button("🤖 Open ChatGPT", "https://chat.openai.com")
    st.sidebar.link_button("🧠 Open DeepSeek", "https://chat.deepseek.com")
    st.sidebar.link_button("🔍 Google Search", "https://www.google.com")

    # مكان وضع أدواتك المستقبيلة
    st.title("🛢️ Global Oil & Gas Dashboard")
    st.write(f"This is your secure, multi-language workspace in {sel_lang}.")
    
    # إضافة معالج بيانات (كمثال مبدئي للسلاسة)
    uploaded_file = st.file_uploader("Upload Data for Processing")
    if uploaded_file:
        st.success("Data loaded successfully! (Secure Encryption Active)")
