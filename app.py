import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import hashlib
from datetime import datetime

# ----------------------
# إعداد قاعدة البيانات
# ----------------------
engine = create_engine("sqlite:///petroleum_db.db", echo=False)

# إنشاء الجداول الأساسية
with engine.connect() as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS production_data (
        Well_Name TEXT,
        Date DATE,
        Oil_Rate REAL,
        Gas_Rate REAL,
        Water_Rate REAL
    )
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS audit_log (
        username TEXT,
        action TEXT,
        timestamp DATETIME
    )
    """)
    # إضافة Admin افتراضي
    res = conn.execute("SELECT * FROM users WHERE username='admin'").fetchall()
    if not res:
        conn.execute(
            "INSERT INTO users (username,password,role) VALUES (:u,:p,:r)",
            {"u": "admin", "p": hashlib.sha256("admin123".encode()).hexdigest(), "r": "Admin"}
        )

# ----------------------
# وظائف الأمان
# ----------------------
def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    hashed = hash_pass(password)
    df = pd.read_sql(f"SELECT role FROM users WHERE username='{username}' AND password='{hashed}'", engine)
    return None if df.empty else df.iloc[0]["role"]

def log_action(username, action):
    pd.DataFrame([{
        "username": username,
        "action": action,
        "timestamp": datetime.now()
    }]).to_sql("audit_log", engine, if_exists="append", index=False)

# ----------------------
# واجهة المستخدم
# ----------------------
st.title("📦 Data Foundation System")

# تسجيل الدخول
username = st.text_input("Username")
password = st.text_input("Password", type="password")
role = authenticate(username, password)

if not role:
    st.warning("Login required | admin / admin123")
    st.stop()

st.success(f"Logged in as {role}")

# رفع البيانات
uploaded_file = st.file_uploader("Upload CSV or Excel", ["csv", "xlsx"])
if uploaded_file and st.button("Process & Save"):
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # تنظيف البيانات
    df.dropna(how="all", inplace=True)
    df.drop_duplicates(inplace=True)

    # التحقق من الأعمدة
    required = ["Well_Name","Date","Oil_Rate"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        st.error(f"Missing columns: {missing}")
    else:
        df.to_sql("production_data", engine, if_exists="append", index=False)
        log_action(username,"Uploaded production data")
        st.success("Data saved successfully")
        st.dataframe(df.head())
