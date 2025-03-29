syms r eta beta rho a h real

r = sqrt(rho^2 + h^2)
delta_Z = (-eta)/((2*pi*sin(beta*h)^2)) * (int(exp(-1i*2*beta*r)/rho, rho, a, inf) - 1*2*cos(beta*h)*int(exp(-beta*1i*(r + rho))/rho, rho, a, inf) - cos(beta*h)^2*int(exp(-1i*2*beta*rho)/rho, rho, a, inf))
