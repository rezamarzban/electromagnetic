# pip install PyNEC==1.7.3.4
# pip install necpp (Optional)
#
# Monopole antenna length=3m, Frequency range=20 to 30MHZ, Reference impedance=50Ohms
#
# Number of segments ,Source voltage and etc can be set at monopole.py
#
# Note: Casting complex values to real discards the imaginary part
#


import numpy as np
import pylab as plt

# Custom libs which coded manually 
import monopole
from antenna_util import reflection_coefficient

freqs = np.linspace(20, 30)
real_impedances = []
reflections = []
z0 = 50

for f in freqs:
  z = monopole.impedance(f, base=0.5, length=3)
  real_impedances.append(z.real) # Or append(z) because of explained matter at note.
  reflections.append(reflection_coefficient(z, z0))

plt.plot(freqs, real_impedances)
plt.xlabel("Frequency")
plt.ylabel("Real impedance")
plt.title("Real impedance vs frequency (base_height=0.5m, antenna length=3m)")
plt.grid(True)
plt.show()
plt.savefig("real_impedance.png")

plt.plot(freqs, reflections)
plt.xlabel("Frequency")
plt.ylabel("Reflection coefficient")
plt.title("Reflection coefficient vs frequency (base_height=0.5m, antenna length=3m)")
plt.grid(True)
plt.show()
plt.savefig("reflection_coefficient.png")
