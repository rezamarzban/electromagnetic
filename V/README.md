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

# Adding a Half-Wave Dipole Antenna to an NGSPICE Netlist

## Overview
A half-wave dipole antenna can be modeled in SPICE simulations using its equivalent input impedance, which for a thin half-wave dipole is approximately $Z \approx 73 + j 42.5$ Ω. This consists of:
- Radiation resistance $R_r = 73$ Ω.
- Inductive reactance $X = 42.5$ Ω.

To add this to the netlist, connect a series RL circuit from the feedpoint (node 3 in the original circuit) to ground (node 0). The inductance $L$ is calculated based on the operating frequency $f = 50$ kHz (fundamental of the square wave):

$$
L = \frac{X}{2 \pi f} = \frac{42.5}{2 \pi \times 50 \times 10^3} \approx 135.3 \, \mu\text{H}
$$

The radiated power $P$ for RMS voltage $V$ at the feedpoint is:

$$
P = V^2 \cdot \frac{R_r}{R_r^2 + X^2}
$$

For a resonant dipole ($X=0$, $R_r \approx 70$ Ω), this simplifies to $P = V^2 / R_r$.

## Steps to Add the Antenna
1. **Identify the feedpoint**: In the original RLC circuit, node 3 is after the inductor L1 and before capacitor C1 to ground. Connect the antenna model across nodes 3 and 0 (replacing or in parallel with C1 if desired; here, we add it in parallel for load effect).

2. **Add components**:
   - Add resistor `Rant 3 4 73` (radiation resistance from node 3 to intermediate node 4).
   - Add inductor `Lant 4 0 135.3u` (reactance from node 4 to ground).

3. **Update simulation**: The `.tran` and control sections remain the same, but you can now probe voltages/currents at nodes 3, 4, or power through the antenna (e.g., via `.measure` for $I^2 R_r$).

4. **Considerations**:
   - This is a lumped-element approximation valid for low frequencies relative to antenna size (here, 50 kHz implies a physically huge antenna ~3 km long, but fine for circuit sim).
   - For resonance ($X=0$), shorten the dipole slightly and use $R_r=70$ Ω with no L.
   - Simulate radiated power: Use post-processing on current through Rant.

## Modified NGSPICE Netlist

```
* RLC circuit with 50kHz square wave input and half-wave dipole antenna

V1 1 0 PULSE(0 5 0 10n 10n 10u 20u)
R1 1 2 0.01
L1 2 3 1u
C1 3 0 100n
Rant 3 4 73
Lant 4 0 135.3u
.tran 10n 1m
.option numdgt=9
.save all
.control
  run
  set filetype=ascii
  wrdata sim.csv v(3)
set hcopydevtype=postscript
hardcopy sim.eps v(3)
.endc
.end
```
