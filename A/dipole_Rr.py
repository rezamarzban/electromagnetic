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
dipole_length = wavelength / 2  # Half-wave dipole length (m)
I0 = 1.0  # Peak current (A)
k = 2 * pi / wavelength  # Wavenumber (rad/m)
omega = 2 * pi * frequency  # Angular frequency (rad/s)

# Far-field approximation for magnetic vector potential
def A_z(theta, r):
    """
    Magnetic vector potential A_z for a half-wave dipole in the far-field.
    :param theta: Angle from the dipole axis (radians)
    :param r: Distance from the antenna (m)
    :return: A_z (Wb/m)
    """
    # Integral of the current distribution (simplified using far-field approximation)
    integral = (2 / k) * (np.cos((pi / 2) * np.cos(theta)) / np.sin(theta)**2)
    return (mu_0 * I0 * np.exp(-1j * k * r) / (4 * pi * r)) * integral

# Electric field from A_z
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
    Total radiated power by integrating the Poynting vector.
    :param r: Distance from the antenna (m)
    :return: P_rad (W)
    """
    def integrand(theta):
        return poynting(theta, r) * 2 * pi * r**2 * np.sin(theta)

    P_rad, _ = quad(integrand, 0, pi)
    return P_rad

# Radiation resistance
R_rad = 2 * total_power(r=1e6) / I0**2  # r is arbitrary in the far-field
print(f"Radiation Resistance: {R_rad:.2f} ohms")
