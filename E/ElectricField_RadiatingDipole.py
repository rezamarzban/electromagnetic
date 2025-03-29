import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
from IPython.display import Image

# Conditional imports for Numba and CuPy
try:
    import numba
except ImportError:
    numba = None

try:
    import cupy as cp
except ImportError:
    cp = None

# Import tqdm for progress bars
try:
    from tqdm.notebook import tqdm
except ImportError:
    tqdm = lambda x, total=None: x  # Fallback to no progress bar if tqdm is not installed

# User selects the acceleration method
use = "numpy"  # Options: "numpy", "numba", "cupy" - change as desired

# Physical constants
c = 1.0          # Speed of light
omega = np.pi / 5  # Angular frequency
p_0 = 1.0        # Dipole moment amplitude

# Create a 2D grid using NumPy
x = np.linspace(-10, 10, 100)
z = np.linspace(-10, 10, 100)
X, Z = np.meshgrid(x, z)

# Convert grid to CuPy arrays if using CuPy
if use == "cupy":
    X = cp.array(X)
    Z = cp.array(Z)

# Generic compute_field function for NumPy and CuPy
def compute_field(lib, X, Z, t, c, omega, p_0):
    """Compute electric field components using the specified library."""
    R = lib.sqrt(X**2 + Z**2)
    R = lib.maximum(R, 1e-6)  # Avoid division by zero
    t_prime = t - R / c
    p_z = p_0 * lib.cos(omega * t_prime)
    p_z_prime = -p_0 * omega * lib.sin(omega * t_prime)
    p_z_double_prime = -p_0 * omega**2 * lib.cos(omega * t_prime)
    n_x = X / R
    n_z = Z / R
    E_x = (3 * p_z * n_z * n_x / R**3 + 
           3 * p_z_prime * n_z * n_x / (c * R**2) + 
           p_z_double_prime * n_z * n_x / (c**2 * R))
    E_z = ((3 * p_z * n_z**2 - p_z) / R**3 + 
           (3 * p_z_prime * n_z**2 - p_z_prime) / (c * R**2) + 
           (p_z_double_prime * n_z**2 - p_z_double_prime) / (c**2 * R))
    # Convert to NumPy arrays if using CuPy
    try:
        E_x = lib.asnumpy(E_x)
        E_z = lib.asnumpy(E_z)
    except AttributeError:
        pass  # No conversion needed for NumPy
    return E_x, E_z

# Numba-optimized version if selected
if use == "numba":
    if numba is None:
        raise ImportError("Numba is not installed. Please install it to use 'numba'.")
    @numba.jit(nopython=True)
    def compute_field_numba(X, Z, t, c, omega, p_0):
        """Compute electric field components with Numba acceleration."""
        R = np.sqrt(X**2 + Z**2)
        R = np.maximum(R, 1e-6)
        t_prime = t - R / c
        p_z = p_0 * np.cos(omega * t_prime)
        p_z_prime = -p_0 * omega * np.sin(omega * t_prime)
        p_z_double_prime = -p_0 * omega**2 * np.cos(omega * t_prime)
        n_x = X / R
        n_z = Z / R
        E_x = (3 * p_z * n_z * n_x / R**3 + 
               3 * p_z_prime * n_z * n_x / (c * R**2) + 
               p_z_double_prime * n_z * n_x / (c**2 * R))
        E_z = ((3 * p_z * n_z**2 - p_z) / R**3 + 
               (3 * p_z_prime * n_z**2 - p_z_prime) / (c * R**2) + 
               (p_z_double_prime * n_z**2 - p_z_double_prime) / (c**2 * R))
        return E_x, E_z
else:
    compute_field_numba = None

# Assign the computation function based on 'use'
if use == "numpy":
    lib = np
    compute_field_func = lambda X, Z, t: compute_field(lib, X, Z, t, c, omega, p_0)
elif use == "cupy":
    if cp is None:
        raise ImportError("CuPy is not installed. Please install it to use 'cupy'.")
    lib = cp
    compute_field_func = lambda X, Z, t: compute_field(lib, X, Z, t, c, omega, p_0)
elif use == "numba":
    compute_field_func = lambda X, Z, t: compute_field_numba(X, Z, t, c, omega, p_0)
else:
    raise ValueError("Invalid 'use' value. Choose 'numpy', 'numba', or 'cupy'.")

# Set up plotting style
plt.style.use('grayscale')

# Create directory for animation frames
frame_dir = 'frames'
if not os.path.exists(frame_dir):
    os.makedirs(frame_dir)

# Function to save a frame
def save_frame(t, frame_num):
    fig, ax = plt.subplots(figsize=(8, 8))
    E_x, E_z = compute_field_func(X, Z, t)
    
    # Plot electric field lines (convert CuPy arrays to NumPy if needed)
    ax.streamplot(X if use != "cupy" else cp.asnumpy(X), 
                  Z if use != "cupy" else cp.asnumpy(Z), 
                  E_x, E_z, density=1.5, color='black', arrowsize=0.5)
    
    # Draw dipole and charges
    ax.plot([0, 0], [-2.5, 2.5], 'k-', linewidth=2)
    charge_sign = np.cos(omega * t)
    top_sign = '+' if charge_sign > 0 else '−'
    bottom_sign = '−' if charge_sign > 0 else '+'
    ax.plot(0, 2.5, 'o', color='gray' if top_sign == '+' else 'black', markersize=10)
    ax.plot(0, -2.5, 'o', color='black' if top_sign == '+' else 'gray', markersize=10)
    ax.text(0.5, 2.5, top_sign, color='gray' if top_sign == '+' else 'black', fontsize=12)
    ax.text(0.5, -2.5, bottom_sign, color='black' if top_sign == '+' else 'gray', fontsize=12)
    
    ax.set(xlim=(-10, 10), ylim=(-10, 10), aspect='equal', 
           xlabel='x', ylabel='z', title=f'Dipole Radiation at t = {t:.2f}')
    
    plt.savefig(os.path.join(frame_dir, f'frame_{frame_num:03d}.png'), dpi=100)
    plt.close(fig)

# Generate animation frames with progress bar
times = np.linspace(0, 20, 100)
for i, t in tqdm(enumerate(times), total=len(times), desc="Generating frames"):
    save_frame(t, i)

# Create GIF with progress bar
images = [imageio.imread(os.path.join(frame_dir, f'frame_{i:03d}.png')) for i in tqdm(range(len(times)), desc="Creating GIF")]
imageio.mimsave('dipole_radiation.gif', images, fps=10)

# Display GIF (e.g., in Jupyter/Colab)
Image(filename='dipole_radiation.gif')
