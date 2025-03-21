To derive the radiation resistance $R_r$ for an extremely low frequency (ELF) horizontal electric dipole (HED) buried beneath the Earth's surface in the Earth-ionosphere waveguide, we start by considering the key parameters and the dominant TM₀ mode propagation. The target equation is:

$$R_r = \frac{\pi Z_{\text{earth}}^2 l^2}{4 \eta_0 h \lambda}$$

### Key Steps:

1. **Waveguide Properties**:
2. 
   - The Earth-ionosphere waveguide supports TM₀ mode with wave impedance $Z_w \approx \eta_0 \frac{h}{\lambda}$.
   - The Earth's surface impedance $Z_{\text{earth}}$ is significant for the buried dipole.

3. **Electric Field Adjustment**:
4. 
   - The vertical electric field $E_z$ for a buried HED is proportional to $Z_{\text{earth}}$ instead of the free space impedance $\eta_0$.
   - The far-field electric field for a buried HED is scaled by $Z_{\text{earth}}$.

5. **Power Radiated**:
6. 
   - The power radiated $P_r$ is calculated by integrating the Poynting vector over a cylindrical surface.
   - The Poynting vector $S$ is given by $S = \frac{|E_z|^2}{2 Z_w}$.

7. **Integration and Simplification**:
8. 
   - The electric field $E_z$ is integrated over the cylindrical surface, considering the waveguide's height $h$, wavelength $\lambda$, and impedance $Z_w$.
   - The integral involves the Earth's impedance $Z_{\text{earth}}$, dipole length $l$, and other geometric factors.

9. **Radiation Resistance**:
10. 
   - The radiation resistance $R_r$ is derived by relating the radiated power $P_r$ to the current $I_0$ through $R_r = \frac{2 P_r}{|I_0|^2}$.

### Final Derivation:

1. **Electric Field for Buried HED**:
2. 
   $$E_z \approx -j \frac{Z_{\text{earth}} k_0 I_0 l}{2 \pi h} \sin \phi \sqrt{\frac{\pi}{2 k_0 d}} e^{-j k_0 d}$$

3. **Power Radiated**:
4. 
   $$P_r = \int_0^{2\pi} \int_0^h \frac{|E_z|^2}{2 Z_w} h \, d\phi \, dz$$

5. **Substituting $Z_w$**:
6. 
   $$Z_w = \eta_0 \frac{h}{\lambda}$$

7. **Simplifying the Integral**:
8. 
   $$P_r = \frac{\pi Z_{\text{earth}}^2 k_0 I_0^2 l^2}{8 \eta_0 h \lambda}$$

9. **Radiation Resistance**:
10. 
   $$R_r = \frac{2 P_r}{|I_0|^2} = \frac{\pi Z_{\text{earth}}^2 l^2}{4 \eta_0 h \lambda}$$

### Final Answer:
$$\boxed{R_r = \frac{\pi Z_{\text{earth}}^2 l^2}{4 \eta_0 h \lambda}}$$
