import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text # أضفنا text هنا
import hashlib
from datetime import datetime

# 1. إعداد قاعدة البيانات
engine = create_engine("sqlite:///petroleum_db.db", echo=False)

# 2. إنشاء الجداول (تم التعديل لتجنب الخطأ الذي ظهر لك)
with engine.connect() as conn:
    # يجب استخدام text() مع أي أمر SQL في النسخ الجديدة
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
    # تأكيد الحفظ
    conn.commit() 

# 3. بقية الكود الخاص بك (تأكد من إضافة text() قبل أي conn.execute)
st.title("📦 Data Foundation System")
st.info("تأكد من وجود ملف requirements.txt ليعمل التطبيق على السحاب")

# ... (بقية منطق تسجيل الدخول والرفع)
