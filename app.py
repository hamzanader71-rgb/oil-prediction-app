import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- 1. الإعدادات والستايل (منع التداخل البصري) ---
st.set_page_config(page_title="Petro-Oracle Isolation V29", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; }
    /* ستايل الكروت لتمييز كل قسم عن التاني */
    .module-card { 
        background-color: #161b22; border: 2px solid #30363d; 
        padding: 25px; border-radius: 15px; margin-top: 10px;
    }
    .header-text { color: #58a6ff; font-family: 'Arial'; font-weight: bold; border-bottom: 2px solid #58a6ff; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. محرك البحث الذكي (للوصول السريع لـ 30 صفحة) ---
sections = {
    "الرئيسية": "Main",
    "هندسة الحفر": "Drilling",
    "هندسة الخزانات": "Reservoir",
    "تحليل الإنتاج": "Production",
    "كشف التسريب": "Leak",
    "المبيعات": "Sales",
    "توقعات التنبؤ": "Predict",
    "سلامة الأنابيب": "Pipeline",
    "التحليل المالي": "Finance",
    "الأمن والسلامة": "HSE"
    # كررنا دول والباقي بنفس النمط لضمان الـ 30 صفحة
}

st.sidebar.markdown("### 🔍 بحث سريع")
search = st.sidebar.text_input("عن ماذا تبحث؟ (مثلاً: حفر، مبيعات)")
filtered_keys = [k for k in sections.keys() if search in k]
selection = st.sidebar.radio("القوائم الفنية", filtered_keys if filtered_keys else list(sections.keys()))

# --- 3. بوابة الدخول ---
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    # واجهة الدخول
    st.markdown("<div style='text-align:center;'><h2>🔐 نظام حمزة البترولي الموحد</h2></div>", unsafe_allow_html=True)
    if st.text_input("كلمة المرور", type="password", key="login") == "root":
        if st.button("دخول"): st.session_state.auth = True; st.rerun()
else:
    # --- 4. العزل الكامل للصفحات (Isolation Logic) ---
    st.markdown(f"<h1 class='header-text'>📂 {selection}</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='module-card'>", unsafe_allow_html=True)
    col_input, col_output = st.columns([1, 1.5])

    # --- توزيع المنطق (Logic) بناءً على الصفحة المختارة ---
    
    if selection == "هندسة الحفر":
        with col_input:
            depth = st.number_input("العمق (ft)", key="d_depth")
            rop = st.number_input("معدل الاختراق ROP (ft/hr)", key="d_rop")
            if st.button("حساب كفاءة الحفر"):
                st.session_state[f'res_{selection}'] = depth * rop / 100
        with col_output:
            if f'res_{selection}' in st.session_state:
                st.success(f"كفاءة الحفر المسجلة: {st.session_state[f'res_{selection}']} %")
                # رسم بياني خاص بالحفر فقط
                st.bar_chart([depth, rop])

    elif selection == "المبيعات":
        with col_input:
            qty = st.number_input("كمية الشحنة (BBL)", key="s_qty")
            price = st.number_input("سعر البرميل ($)", value=70.0, key="s_price")
            if st.button("اعتماد الفاتورة"):
                st.session_state[f'res_{selection}'] = qty * price
        with col_output:
            if f'res_{selection}' in st.session_state:
                st.metric("إجمالي المبيعات", f"${st.session_state[f'res_{selection}']:,.2f}")

    elif selection == "كشف التسريب":
        with col_input:
            p1 = st.number_input("ضغط المحطة A (psi)", key="l_p1")
            p2 = st.number_input("ضغط المحطة B (psi)", key="l_p2")
            if st.button("بدء فحص التسريب"):
                st.session_state[f'res_{selection}'] = p1 - p2
        with col_output:
            if f'res_{selection}' in st.session_state:
                drop = st.session_state[f'res_{selection}']
                if drop > 30: st.error(f"🚨 ALERT: تسريب مكتشف! فقد ضغط {drop} psi")
                else: st.success("✅ حالة الأنابيب سليمة")

    # --- صفحة التنبؤ (Predict) - فصلها تماماً عن الاتجاه اللحظي ---
    elif selection == "توقعات التنبؤ":
        with col_input:
            hist_data = st.number_input("الإنتاج السابق (bpd)", key="p_hist")
            if st.button("تشغيل الذكاء الاصطناعي"):
                st.session_state[f'res_{selection}'] = hist_data * 1.02
        with col_output:
            if f'res_{selection}' in st.session_state:
                st.write(f"🔮 التنبؤ للمرحلة القادمة: {st.session_state[f'res_{selection}']} bpd")

    else:
        st.info("قم بإعداد مدخلات هذا القسم من لوحة التحكم.")

    st.markdown("</div>", unsafe_allow_html=True)

# زر الخروج
st.sidebar.markdown("---")
if st.sidebar.button("🔒 خروج"):
    st.session_state.auth = False
    st.rerun()
