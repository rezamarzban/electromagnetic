import numpy as np
import meep as mp

import matplotlib

matplotlib.use("agg")
import matplotlib.pyplot as plt

sxy = 300
f = 0.005
src_cmpt = mp.Ey

area = mp.Vector3(sxy+2,sxy+2,0)

dip = [mp.Block(mp.Vector3(0.01, 49.5),
        center=mp.Vector3(0,25),
        material=mp.metal),

        mp.Block(mp.Vector3(0.01, 49.5),
        center=mp.Vector3(0,-25),
        material=mp.metal),

        mp.Block(mp.Vector3(0.01, 0.5),
        center=mp.Vector3(0, 0),
        material=mp.Medium( D_conductivity=0.05))
        ]

src = [mp.Source(mp.ContinuousSource(frequency=f),
        center=mp.Vector3(0,0,0),
        component=mp.Ey,
        amplitude=1.0),
        ]

sim = mp.Simulation(cell_size=area, boundary_layers=[mp.PML(1)],
                    geometry=dip, sources=src, resolution=10)

plt.figure(dpi=100)
sim.plot2D()
plt.savefig("sim.png")
plt.show()

sim.run(until=200)

ey_data = sim.get_array(center=mp.Vector3(0, 0, 0), size=mp.Vector3(sxy, sxy, 0), component=mp.Ey)

radiated_power = np.sum((np.abs(ey_data) ** 2) / 2)

print("Radiated Power:", radiated_power)
