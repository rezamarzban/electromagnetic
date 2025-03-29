


Mathematica code to showing Electric Lines of Force of Infinitesimal Dipole:

```
l = 0.2;

dip = {RGBColor[1, 0, 0], Arrow[{{0, -l/2}, {0, l/2}}]};

ncell = 8;

k0 = 2 * Pi;

R[x_, y_] := k0 * Sqrt[x^2 + y^2];

θ[x_, y_] := ArcTan[x, y];

contrs = Table[c, {c, -0.9, 0.9, 0.2}];

anim = Table[
  ContourPlot[
    (Cos[R[x, y] - T] + Sin[R[x, y] - T] / R[x, y]) * (Sin[θ[x, y]])^2,
    {x, -1, 1}, {y, -1, 1},
    PlotPoints -> 100,
    Contours -> contrs,
    ContourShading -> False,
    ImageSize -> {288, 288},
    FrameTicks -> None,
    Epilog -> dip
  ],
  {T, 0, Pi - Pi/ncell, Pi/ncell}
];
```

It's equivalent in python is `ElectricField_RadiatingDipole_V2.py` code.

Please be note that another python code, The `ElectricField_RadiatingDipole.py` code, is educational and not real.
