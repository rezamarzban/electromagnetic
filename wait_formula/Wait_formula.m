syms r eta beta rho a h real

beta = 2*pi/100;
a = 18;
h = 20;

r = sqrt(rho^2 + h^2);

expr0 = (-eta)/((2*pi*sin(beta*h)^2));
expr1 = int(exp(-1i*2*beta*r)/rho, rho, a, inf); 
expr2 = -1*2*cos(beta*h)*int(exp(-beta*1i*(r + rho))/rho, rho, a, inf); 
expr3 = -cos(beta*h)^2*int(exp(-1i*2*beta*rho)/rho, rho, a, inf);

norm = 4*pi*expr0/eta;

norm_deltaZ_re = real(vpa(norm) * (vpa(expr1) + vpa(expr2) + vpa(expr3)))
