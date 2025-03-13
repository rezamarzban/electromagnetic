import numpy as np
from scipy.optimize import fsolve

# Constants
c = 3e8          # Speed of light (m/s)
f = 82           # Frequency (Hz)
lambda_ = c / f  # Wavelength (m)
P_rad = 3.31     # Radiated power (W)
alpha = 1 / 1000 # Attenuation constant (dB/km)
r_0 = 1          # Reference distance (km)
P_sens = 1e-14   # Receiver sensitivity (W, -110 dBm)

# Function to compute received power (r in km)
def P_r(r):
    spreading_loss_db = 10 * np.log10(r / r_0)  # Cylindrical spreading loss
    attenuation_loss_db = alpha * r              # Exponential attenuation
    total_loss_db = spreading_loss_db + attenuation_loss_db
    P_r = P_rad * 10**(-total_loss_db / 10)
    return P_r

# Equation to solve: P_r(r) - P_sens = 0
def equation(r):
    return P_r(r) - P_sens

# Initial guess for r (in km)
r_initial_guess = 20000  # 20,000 km

# Solve for r
r_solution, = fsolve(equation, r_initial_guess)

# Output result
print(f"Maximum distance: {r_solution:.0f} km")
