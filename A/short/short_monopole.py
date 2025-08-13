import numpy as np
from scipy.integrate import dblquad

# Constants
c = 3e8  # Speed of light in vacuum (m/s)
mu0 = 4e-7 * np.pi  # Vacuum permeability (H/m)
epsilon0 = 8.854e-12  # Vacuum permittivity (F/m)
eta = np.sqrt(mu0 / epsilon0)  # Intrinsic impedance of free space (~376.73 Ω, close to 377 Ω)

# Parameters (example values; can be adjusted)
h = 3000  # Monopole antenna height (m); assumes h << lambda for short antenna approximation
f = 100  # Operating frequency (Hz); low frequency for validity
I0 = 1  # Peak current at base (A); normalized to 1A for resistance calculation

# Derived parameters
omega = 2 * np.pi * f  # Angular frequency (rad/s)
beta = omega / c  # Wavenumber (rad/m)
lambda_ = c / f  # Wavelength (m)

# Explanation of the calculation:
# For a short vertical monopole over a perfect ground plane with triangular current distribution I(z) = I0 (1 - z/h),
# the radiation fields in the upper hemisphere match those of an equivalent short dipole of length 2h in free space.
# The effective current moment (integral of I(z) dz over the equivalent dipole) is I0 * h.
# This accounts for the image current doubling the contribution compared to ignoring the ground plane.

# Compute the effective integral for the vector potential
integral_A = I0 * h  # Effective ∫ I(z) dz = I0 * h (includes image current contribution)

# Magnitude of the z-component of the vector potential A_z in far field (r dependence omitted as it cancels in power calc)
A_z = (mu0 / (4 * np.pi)) * integral_A

# Magnitude factor for E_theta (far-field electric field); full |E_theta| = E_theta_mag * sin(theta) / r
E_theta_mag = omega * A_z

# Integrand for radiated power using Poynting vector over the upper hemisphere
# P_rad = ∫∫ (|E_theta|^2 / (2 * eta)) r^2 sin(theta) d theta d phi
# With |E_theta| = E_theta_mag * sin(theta) / r, this simplifies to integrand ~ (E_theta_mag^2 * sin^3(theta)) / (2 * eta)
def integrand(theta, phi):
    sin_theta = np.sin(theta)
    return (E_theta_mag**2 * sin_theta**3) / (2 * eta)

# Perform double integral over phi (0 to 2π) and theta (0 to π/2 for monopole)
P_rad, _ = dblquad(integrand, 0, 2 * np.pi, lambda x: 0, lambda x: np.pi / 2)

# Radiation resistance: R_rad = 2 * P_rad / I0^2 (normalized to base current I0)
R_rad = 2 * P_rad / I0**2

# Output results
print(f"Radiation Resistance (First-Principles): {R_rad:.4e} Ω")
# Standard approximate formula for short monopole: R_rad ≈ 40 π² (h/λ)² Ω (using η ≈ 120π ≈ 377 Ω)
print(f"Formula Result: {40 * np.pi**2 * (h / lambda_)**2:.4e} Ω")
