import math

# Constants
c = 3e8          # Speed of light (m/s)
mu_0 = 4 * math.pi * 1e-7  # Permeability of free space (H/m)
eta_0 = 377      # Free-space impedance (Ω)
pi = math.pi

# ZEVS parameters
f = 82           # Frequency (Hz)
l_y = 60000      # Antenna length (m)
h = 80000        # Ionosphere height (m)
sigma = 1e-4     # Earth conductivity (S/m)

# Calculations
omega = 2 * pi * f              # Angular frequency (rad/s)
lambda_ = c / f                 # Wavelength (m)
Z_s = math.sqrt(omega * mu_0 / sigma)  # Surface impedance magnitude (Ω)
Z_s_squared = Z_s**2            # Z_s^2 (Ω^2)

numerator = Z_s_squared * pi * l_y**2
denominator = 4 * eta_0 * h * lambda_
R_r = numerator / denominator   # Radiation resistance (Ω)

# Output
print(f"Frequency: {f} Hz")
print(f"Wavelength: {lambda_:,.0f} m")
print(f"Surface Impedance |Z_s|: {Z_s:.3f} Ω")
print(f"Z_s^2: {Z_s_squared:.3f} Ω^2")
print(f"Radiation Resistance R_r: {R_r:.3e} Ω")
