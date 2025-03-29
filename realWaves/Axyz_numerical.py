import numpy as np

# Parameters
mu0 = 4 * np.pi * 1e-7  # Permeability of free space (H/m)
epsilon0 = 8.854e-12    # Permittivity of free space (F/m)
c = 3e8                # Speed of light (m/s)
omega = 2 * np.pi * 1e3 # Angular frequency (e.g., 1 kHz sinusoidal)
d = 1                  # Characteristic dimension (e.g., length of dipole)
I0 = 1                 # Amplitude of the current (A)

# Frequency of the wave
f = omega / (2 * np.pi) # Frequency in Hz (e.g., 1 kHz)

# Period of the wave
T = 1 / f              # Period of the wave in seconds

# Source coordinates
x0 = 0                 # x-coordinate of the source
y0 = 0                 # y-coordinate of the source
z0 = 0                 # z-coordinate of the source

# Define the grid of coordinates with specified spacing
x = np.arange(-10, 10.5, 0.5)  # Define x coordinates
y = np.arange(-10, 10.5, 0.5)  # Define y coordinates
z = np.arange(-10, 10.5, 0.5)  # Define z coordinates

# Define the specific time point
t_val = np.pi / 4 * T         # Time at which to compute radiated power

# Initialize the 4D matrix to store the vector potential A
A = np.zeros((len(x), len(y), len(z), 3))

# Calculate vector potential A using nested loops
for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(z)):
            # Current coordinates
            xi = x[i]
            yj = y[j]
            zk = z[k]

            # Calculate the distance r_pq
            r_pq = np.sqrt((xi - x0)**2 + (yj - y0)**2 + (zk - z0)**2)

            # Avoid division by zero at the source location
            if r_pq == 0:
                r_pq = np.finfo(float).eps  # A very small number to prevent division by zero

            # Calculate the retarded time
            retarded_time = t_val - r_pq / c

            # Calculate the shifted current I_shifted
            I_shifted = I0 * np.sin(omega * retarded_time)  # Shifted current function

            # Calculate the vector potential A at (xi, yj, zk)
            A_ijk = (mu0 * d / (4 * np.pi * r_pq)) * I_shifted

            # Store the vector potential A as a 3D vector
            A[i, j, k, :] = A_ijk * np.array([(xi - x0) / r_pq, (yj - y0) / r_pq, (zk - z0) / r_pq])

# Now A(x, y, z) is a 3D matrix where each element is a 3D vector [Ax, Ay, Az].
