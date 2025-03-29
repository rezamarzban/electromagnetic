### Key Formulas for Antenna Analysis

#### 1. Current Magnitude (V is peak voltage):
$$|I|=\frac{V}{Z}=\frac{V}{\sqrt{R_r^2 + X^2}}$$

#### 2. Phase Angle:
$$\phi=\arctan\left(\frac{X}{R_r}\right)$$

#### 3. In-Phase (Real) Component of the Current:
$$I_{\text{real}}=|I|\cos\phi$$

#### 4. Reactive (Imaginary) Component of the Current:
$$I_{\text{reac}}=|I|\sin\phi$$

#### 5. Radiated Power:
$$P_{\text{rad}}=\frac{1}{2}|I|^2R_r$$


### Variable Explanations
- **`V`**: Peak voltage (volts) – Maximum amplitude of the sinusoidal voltage driving the circuit.
- **`|I|`**: Peak current magnitude (amperes) – Maximum amplitude of the sinusoidal current, calculated as `V / sqrt(R_r^2 + X^2)`.
- **`R_r`**: Radiation resistance (ohms) – Real impedance component, representing radiated power.
- **`X`**: Reactance (ohms) – Imaginary impedance component, due to capacitance or inductance.
- **`phi`**: Phase angle (radians) – Angle between voltage and current, given by `arctan(X / R_r)`.
- **`I_real`**: In-phase current (amperes) – Peak current component in phase with voltage, `|I| * cos(phi)`.
- **`I_reac`**: Reactive current (amperes) – Peak current component 90° out of phase, `|I| * sin(phi)`.
- **`P_rad`**: Radiated power (watts) – Average power radiated, calculated as `0.5 * |I|^2 * R_r`.

### Verification 

The accuracy of these formulas and codes is verified by same simulation results in `Altair FEKO`.
