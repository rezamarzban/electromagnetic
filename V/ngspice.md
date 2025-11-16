# Adding a Half-Wave Dipole Antenna to an NGSPICE Netlist

## Overview
A half-wave dipole antenna can be modeled in SPICE simulations using its equivalent input impedance, which for a thin half-wave dipole is approximately $Z \approx 73 + j 42.5$ Ω. This consists of:
- Radiation resistance $R_r = 73$ Ω.
- Inductive reactance $X = 42.5$ Ω.

To add this to the netlist, connect a series RL circuit from the feedpoint (node 3 in the original circuit) to ground (node 0). The inductance $L$ is calculated based on the operating frequency $f = \(\frac{1}{2\pi\sqrt{LC}}\)$ (which f = 1/(2π√(LC)) based on L1 and C1):

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
* RLC circuit with 50kHz square wave input and half-wave dipole antenna

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
