import cupy as cp

# Parameters for antenna calculations
r = 1000                           # Distance from antenna
l = 1                              # Dipole length (example value)
eta = 377                           # Free space impedance

# Define theta
theta = cp.arange(0, cp.pi + 0.01, 0.01)  # Angle from 0 to pi in steps of 0.01

# Time vector for complex signal
time_step = 1e-9                     # Time step (sampling interval)
t = cp.arange(0, 5e-6 + time_step, time_step)  # Time vector

# Complex signal (example, adjust as needed)
signal = 3 ** (1e8 * cp.mod(t, 1e-8))  # Example signal

# Perform FFT
n = len(signal)                      # Length of the signal
Y = cp.fft.fft(signal)              # FFT of the signal

# Sampling frequency
Fs = 1 / time_step                   # Sampling frequency

# Frequency vector
f = cp.fft.fftfreq(n, d=time_step)  # Frequency vector
f = f[:n // 2]                       # Single-sided spectrum

# Only take the first half of Y (single-sided spectrum)
Y = Y[:n // 2]

# Amplitude and phase
amplitude = cp.abs(Y) * 2 / n        # Amplitude of each component (scaled)
phase_angle = cp.angle(Y)            # Phase of each component

# Initialize result variables
P_rad_total = 0                     # Total radiated power
results = []                        # Store results for sorting

# Loop through each frequency component
for idx in range(len(amplitude)):
    freq = f[idx]                   # Frequency in Hz
    omega = 2 * cp.pi * freq        # Angular frequency in rad/s
    I = amplitude[idx]              # Amplitude
    phase_angle_val = phase_angle[idx]  # Phase in radians

    # Calculate K for the current frequency
    lambda_ = 3e8 / freq             # Wavelength (example: speed of light / frequency)
    K = 2 * cp.pi / lambda_         # Wave number

    # Compute E_theta and H_phi for each frequency component
    E_theta = ((1j * K * I * l * eta) / (4 * cp.pi * r)) * cp.sin(theta) * cp.exp(-1j * K * r)
    H_phi = E_theta / eta

    # Compute S_theta
    S_theta = 0.5 * cp.real(E_theta * cp.conj(H_phi))

    # Numerical integration to find P_rad
    integrand = S_theta * r**2 * cp.sin(theta)
    P_rad = cp.trapz(integrand, theta) * 2 * cp.pi

    # Accumulate total radiated power
    P_rad_total += P_rad

    # Calculate R_r for the current frequency component
    R_r = 2 * P_rad / I**2

    # Store the results
    results.append([freq.get(), I.get(), omega.get(), phase_angle_val.get(), R_r.get()])

# Convert results to a numpy array for sorting
results = cp.asarray(results)

# Sort results by amplitude in descending order and select top 20 components
sorted_indices = cp.argsort(-results[:, 1])  # Sort by amplitude (column 1) in descending order
sorted_results = results[sorted_indices]
top_20_results = sorted_results[:min(20, len(sorted_results))]

# Print top 20 components
print('Top 20 Components:')
for idx, res in enumerate(top_20_results):
    print(f'{idx + 1}: Frequency = {res[0]:.3e} Hz, I = {res[1]:.3f}, omega = {res[2]:.3f} rad/s, phase = {res[3]:.3f} rad, R_r = {res[4]:.3f}')

# Display total radiated power
print(f'Total Radiated Power of all components: {P_rad_total.get()}')
