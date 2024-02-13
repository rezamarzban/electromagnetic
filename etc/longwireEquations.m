clear all
clc

% Define symbolic variables
syms r theta phi I mu_0 l t omega real

% Magnetic vector potential for a long wire carrying current along z-axis in spherical coordinates
A_phi = (mu_0 * I * sin(omega * t)) / (2 * pi) * log(r/l)

A = [0, 0, A_phi]

H = (1 / mu_0) * curl(A, [r, theta, phi])

E = -diff(A, t)
