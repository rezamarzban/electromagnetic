from sympy import *

r, eta, beta, rho, a, h = symbols('r eta beta rho a h', real=True)
delta_Z = (-eta)/((2*pi*sin(beta*h)**2)) * (Integral(exp(-1j*2*beta*r)/rho, (rho, a, oo)) - 1*2*cos(beta*h)*Integral(exp(-beta*1j*(r + rho))/rho, (rho, a, oo)) - cos(beta*h)**2*Integral(exp(-1j*2*beta*rho)/rho, (rho, a, oo)))
