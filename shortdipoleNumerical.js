dipole_length = 0.1; 
I = 2; 
K = (2 * pi / 6); 
r = 1000; 
n = 360; 
theta = 0:pi/n:pi; 
E_theta = ((1i * K * I * dipole_length * 377 ) / (4 * pi * r)) * sin(theta) * exp(-1i * K * r); 
H_phi = E_theta / 377; 
S_theta = 0.5 * re(E_theta .* conj(H_phi)); 
P_rad = (pi/n) * sum(S_theta * sin(theta) * r^2) * 2 * pi
Rr = 2 * P_rad / I^2
