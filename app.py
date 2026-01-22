import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text # أضفنا text هنا
import hashlib
from datetime import datetime

# إعداد قاعدة البيانات
engine = create_engine("sqlite:///petroleum_db.db", echo=False)

# إنشاء الجداول - تم التعديل باستخدام text() لتجنب الخطأ
def init_db():
    with engine.begin() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
        """))
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS production_data (
            Well_Name TEXT,
            Date DATE,
            Oil_Rate REAL,
            Gas_Rate REAL,
            Water_Rate REAL
        )
        """))
        # إضافة مسؤول افتراضي إذا لم يوجد
        check_admin = conn.execute(text("SELECT * FROM users WHERE username='admin'")).fetchone()
        if not check_admin:
            conn.execute(text("INSERT INTO users (username, password, role) VALUES (:u, :p, :r)"),
                {"u": "admin", "p": hashlib.sha256("admin123".encode()).hexdigest(), "r": "Admin"})

init_db()

# وظائف الأمان
def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    hashed = hash_pass(password)
    with engine.connect() as conn:
        query = text("SELECT role FROM users WHERE username=:u AND password=:p")
        res = conn.execute(query, {"u": username, "p": hashed}).fetchone()
        return res[0] if res else None

# واجهة التطبيق
st.title("📦 Data Foundation System")

if 'auth' not in st.session_state:
    st.session_state.auth = None

if st.session_state.auth is None:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        role = authenticate(username, password)
        if role:
            st.session_state.auth = role
            st.rerun()
        else:
            st.error("خطأ في البيانات")
else:
    st.success(f"مرحباً بك بصلاحية: {st.session_state.auth}")
    
    # قسم الرفع
    uploaded_file = st.file_uploader("ارفع ملف البيانات (CSV or Excel)", type=["csv", "xlsx"])
    if uploaded_file and st.button("معالجة وحفظ"):
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        
        # تنظيف البيانات
        df.dropna(how="all", inplace=True)
        
        # حفظ في القاعدة
        df.to_sql("production_data", engine, if_exists="append", index=False)
        st.success("تم حفظ البيانات بنجاح في قاعدة البيانات السحابية")
        st.dataframe(df.head())
# ... (بقية منطق تسجيل الدخول والرفع)
