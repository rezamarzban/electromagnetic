import numpy as np

# Parameters for antenna calculations
r = 1000                           # Distance from antenna
l = 1                              # Dipole length (example value)
eta = 377                           # Free space impedance

# Define theta
theta = np.arange(0, np.pi + 0.01, 0.01)  # Angle from 0 to pi in steps of 0.01

# Time vector for complex signal
time_step = 1e-9                     # Time step (sampling interval)
t = np.arange(0, 5e-6 + time_step, time_step)  # Time vector

# Complex signal (example, adjust as needed)
signal = 3 ** (1e8 * np.mod(t, 1e-8))  # Example signal

# Perform FFT
n = len(signal)                      # Length of the signal
Y = np.fft.fft(signal)              # FFT of the signal

# Sampling frequency
Fs = 1 / time_step                   # Sampling frequency

# Frequency vector
f = np.fft.fftfreq(n, d=time_step)  # Frequency vector
f = f[:n // 2]                       # Single-sided spectrum

# Only take the first half of Y (single-sided spectrum)
Y = Y[:n // 2]

# Amplitude and phase
amplitude = np.abs(Y) * 2 / n        # Amplitude of each component (scaled)
phase_angle = np.angle(Y)            # Phase of each component

# Initialize result variables
P_rad_total = 0                     # Total radiated power
results = []                        # Store results for sorting

# Loop through each frequency component
for idx in range(len(amplitude)):
    freq = f[idx]                   # Frequency in Hz
    omega = 2 * np.pi * freq        # Angular frequency in rad/s
    I = amplitude[idx]              # Amplitude
    phase_angle_val = phase_angle[idx]  # Phase in radians

    # Calculate K for the current frequency
    lambda_ = 3e8 / freq             # Wavelength (example: speed of light / frequency)
    K = 2 * np.pi / lambda_         # Wave number

    # Compute E_theta and H_phi for each frequency component
    E_theta = ((1j * K * I * l * eta) / (4 * np.pi * r)) * np.sin(theta) * np.exp(-1j * K * r)
    H_phi = E_theta / eta

    # Compute S_theta
    S_theta = 0.5 * np.real(E_theta * np.conj(H_phi))

    # Numerical integration to find P_rad
    integrand = S_theta * r**2 * np.sin(theta)
    P_rad = np.trapz(integrand, theta) * 2 * np.pi

    # Accumulate total radiated power
    P_rad_total += P_rad

    # Calculate R_r for the current frequency component
    R_r = 2 * P_rad / I**2

    # Store the results
    results.append([freq, I, omega, phase_angle_val, R_r])

# Convert results to a numpy array for sorting
results = np.array(results)

# Sort results by amplitude in descending order and select top 20 components
sorted_results = results[np.argsort(-results[:, 1])]  # Sort by amplitude (column 1) in descending order
top_20_results = sorted_results[:min(20, len(sorted_results))]

# Print top 20 components
print('Top 20 Components:')
for idx, res in enumerate(top_20_results):
    print(f'{idx + 1}: Frequency = {res[0]:.3e} Hz, I = {res[1]:.3f}, omega = {res[2]:.3f} rad/s, phase = {res[3]:.3f} rad, R_r = {res[4]:.3f}')

# Display total radiated power
print(f'Total Radiated Power of all components: {P_rad_total}')
