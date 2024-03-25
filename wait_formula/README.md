Wait's formula:
![image1](Wait_formula.jpg)

Very complex Wait's formula is derived from Norton-Sommerfeld equations, To calculating this confusing formula by `Symbolic` package at `Octave` use `Wait_formula.m` file as below. Also be noticed that `SymPy` is lacking to solve and calculating complex integrals with imaginary part! But `Symbolic` package at `Octave` which use `SymPy` doesn't lack:

```
pkg load symbolic

syms r eta beta rho a h real

beta = 2*pi/100;
a = 18;
h = 20;

r = sqrt(rho^2 + h^2);

expr0 = (-eta)/((2*pi*sin(beta*h)^2));
expr1 = int(exp(-1i*2*beta*r)/rho, rho, a, inf); 
expr2 = -1*2*cos(beta*h)*int(exp(-beta*1i*(r + rho))/rho, rho, a, inf); 
expr3 = -cos(beta*h)^2*int(exp(-1i*2*beta*rho)/rho, rho, a, inf);

norm = 4*pi*expr0/eta;

norm_deltaZ_re = real(double(norm) * (double(expr1) + double(expr2) + double(expr3)))
```

It calculate normalized radiation resistance (=Real{4π∆Z/η}) of a sample antenna which is related only to ground wave propagation part (see below image for more info), In few lines of codes!

![image2](DeltaZ.jpg)

It is recommended to use `MATLAB` and `Altair FEKO`, `ANSYS Maxwell ` and etc to calculating and simulating electromagnetic problems.
