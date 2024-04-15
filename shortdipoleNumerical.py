import numpy as np

r = 1000
theta = np.arange(0,np.pi,0.01)
I = 2
l = 0.1
K = 2*np.pi/6
eth0 = 377

E_theta = ((1j * K * I * l * eth0) / (4 * np.pi * r)) * np.sin(theta) * np.exp(-1j * K * r)
H_phi = E_theta / eth0
S_theta = 0.5 * np.real(E_theta * np.conjugate(H_phi))
P_rad = np.trapz(S_theta * r**2 * np.sin(theta), theta) * 2 * np.pi
Rr = 2 * P_rad / I**2

print(P_rad)
print(Rr)
