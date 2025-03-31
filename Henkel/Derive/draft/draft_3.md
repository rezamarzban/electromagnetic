Rr equation derivation 

```python
import sympy as sp

# Define the symbols used in the derivation.
I0, ly, eta0, k, h, r, Zs, λ, theta, phi = sp.symbols('I0 ly eta0 k h r Zs λ theta phi', positive=True)
pi = sp.pi

# -----------------------------------------------------------------------------
# 1. Electric Field E_z in terms of the Hankel function of the second kind (order zero)
J0 = sp.besselj(0, k*r)  # Bessel function of the first kind
Y0 = sp.bessely(0, k*r)  # Bessel function of the second kind
H0_2 = J0 - sp.I * Y0  # Hankel function of the second kind

Ez = (sp.sqrt(30) * I0 * ly * eta0 * k / (32 * sp.sqrt(h * r))) * sp.sin(theta) * H0_2

# -----------------------------------------------------------------------------
# 2. Asymptotic Form of the Hankel Function H0^(2)(kr)
H0_asym = sp.sqrt(2/(pi*k*r)) * sp.exp(-sp.I*(k*r - sp.pi/4))

# Magnitude squared of the asymptotic form
H0_asym_abs_sq = sp.simplify(sp.Abs(H0_asym)**2)  # This simplifies to 2/(pi*k*r)

# -----------------------------------------------------------------------------
# 3. Power Density S_r
Ez_mag_sq = sp.simplify((sp.sqrt(30)*I0*ly*eta0*k/(32*sp.sqrt(h*r)))**2 * sp.sin(theta)**2 * (2/(pi*k*r)))
Sr = sp.simplify((1/sp.Integer(2)) * Ez_mag_sq / eta0)

# -----------------------------------------------------------------------------
# 4. Radiated Power P_r
reflection_factor = 4 * (Zs**2/eta0**2) * sp.cos(theta)**2
dA = r**2 * sp.sin(theta)

Pr = sp.simplify(sp.integrate(sp.integrate(Sr * reflection_factor * dA, (theta, 0, sp.pi)), (phi, 0, 2*sp.pi)))

# -----------------------------------------------------------------------------
# 5. Radiation Resistance R_r
Rr_expr = sp.solve(sp.Eq((1/sp.Integer(2))*I0**2 * sp.symbols('Rr', real=True), Pr), sp.symbols('Rr', real=True))[0]

# Replace k with 2π/λ
Rr_expr = Rr_expr.subs(k, 2*pi/λ)
Rr_expr = sp.simplify(Rr_expr)

# -----------------------------------------------------------------------------
# Display the derived equations with explanations.
print("Derived Equations (Symbolic Form):\n")

print("1. Electric Field E_z (in terms of the Hankel function):")
sp.pretty_print(Ez)

print("\n2. Asymptotic Form of H0^(2)(kr):")
sp.pretty_print(H0_asym)
print("Its magnitude squared simplifies to:")
sp.pretty_print(H0_asym_abs_sq)

print("\n3. Power Density S_r:")
sp.pretty_print(Sr)

print("\n4. Radiated Power P_r (after angular integration):")
sp.pretty_print(Pr)

print("\n5. Radiation Resistance R_r:")
sp.pretty_print(Rr_expr)
```
