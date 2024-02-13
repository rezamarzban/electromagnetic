# electromagnetic
Electromagnetic formulas, simulation softwares and codes

The goal of these codes is knockout the complex physics electromagnetic equations and calculations by few lines of MATLAB and Python codes. It is head of complex physics electromagnetic equations and calculations, It goes straight to the point instead of giving foliage for solving the problem immediately.

All of physics electromagnetic chapter of a book gathered together in few lines of MATLAB and Python codes here. For example deriving and calculating Poynting Vector integral from farfield radiation electricity field equation for calculating most critical antenna behaviors such as radiated power and radiation resistance in few lines of Python code:

short dipole equations 

```
import sympy as sp

r, theta, phi, I, l, K, eth0 = sp.symbols('r theta phi I l K eth0', real=True)

E_theta = ((1j * K * I * l * eth0) / (4 * sp.pi * r)) * sp.sin(theta) * sp.exp(-1j * K * r)
H_phi = E_theta / eth0
S_theta = 0.5 * sp.re(E_theta * sp.conjugate(H_phi))
P_rad = sp.integrate(sp.integrate(S_theta * r**2 * sp.sin(theta), (theta, 0, sp.pi)), (phi, 0, 2*sp.pi))
Rr = 2 * P_rad / I**2

Power = P_rad.subs([(eth0, 377), (I, 2), (l, 0.1), (K, 2*sp.pi/6)]).evalf()  # Watts
Radiation_resistance = Rr.subs([(eth0, 377), (l, 0.1), (K, 2*sp.pi/6)]).evalf()  # Ohms

print(Power)
print(Radiation_resistance)
```
