### Defining Radiated Power

The radiated power $P_r$ represents the total electromagnetic power flowing outward through a cylindrical surface surrounding a dipole in a waveguide. This surface has a radius $d$ and height $h$. In cylindrical coordinates $(r, \phi, z)$, with the dipole aligned along the $z$-axis, the power flows radially outward at $r = d$. The differential area element on this cylindrical surface is $d \, d\phi \, dz$, where $\phi$ ranges from 0 to $2\pi$ (full azimuthal sweep) and $z$ ranges from 0 to $h$ (height of the waveguide section).

The power is calculated by integrating the radial component of the Poynting vector $S_r$ over this surface:

$$P_r = \int_0^{2\pi} \int_0^h S_r \, d \, d\phi \, dz$$

For the TM₀ mode (transverse magnetic, with no azimuthal magnetic field component), the radial Poynting vector is related to the electric field. Specifically:

$$S_r = \frac{|E_z|^2}{2 Z_w}$$

Here, $E_z$ is the longitudinal electric field component (since TM modes have $H_z = 0$), and $Z_w$ is the wave impedance for the mode in the waveguide, given as:

$$Z_w = \eta_0 \frac{h}{\lambda}$$

where:
- $\eta_0$ is the intrinsic impedance of free space ($\approx 376.73 \, \Omega$),
- $h$ is the height of the waveguide,
- $\lambda$ is the wavelength.

Thus, the power becomes:

$$P_r = \int_0^{2\pi} \int_0^h \frac{|E_z|^2}{2 Z_w} \, d \, d\phi \, dz$$

---

### Expressing the Electric Field $E_z$

The electric field $E_z$ for the dipole in the cylindrical waveguide is provided as:

$$E_z = -j \frac{Z_{\text{earth}} k_0 I_0 l}{2 \pi h} \sin \phi \sqrt{\frac{\pi}{2 k_0 d}} e^{-j k_0 d}$$

where:
- $Z_{\text{earth}}$ is an impedance related to the boundary (assumed real for simplicity, or we take its magnitude if complex),
- $k_0 = \frac{2\pi}{\lambda}$ is the free-space wavenumber,
- $I_0$ is the dipole current amplitude,
- $l$ is the dipole length,
- $h$ is the waveguide height,
- $d$ is the radial distance to the cylindrical surface,
- $\phi$ is the azimuthal angle,
- $j = \sqrt{-1}$ is the imaginary unit.

To compute the power, we need the magnitude squared, $|E_z|^2$. Let’s break it down:

- Magnitude of complex factors:
  - $|-j| = 1$,
  - $|e^{-j k_0 d}| = 1$ (since it’s a phase factor),
  - $\sin \phi$ is real, so $|\sin \phi| = \sin \phi$ when squared becomes $\sin^2 \phi$,
  - Assume $Z_{\text{earth}}$ is real (or replace with $|Z_{\text{earth}}|$ if complex).

Thus:

$$|E_z| = \left| \frac{Z_{\text{earth}} k_0 I_0 l}{2 \pi h} \sin \phi \sqrt{\frac{\pi}{2 k_0 d}} \right|$$

$$|E_z|^2 = \left( \frac{Z_{\text{earth}} k_0 I_0 l}{2 \pi h} \right)^2 \sin^2 \phi \frac{\pi}{2 k_0 d}$$

Simplify:

$$|E_z|^2 = \frac{Z_{\text{earth}}^2 k_0^2 I_0^2 l^2}{4 \pi^2 h^2} \sin^2 \phi \frac{\pi}{2 k_0 d}$$

---

### Setting Up the Power Integral

Substitute $|E_z|^2$ into the power expression:

$$P_r = \int_0^{2\pi} \int_0^h \frac{1}{2 Z_w} \cdot \frac{Z_{\text{earth}}^2 k_0^2 I_0^2 l^2}{4 \pi^2 h^2} \sin^2 \phi \frac{\pi}{2 k_0 d} \, d \, d\phi \, dz$$

Factor out constants (those not depending on $\phi$ or $z$):

$$P_r = \frac{Z_{\text{earth}}^2 k_0^2 I_0^2 l^2}{8 \pi^2 h^2 Z_w} \cdot \frac{\pi}{2 k_0 d} \cdot d \cdot \int_0^{2\pi} \sin^2 \phi \, d\phi \int_0^h dz$$

Notice that $d$ (radius) appears both inside and outside the integral due to the area element. The $d$ terms cancel:

$$P_r = \frac{Z_{\text{earth}}^2 k_0^2 I_0^2 l^2}{8 \pi^2 h^2 Z_w} \cdot \frac{\pi}{2 k_0} \int_0^{2\pi} \sin^2 \phi \, d\phi \int_0^h dz$$

---

### Evaluating the Integrals

- **Height integral**: Since $|E_z|^2$ and $Z_w$ are independent of $z$ (assuming uniformity along the waveguide height):

$$\int_0^h dz = h$$

- **Azimuthal integral**: The average value of $\sin^2 \phi$ over a full cycle is:

$$\int_0^{2\pi} \sin^2 \phi \, d\phi$$

Using the identity $\sin^2 \phi = \frac{1 - \cos 2\phi}{2}$:

$$\int_0^{2\pi} \frac{1 - \cos 2\phi}{2} \, d\phi = \frac{1}{2} \left[ \phi - \frac{\sin 2\phi}{2} \right]_0^{2\pi} = \frac{1}{2} \left[ 2\pi - 0 \right] = \pi$$

So:

$$P_r = \frac{Z_{\text{earth}}^2 k_0^2 I_0^2 l^2}{8 \pi^2 h^2 Z_w} \cdot \frac{\pi}{2 k_0} \cdot \pi \cdot h$$

Simplify step-by-step:

$$P_r = \frac{Z_{\text{earth}}^2 k_0^2 I_0^2 l^2}{8 \pi^2 h^2 Z_w} \cdot \frac{\pi^2 h}{2 k_0}$$

$$= \frac{Z_{\text{earth}}^2 k_0^2 I_0^2 l^2 h}{16 \pi^2 h^2 Z_w k_0}$$

$$= \frac{Z_{\text{earth}}^2 k_0 I_0^2 l^2}{16 \pi^2 h Z_w}$$

---

### Substituting $Z_w$ and $k_0$

Now, substitute $Z_w = \eta_0 \frac{h}{\lambda}$:

$$P_r = \frac{Z_{\text{earth}}^2 k_0 I_0^2 l^2}{16 \pi^2 h \cdot \eta_0 \frac{h}{\lambda}} = \frac{Z_{\text{earth}}^2 k_0 I_0^2 l^2 \lambda}{16 \pi^2 h^2 \eta_0}$$

Substitute $k_0 = \frac{2\pi}{\lambda}$:

$$P_r = \frac{Z_{\text{earth}}^2 \cdot \frac{2\pi}{\lambda} \cdot I_0^2 l^2 \lambda}{16 \pi^2 h^2 \eta_0}$$

The $\lambda$ terms cancel:

$$P_r = \frac{Z_{\text{earth}}^2 \cdot 2\pi I_0^2 l^2}{16 \pi^2 h^2 \eta_0}$$

Simplify:

$$P_r = \frac{Z_{\text{earth}}^2 I_0^2 l^2}{8 \pi h^2 \eta_0}$$

---

### Final Expression

The radiated power for the dipole in the cylindrical waveguide is:

$$P_r = \frac{Z_{\text{earth}}^2 I_0^2 l^2}{8 \pi \eta_0 h^2}$$

---

### Verification

Let’s check the units to ensure physical consistency:
- $Z_{\text{earth}}^2$: $\Omega^2$ (ohms squared),
- $I_0^2$: $A^2$ (amperes squared),
- $l^2$: $m^2$ (meters squared),
- $\eta_0$: $\Omega$ (ohms),
- $h^2$: $m^2$ (meters squared).

$$\frac{\Omega^2 \cdot A^2 \cdot m^2}{\Omega \cdot m^2} = \Omega A^2 = W$$

The units match power (watts), confirming the derivation is dimensionally correct.

Additionally, the absence of $d$ (radius) in the final expression makes sense, as the power should represent the total radiated power, and the field’s radial dependence was integrated over the surface at $r = d$, with dependencies canceling appropriately.

---

### Conclusion

After careful derivation, the radiated power $P_r$ for a dipole in a cylindrical waveguide, operating in the TM₀ mode, is:

$$P_r = \frac{Z_{\text{earth}}^2 I_0^2 l^2}{8 \pi \eta_0 h^2}$$

This expression depends on the boundary impedance, dipole current and length, waveguide height, and free-space impedance, providing a clear and concise result for the power radiated.
