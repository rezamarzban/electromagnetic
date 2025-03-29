import numpy as np
import matplotlib.pyplot as plt

# Define dipole antenna parameters
frequency = 2.4e9  # Frequency in Hertz (example: 2.4 GHz)
lambda_ = 300000000 / frequency  # Wavelength
dipole_length = lambda_ / 2  # Half-wavelength dipole

I = 1  # Antenna current in Ampere
K = (2 * np.pi / lambda_)  # Wave number
r_farfield = (2 * lambda_)  # Farfield occur at distance greater than lambda/4
n = 360  # Number of each theta and phi elements

# Define spatial coordinates
theta = np.linspace(0, 2 * np.pi, n)  # Azimuthal angle
phi = np.linspace(0, 2 * np.pi, n)  # Polar angle

# Far-field electric field components for a half-wavelength dipole
E_theta = ((1j * K * I * dipole_length * 377) / (4 * np.pi * r_farfield)) * np.sin(theta) * np.exp(-1j * K * r_farfield)
E_phi = np.zeros_like(phi)  # Assume E_phi is negligible for a dipole along the z-axis

# Magnetic field components are derived from the electric field
H_theta = E_phi / 377
H_phi = E_theta / 377

# Define Poynting vector components
S_theta = 0.5 * np.real(E_theta * np.conj(H_phi))
S_phi = 0.5 * np.real(E_phi * np.conj(H_theta))

# Calculate total Poynting vector magnitude
S_total = np.sqrt(S_theta**2 + S_phi**2)

# Plot azimuth radiation pattern
plt.polar(theta - (np.pi / 2), S_total)
plt.title('Radiation pattern (Theta)')
plt.legend(['Watt/m²'])
