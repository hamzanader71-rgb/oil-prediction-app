import math
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

# -------------------- كلاس Fluid --------------------
class Fluid:
    def __init__(self, temperature=25, cp=2000, fractions=None, gas_M=0.018, gas_Z=1.0):
        self.temperature = temperature
        self.cp = cp
        self.fractions = fractions if fractions else {"oil":0.8,"water":0.1,"gas":0.1}
        self.rho_oil=850
        self.rho_water=1000
        self.rho_gas=1.2
        self.mu_oil=0.05
        self.mu_water=0.001
        self.mu_gas=0.000018
        self.gas_M = gas_M
        self.gas_Z = gas_Z
        self.R = 8.314

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
    def __init__(self, name, D_mm, L_m, roughness_mm=0.045, U_W_m2K=10, T_ambient_C=25, segments=100, elevation_change_m=0):
        self.name=name
        self.D_mm=D_mm
        self.L_m=L_m
        self.roughness_mm=roughness_mm
        self.U = U_W_m2K
        self.T_ambient = T_ambient_C
        self.fittings = {}
        self.segments = segments
        self.elevation_change = elevation_change_m

    def add_fitting(self, name, count=1):
        self.fittings[name]=self.fittings.get(name,0)+count

    def area(self):
        D=self.D_mm/1000
        return math.pi*(D/2)**2

    def velocity(self,Q_m3h):
        return (Q_m3h/3600)/self.area()

    def reynolds(self,Q_m3h,fluid):
        D=self.D_mm/1000
        v=self.velocity(Q_m3h)
        mu_eff = fluid.effective_mu()
        rho_eff = fluid.rho_mix()
        return (rho_eff * v * D)/mu_eff

    def friction_factor(self,Re):
        D=self.D_mm/1000
        eps=self.roughness_mm/1000
        if Re<2300: return 64/Re
        if Re<=4000: return 0.5*(64/2300 + 0.25/(math.log10((eps/(3.7*D)) + (5.74/Re**0.9)))**2)
        return 0.25/(math.log10((eps/(3.7*D)) + (5.74/Re**0.9)))**2

    def minor_losses(self):
        FITTING_K={"elbow_90":0.9,"elbow_45":0.4,"gate_valve_open":0.2,"tee_run":0.3}
        total=0
        for f,count in self.fittings.items():
            total+=FITTING_K.get(f,0)*count
        return total

    def temperature_drop_segment(self, fluid, Q_m3h, segment_length):
        v=self.velocity(Q_m3h)
        D=self.D_mm/1000
        A_surface=math.pi*D*segment_length
        m_dot=fluid.rho_mix()*v*self.area()
        delta_T=-(self.U*A_surface*(fluid.temperature-self.T_ambient))/(m_dot*fluid.cp)
        return delta_T

    # -------------------- Multiphase Flow with Flow Regime --------------------
    def multiphase_pressure_drop(self, Q_m3h, fluid, inlet_pressure_Pa, JT_coeff=0.2):
        g = 9.81
        segment_length = self.L_m / self.segments
        P = inlet_pressure_Pa
        T = fluid.temperature
        pressures = [P/100000]
        temps = [T]
        flow_regimes = []

        for i in range(self.segments):
            if P <= 101325:  # حماية الانهيار عند الضغط الجوي
                break
            fluid.update_properties(P)
            v_total = self.velocity(Q_m3h)

            # Homogeneous model: الأطوار تتحرك بنفس السرعة
            gas_frac = fluid.fractions.get("gas",0)
            if gas_frac < 0.2:
                flow_regime = "Stratified"
            elif gas_frac < 0.5:
                flow_regime = "Slug"
            else:
                flow_regime = "Dispersed/Bubbly"
            flow_regimes.append(flow_regime)

            Re_mix = self.reynolds(Q_m3h, fluid)
            f = self.friction_factor(Re_mix)
            dP_friction = (f*(segment_length/(self.D_mm/1000)) + self.minor_losses()/self.segments)*(fluid.rho_mix()*v_total**2/2)
            dP_gravity = fluid.rho_mix()*g*(self.elevation_change/self.segments)
            dP = dP_friction + dP_gravity

            dT_JT = JT_coeff*(dP/100000)
            delta_T_heat = self.temperature_drop_segment(fluid, Q_m3h, segment_length)
            T += (delta_T_heat - dT_JT)
            fluid.temperature = T
            P -= dP

            pressures.append(P/100000)
            temps.append(T)

        return pressures, temps, flow_regimes[-1] if flow_regimes else "N/A"

    def plot_profile(self, Q_m3h, fluid, inlet_pressure_Pa):
        pressures, temps, final_regime = self.multiphase_pressure_drop(Q_m3h, fluid, inlet_pressure_Pa)
        segment_length = self.L_m / self.segments
        plt.figure(figsize=(10,5))
        plt.subplot(1,2,1)
        plt.plot([i*segment_length for i in range(len(pressures))],pressures)
        plt.xlabel('Length (m)')
        plt.ylabel('Pressure (Bar)')
        plt.title('Pressure Profile')

        plt.subplot(1,2,2)
        plt.plot([i*segment_length for i in range(len(temps))],temps)
        plt.xlabel('Length (m)')
        plt.ylabel('Temperature (C)')
        plt.title('Temperature Profile')

        plt.tight_layout()
        plt.show()

# -------------------- GUI --------------------
class PipeSimulatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Pipe Flow Simulator")

        # Fluid inputs
        tk.Label(master, text="Oil %:").grid(row=0,column=0)
        self.oil_var=tk.DoubleVar(value=80)
        tk.Entry(master,textvariable=self.oil_var).grid(row=0,column=1)

        tk.Label(master, text="Water %:").grid(row=1,column=0)
        self.water_var=tk.DoubleVar(value=10)
        tk.Entry(master,textvariable=self.water_var).grid(row=1,column=1)

        tk.Label(master, text="Gas %:").grid(row=2,column=0)
        self.gas_var=tk.DoubleVar(value=10)
        tk.Entry(master,textvariable=self.gas_var).grid(row=2,column=1)

        tk.Label(master, text="Temp (C):").grid(row=3,column=0)
        self.temp_var=tk.DoubleVar(value=25)
        tk.Entry(master,textvariable=self.temp_var).grid(row=3,column=1)

        tk.Label(master, text="Pressure (Pa):").grid(row=4,column=0)
        self.pressure_var=tk.DoubleVar(value=5e6)
        tk.Entry(master,textvariable=self.pressure_var).grid(row=4,column=1)

        tk.Label(master, text="Gas M (kg/mol):").grid(row=5,column=0)
        self.gasM_var=tk.DoubleVar(value=0.018)
        tk.Entry(master,textvariable=self.gasM_var).grid(row=5,column=1)

        tk.Label(master, text="Gas Z:").grid(row=6,column=0)
        self.gasZ_var=tk.DoubleVar(value=1.0)
        tk.Entry(master,textvariable=self.gasZ_var).grid(row=6,column=1)

        # Pipe inputs
        tk.Label(master, text="Pipe Name:").grid(row=0,column=2)
        self.pipe_name_var=tk.StringVar(value="Pipe1")
        tk.Entry(master,textvariable=self.pipe_name_var).grid(row=0,column=3)

        tk.Label(master, text="D (mm):").grid(row=1,column=2)
        self.D_var=tk.DoubleVar(value=100)
        tk.Entry(master,textvariable=self.D_var).grid(row=1,column=3)

        tk.Label(master, text="L (m):").grid(row=2,column=2)
        self.L_var=tk.DoubleVar(value=2000)
        tk.Entry(master,textvariable=self.L_var).grid(row=2,column=3)

        tk.Label(master, text="Elevation (m):").grid(row=3,column=2)
        self.elevation_var=tk.DoubleVar(value=0)
        tk.Entry(master,textvariable=self.elevation_var).grid(row=3,column=3)

        tk.Label(master, text="Flow Rate (m3/h):").grid(row=4,column=2)
        self.flow_var=tk.DoubleVar(value=50)
        tk.Entry(master,textvariable=self.flow_var).grid(row=4,column=3)

        # Buttons
        tk.Button(master, text="Run Simulation", command=self.run_simulation).grid(row=7,column=1)
        tk.Button(master, text="Plot Profile", command=self.plot_profile).grid(row=7,column=3)

        # Results
        self.results_text=tk.Text(master,height=10,width=60)
        self.results_text.grid(row=8,column=0,columnspan=4)

    def run_simulation(self):
        oil=self.oil_var.get()
        water=self.water_var.get()
        gas=self.gas_var.get()
        total=oil+water+gas
        if not math.isclose(total,100):
            messagebox.showwarning("Warning","Sum of fractions must be 100%")
            return
        fractions={"oil":oil/100,"water":water/100,"gas":gas/100}
        fluid=Fluid(temperature=self.temp_var.get(),fractions=fractions, gas_M=self.gasM_var.get(), gas_Z=self.gasZ_var.get())
        pipe=Pipe(self.pipe_name_var.get(), D_mm=self.D_var.get(), L_m=self.L_var.get(), elevation_change_m=self.elevation_var.get())
        pressures, temps, flow_regime = pipe.multiphase_pressure_drop(self.flow_var.get(), fluid, self.pressure_var.get())
        self.results_text.delete(1.0,tk.END)
        self.results_text.insert(tk.END,f"Pressure Drop: {pressures[0]-pressures[-1]:.3f} Bar\nFinal Temp: {temps[-1]:.2f} C\nFlow Regime: {flow_regime}")

    def plot_profile(self):
        oil=self.oil_var.get()
        water=self.water_var.get()
        gas=self.gas_var.get()
        fractions={"oil":oil/100,"water":water/100,"gas":gas/100}
        fluid=Fluid(temperature=self.temp_var.get(),fractions=fractions, gas_M=self.gasM_var.get(), gas_Z=self.gasZ_var.get())
        pipe=Pipe(self.pipe_name_var.get(), D_mm=self.D_var.get(), L_m=self.L_var.get(), elevation_change_m=self.elevation_var.get())
        pipe.plot_profile(self.flow_var.get(), fluid, self.pressure_var.get())

# -------------------- تشغيل الواجهة --------------------
if __name__=="__main__":
    root=tk.Tk()
    gui=PipeSimulatorGUI(root)
    root.mainloop()
