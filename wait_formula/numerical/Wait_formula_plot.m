clear all
clc

beta = 2*pi/100;
h = 25;

eta = 500;

n = 1;

for i = 10:250
    
    a = i;
    x(n) = a/h;
    
    rho = a:0.1:5000;
    
    expr0 = (-eta)/((2*pi*sin(beta*h)^2));
    expr1 = trapz(rho, exp(-1i*2*beta*sqrt(rho.^2 + h^2))./rho); 
    expr2 = -1*2*cos(beta*h)*trapz(rho, exp(-beta*1i*(sqrt(rho.^2 + h^2) + rho))./rho); 
    expr3 = -cos(beta*h)^2*trapz(rho, exp(-1i*2*beta.*rho)./rho);
    
    norm = 4*pi*expr0/eta;
    
    norm_deltaZ_re(n) = real(norm * (expr1 + expr2 + expr3));
    n = n+1;

end

plot(x, norm_deltaZ_re);
xlabel('a/h');
ylabel('Normalized radiation resistance');
title('Normalized radiation resistance vs a/h');
grid on;
legend('h/lambda=0.25')