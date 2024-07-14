from numpy import *

beta = 2 * pi / 100
a = 18
h = 20

rho = arange(a, 1000, 0.01)

norm_deltaZ = (-2 / (sin(beta * h) ** 2)) * (trapz(exp(-1j * 2 * beta * sqrt(rho ** 2 + h ** 2)) / rho, rho) - 1 * 2 * cos(beta * h) * trapz(exp(-beta * 1j * (sqrt(rho ** 2 + h ** 2) + rho)) / rho, rho) - cos(beta * h) ** 2 * trapz(exp(-1j * 2 * beta * rho) / rho, rho))

print(norm_deltaZ)
