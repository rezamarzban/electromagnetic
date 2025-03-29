import sympy as sp

# Define the symbols
Z_s, l_y, h, lambda_ = sp.symbols('Z_s l_y h lambda')

# Define the free-space impedance
eta_0 = 377  # Ohms

# Radiation resistance equation
R_r = (Z_s**2 * sp.pi * l_y**2) / (4 * eta_0 * h * lambda_)

# Display the result
sp.pprint(R_r)
