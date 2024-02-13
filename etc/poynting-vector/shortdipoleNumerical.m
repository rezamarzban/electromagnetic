clear all;
clc;

% Define dipole antenna parameters
frequency = 2.4e9; % Frequency in Hertz (example: 2.4 GHz)
lambda = 300000000 / frequency; % Wavelength
dipole_length = lambda / 2; % Half-wavelength dipole

I = 1; % Antenna current in Ampere
K = (2 * pi / lambda); % Wave number 
r_farfield = (2 * lambda); % Farfield occur at distance greater than lambda/4

n = 360; % Number of each theta and phi elements

% Define spatial coordinates
theta = linspace(0, 2*pi, n); % Azimuthal angle
phi = linspace(0, 2*pi, n); % Polar angle

% Far-field electric field components for a half-wavelength dipole
E_theta = ((1i * K * I * dipole_length * 377 ) / (4 * pi * r_farfield)) * sin(theta) * exp(-1i * K * r_farfield);
E_phi = zeros(size(phi)); % Assume E_phi is negligible for a dipole along the z-axis

% Magnetic field components are derived from the electric field
H_theta = E_phi / 377;
H_phi = E_theta / 377;

% Define Poynting vector components
S_theta = 0.5 * real(E_theta .* conj(H_phi));
S_phi = 0.5 * real(E_phi .* conj(H_theta));

% Calculate total Poynting vector magnitude
S_total = sqrt(S_theta.^2 + S_phi.^2);
