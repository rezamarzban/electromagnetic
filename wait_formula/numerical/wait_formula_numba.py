from numba import jit
from numpy import *

@jit(nopython=True)
def compute_norm_deltaZ():
    beta = 2 * pi / 100
    a = 18
    h = 20

    rho = arange(a, 1000, 0.01)

    trapz1 = trapz(exp(-1j * 2 * beta * sqrt(rho ** 2 + h ** 2)) / rho, rho)
    trapz2 = trapz(exp(-beta * 1j * (sqrt(rho ** 2 + h ** 2) + rho)) / rho, rho)
    trapz3 = trapz(exp(-1j * 2 * beta * rho) / rho, rho)

    norm_deltaZ = (-2 / (sin(beta * h) ** 2)) * (trapz1 - 1 * 2 * cos(beta * h) * trapz2 - cos(beta * h) ** 2 * trapz3)
    
    return norm_deltaZ

print(compute_norm_deltaZ())
