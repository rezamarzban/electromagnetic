r = 1000;
theta = 0:0.01:pi;
I = 2;
l = 0.1;
K = 2*pi/6;
eth0 = 377;

E_theta = ((1i * K * I * l * eth0) / (4 * pi * r)) * sin(theta) .* exp(-1i * K * r);
H_phi = E_theta / eth0;
S_theta = 0.5 * real(E_theta .* conj(H_phi));
P_rad = trapz(theta, S_theta .* r.^2 .* sin(theta)) * 2 * pi;
Rr = 2 * P_rad / I^2;

disp(P_rad);
disp(Rr);
