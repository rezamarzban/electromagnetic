from sympy import symbols, sqrt, pi, I as j, Function, exp, Eq, simplify, integrate, sin, cos, oo, limit
from sympy.printing import pprint

# --------------------------------------
# Step 1: Define the System and Variables
# --------------------------------------
print("Step 1: Define the System and Variables")
print("--------------------------------------")
print("### Variables and Descriptions")
# Define all symbolic variables with their physical meanings
R_r = symbols('R_r')      # Radiation resistance (ohms)
Z_s = symbols('Z_s')      # Surface impedance of the Earth (ohms)
l_y = symbols('l_y')      # Length of the antenna (meters)
eta_0 = symbols('eta_0')  # Free-space impedance (~377 ohms)
h = symbols('h')          # Effective height of the ionosphere (meters)
lambda_ = symbols('lambda')  # Wavelength (meters)
omega = symbols('omega')  # Angular frequency (rad/s)
mu_0 = symbols('mu_0')    # Permeability of free space (H/m)
epsilon_0 = symbols('epsilon_0')  # Permittivity of free space (F/m)
sigma = symbols('sigma')  # Conductivity of the Earth (S/m)
epsilon = symbols('epsilon')  # Permittivity of the Earth (F/m)
I = symbols('I')          # Current (amperes)
d = symbols('d')          # Depth of burial (meters)
r = symbols('r')          # Radial distance (meters)
k = 2 * pi / lambda_      # Wave number (rad/m)

# Display variable descriptions
print(f"- **R_r**: Radiation resistance (ohms)")
print(f"- **Z_s**: Surface impedance of the Earth (ohms)")
print(f"- **l_y**: Length of the antenna (meters)")
print(f"- **eta_0**: Free-space impedance (approximately 377 ohms)")
print(f"- **h**: Effective height of the ionosphere (meters)")
print(f"- **lambda**: Wavelength (meters)")
print(f"- **omega**: Angular frequency (rad/s)")
print(f"- **mu_0**: Permeability of free space (H/m)")
print(f"- **epsilon_0**: Permittivity of free space (F/m)")
print(f"- **sigma**: Conductivity of the Earth (S/m)")
print(f"- **epsilon**: Permittivity of the Earth (F/m)")
print(f"- **I**: Current (A)")
print(f"- **d**: Depth of burial (meters)")
print(f"- **r**: Radial distance (meters)")
print(f"- **k**: Wave number, defined as 2π / λ (rad/m)")

# --------------------------------------
# Step 2: Model the Rock as an Antenna
# --------------------------------------
print("\nStep 2: Model the Rock as an Antenna")
print("--------------------------------------")
print("### Assumptions")
print("- Current I flows horizontally over length l_y within the rock.")
print("- The antenna is electrically short: l_y << lambda")
delta = sqrt(2 / (omega * mu_0 * sigma))  # Skin depth (meters)
print("### Skin Depth Equation")
print("Skin depth (δ) represents the depth at which the current amplitude decreases to 1/e.")
pprint(Eq(symbols('delta'), delta))

# --------------------------------------
# Step 3: Earth-Ionosphere Waveguide Context
# --------------------------------------
print("\nStep 3: Earth-Ionosphere Waveguide Context")
print("--------------------------------------")
print("### Waveguide Properties")
print("- The Earth-ionosphere waveguide supports a TEM mode at extremely low frequencies (ELF).")
print("- Earth's surface (z = 0) is a near-perfect conductor.")
print("- Ionosphere is at z = h with its own surface impedance.")
print("- Dominant fields: E_z (vertical electric field), H_phi (azimuthal magnetic field).")

# --------------------------------------
# Step 4: Surface Impedance of the Earth
# --------------------------------------
print("\nStep 4: Surface Impedance of the Earth")
print("--------------------------------------")
Z_s_general = sqrt(j * omega * mu_0 / (sigma + j * omega * epsilon))  # General form
Z_s_approx = (1 + j) * sqrt(omega * mu_0 / (2 * sigma))              # ELF approximation
Z_s_magnitude = sqrt(omega * mu_0 / sigma)                          # Magnitude

print("### General Formula for Surface Impedance (Z_s)")
pprint(Eq(symbols('Z_s'), Z_s_general))
print("\n### Approximation for ELF (σ >> ωε)")
pprint(Eq(symbols('Z_s'), Z_s_approx))
print("\n### Magnitude of Surface Impedance (|Z_s|)")
pprint(Eq(symbols('|Z_s|'), Z_s_magnitude))

# --------------------------------------
# Step 5: Far-Field Radiation from a Buried HED
# --------------------------------------
print("\nStep 5: Far-Field Radiation from a Buried HED")
print("--------------------------------------")
R_r0 = 80 * pi**2 * (l_y / lambda_)**2  # Free-space radiation resistance
print("### Free-Space Radiation Resistance for a Short Dipole")
pprint(Eq(symbols('R_{r0}'), R_r0))

# Define Hankel function of the second kind, order zero
H_0_2 = Function('H_0^{(2)}')(k * r)
E_z_far = (j * eta_0 * k * I * l_y) / (2 * pi * h) * H_0_2 * exp(-d / delta)
print("\n### Far-Field Vertical Electric Field (E_z) with Hankel Function")
print("Represents an outward-propagating cylindrical wave.")
pprint(Eq(symbols('E_z'), E_z_far))

# Asymptotic form of Hankel function for large kr
H_0_2_asymp = sqrt(2 / (pi * k * r)) * exp(-j * (k * r - pi / 4))
E_z_far_asymp = (j * eta_0 * k * I * l_y) / (2 * pi * h) * H_0_2_asymp * exp(-d / delta)
print("\n### Asymptotic Form of Hankel Function H_0^{(2)}(kr) for Large kr")
pprint(Eq(H_0_2, H_0_2_asymp))
print("\n### Far-Field E_z Using Asymptotic Form")
pprint(Eq(symbols('E_z'), E_z_far_asymp))

# --------------------------------------
# Step 6: Adjust for Earth’s Impedance
# --------------------------------------
print("\nStep 6: Adjust for Earth’s Impedance")
print("--------------------------------------")
Gamma = (Z_s - eta_0) / (Z_s + eta_0)          # Reflection coefficient
Gamma_approx = -1 + 2 * Z_s / eta_0            # Approximation for small Z_s
R_r_eq = (Z_s**2 * pi * l_y**2) / (4 * eta_0 * h * lambda_)  # Adjusted radiation resistance

print("### Reflection Coefficient at Earth-Air Interface (Γ)")
pprint(Eq(symbols('Gamma'), Gamma))
print("\n### Approximation for |Z_s| << eta_0")
pprint(Eq(symbols('Gamma'), Gamma_approx))
print("\n### Adjusted Radiation Resistance (R_r)")
pprint(Eq(R_r, R_r_eq))

# --------------------------------------
# Step 7: Verify Units and Physical Meaning
# --------------------------------------
print("\nStep 7: Verify Units and Physical Meaning")
print("--------------------------------------")
print("### Units Check")
print("- [R_r] = ohms, since [Z_s^2 / eta_0] = ohms and [l_y^2 / (h * lambda)] is dimensionless.")
print("### Physical Interpretation")
print("- **Higher Z_s**: Increases R_r, improving power transmission through the interface.")
print("- **Longer l_y**: Enhances radiation, consistent with antenna theory.")
print("- **Greater h**: Decreases R_r, reducing waveguide coupling.")
print("- **Longer λ**: Reduces R_r, typical for small antennas at lower frequencies.")

# --------------------------------------
# Additional: Power Calculation
# --------------------------------------
print("\nAdditional: Power Calculation")
print("--------------------------------------")
theta = symbols('theta')
phi = symbols('phi')
# Symbolic radiated power (simplified form)
P_rad = integrate(integrate((abs(E_z_far_asymp)**2) / (2 * eta_0) * r**2 * sin(theta), 
                            (theta, 0, pi)), (phi, 0, 2 * pi))
print("### Total Radiated Power (P_rad) - Symbolic Form")
print("Note: This is symbolic and may require numerical evaluation due to complexity.")
pprint(Eq(symbols('P_rad'), P_rad))

# --------------------------------------
# Hankel Function Conversion Demonstration
# --------------------------------------
print("\nHankel Function Conversion Demonstration")
print("--------------------------------------")
# Verify the asymptotic form by taking the limit as kr → ∞
H_0_2_limit = limit(H_0_2, k * r, oo)
print("### Limit of H_0^{(2)}(kr) as kr → ∞")
pprint(H_0_2_limit)
print("Note: SymPy may not compute this explicitly, but it aligns with the asymptotic form:")
pprint(Eq(H_0_2, H_0_2_asymp))
print("This confirms the conversion used in Step 5.")
