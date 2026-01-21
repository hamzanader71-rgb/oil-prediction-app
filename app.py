import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor

st.set_page_config(page_title="Oil Production Predictor", layout="centered")

st.title("🛢️ Oil Production Prediction System")
st.write("Enter the parameters below to predict daily production.")

# قاعدة بيانات التدريب
data = {
    'pressure': [100, 150, 200, 250, 300, 350, 400, 450, 500],
    'temperature': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'drilling_speed': [10, 12, 15, 18, 20, 22, 25, 28, 30],
    'viscosity': [1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
    'depth': [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
    'production': [500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500]
}
df = pd.DataFrame(data)
model = GradientBoostingRegressor().fit(df.drop('production', axis=1), df['production'])

# مدخلات المستخدم
with st.container():
    p = st.number_input("Pressure (PSI)", value=280)
    t = st.number_input("Temperature (C)", value=85)
    s = st.number_input("Drilling Speed (m/h)", value=19)
    v = st.number_input("Viscosity (cp)", value=3.2)
    d = st.number_input("Depth (m)", value=2700)

if st.button("Predict Production", use_container_width=True):
    prediction = model.predict([[p, t, s, v, d]])
    st.success(f"🚀 Estimated Production: {prediction[0]:.2f} Barrels/Day")
    
    # الرسم البياني
    fig, ax = plt.subplots()
    ax.scatter(df['depth'], df['production'], color='blue', label='Historical Data')
    ax.scatter([d], [prediction[0]], color='red', s=100, label='Your Prediction', marker='*')
    ax.set_xlabel("Depth (m)")
    ax.set_ylabel("Production (Barrels)")
    ax.legend()
    st.pyplot(fig)
