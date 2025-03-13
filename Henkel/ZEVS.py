import numpy as np

# Parameters
f = 82  # Frequency in Hz
c = 3e8  # Speed of light in m/s (approximated for simplicity)
lambda_ = c / f  # Wavelength in meters
eta_0 = 377  # Free-space impedance in ohms
h = 60e3  # Ionosphere height in meters
l_y = 60e3  # Antenna length in meters
sigma = 1e-2  # Earth conductivity in S/m
mu_0 = 4e-7 * np.pi  # Permeability of free space in H/m
omega = 2 * np.pi * f  # Angular frequency in rad/s

# Surface impedance magnitude
Z_s_mag = np.sqrt(omega * mu_0 / sigma)
Z_s_sq = Z_s_mag**2

# Radiation resistance
R_r = (Z_s_sq * np.pi * l_y**2) / (4 * eta_0 * h * lambda_)

print(f"Radiation resistance R_r: {R_r:.2e} ohms")
