clear all;
close all;
format long;

PI = 4.0*atan(1.0);
E = 120.0*PI;
THETA = PI/180.0;
UMAX = 0.0;
PRAD = 0.0;
TOL = 1.0E-5;

%---The radius of the loop antenna (in wavelengths)---

A = 1;

%---Main program------------------------------------

I = 1;
while(I <= 180)
   XI = I*PI/180.0;
   X = 2.0*PI*A*sin(XI);
   if(abs(X) < TOL)
      F = 0.0;
   else
      F = besselj(1,X);
   end
   U = A^2*(2.0*PI)^2/8.0*E*F^2;
   if(U > UMAX)
      UMAX = U;
   end
   UA = U*sin(XI)*THETA*2*PI;
   PRAD = PRAD+UA;
   I = I+1;
end
D = (4.0*PI*UMAX)/PRAD;
DDB = 10.0*log10(D);
RR = 2.0*PRAD;

fprintf("Radiation resistance of loop antenna: %d Ohm", RR);
