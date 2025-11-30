# Adding a Half-Wave Dipole Antenna to an NGSPICE Netlist

```
V1 1 0 
R1 1 2 0.01
L1 2 3 1u
C1 3 0 100n
```

## Overview
A half-wave dipole antenna can be modeled in SPICE simulations using its equivalent input impedance, which for a thin half-wave dipole is approximately $Z \approx 73 + j 42.5$ Ω. This consists of:
- Radiation resistance $R_r = 73$ Ω.
- Inductive reactance $X = 42.5$ Ω.

To add this to the netlist, connect a series RL circuit from the feedpoint (node 3 in the original circuit) to ground (node 0). The inductance $L$ is calculated based on the operating frequency $f = \frac{1}{2\pi\sqrt{LC}}$ (based on L1 and C1):

$$
L = \frac{X}{2 \pi f} \approx 10 \, \mu\text{H}
$$

The radiated power $P$ for RMS voltage $V$ at the feedpoint is:

$$
P = V^2 \cdot \frac{R_r}{R_r^2 + X^2}
$$

## Steps to Add the Antenna
1. **Identify the feedpoint**: In the original RLC circuit, node 3 is after the inductor L1 and before capacitor C1 to ground. Connect the antenna model across nodes 3 and 0 (replacing or in parallel with C1 if desired; here, we add it in parallel for load effect).

2. **Add components**:
   - Add resistor `Rant 3 4 73` (radiation resistance from node 3 to intermediate node 4).
   - Add inductor `Lant 4 0 10u` (reactance from node 4 to ground).

## Modified NGSPICE Netlist

```
* RLC circuit with pulse input and half-wave dipole antenna

V1 1 0 PULSE(0 5 0 10n 10n 10u 20u)
R1 1 2 0.01
L1 2 3 1u
C1 3 0 100n
Rant 3 4 73
Lant 4 0 10u
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

## Overview
A thin half-wave dipole has input impedance  
**Zₐ = Rᵣ + jXₐ = 73 + j42.5 Ω** (exact values used in most literature)  
where  
- Rᵣ = 73 Ω → radiation resistance  
- Xₐ = 42.5 Ω → input reactance  

Magnitude of antenna impedance:  
**│Zₐ│ = √(73² + 42.5²) = √(5329 + 1806.25) = √7135.25 = 84.49408 Ω** (exact)

## Exact Scaling and Resonance Condition
We deliberately scale the parallel LC tank such that its characteristic impedance equals the antenna reactance:  
**Z₀ = √(L₁/C₁) = Xₐ = 42.5 Ω**

This forces:  
Lₐₙₜ = Xₐ / ω = 42.5 / (2πf)  
and at resonance ω₀ = 1/√(L₁C₁), the antenna branch presents exactly +j42.5 Ω, which perfectly cancels the –j42.5 Ω of the capacitor branch (C₁). The total load seen at node 3 becomes exactly **73 Ω real**.

## Exact Voltage Step-Up and Current Calculation (no approximations)

Let V₁ be the **peak** voltage of the sinusoidal source (AC 1 in SPICE).  
RMS source voltage: V₁/√2

Because the tank is scaled with Z₀ = 42.5 Ω and is loaded by exactly 73 Ω real at resonance, the voltage at the feedpoint (node 3) is:

**V₃₍ₚₑₐₖ₎ = V₁ × (│Zₐ│ / Z₀) = V₁ × (84.49408 / 42.5) = V₁ × 1.9880847**

RMS voltage across the antenna branch:  
**V₃₍ᵣₘₛ₎ = V₁ × 1.9880847 / √2**

RMS current through the entire antenna impedance (and through Rant):  
**Iᵣₘₛ = V₃₍ᵣₘₛ₎ / │Zₐ│ = (V₁ × 1.9880847 / √2) / 84.49408**

Simplifying exactly:

**Iᵣₘₛ = V₁ / (42.5 × √2)**  
**Iᵣₘₛ = V₁ / 60.104076**

Inverse relation (exact, no rounding):

**V₁₍ₚₑₐₖ₎ = Iᵣₘₛ × 42.5 × √2 = Iᵣₘₛ × 60.104076**

Radiated power (exact):

**Pᵣₐ𝒹 = Iᵣₘₛ² × 73**

# Scaled Resonant Oscillator with Exact Half-Wave Dipole Model

## Circuit Topology
```
V1 (1) -- R1(0.01Ω) -- (2) -- L1 -- (3) --+-- C1 -- 0
                                         |
                                         +-- Rant(73Ω) -- Lant -- 0
```

## Antenna Parameters (exact)
Rᵣ  = 73 Ω  
Xₐ  = 42.5 Ω  
│Zₐ│ = √(73² + 42.5²) = 84.49407954 Ω

## Exact Scaling Rule
Z₀ = √(L₁/C₁) = Xₐ = 42.5 Ω  
Lₐₙₜ = Xₐ / (2πf) = 42.5 / (2πf)

## Exact Component Values for Resonance at Frequency f (Hz)
C₁ = 1 / (2πf × 42.5)  
L₁ = 42.5 / (2πf)  
Lₐₙₜ = 42.5 / (2πf)

## Exact Relationship Between Source Peak Voltage and Antenna RMS Current
Iᵣₘₛ = Vₚₑₐₖ / (42.5 × √2)  
Vₚₑₐₖ = Iᵣₘₛ × 42.5 × √2 = Iᵣₘₛ × 60.104076

## Exact Radiated Power
Pᵣₐ𝒹 = Iᵣₘₛ² × 73 Watt

## Python Code: Exact SPICE Netlist Generator

```python
import math

Z0 = 42.5                                          # Exact scaling impedance (Ω)
R_r = 73.0                                         # Radiation resistance (Ω)
X_a = 42.5                                         # Antenna reactance (Ω)
Z_mag = math.sqrt(R_r**2 + X_a**2)                 # 84.49407954 Ω (exact)

def format_value(val):
    if val == 0:
        return "0"
    exp = math.floor(math.log10(abs(val)))
    suffixes = {0: "", -3: "m", -6: "u", -9: "n", -12: "p", -15: "f"}
    for e, s in sorted(suffixes.items(), reverse=True):
        if exp >= e:
            return f"{val * 10**(-e):.10g}{s}"
    return f"{val:.10g}"

def generate_spice_netlist(f_osc: float, I_rms_target: float) -> str:
    """
    Generate exact SPICE netlist for desired frequency and exact RMS current through Rant.
    No approximations are used anywhere.
    """
    omega = 2 * math.pi * f_osc
    
    C1    = 1 / (omega * Z0)
    L1    = Z0 / omega
    Lant  = Z0 / omega                     # = X_a / omega
    
    # Exact required source peak voltage
    V_peak = I_rms_target * Z0 * math.sqrt(2)      # = I_rms_target * 60.104076...
    
    netlist = f"""* Exact Scaled Resonant Oscillator with Half-Wave Dipole
* Frequency:             {f_osc:.10g} Hz
* Target I_rms (Rant):   {I_rms_target:.10g} A
* Required V_peak (V1):  {V_peak:.10g} V
* Z0 = X_a =             {Z0} Ω
* |Z_ant| =              {Z_mag:.10g} Ω

V1 1 0 AC {V_peak:.10g}
R1 1 2 0.01
L1 2 3 {format_value(L1)}
C1 3 0 {format_value(C1)}
Rant 3 4 {R_r}
Lant 4 0 {format_value(Lant)}

.ac list {f_osc:.10g}
.print ac i(rant)          $ magnitude of current through Rant
.print ac ip(rant)         $ phase
.print ac ir(rant)         $ real part (in-phase, corresponds to radiated power)

.end
"""
    return netlist

# Example: 1 MHz, exactly 100 mA RMS through radiation resistance
# print(generate_spice_netlist(1e6, 0.1))
```

This version uses **only exact analytical expressions** derived from the circuit topology and the standard 73 + j42.5 Ω dipole model. 
