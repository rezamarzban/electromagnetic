# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define constants
l = 0.2              # Length parameter for the dipole
ncell = 8            # Number of frames in the animation
k0 = 2 * np.pi       # Wave number

# Define functions
def R(x, y):
    """Compute the radial distance scaled by k0."""
    return k0 * np.sqrt(x**2 + y**2)

def theta(x, y):
    """Compute the angular coordinate."""
    return np.arctan2(y, x)  # Returns angle in correct quadrant

# Set contour levels
contrs = np.arange(-0.9, 1.0, 0.2)  # Contour levels from -0.9 to 0.9 with step 0.2

# Create a grid for plotting
x = np.linspace(-1, 1, 100)  # x-axis range
y = np.linspace(-1, 1, 100)  # y-axis range
X, Y = np.meshgrid(x, y)     # 2D grid of x and y coordinates

# Define time steps for animation
T_values = np.linspace(0, np.pi - np.pi/ncell, ncell)

# Function to compute the field at each point
def compute_field(T):
    """Calculate the field value for a given time T."""
    R_xy = R(X, Y)
    theta_xy = theta(X, Y)
    # Handle division by zero at the origin
    with np.errstate(divide='ignore', invalid='ignore'):
        field = (np.cos(R_xy - T) + np.sin(R_xy - T) / R_xy) * (np.cos(theta_xy))**2
    field[np.isnan(field)] = 0  # Replace NaN values (at origin) with 0
    return field

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xticks([])  # Remove x-axis ticks
ax.set_yticks([])  # Remove y-axis ticks

# Initial contour plot (for T=0)
field = compute_field(0)
cont = ax.contour(X, Y, field, levels=contrs, colors='black')

# Add dipole arrow at the center
dipole = ax.arrow(0, -l/2, 0, l, head_width=0.05, head_length=0.1, fc='red', ec='red')

# Animation update function
def update(frame):
    """Update the plot for each animation frame."""
    ax.cla()  # Clear the previous frame
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    T = T_values[frame]
    field = compute_field(T)
    ax.contour(X, Y, field, levels=contrs, colors='black')  # Draw contours
    ax.arrow(0, -l/2, 0, l, head_width=0.05, head_length=0.1, fc='red', ec='red')  # Redraw dipole
    return ax,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(T_values), interval=200)

# Display the animation (comment/uncomment based on your environment)
# For Jupyter/Colab:
from IPython.display import HTML
HTML(ani.to_jshtml())  # Render animation as HTML5 video

# For standard Python environments, uncomment the line below instead:
# plt.show()
