# electromagnetic
Electromagnetic formulas, simulation softwares and codes

The goal of these codes is to simplify complex electromagnetic physics equations and calculations into just a few lines of MATLAB and Python code. These codes get straight to the point, avoiding unnecessary details, to solve problems efficiently.

All the equations from a physics textbook on electromagnetism are condensed into a few lines of MATLAB and Python code here. For example, deriving and calculating the Poynting Vector integral from the far-field radiation electric field equation allows you to determine critical antenna behaviors such as radiated power and radiation resistance in just a few lines of Python code:

short dipole antenna equations 

```
import sympy as sp

r, theta, phi, I, l, K, eth0 = sp.symbols('r theta phi I l K eth0', real=True)

E_theta = ((1j * K * I * l * eth0) / (4 * sp.pi * r)) * sp.sin(theta) * sp.exp(-1j * K * r)
H_phi = E_theta / eth0
S_theta = 0.5 * sp.re(E_theta * sp.conjugate(H_phi))
P_rad = sp.integrate(sp.integrate(S_theta * r**2 * sp.sin(theta), (theta, 0, sp.pi)), (phi, 0, 2*sp.pi))
Rr = 2 * P_rad / I**2

Power = P_rad.subs([(eth0, 377), (I, 2), (l, 0.1), (K, 2*sp.pi/6)]).evalf()  # Watts
Radiation_resistance = Rr.subs([(eth0, 377), (l, 0.1), (K, 2*sp.pi/6)]).evalf()  # Ohms

print(Power)
print(Radiation_resistance)
```

In addition to printing short dipole antenna equations in a clear and concise format, you can use this code as shown below, continuing from the previous example. This is also fully explained in the `shortdipoleEquations.ipynb` file:

```
from sympy import init_printing
init_printing()
```

![image1](shortdipoleEquations.jpg)

Additionally, various numerical method codes are provided in different languages (MATLAB, Python, FORTRAN, Java, C++, JavaScript, HTML). The `shortdipoleNumerical.js` code can be used in `Math Notepad`, which is powered by `mathjs.org`. This means you only need a web browser to run it, without any software installation. Guidance can be found here:

https://github.com/rezamarzban/mathjs/tree/main/mathnotepad

Another web-based code is available: run the `shortdipoleNumerical.html` code by downloading and opening it in a web browser on any OS, without requiring any additional libraries or an internet connection. You can also easily edit `shortdipoleNumerical.html` with a simple text editor like `Notepad`. So:

IDE: `Notepad`

Compiler: `Web browser`

These are the simplest tools in the world of IT and programming languages that can solve the most complex problems in the world of math and physics.
