import streamlit as st
import math
import matplotlib.pyplot as plt

# -------------------- كلاس Fluid --------------------
class Fluid:
    def __init__(self, temperature=25, cp=2000, fractions=None, gas_M=0.018, gas_Z=1.0):
        self.temperature = temperature
        self.cp = cp
        self.fractions = fractions if fractions else {"oil":0.8,"water":0.1,"gas":0.1}
        self.rho_oil, self.rho_water = 850, 1000
        self.mu_oil, self.mu_water, self.mu_gas = 0.05, 0.001, 0.000018
        self.gas_M, self.gas_Z, self.R = gas_M, gas_Z, 8.314
        self.rho_gas = 1.2

    def rho_mix(self):
        return (self.fractions.get("oil",0)*self.rho_oil +
                self.fractions.get("water",0)*self.rho_water +
                self.fractions.get("gas",0)*self.rho_gas)

    def effective_mu(self):
        return (self.fractions.get("oil",0)*self.mu_oil +
                self.fractions.get("water",0)*self.mu_water +
                self.fractions.get("gas",0)*self.mu_gas)

    def update_properties(self, P_Pa):
        T_K = self.temperature + 273.15
        P_Pa = max(P_Pa, 101325)
        self.rho_gas = (P_Pa * self.gas_M) / (self.gas_Z * self.R * T_K)

# -------------------- كلاس Pipe --------------------
class Pipe:
    def __init__(self, D_mm, L_m, U=10, T_amb=25, segments=100, elev=0):
        self.D_mm, self.L_m, self.U, self.T_ambient = D_mm, L_m, U, T_amb
        self.segments, self.elevation_change = segments, elev

    def area(self): return math.pi * ((self.D_mm/1000)/2)**2
    def velocity(self, Q_m3h): return (Q_m3h/3600) / self.area()

    def multiphase_pressure_drop(self, Q_m3h, fluid, inlet_P_Pa, JT=0.2):
        segment_L = self.L_m / self.segments
        P, T = inlet_P_Pa, fluid.temperature
        pressures, temps, regimes = [P/100000], [T], []

        for _ in range(self.segments):
            if P <= 101325: break
            fluid.update_properties(P)
            v = self.velocity(Q_m3h)
            
            # Flow Regime logic
            g_frac = fluid.fractions.get("gas",0)
            regime = "Stratified" if g_frac < 0.2 else "Slug" if g_frac < 0.5 else "Bubbly"
            regimes.append(regime)

            # dP & dT
            Re = (fluid.rho_mix() * v * (self.D_mm/1000)) / fluid.effective_mu()
            f = 0.25/(math.log10((0.045/1000/(3.7*(self.D_mm/1000))) + (5.74/Re**0.9)))**2 if Re > 4000 else 64/Re
            dP = (f*(segment_L/(self.D_mm/1000)))*(fluid.rho_mix()*v**2/2) + (fluid.rho_mix()*9.81*(self.elevation_change/self.segments))
            
            T += (-(self.U*math.pi*(self.D_mm/1000)*segment_L*(T-self.T_ambient))/(fluid.rho_mix()*v*self.area()*fluid.cp) - JT*(dP/100000))
            P -= dP
            pressures.append(P/100000); temps.append(T)
        return pressures, temps, regimes[-1] if regimes else "N/A"

# -------------------- Streamlit Interface --------------------
st.set_page_config(page_title="Pipe Flow Simulator", layout="wide")
st.title("🛢️ Advanced Multiphase Pipe Simulator")

with st.sidebar:
    st.header("Fluid Properties")
    o = st.slider("Oil %", 0, 100, 80)
    w = st.slider("Water %", 0, 100, 10)
    g = st.slider("Gas %", 0, 100, 10)
    p_in = st.number_input("Inlet Pressure (Pa)", value=5000000)
    t_in = st.number_input("Inlet Temp (C)", value=25.0)
    
    st.header("Pipe Geometry")
    diam = st.number_input("Diameter (mm)", value=100.0)
    length = st.number_input("Length (m)", value=2000.0)
    elev = st.number_input("Elevation Change (m)", value=0.0)
    flow = st.number_input("Flow Rate (m3/h)", value=50.0)

if st.button("Run Simulation"):
    if (o + w + g) != 100:
        st.error("Error: Sum of fractions must be 100%")
    else:
        fluid = Fluid(temperature=t_in, fractions={"oil":o/100,"water":w/100,"gas":g/100})
        pipe = Pipe(D_mm=diam, L_m=length, elev=elev)
        pres, tmps, regime = pipe.multiphase_pressure_drop(flow, fluid, p_in)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Pressure Drop", f"{pres[0]-pres[-1]:.2f} Bar")
            st.metric("Flow Regime", regime)
        with col2:
            st.metric("Final Temperature", f"{tmps[-1]:.2f} °C")

        fig, ax = plt.subplots(1, 2, figsize=(12, 4))
        dist = [i*(length/100) for i in range(len(pres))]
        ax[0].plot(dist, pres, color='blue'); ax[0].set_title("Pressure Profile (Bar)")
        ax[1].plot(dist, tmps, color='red'); ax[1].set_title("Temperature Profile (°C)")
        st.pyplot(fig)
