To calculate the radiation resistance \( R_{\text{rad}} \) of a **short monopole antenna** at **low frequencies** using Maxwell’s equations and the magnetic vector potential, here is derivation of the formula.

---

### **Derivation Using Maxwell’s Equations**

1. **Magnetic Vector Potential (\( \mathbf{A} \))**:
   For a vertical monopole with current \( I(z) = I_0 \left(1 - \frac{z}{h}\right) \) (linear approximation for \( h \ll \lambda \)):
   $$\mathbf{A} = \frac{\mu_0}{4\pi} \int_0^h \frac{I(z') e^{-j\beta r'}}{r'} \, dz' \, \hat{\mathbf{z}},$$
   where \( \beta = \frac{2\pi}{\lambda} \), \( \lambda = \frac{c}{f} \), and \( r' \approx r - z' \cos\theta \) in the far field.

2. **Far-Field Simplification**:
   For \( h \ll \lambda \), \( e^{j\beta z' \cos\theta} \approx 1 \). The integral simplifies to:
   $$A_z \approx \frac{\mu_0 I_0 h}{8\pi r} e^{-j\beta r}.$$

3. **Electric and Magnetic Fields**:
   Using \( \mathbf{E} = -j\omega\mathbf{A} \) and \( \mathbf{H} = \frac{1}{\eta} \hat{\mathbf{r}} \times \mathbf{E} \), the radiated power is:
   $$P_{\text{rad}} = \int \frac{|\mathbf{E}|^2}{2\eta} \, d\Omega = \frac{40\pi^2 I_0^2 h^2}{\lambda^2}.$$

4. **Radiation Resistance**:
   $$R_{\text{rad}} = \frac{2P_{\text{rad}}}{I_0^2} = 40\pi^2 \left(\frac{h}{\lambda}\right)^2 \approx 395 \left(\frac{h}{\lambda}\right)^2 \, \Omega.$$

---

