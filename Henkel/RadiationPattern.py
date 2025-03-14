import numpy as np
from scipy.special import hankel2
import matplotlib.pyplot as plt

# Constants
f = 76  # Hz
c = 3e8  # m/s
omega = 2 * np.pi * f
k = omega / c
eta_0 = 376.73
mu_0 = 4 * np.pi * 1e-7
sigma = 5e-3
d = 100
I = 200
l_y = 22e3
h = 60e3

# Skin depth
gamma = np.sqrt(1j * omega * mu_0 * sigma)
delta = 1 / np.real(gamma)
print(f"Skin depth: {delta:.2f} m")

# Surface impedance
Z_s = 1j * omega * mu_0 / gamma
print(f"Surface impedance: {Z_s:.5f} Ohm")

# Effective wavenumber
k_eff = k + 1j * Z_s / (2 * eta_0 * h)
print(f"Effective k: {k_eff:.5e} rad/m (real: {k_eff.real:.5e}, imag: {k_eff.imag:.5e})")

# Radial distances
r = np.logspace(1, 6, 1000000)
kr_eff = k_eff * r

# Hankel function
H_0_2 = hankel2(0, kr_eff)

# Fields
E_z_far = (1j * eta_0 * k * I * l_y) / (2 * np.pi * h) * H_0_2 * np.exp(-d / delta)
H_phi_far = E_z_far / eta_0
S_r = 0.5 * np.real(E_z_far * np.conj(H_phi_far))

# Plotting
plt.figure(figsize=(10, 6))
plt.loglog(r, S_r)
plt.xlabel('Distance (km)')
plt.ylabel('Poynting Vector (W/m²)')
plt.grid(True, which="both")
plt.title('Radial Poynting Vector vs Distance (Full k_eff)')
plt.show()
