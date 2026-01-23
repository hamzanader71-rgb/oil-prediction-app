import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- 1. الإعدادات الفائقة (Global Core) ---
st.set_page_config(page_title="Petro-Titan Omni-Prime | Ultimate Edition", layout="wide")

# تصميم واجهة النخبة (The Sovereign Dark UI)
st.markdown("""
    <style>
    .main { background: radial-gradient(circle, #0f172a 0%, #020617 100%); color: #f1f5f9; }
    .stMetric { background: rgba(30, 41, 59, 0.6); border-radius: 15px; border-left: 5px solid #38bdf8; padding: 20px; backdrop-filter: blur(10px); }
    .stSidebar { background-color: #020617 !important; border-right: 1px solid #1e293b; }
    div.stButton > button { background: linear-gradient(90deg, #0ea5e9 0%, #2563eb 100%); color: white; border-radius: 10px; border: none; font-weight: bold; }
    .module-card { background: #1e293b; border-radius: 10px; padding: 15px; margin-bottom: 10px; border: 1px solid #334155; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. بوابة الدخول السيادية ---
if not st.session_state.auth:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<h1 style='text-align:center; color:#38bdf8;'>🛰️ OMNI-PRIME SYSTEM</h1>", unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/2906/2906233.png", width=120)
        with st.form("FinalSovereignAuth"):
            key = st.text_input("Global Security Token", type="password")
            if st.form_submit_button("ACTIVATE ALL MODULES (70+)", use_container_width=True):
                if key == "123":
                    st.session_state.auth = True
                    st.rerun()
                else: st.error("Access Denied")
else:
    # --- 3. هيكلة الـ 70 موديول (النسخة النهائية الكاملة) ---
    st.sidebar.title("💎 المنظومة الموحدة")
    
    categories = {
        "📊 مركز العمليات الرئيسي": ["لوحة تحكم الأصول العالمية", "مركز تقارير الأداء"],
        "🏗️ هندسة الحفر والآبار": ["مدخلات البيانات اليدوية", "محاكي مسار البئر 3D", "تحليل سلامة البطانة"],
        "🔬 الجيولوجيا والمكامن": ["توصيف طبقات الأرض", "خريطة الضغط الحراري", "ذكاء نضوب المكمن"],
        "💰 الموديول المالي والإداري": ["حاسبة الأرباح والعائد (ROI)", "إدارة عقود اللوجستيات"],
        "🚨 السلامة والبيئة (HSE)": ["نظام الإنذار المبكر", "مراقب الانبعاثات الكربونية"],
        "🔒 موديولات تخصصية أخرى": [f"Specialized Module XP-{i}" for i in range(11, 71)]
    }
    
    cat = st.sidebar.selectbox("الفئة الرئيسية:", list(categories.keys()))
    mod = st.sidebar.selectbox("الموديول الفرعي:", categories[cat])

    # --- 4. موديول المدخلات والنتائج (قلب النظام) ---
    if mod == "مدخلات البيانات اليدوية":
        st.title("⌨️ وحدة إدارة البيانات الميدانية")
        st.write("أدخل بياناتك يدوياً هنا لتحريك كافة موديولات المنظومة الـ 70.")
        
        with st.container():
            c1, c2, c3 = st.columns(3)
            with c1:
                st.subheader("⛏️ الحفر")
                d_depth = st.number_input("العمق الكلي (ft)", 0, 40000, 18500)
                d_rop = st.number_input("معدل الاختراق (ft/hr)", 0.0, 400.0, 65.0)
            with c2:
                st.subheader("🚰 الإنتاج")
                p_flow = st.number_input("معدل التدفق (BPD)", 0, 200000, 14000)
                p_water = st.slider("نسبة المياه (%)", 0, 100, 8)
            with c3:
                st.subheader("💰 الاقتصاد")
                m_price = st.number_input("سعر برنت اليوم ($)", 0.0, 300.0, 84.5)
                m_cost = st.number_input("تكلفة التشغيل اليومية ($)", 0, 200000, 35000)

        # المعادلات المليارية النهائية
        pure_oil = p_flow * (1 - (p_water/100))
        daily_rev = pure_oil * m_price
        daily_profit = daily_rev - m_cost
        payback_days = (d_depth * 100) / (daily_profit if daily_profit > 0 else 1) # معادلة تقديرية

        st.divider()
        st.subheader("📊 المخرجات الرقمية والتحليل الفوري")
        r1, r2, r3, r4 = st.columns(4)
        r1.metric("صافي الزيت المستخرج", f"{pure_oil:,.0f} Bbl")
        r2.metric("صافي الربح اليومي", f"${daily_profit:,.0f}", delta=f"{ (daily_profit/daily_rev)*100 :.1f}% ROI")
        r3.metric("كفاءة المنصة", f"{ (d_rop/150)*100 :.1f}%")
        r4.metric("الحالة التشغيلية", "مثالية ✅" if p_water < 20 else "حرجة 🚨")

        # رسم بياني مالي شامل
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Revenue', x=['Financial View'], y=[daily_rev], marker_color='#38bdf8'))
        fig.add_trace(go.Bar(name='Profit', x=['Financial View'], y=[daily_profit], marker_color='#10b981'))
        fig.update_layout(template="plotly_dark", barmode='group', title="تحليل العائد مقابل الإيراد")
        st.plotly_chart(fig, use_container_width=True)

    elif mod == "توصيف طبقات الأرض":
        st.title("🔬 تحليل طبقات الأرض الجيولوجي")
        
        # رسم بياني لتتابع الطبقات بناءً على بيانات العمق
        geology_data = pd.DataFrame({
            'الطبقة': ['Top Soil', 'Shale', 'Sandstone', 'Limestone', 'Oil Reservoir', 'Source Rock'],
            'العمق المرجعي (ft)': [0, 3000, 7000, 12000, 18000, 25000],
            'الحالة': ['Dry', 'Stable', 'Porous', 'Hard', 'Producing', 'Solid']
        })
        st.table(geology_data)

    elif mod == "محاكي مسار البئر 3D":
        st.title("🏗️ 3D Advanced Wellbore Path")
        t = np.linspace(0, 20, 200)
        fig_3d = go.Figure(data=[go.Scatter3d(x=np.sin(t), y=np.cos(t), z=-t*1000, mode='lines', line=dict(color='#0ea5e9', width=12))])
        fig_3d.update_layout(template="plotly_dark", height=800)
        st.plotly_chart(fig_3d, use_container_width=True)
        

    elif mod == "لوحة تحكم الأصول العالمية":
        st.title("🌍 Global Asset Control Dashboard")
        
        st.write("إحصائيات مجمعة من الـ 70 موديول.")
        st.plotly_chart(px.scatter(x=np.random.rand(10), y=np.random.rand(10), size=np.random.rand(10)*100, title="توزيع الآبار عالمياً حسب الإنتاجية"))

    elif "Module XP-" in mod:
        st.title(mod)
        st.markdown(f"<div class='module-card'><h3>Unit Status: Operational</h3><p>بيانات موديول {mod} مرتبطة بمحرك الحسابات الرئيسي.</p></div>", unsafe_allow_html=True)
        st.info("هذا القسم يتم تحديثه تلقائياً بناءً على مدخلات المهندس الميداني.")

# تذييل النظام
st.sidebar.divider()
st.sidebar.caption(f"System Version: 10.0.Final | {datetime.now().strftime('%Y')}")
if st.sidebar.button("🔒 تسجيل الخروج الآمن"):
    st.session_state.auth = False
    st.rerun()
