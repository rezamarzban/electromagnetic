import sympy as sp
from sympy import sqrt, pi, exp, I, simplify

# Define symbols (real and positive)
Z_s, I, l_y, eta_0, h, lambda_, r = sp.symbols('Z_s I l_y eta_0 h lambda r', real=True, positive=True)
k = sp.symbols('k', real=True, positive=True)

# Vertical electric field E_z (far-field approximation with phase term)
E_z = (Z_s**(3/2) * I * l_y / (2 * sqrt(eta_0) * h * sqrt(2 * lambda_ * r))) * exp(sqrt(-1)*(k*r - pi/4))

# Step 1: Compute |E_z|^2 (magnitude squared)
E_z_mag_sq = E_z * sp.conjugate(E_z)
E_z_mag_sq = simplify(E_z_mag_sq)  # Removes exponential terms (|exp(-j(...))|^2 = 1)

# Step 2: Poynting vector S_r = |E_z|^2 / (2 * Z_s)
S_r = E_z_mag_sq / (2 * Z_s)

# Step 3: Total radiated power (integrate S_r over cylindrical surface)
P = S_r * 2 * pi * r * h  # Surface area = 2πr * h
P = simplify(P)

# Step 4: Radiation resistance R_r = 2P / I^2
R_r = (2 * P) / (I**2)
R_r = simplify(R_r)

# Substitute k = 2π / lambda_
R_r = R_r.subs(k, 2 * pi / lambda_)
R_r = simplify(R_r)

# Final result
print("Radiation Resistance R_r:")
sp.pprint(R_r)
