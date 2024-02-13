* Use expert electromagnetic simulation softwares such as Altair Feko, ANSYS Maxwell, CST Studio, Magus pro, MATLAB Antenna toolbox and so on.

Eff = f(I0, k, r)

Hff = Eff / eth0

S_av = 1/2 Re{Eff × Hff*}

P_rad = integral S_av.dS

Rr = 2 P_rad / I0^2

I_real = P_rad / V

I0 = V / R_ant

R_ant = R_overall (Ideally is equal to R_img)

R_img = Omega L

which:

Eff is farfield radiation electricity field

Hff is farfield radiation magnetic field 

S_av is average Poynting Vector 

P_rad is radiated power 

Rr is radiation resistance 

I0 is antenna current max at zero point

I_real is real part of antenna current which consumed at radiation and heat loss, It is part of current magnitude of antenna (I_real < I0)

k is wavenumber

r is farfield radius >> lambda

eth0 is impedance of Air = 377 Ohm, Radiation resistance of Air

dS is over a sphere of radius r include radical component (r² sin(Theta) dTheta dPhi)

V is antenna voltage 

R_ant is antenna resistance or R_overall against antenna feed voltage which R_ant = V / I0

R_overall is overall resistance of antenna against antenna feed voltage which determine antenna current I0 = V / R_overall. It is consist of image impedance, Ohmic resistance and radiation resistance. If assume antenna is a circuit, At close circuit (loop antennas) and open circuit (dipole and monopole antennas) the R_overall will be obtained via different formulas at different conditions.

R_ohm is ohmic antenna resistance 

R_img is antenna image resistance 

Omega is frequency radiant = 2πf

L is inductance capacity of antenna 

* most notable components

 `P_rad = I0² Rr / 2`
 
 `I0 = V / (R, Rr, R_img)`
