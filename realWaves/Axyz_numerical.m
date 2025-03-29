clc;
clear all;

% Parameters
mu0 = 4*pi*1e-7;  % Permeability of free space (H/m)
epsilon0 = 8.854e-12; % Permittivity of free space (F/m)
c = 3e8;          % Speed of light (m/s)
omega = 2*pi*1e3; % Angular frequency (e.g., 1 kHz sinusoidal)
d = 1;            % Characteristic dimension (e.g., length of dipole)
I0 = 1;           % Amplitude of the current (A)

% Frequency of the wave
f = omega / (2*pi); % Frequency in Hz (e.g., 1 kHz)

% Period of the wave
T = 1 / f;        % Period of the wave in seconds

% Source coordinates
x0 = 0;           % x-coordinate of the source
y0 = 0;           % y-coordinate of the source
z0 = 0;           % z-coordinate of the source

% Define the grid of coordinates with specified spacing
x = -10:0.5:10;  % Define x coordinates
y = -10:0.5:10;  % Define y coordinates
z = -10:0.5:10;  % Define z coordinates

% Define the specific time point
t_val = pi / 4 * T;         % Time at which to compute radiated power

% Initialize the 3D matrix to store the vector potential A
A = zeros(length(x), length(y), length(z), 3);

% Calculate vector potential A using nested loops
for i = 1:length(x)
    for j = 1:length(y)
        for k = 1:length(z)
            % Current coordinates
            xi = x(i);
            yj = y(j);
            zk = z(k);

            % Calculate the distance r_pq
            r_pq = sqrt((xi - x0)^2 + (yj - y0)^2 + (zk - z0)^2);

            % Avoid division by zero at the source location
            if r_pq == 0
                r_pq = eps; % A very small number to prevent division by zero
            end

            % Calculate the retarded time
            retarded_time = t_val - r_pq / c;

            % Calculate the shifted current I_shifted
            I_shifted = I0 * sin(omega * retarded_time);  % Shifted current function

            % Calculate the vector potential A at (xi, yj, zk)
            A_ijk = (mu0 * d / (4 * pi * r_pq)) * I_shifted;

            % Store the vector potential A as a 3D vector
            A(i, j, k, :) = A_ijk * [(xi - x0) / r_pq, (yj - y0) / r_pq, (zk - z0) / r_pq];
        end
    end
end

% Now A(x, y, z) is a 3D matrix where each element is a 3D vector [Ax, Ay, Az].
                                       
