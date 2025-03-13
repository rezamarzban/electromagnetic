from sympy import symbols, sqrt, pi, I as j, Function, exp, Eq
from sympy.printing import pprint

# Step 1: Define the System and Variables
print("Step 1: Define the System and Variables")
print("--------------------------------------")
print("Variables and their descriptions:")
R_r = symbols('R_r')      # Radiation resistance
Z_s = symbols('Z_s')      # Surface impedance of the Earth
l_y = symbols('l_y')      # Length of the antenna
eta_0 = symbols('eta_0')  # Free-space impedance
h = symbols('h')          # Effective height of the ionosphere
lambda_ = symbols('lambda')  # Wavelength

print(f"R_r: Radiation resistance (ohms)")
print(f"Z_s: Surface impedance of the Earth (ohms)")
print(f"l_y: Length of the antenna (meters)")
print(f"eta_0: Free-space impedance (approximately 377 ohms)")
print(f"h: Effective height of the ionosphere (meters)")
print(f"lambda: Wavelength (meters)")

# Step 2: Model the Rock as an Antenna
print("\nStep 2: Model the Rock as an Antenna")
print("--------------------------------------")
I = symbols('I')          # Current
sigma = symbols('sigma')  # Conductivity of the Earth
omega = symbols('omega')  # Angular frequency
mu_0 = symbols('mu_0')    # Permeability of free space
delta = sqrt(2 / (omega * mu_0 * sigma))  # Skin depth

print("Assumptions: Current I flows horizontally over length l_y within the rock.")
print("The antenna is electrically short: l_y << lambda")
print("Skin depth equation:")
pprint(Eq(symbols('delta'), delta))

# Step 3: Earth-Ionosphere Waveguide Context
print("\nStep 3: Earth-Ionosphere Waveguide Context")
print("--------------------------------------")
print("The Earth-ionosphere waveguide supports a TEM mode at ELF frequencies.")
print("The Earth's surface (z = 0) is a near-perfect conductor.")
print("The ionosphere is at z = h with its own surface impedance.")
print("Dominant field components are E_z (vertical electric field) and H_phi (azimuthal magnetic field).")

# Step 4: Surface Impedance of the Earth
print("\nStep 4: Surface Impedance of the Earth")
print("--------------------------------------")
epsilon = symbols('epsilon')  # Permittivity of the Earth
Z_s_general = sqrt(j * omega * mu_0 / (sigma + j * omega * epsilon))
Z_s_approx = (1 + j) * sqrt(omega * mu_0 / (2 * sigma))
Z_s_magnitude = sqrt(omega * mu_0 / sigma)

print("General formula for surface impedance Z_s:")
pprint(Eq(symbols('Z_s'), Z_s_general))
print("\nApproximation for ELF frequencies (sigma >> omega * epsilon):")
pprint(Eq(symbols('Z_s'), Z_s_approx))
print("\nMagnitude of Z_s:")
pprint(Eq(symbols('|Z_s|'), Z_s_magnitude))

# Step 5: Far-Field Radiation from a Buried HED
print("\nStep 5: Far-Field Radiation from a Buried HED")
print("--------------------------------------")
k = 2 * pi / lambda_      # Wave number
d = symbols('d')          # Depth of burial
r = symbols('r')          # Radial distance
H_0_2 = Function('H_0^{(2)}')(k * r)  # Hankel function of the second kind, order zero

R_r0 = 80 * pi**2 * (l_y / lambda_)**2
E_z_far = (j * eta_0 * k * I * l_y) / (2 * pi * h) * H_0_2 * exp(-d / delta)

print("Free-space radiation resistance for a short dipole:")
pprint(Eq(symbols('R_{r0}'), R_r0))
print("\nFar-field vertical electric field in the waveguide:")
pprint(Eq(symbols('E_z'), E_z_far))
print("\nPower radiated (proportional form):")
print("P_rad ∝ (eta_0 * I^2 * l_y^2) / (2 * pi * h)")

# Step 6: Adjust for Earth’s Impedance
print("\nStep 6: Adjust for Earth’s Impedance")
print("--------------------------------------")
Gamma = (Z_s - eta_0) / (Z_s + eta_0)
Gamma_approx = -1 + 2 * Z_s / eta_0
R_r_eq = (Z_s**2 * pi * l_y**2) / (4 * eta_0 * h * lambda_)

print("Reflection coefficient at the Earth-air interface:")
pprint(Eq(symbols('Gamma'), Gamma))
print("\nApproximation for |Z_s| << eta_0:")
pprint(Eq(symbols('Gamma'), Gamma_approx))
print("\nDerived radiation resistance adjusted for Earth's impedance:")
pprint(Eq(R_r, R_r_eq))

# Step 7: Verify Units and Physical Meaning
print("\nStep 7: Verify Units and Physical Meaning")
print("--------------------------------------")
print("Units check: [R_r] = ohms, as [Z_s^2 / eta_0] = ohms, and [l_y^2 / (h * lambda)] is dimensionless.")
print("Physical interpretation:")
print("- Higher Z_s increases R_r, reflecting better power transmission through the interface.")
print("- Longer l_y enhances radiation, as expected for an antenna.")
print("- Greater h (ionosphere height) decreases R_r, reducing coupling to the waveguide.")
print("- Longer lambda (lower frequency) reduces R_r, typical for small antennas.")
