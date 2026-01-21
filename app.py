import streamlit as st

# إعدادات التطبيق ليكون مريحاً للعين على الموبايل
st.set_page_config(page_title="Oil Expert Pro", page_icon="⛽", layout="centered")

# تنسيق الألوان (الوضع الليلي الفخم)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3em; background-color: #28a745; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("⛽ نظام خبير البترول")
st.write("مرحباً مهندس حمزة، أدخل بيانات البئر أدناه:")

# مدخلات البيانات بتصميم طولي للموبايل
pressure = st.number_input("الضغط الحالي (PSI)", value=1200)
temp = st.number_input("درجة الحرارة (F)", value=160)
depth = st.slider("العمق الإجمالي (قدم)", 1000, 10000, 5000)

if st.button("🚀 ابدأ تحليل التوقع"):
    # معادلة التوقع الاحترافية
    result = (pressure * 0.45) + (temp * 0.25) - (depth * 0.02)
    st.markdown("---")
    st.subheader(f"الإنتاج المقدر: {max(0, result):.2f} برميل/يوم")
    
    if result > 350:
        st.success("✅ أداء البئر ممتاز")
    else:
        st.warning("⚠️ إنتاج يحتاج لمراقبة فنية")
    ax.scatter(df['depth'], df['production'], color='blue', label='Historical Data')
    ax.scatter([d], [prediction[0]], color='red', s=100, label='Your Prediction', marker='*')
    ax.set_xlabel("Depth (m)")
    ax.set_ylabel("Production (Barrels)")
    ax.legend()
    st.pyplot(fig)
