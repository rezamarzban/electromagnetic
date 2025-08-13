
### Overview
The analysis computes the radiation resistance ($R_\mathrm{rad}$) of a short vertical monopole antenna at low frequencies using two methods: a first-principles approach (via vector potential, far-field electric field, and Poynting vector integration) and the standard formula. Assumptions include a triangular current distribution $$I(z) = I_0 (1 - z/h)$$ for $0 \leq z \leq h$, a perfect ground plane, and $h \ll \lambda$. Parameters are $h = 3000$ m, $f = 100$ Hz ($\lambda = c/f = 3 \times 10^6$ m, $h/\lambda = 0.001$), and $I_0 = 1$ A, yielding $R_\mathrm{rad} \approx 3.95 \times 10^{-4} \, \Omega$.

### Step 1: Constants and Parameters
- **Equations**:
  - Speed of light: $c = 3 \times 10^8$ m/s.
  - Permeability: $\mu_0 = 4\pi \times 10^{-7}$ H/m.
  - Permittivity: $\epsilon_0 = 8.854 \times 10^{-12}$ F/m.
  - Impedance: $\eta = \sqrt{\mu_0 / \epsilon_0} \approx 376.73 \, \Omega$.
- **Parameters**: $h = 3000$ m, $f = 100$ Hz, $I_0 = 1$ A.
- **Derived**:
  - Angular frequency: $\omega = 2\pi f = 628.32$ rad/s.
  - Wavenumber: $\beta = \omega / c = 2.0944 \times 10^{-6}$ rad/m.
  - Wavelength: $\lambda = c / f = 3 \times 10^6$ m.

### Step 2: Effective Current Integral
- **Equation**: The monopole’s current $I(z) = I_0 (1 - z/h)$ is mirrored by the ground plane, equivalent to a dipole of length $2h$ with $I(z) = I_0 (1 - |z|/h)$ for $-h \leq z \leq h$. The current moment is $$\int_{-h}^h I(z) \, dz = 2 \int_0^h I_0 (1 - z/h) \, dz = I_0 h$$.
- **Evaluation**: $integral_A = I_0 h = 1 \times 3000 = 3000$ A·m.

### Step 3: Vector Potential $A_z$
- **Equation**: Far-field vector potential (phase neglected): $$A_z = \frac{\mu_0}{4\pi r} \int I(z) \, dz = \frac{\mu_0 I_0 h}{4\pi}$$ (r-dependence omitted as it cancels).
- **Evaluation**: $$A_z = \frac{4\pi \times 10^{-7} \times 3000}{4\pi} = 3 \times 10^{-4}$$ H.

### Step 4: Electric Field Magnitude Factor $E_\theta\_\mathrm{mag}$
- **Equation**: Far-field $E_\theta$ is $$|E_\theta| = \omega |A_z| \sin \theta / r$$, with magnitude factor $$E_\theta\_\mathrm{mag} = \omega A_z = \omega \frac{\mu_0 I_0 h}{4\pi}$$.
- **Evaluation**: $$E_\theta\_\mathrm{mag} = 628.32 \times 3 \times 10^{-4} = 0.1885$$ V.

### Step 5: Integrand for Radiated Power
- **Equation**: Poynting vector gives $$P_\mathrm{rad} = \int_0^{2\pi} \int_0^{\pi/2} \frac{|E_\theta|^2}{2 \eta} r^2 \sin \theta \, d\theta \, d\phi$$, where $$|E_\theta| = E_\theta\_\mathrm{mag} \sin \theta / r$$. Integrand is $$\frac{E_\theta\_\mathrm{mag}^2 \sin^3 \theta}{2 \eta}$$.

### Step 6: Numerical Integration for $P_\mathrm{rad}$
- **Equation**: $$P_\mathrm{rad} = \frac{E_\theta\_\mathrm{mag}^2}{2 \eta} \int_0^{2\pi} d\phi \int_0^{\pi/2} \sin^3 \theta \, d\theta = \frac{2\pi E_\theta\_\mathrm{mag}^2}{3 \eta}$$, since $$\int_0^{\pi/2} \sin^3 \theta \, d\theta = 2/3$$. Substituting $E_\theta\_\mathrm{mag}$: $$P_\mathrm{rad} = \frac{\eta \beta^2 I_0^2 h^2}{24 \pi}$$.
- **Evaluation**: $P_\mathrm{rad} \approx 1.9753 \times 10^{-4}$ W (from $R_\mathrm{rad}$).

### Step 7: Radiation Resistance $R_\mathrm{rad}$
- **Equation**: $$R_\mathrm{rad} = 2 P_\mathrm{rad} / I_0^2 = \frac{\eta \beta^2 h^2}{12 \pi}$$. Since $\beta = 2\pi / \lambda$, $$R_\mathrm{rad} = \frac{\eta 4\pi^2 (h/\lambda)^2}{12 \pi} \approx 40 \pi^2 (h/\lambda)^2$$ (with $\eta \approx 120\pi$).
- **Evaluation**: $R_\mathrm{rad} \approx 3.9505 \times 10^{-4} \, \Omega$ (exact $\eta$).

### Step 8: Standard Formula
- **Equation**: $$R_\mathrm{rad} \approx 40 \pi^2 (h / \lambda)^2$$.
- **Evaluation**: $(h / \lambda)^2 = 10^{-6}$, $40 \pi^2 \approx 394.784$, so $3.9478 \times 10^{-4} \, \Omega$.
- **Note**: The 0.07% difference is due to $\eta = 376.73$ vs. $120\pi \approx 377$.
