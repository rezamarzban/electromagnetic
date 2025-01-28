import numpy as np
from scipy.integrate import dblquad

# Constants
c = 3e8  # Speed of light (m/s)
mu0 = 4e-7 * np.pi  # Permeability (H/m)
epsilon0 = 8.854e-12  # Permittivity (F/m)
eta = np.sqrt(mu0 / epsilon0)  # ~377 Ω

# Parameters
h = 3000  # Antenna height (m)
f = 100  # Frequency (Hz)
I0 = 1  # Assume 1A current for normalization

# Derived values
omega = 2 * np.pi * f
beta = 2 * np.pi * f / c
lambda_ = c / f

# Integrate A_z (simplified for h << lambda)
integral_A = (I0 * h) / 2  # ∫(1 - z/h) dz from 0 to h
A_z = (mu0 / (4 * np.pi)) * integral_A  # Far-field A_z (approximate)

# Electric field magnitude (E_theta)
E_theta_mag = omega * A_z  # |E_theta| = ω * |A_z| * sinθ (sinθ term handled in integral)

# Radiated power via Poynting vector integration
def integrand(theta, phi):
    sin_theta = np.sin(theta)
    return (E_theta_mag**2 * sin_theta**3) / (2 * eta)

# Integrate over θ: 0 to π/2 (monopole), φ: 0 to 2π
P_rad, _ = dblquad(integrand, 0, 2*np.pi, lambda x: 0, lambda x: np.pi/2)
R_rad = 2 * P_rad / I0**2  # Radiation resistance

print(f"Radiation Resistance (First-Principles): {R_rad:.4e} Ω")
print(f"Formula Result: {40 * np.pi**2 * (h/lambda_)**2:.4e} Ω")
