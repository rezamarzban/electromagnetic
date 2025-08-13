# Equations for Thin Center-Fed Dipole Antenna

This document lists the equations and integral evaluations used in the analysis of a thin center-fed dipole antenna of length $L$, operating at frequency $f$, with wavelength $\lambda = c/f$, and peak current $I_0$ at the center. The antenna is z-directed, extending from $z = -L/2$ to $z = L/2$, with a sinusoidal current distribution $I(z) = I_0 \frac{\sin(k (L/2 - |z|))}{\sin \beta}$, where $\beta = k L / 2$. All equations are valid for any $L/\lambda$ (from 0.001 to 1000) under the thin-wire approximation (radius $\ll \lambda, L$), assuming free space and a perfect conductor. Each equation is presented with its physical role and derivation context.

## 1. Wavenumber
The wavenumber $k$ relates the wavelength $\lambda$ to the spatial phase variation of the electromagnetic wave.

**Equation**: $$k = \frac{2\pi}{\lambda}$$

**Explanation**: The wavenumber $k$ is the number of radians per unit length, derived from the wave's periodicity in free space, where $\lambda = c/f$ and $c$ is the speed of light ($3 \times 10^8$ m/s). This is fundamental for wave propagation calculations.

## 2. Angular Frequency
The angular frequency $\omega$ relates the operating frequency $f$ to the temporal phase variation.

**Equation**: $$\omega = 2\pi f$$

**Explanation**: The angular frequency $\omega$ (rad/s) is derived from the frequency $f$ (Hz), representing the rate of oscillation of the electromagnetic field. It is used in time-harmonic field expressions.

## 3. Phase Constant
The phase constant $\beta$ relates the wavenumber $k$ and dipole length $L$ for the current distribution.

**Equation**: $$\beta = k \frac{L}{2}$$

**Explanation**: The phase constant $\beta$ (also called $\beta = k L / 2$) arises in the sinusoidal current distribution $I(z) = I_0 \frac{\sin(k (L/2 - |z|))}{\sin \beta}$, where it normalizes the current to $I_0$ at $z = 0$. It determines the phase variation along the antenna.

## 4. Intrinsic Impedance
The intrinsic impedance $\eta_0$ characterizes the electromagnetic properties of free space.

**Equation**: $$\eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}}$$

**Explanation**: The intrinsic impedance $\eta_0 \approx 377 \, \Omega$ is the ratio of electric to magnetic field amplitudes in a plane wave in free space, where $\mu_0 = 4\pi \times 10^{-7}$ H/m and $\epsilon_0 \approx 8.854 \times 10^{-12}$ F/m. It relates $E_\theta$ and $H_\phi$ in the far field.

## 5. Magnetic Vector Potential
The magnetic vector potential $A_z$ describes the source of the electromagnetic fields in the far field.

**Equation**: $$A_z(r, \theta) = \frac{\mu_0 I_0 e^{-j k r}}{4 \pi r} \int_{-L/2}^{L/2} \frac{\sin(k (L/2 - |z'|))}{\sin \beta} e^{j k z' \cos \theta} \, dz'$$

**Integral Evaluation**: The integral is evaluated as follows:
- The current is $I(z') = I_0 \frac{\sin(k (L/2 - |z'|))}{\sin \beta}$, symmetric about $z' = 0$.
- The integral becomes:
  $$\int_{-L/2}^{L/2} \frac{\sin(k (L/2 - |z'|))}{\sin \beta} e^{j k z' \cos \theta} \, dz' = \frac{2}{\sin \beta} \int_0^{L/2} \sin(k (L/2 - z')) \cos(k z' \cos \theta) \, dz'.$$
- Using the identity $\sin a \cos b = \frac{1}{2} [\sin(a+b) + \sin(a-b)]$, let $u = k z'$, $a = k L/2 - u$, $b = u \cos \theta$:
  $$\int_0^{L/2} \sin(k (L/2 - z')) \cos(k z' \cos \theta) \, dz' = \frac{1}{k} \int_0^{k L/2} \sin(k L/2 - u) \cos(u \cos \theta) \, du.$$
- The integral evaluates to:
  $$\frac{1}{2k} \left[ \int_0^{k L/2} \sin(k L/2 - u + u \cos \theta) \, du + \int_0^{k L/2} \sin(k L/2 - u - u \cos \theta) \, du \right].$$
- Substituting $v = k L/2 - u \pm u \cos \theta$, and simplifying, the result is:
  $$\frac{2}{k} \frac{\cos(\beta \cos \theta) - \cos \beta}{\sin^2 \theta}, \quad \text{for } \sin \theta \neq 0.$$
- Thus:
  $$A_z(r, \theta) = \frac{\mu_0 I_0 e^{-j k r}}{4 \pi r} \cdot \frac{2}{k} \frac{\cos(\beta \cos \theta) - \cos \beta}{\sin \beta \sin^2 \theta}.$$
- For $\sin \theta \approx 0$ or $\sin \beta \approx 0$, numerical approximations (e.g., $L/2$) handle singularities.

**Explanation**: The vector potential $A_z$ is derived from the current distribution using the retarded potential formula. The integral accounts for the phase delay ($e^{j k z' \cos \theta}$) due to observation at angle $\theta$ and distance $r$ in the far field ($r \gg \lambda, L$). The result matches standard antenna theory for a sinusoidal current.

```
import numpy as np
from scipy.constants import mu_0, epsilon_0, pi, c

# Constants and parameters
mu_0 = 4 * pi * 1e-7
c = 3e8
frequency = 100e6
wavelength = c / frequency
L_over_lambda = 0.5
dipole_length = L_over_lambda * wavelength
I0 = 1.0
k = 2 * pi / wavelength
beta = k * dipole_length / 2
theta = pi / 2  # Example angle (rad)
r = 1e6  # Example distance (m)

# Equation implementation
sin_theta = np.sin(theta)
if np.abs(sin_theta) < 1e-8:
    integral = dipole_length / 2
else:
    cos_term = np.cos(beta * np.cos(theta)) - np.cos(beta)
    denom = np.sin(beta) * sin_theta**2
    if np.abs(denom) < 1e-12:
        integral = dipole_length / 2
    else:
        integral = (2 / k) * cos_term / denom
A_z_value = (mu_0 * I0 * np.exp(-1j * k * r) / (4 * pi * r)) * integral

print(f"Magnetic vector potential A_z: {A_z_value:.2e} Wb/m")
```

## 6. Electric Field
The far-field electric field component $E_\theta$ is derived from the vector potential.

**Equation**: $$E_\theta(r, \theta) = -j \omega A_z(r, \theta) \sin \theta$$

**Explanation**: In the far field, the electric field has only a $\theta$-component, related to $A_z$ via $E_\theta = j \omega A_\theta$, where $A_\theta = -A_z \sin \theta$ in spherical coordinates. Thus, $E_\theta = -j \omega A_z \sin \theta$. Substituting $A_z$ gives:
$$E_\theta = j \frac{\eta_0 I_0 e^{-j k r}}{2 \pi r} \frac{\cos(\beta \cos \theta) - \cos \beta}{\sin \beta \sin \theta}.$$
The code uses $-j$, a convention choice (time factor $e^{j \omega t}$ vs. $e^{-j \omega t}$), but magnitudes are consistent.

```
import numpy as np
from scipy.constants import mu_0, epsilon_0, pi, c

# Constants and parameters (reusing from previous)
mu_0 = 4 * pi * 1e-7
c = 3e8
frequency = 100e6
wavelength = c / frequency
L_over_lambda = 0.5
dipole_length = L_over_lambda * wavelength
I0 = 1.0
k = 2 * pi / wavelength
omega = 2 * pi * frequency
beta = k * dipole_length / 2
theta = pi / 2  # rad
r = 1e6  # m

# Compute A_z first
sin_theta = np.sin(theta)
if np.abs(sin_theta) < 1e-8:
    integral = dipole_length / 2
else:
    cos_term = np.cos(beta * np.cos(theta)) - np.cos(beta)
    denom = np.sin(beta) * sin_theta**2
    if np.abs(denom) < 1e-12:
        integral = dipole_length / 2
    else:
        integral = (2 / k) * cos_term / denom
A_z_value = (mu_0 * I0 * np.exp(-1j * k * r) / (4 * pi * r)) * integral

# Equation
E_theta_value = -1j * omega * A_z_value * np.sin(theta)

print(f"Electric field E_theta: {E_theta_value:.2e} V/m")
```

## 7. Magnetic Field
The far-field magnetic field component $H_\phi$ is related to the electric field.

**Equation**: $$H_\phi(r, \theta) = \frac{E_\theta(r, \theta)}{\eta_0}$$

**Explanation**: In the far field, the electromagnetic wave is a TEM wave, with $H_\phi = E_\theta / \eta_0$, where $\eta_0$ is the intrinsic impedance. This follows from Maxwell’s equations and the plane-wave-like behavior far from the antenna.

```
import numpy as np
from scipy.constants import mu_0, epsilon_0, pi, c

# Constants and parameters (reusing)
mu_0 = 4 * pi * 1e-7
epsilon_0 = 8.854187817e-12
eta_0 = np.sqrt(mu_0 / epsilon_0)
c = 3e8
frequency = 100e6
wavelength = c / frequency
L_over_lambda = 0.5
dipole_length = L_over_lambda * wavelength
I0 = 1.0
k = 2 * pi / wavelength
omega = 2 * pi * frequency
beta = k * dipole_length / 2
theta = pi / 2  # rad
r = 1e6  # m

# Compute A_z and E_theta first
sin_theta = np.sin(theta)
if np.abs(sin_theta) < 1e-8:
    integral = dipole_length / 2
else:
    cos_term = np.cos(beta * np.cos(theta)) - np.cos(beta)
    denom = np.sin(beta) * sin_theta**2
    if np.abs(denom) < 1e-12:
        integral = dipole_length / 2
    else:
        integral = (2 / k) * cos_term / denom
A_z_value = (mu_0 * I0 * np.exp(-1j * k * r) / (4 * pi * r)) * integral
E_theta_value = -1j * omega * A_z_value * np.sin(theta)

# Equation
H_phi_value = E_theta_value / eta_0

print(f"Magnetic field H_phi: {H_phi_value:.2e} A/m")
```

## 8. Time-Averaged Poynting Vector Magnitude
The time-averaged power density $S$ quantifies the radiated power flux.

**Equation**: $$S(r, \theta) = \frac{1}{2} \operatorname{Re}(E_\theta H_\phi^*) = \frac{|E_\theta|^2}{2 \eta_0}$$

**Explanation**: The Poynting vector $\mathbf{S} = \frac{1}{2} \operatorname{Re}(\mathbf{E} \times \mathbf{H}^*)$ gives the time-averaged power density. Since $\mathbf{E} = E_\theta \hat{\theta}$, $\mathbf{H} = H_\phi \hat{\phi}$, and $E_\theta = \eta_0 H_\phi$, the magnitude is $S = \frac{1}{2} |E_\theta|^2 / \eta_0$. This represents the power radiated per unit area.

```
import numpy as np
from scipy.constants import mu_0, epsilon_0, pi, c

# Constants and parameters (reusing)
mu_0 = 4 * pi * 1e-7
epsilon_0 = 8.854187817e-12
eta_0 = np.sqrt(mu_0 / epsilon_0)
c = 3e8
frequency = 100e6
wavelength = c / frequency
L_over_lambda = 0.5
dipole_length = L_over_lambda * wavelength
I0 = 1.0
k = 2 * pi / wavelength
omega = 2 * pi * frequency
beta = k * dipole_length / 2
theta = pi / 2  # rad
r = 1e6  # m

# Compute E_theta first
sin_theta = np.sin(theta)
if np.abs(sin_theta) < 1e-8:
    integral = dipole_length / 2
else:
    cos_term = np.cos(beta * np.cos(theta)) - np.cos(beta)
    denom = np.sin(beta) * sin_theta**2
    if np.abs(denom) < 1e-12:
        integral = dipole_length / 2
    else:
        integral = (2 / k) * cos_term / denom
A_z_value = (mu_0 * I0 * np.exp(-1j * k * r) / (4 * pi * r)) * integral
E_theta_value = -1j * omega * A_z_value * np.sin(theta)

# Equation
poynting_value = (np.abs(E_theta_value)**2) / (2 * eta_0)

print(f"Poynting vector magnitude S: {poynting_value:.2e} W/m²")
```

## 9. Total Radiated Power
The total radiated power $P_\mathrm{rad}$ is obtained by integrating the Poynting vector over a sphere.

**Equation**: $$P_\mathrm{rad} = \int_0^\pi 2 \pi r^2 S(r, \theta) \sin \theta \, d\theta$$

**Explanation**: The total power is found by integrating $S(r, \theta)$ over a sphere of radius $r$:
$$P_\mathrm{rad} = \int_0^{2\pi} \int_0^\pi S r^2 \sin \theta \, d\theta \, d\phi = 2\pi r^2 \int_0^\pi S \sin \theta \, d\theta.$$
Substituting $S = \frac{|E_\theta|^2}{2 \eta_0}$, the integral becomes:
$$P_\mathrm{rad} = \frac{\eta_0 I_0^2}{4 \pi \sin^2 \beta} \int_0^\pi \frac{[\cos(\beta \cos \theta) - \cos \beta]^2}{\sin \theta} \, d\theta.$$
This is evaluated numerically due to the complexity of the integrand, which involves cosine and sine integral functions (Ci, Si) in analytical forms.

```
import numpy as np
from scipy.constants import mu_0, epsilon_0, pi, c
from scipy.integrate import quad

# Constants and parameters
mu_0 = 4 * pi * 1e-7
epsilon_0 = 8.854187817e-12
eta_0 = np.sqrt(mu_0 / epsilon_0)
c = 3e8
frequency = 100e6
wavelength = c / frequency
L_over_lambda = 0.5
dipole_length = L_over_lambda * wavelength
I0 = 1.0
k = 2 * pi / wavelength
omega = 2 * pi * frequency
beta = k * dipole_length / 2
r = 1e6  # m (arbitrary far-field distance)

# Helper function for Poynting (as in equation 8)
def poynting(theta, r):
    sin_theta = np.sin(theta)
    if np.abs(sin_theta) < 1e-8:
        integral = dipole_length / 2
    else:
        cos_term = np.cos(beta * np.cos(theta)) - np.cos(beta)
        denom = np.sin(beta) * sin_theta**2
        if np.abs(denom) < 1e-12:
            integral = dipole_length / 2
        else:
            integral = (2 / k) * cos_term / denom
    A_z_value = (mu_0 * I0 * np.exp(-1j * k * r) / (4 * pi * r)) * integral
    E_theta_value = -1j * omega * A_z_value * np.sin(theta)
    return (np.abs(E_theta_value)**2) / (2 * eta_0)

# Equation: Integrand and integration
def integrand(theta):
    return poynting(theta, r) * 2 * pi * r**2 * np.sin(theta)

P_rad, _ = quad(integrand, 0, pi, epsabs=1e-8, epsrel=1e-4, limit=1000)

print(f"Total radiated power P_rad: {P_rad:.2f} W")
```

## 10. Radiation Resistance
The radiation resistance $R_\mathrm{rad}$ relates the radiated power to the input current.

**Equation**: $$R_\mathrm{rad} = \frac{2 P_\mathrm{rad}}{I_0^2}$$

**Explanation**: The radiation resistance is defined via the time-averaged power radiated, $P_\mathrm{rad} = \frac{1}{2} I_0^2 R_\mathrm{rad}$, where $I_0$ is the peak current amplitude at the feed point. Thus, $R_\mathrm{rad} = 2 P_\mathrm{rad} / I_0^2$. For a half-wave dipole ($L = \lambda/2$, $\beta = \pi/2$), $R_\mathrm{rad} \approx 73 \, \Omega$. For $L = n\lambda$ (integer $n$), $\sin \beta \approx 0$, causing $R_\mathrm{rad}$ to approach infinity, as handled in the code.

```
import numpy as np
from scipy.constants import mu_0, epsilon_0, pi, c
from scipy.integrate import quad

# Constants and parameters (reusing)
mu_0 = 4 * pi * 1e-7
epsilon_0 = 8.854187817e-12
eta_0 = np.sqrt(mu_0 / epsilon_0)
c = 3e8
frequency = 100e6
wavelength = c / frequency
L_over_lambda = 0.5
dipole_length = L_over_lambda * wavelength
I0 = 1.0
k = 2 * pi / wavelength
omega = 2 * pi * frequency
beta = k * dipole_length / 2
r = 1e6  # m

# Helper: Poynting function
def poynting(theta, r):
    sin_theta = np.sin(theta)
    if np.abs(sin_theta) < 1e-8:
        integral = dipole_length / 2
    else:
        cos_term = np.cos(beta * np.cos(theta)) - np.cos(beta)
        denom = np.sin(beta) * sin_theta**2
        if np.abs(denom) < 1e-12:
            integral = dipole_length / 2
        else:
            integral = (2 / k) * cos_term / denom
    A_z_value = (mu_0 * I0 * np.exp(-1j * k * r) / (4 * pi * r)) * integral
    E_theta_value = -1j * omega * A_z_value * np.sin(theta)
    return (np.abs(E_theta_value)**2) / (2 * eta_0)

# Compute P_rad first
def integrand(theta):
    return poynting(theta, r) * 2 * pi * r**2 * np.sin(theta)

P_rad, _ = quad(integrand, 0, pi, epsabs=1e-8, epsrel=1e-4, limit=1000)

# Equation
if np.abs(np.sin(beta)) < 1e-12:
    print("Sin(beta) is zero, radiation resistance approaches infinity.")
else:
    R_rad = 2 * P_rad / I0**2
    print(f"Radiation resistance R_rad: {R_rad:.2f} ohms")
```

