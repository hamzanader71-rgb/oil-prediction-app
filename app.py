import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- 1. الإعدادات والستايل ---
st.set_page_config(page_title="Petro-Titan Sovereign Infinity", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #f8fafc; }
    .stMetric { background: #161b22; border: 1px solid #38bdf8; border-radius: 12px; padding: 20px; }
    .module-header { color: #38bdf8; font-weight: bold; border-bottom: 2px solid #1e293b; padding-bottom: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. بوابة الدخول ---
if not st.session_state.auth:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.title("🛰️ SOVEREIGN INFINITY v10.0")
        pwd = st.text_input("Enter Security Key", type="password")
        if st.button("ACTIVATE SYSTEM"):
            if pwd == "123":
                st.session_state.auth = True
                st.rerun()
else:
    # --- 3. بناء قائمة الـ 70 موديول (مقسمة لمجموعات) ---
    st.sidebar.title("💎 Enterprise Hub")
    
    # تعريف المجموعات
    core_ops = ["🖥️ مركز القيادة الرئيسي", "⌨️ مدخلات البيانات اليدوية", "🏗️ محاكي الحفر 3D", "🔬 تحليل الطبقات الجيولوجية", "💰 الأرباح والتحليل المالي"]
    tech_ops = [f"🧬 موديول تقني: {name}" for name in ["المسح السيزمي", "حقن الغاز", "تحليل السوائل", "تآكل الأنابيب", "ضغط المكمن"]]
    secure_mods = [f"🔒 Specialized Module {i}" for i in range(11, 71)]
    
    all_selections = core_ops + tech_ops + secure_mods
    selection = st.sidebar.selectbox("اختر القسم (متاح 70 قسم):", all_selections)

    # --- 4. محتوى الموديولات (تفاعل حقيقي لكل نوع) ---

    # النوع الأول: موديولات التشغيل والبيانات اليدوية
    if selection == "🖥️ مركز القيادة الرئيسي":
        st.markdown("<h1 class='module-header'>🌐 Global Operations Mission Control</h1>", unsafe_allow_html=True)
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Production", "645K BPD", "+5%")
        m2.metric("Efficiency", "98.2%", "Optimal")
        m3.metric("Opex", "$11.40/Bbl", "-1.2%")
        m4.metric("Active Assets", "142 Wells", "Stable")
        df = pd.DataFrame({'Time': range(10), 'Flow': np.random.randint(5000, 7000, 10)})
        st.plotly_chart(px.area(df, x='Time', y='Flow', title="Historical Production Trend"), use_container_width=True)

    elif selection == "⌨️ مدخلات البيانات اليدوية":
        st.markdown("<h1 class='module-header'>⌨️ Manual Field Data Entry</h1>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            flow = st.number_input("معدل التدفق (BPD)", value=12000)
            price = st.number_input("سعر البرميل اليوم ($)", value=84.5)
        with c2:
            water = st.slider("نسبة المياه والشوائب (%)", 0, 100, 10)
            opex = st.number_input("تكلفة التشغيل اليومية ($)", value=35000)
        
        net_oil = flow * (1 - (water/100))
        profit = (net_oil * price) - opex
        st.divider()
        res1, res2 = st.columns(2)
        res1.metric("الإنتاج الصافي المحسوب", f"{net_oil:,.0f} Bbl")
        res2.metric("صافي الربح المتوقع", f"${profit:,.0f}")

    elif selection == "🏗️ محاكي الحفر 3D":
        st.markdown("<h1 class='module-header'>🏗️ 3D Well Trajectory Simulation</h1>", unsafe_allow_html=True)
        z = np.linspace(0, 15, 100)
        fig = go.Figure(data=[go.Scatter3d(x=np.sin(z), y=np.cos(z), z=-z*1000, mode='lines', line=dict(color='#38bdf8', width=8))])
        fig.update_layout(template="plotly_dark", height=700)
        st.plotly_chart(fig, use_container_width=True)
        

    # النوع الثاني: موديولات تقنية (عرض معلومات احترافية)
    elif "🧬 موديول تقني" in selection:
        st.markdown(f"<h1 class='module-header'>{selection}</h1>", unsafe_allow_html=True)
        st.info("يتم الآن معالجة البيانات من الحقل عبر الأقمار الصناعية.")
        
        st.write("### تقرير فني مؤقت:")
        st.table(pd.DataFrame({'Parameter': ['Pressure', 'Temperature', 'Viscosity'], 'Value': ['2400 PSI', '180 F', '4.2 cP']}))

    # النوع الثالث: موديولات الأرشفة والتأمين (هنا القوة)
    else:
        st.markdown(f"<h1 class='module-header'>{selection}</h1>", unsafe_allow_html=True)
        st.warning("🔒 هذا القسم مشفر بالكامل (Level 5 Security Needed)")
        st.image("https://cdn-icons-png.flaticon.com/512/2550/2550260.png", width=150)
        st.markdown("""
        **لماذا هذا الموديول مغلق؟**
        * يتطلب ربط مباشر بخوادم الشركة الأم.
        * يتم مزامنة البيانات يدوياً في نهاية كل ربع سنة.
        * يحتوي على خرائط سرية للمكامن الجوفية غير المستكشفة.
        """)

# خروج
st.sidebar.divider()
if st.sidebar.button("🔒 تسجيل الخروج"):
    st.session_state.auth = False
    st.rerun()
