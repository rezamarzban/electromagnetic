# Radiation Resistance of a Half-Wave Dipole Antenna via Maxwell's Equations

## Theoretical Derivation

### **1. Current Distribution**
For a half-wave dipole of length \( L = \lambda/2 \), the sinusoidal current distribution is:
$$I(z') = I_0 \sin\left(k\left(\frac{L}{2} - |z'|\right)\right), \quad -\frac{L}{2} \leq z' \leq \frac{L}{2} $$
where \( k = \frac{2\pi}{\lambda} \), and \( I_0 \) is the peak current.

---

### **2. Magnetic Vector Potential**
The magnetic vector potential for a dipole aligned along the \( z \)-axis is:
$$A_z(r) = \frac{\mu_0}{4\pi} \int_{-L/2}^{L/2} \frac{I(z') e^{-jkR}}{R} \, dz' $$
In the **far-field** (\( r \gg \lambda \)):
- \( R \approx r - z'\cos\theta \) (phase term),
- \( R \approx r \) (amplitude term).

Simplifies to:
$$A_z(r) \approx \frac{\mu_0 I_0 e^{-jkr}}{4\pi r} \int_{-L/2}^{L/2} \sin\left(k\left(\frac{L}{2} - |z'|\right)\right) e^{jkz'\cos\theta} \, dz' $$

---

### **3. Solving the Integral**
For \( L = \lambda/2 \), the integral evaluates to:
$$\int_{-L/2}^{L/2} \sin\left(k\left(\frac{L}{2} - |z'|\right)\right) e^{jkz'\cos\theta} \, dz' = \frac{2}{k} \frac{\cos\left(\frac{\pi}{2} \cos\theta\right)}{\sin^2\theta} $$

---

### **4. Electric and Magnetic Fields**
- **Electric Field** (\( \mathbf{E} \)):
$$E_\theta = -j\omega \mu_0 A_z \sin\theta = \frac{j\eta_0 I_0 e^{-jkr}}{2\pi r} \frac{\cos\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta} $$
- **Magnetic Field** (\( \mathbf{H} \)):
$$H_\phi = \frac{E_\theta}{\eta_0} $$

---

### **5. Poynting Vector and Radiated Power**
- **Time-Averaged Poynting Vector**:
$$S = \frac{1}{2} \text{Re}(E_\theta H_\phi^*) = \frac{\eta_0 |I_0|^2}{8\pi^2 r^2} \frac{\cos^2\left(\frac{\pi}{2}\cos\theta\right)}{\sin^2\theta} $$
- **Total Radiated Power**:
$$P_{\text{rad}} = \int_0^{2\pi} \int_0^\pi S \, r^2 \sin\theta \, d\theta d\phi = \frac{\eta_0 |I_0|^2}{4\pi} \int_0^\pi \frac{\cos^2\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta} \, d\theta $$

---

### **6. Radiation Resistance**
$$R_{\text{rad}} = \frac{2P_{\text{rad}}}{I_0^2} = \frac{\eta_0}{2\pi} \int_0^\pi \frac{\cos^2\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta} \, d\theta \approx 73 \, \Omega $$

---

## Key Result
The radiation resistance of a half-wave dipole antenna is approximately **73 Ω**, derived rigorously from Maxwell's equations using the magnetic vector potential formalism.
