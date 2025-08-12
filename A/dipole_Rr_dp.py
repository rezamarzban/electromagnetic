import numpy as np
from scipy.constants import mu_0, epsilon_0, pi, c
from scipy.integrate import quad

# Constants
mu_0 = 4 * pi * 1e-7  # Permeability of free space (H/m)
epsilon_0 = 8.854187817e-12  # Permittivity of free space (F/m)
c = 3e8  # Speed of light (m/s)
eta_0 = np.sqrt(mu_0 / epsilon_0)  # Intrinsic impedance of free space (ohms)

# Antenna parameters
frequency = 100e6  # Frequency (Hz)
wavelength = c / frequency  # Wavelength (m)
L_over_lambda = 0.5  # Length over wavelength (0.001 to 1000)
dipole_length = L_over_lambda * wavelength  # Dipole length (m)
I0 = 1.0  # Peak current (A)
k = 2 * pi / wavelength  # Wavenumber (rad/m)
omega = 2 * pi * frequency  # Angular frequency (rad/s)
beta = k * dipole_length / 2  # beta = k L / 2

# Far-field approximation for magnetic vector potential
def A_z(theta, r):
    """
    Magnetic vector potential A_z for a center-fed dipole in the far-field.
    :param theta: Angle from the dipole axis (radians)
    :param r: Distance from the antenna (m)
    :return: A_z (Wb/m)
    """
    sin_theta = np.sin(theta)
    if np.abs(sin_theta) < 1e-8:  # Handle theta near 0 or pi
        return (mu_0 * I0 * np.exp(-1j * k * r) / (4 * pi * r)) * dipole_length
    cos_term = np.cos(beta * np.cos(theta)) - np.cos(beta)
    denom = np.sin(theta)**2
    integral = (2 / k) * cos_term / denom if np.abs(denom) > 1e-12 else dipole_length
    return (mu_0 * I0 * np.exp(-1j * k * r) / (4 * pi * r)) * integral

# Electric field
def E_theta(theta, r):
    """
    Far-field electric field E_theta.
    :param theta: Angle from the dipole axis (radians)
    :param r: Distance from the antenna (m)
    :return: E_theta (V/m)
    """
    return -1j * omega * A_z(theta, r) * np.sin(theta)

# Poynting vector magnitude
def poynting(theta, r):
    """
    Time-averaged Poynting vector magnitude.
    :param theta: Angle from the dipole axis (radians)
    :param r: Distance from the antenna (m)
    :return: S (W/m^2)
    """
    E = E_theta(theta, r)
    H = E / eta_0
    return 0.5 * np.real(E * np.conj(H))

# Total radiated power
def total_power(r):
    """
    Total radiated power by integrating the Poynting vector over theta from 0 to pi/2.
    :param r: Distance from the antenna (m)
    :return: P_rad (W)
    """
    def integrand(theta):
        return poynting(theta, r) * 2 * pi * r**2 * np.sin(theta)
    
    # Integrate from 0 to pi/2 and double for symmetry
    P_rad, _ = quad(integrand, 0, pi/2, epsabs=1e-8, epsrel=1e-4, limit=2000)
    return 2 * P_rad  # Account for theta from pi/2 to pi

# Radiation resistance
if np.abs(np.sin(beta)) < 1e-12:
    print(f"Warning: L/lambda = {L_over_lambda:.3f} leads to zero feedpoint current. "
          "R_rad may be undefined or require maximum current normalization.")
else:
    R_rad = 2 * total_power(r=1e6) / I0**2  # Far-field, r arbitrary
    print(f"Radiation Resistance for L/lambda = {L_over_lambda:.3f}: {R_rad:.2f} ohms")
