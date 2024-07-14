beta = 2*pi/100;
a = 18;
h = 20;

rho = a:0.01:1000;

norm_deltaZ = (-2/(sin(beta*h)^2)) * (trapz(rho, exp(-1i*2*beta*sqrt(rho.^2 + h^2))./rho) - 1*2*cos(beta*h)*trapz(rho, exp(-beta*1i*(sqrt(rho.^2 + h^2) + rho))./rho) - cos(beta*h)^2*trapz(rho, exp(-1i*2*beta.*rho)./rho))
