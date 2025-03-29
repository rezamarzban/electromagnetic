clear all
clc

% Define symbolic variables
syms r theta phi I l K eth0 real

% Derive equations 
E_theta = ((1i * K * I * l * eth0 ) / (4 * pi * r)) * sin(theta) * exp(-1i * K * r)

H_phi = E_theta / eth0

S_theta = 0.5 * real(E_theta .* conj(H_phi))

P_rad = int(int(S_theta * r^2 * sin(theta), theta, 0, pi), phi, 0, 2*pi)

Rr =  2 * P_rad / I^2

% Evaluate functions with sample variable values
Power =  eval(subs(P_rad, [eth0, I, l, K], [377, 2, 0.1, 2*pi/6])) % Watts

Radiation_ressistance = eval(subs(Rr, [eth0, l, K], [377, 0.1, 2*pi/6])) % Ohms
