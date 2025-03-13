import numpy as np

# Define the parameters for the Clam Lake ELF transmitter
frequency = 76  # Frequency in Hz
speed_of_light = 3e8  # Speed of light in meters per second (m/s)
antenna_length = 22530  # Antenna length in meters (14 miles ≈ 22,530 meters)
eta_0 = 377  # Free-space impedance in ohms
ionosphere_height = 60000  # Effective height of the ionosphere in meters
earth_conductivity = 0.005  # Earth conductivity in Siemens per meter (S/m), assumed value
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space in Henry per meter (H/m)

# Calculate the wavelength (lambda)
# Formula: λ = c / f
wavelength = speed_of_light / frequency  # in meters

# Calculate the angular frequency (omega)
# Formula: ω = 2 * π * f
omega = 2 * np.pi * frequency  # in radians per second (rad/s)

# Calculate the magnitude of the surface impedance (|Z_s|)
# For ELF frequencies: |Z_s| ≈ sqrt(ω * μ_0 / σ)
Z_s_magnitude = np.sqrt(omega * mu_0 / earth_conductivity)  # in ohms

# Calculate the radiation resistance (R_r)
# Formula: R_r = (Z_s^2 * π * l_y^2) / (4 * η_0 * h * λ)
R_r = (Z_s_magnitude**2 * np.pi * antenna_length**2) / (4 * eta_0 * ionosphere_height * wavelength)

# Print the result with scientific notation for readability
print(f"Radiation resistance R_r for Clam Lake ELF transmitter: {R_r:.2e} ohms")
