import numpy as np
from scipy.optimize import fsolve

# Constants based on Clam Lake ELF transmitter
P_rad = 3        # Radiated power (W), approximate for Clam Lake
alpha = 0.001    # Attenuation constant (dB/km)
r_0 = 1          # Reference distance (km)
P_sens = 1e-14   # Receiver sensitivity (W, -110 dBm)

# Function to compute received power (r in km)
def P_r(r):
    """
    Calculate received power at distance r (km).
    """
    if r <= 0:  # Avoid division by zero or negative distances
        return P_rad
    spreading_loss_db = 10 * np.log10(r / r_0)  # Cylindrical spreading loss
    attenuation_loss_db = alpha * r             # Attenuation loss
    total_loss_db = spreading_loss_db + attenuation_loss_db
    return P_rad * 10**(-total_loss_db / 10)

# Function to solve: P_r(r) - P_sens = 0
def equation(r):
    return P_r(r) - P_sens

# Initial guess for the solver (in km)
r_initial_guess = 20000  # Approximately half Earth's circumference

# Solve for the distance where P_r equals P_sens
r_solution, = fsolve(equation, r_initial_guess)

# Output the result
print(f"Theoretical maximum receiving distance: {r_solution:.0f} km")
print("Note: Practically limited to ~20,000 km, half the Earth's circumference.")
