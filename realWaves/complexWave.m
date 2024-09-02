clc;
clear;
close all;

% Parameters for antenna calculations
r = 1000;                           % Distance from antenna
l = 1;                             % Dipole length (example value)
eta = 377;                          % Free space impedance

% Define theta
theta = 0:0.01:pi;                  % Angle from 0 to pi in steps of 0.01

% Time vector for complex signal
time_step = 1e-9;                  % Time step (sampling interval)
t = 0:time_step:5e-6;              % Time vector

% Complex signal (example, adjust as needed)
signal = 3 .^ (1e8 * mod(t, 1e-8));            % Example signal

% Perform FFT
n = length(signal);                 % Length of the signal
Y = fft(signal);                    % FFT of the signal

% Sampling frequency
Fs = 1 / time_step;                 % Sampling frequency

% Frequency vector
f = (0:n-1)*(Fs/n);                 % Frequency vector
f = f(1:floor(n/2));                % Single-sided spectrum

% Only take the first half of Y (single-sided spectrum)
Y = Y(1:floor(n/2));  

% Amplitude and phase
amplitude = abs(Y) * 2 / n;         % Amplitude of each component (scaled)
phase_angle = angle(Y);             % Phase of each component

% Initialize result variables
P_rad_total = 0;                    % Total radiated power
results = [];                       % Store results for sorting

% Loop through each frequency component
for idx = 1:length(amplitude)
    freq = f(idx);                  % Frequency in Hz
    omega = 2*pi*freq;              % Angular frequency in rad/s
    I = amplitude(idx);             % Amplitude
    phase_angle_val = phase_angle(idx); % Phase in radians

    % Calculate K for the current frequency
    lambda = 3e8 / freq;            % Wavelength (example: speed of light / frequency)
    K = 2 * pi / lambda;            % Wave number

    % Compute E_theta and H_phi for each frequency component
    E_theta = ((1i * K * I * l * eta) / (4 * pi * r)) * sin(theta) .* exp(-1i * K * r);
    H_phi = E_theta / eta;

    % Compute S_theta and P_rad for each component
    S_theta = 0.5 * real(E_theta .* conj(H_phi));
    % Integrate S_theta over theta to find P_rad
    P_rad = trapz(theta, S_theta .* r.^2 .* sin(theta)) * 2 * pi;

    % Accumulate total radiated power
    P_rad_total = P_rad_total + P_rad;

    % Calculate R_r for the current frequency component
    R_r = 2 * P_rad / I^2;

    % Store the results
    results = [results; freq, I, omega, phase_angle_val, R_r]; % [Frequency, Amplitude, Omega, Phase, R_r]
end

% Sort results by amplitude in descending order and select top 20 components
sorted_results = sortrows(results, -2); % Sort by amplitude (column 2) in descending order
top_20_results = sorted_results(1:min(20, size(sorted_results, 1)), :);

% Print top 20 components
fprintf('Top 20 Components:\n');
for idx = 1:size(top_20_results, 1)
    fprintf('%d: Frequency = %.3e Hz, I = %.3f, omega = %.3f rad/s, phase = %.3f rad, R_r = %.3f\n', ...
        idx, top_20_results(idx, 1), top_20_results(idx, 2), top_20_results(idx, 3), top_20_results(idx, 4), top_20_results(idx, 5));
end

% Display total radiated power
disp(['Total Radiated Power of all components: ', num2str(P_rad_total)]);
