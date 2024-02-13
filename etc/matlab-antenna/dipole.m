clear all;
close all;
format long;

%---Definition of constants and initialization---

PI = 4.0*atan(1.0);
E = 120.0*PI;
THETA = PI/180.0;
UMAX = 0.0;
PRAD = 0.0;
TOL = 1.0E-6;

%---The length and radius of the dipole (in wavelengths)---

L = 0.5;
r = 0.005;

%---Main program----------------------

A = L*PI;
I = 1;
while(I <= 180)
   XI = I*PI/180.0;
   if(XI ~= PI)
      U = ((cos(A*cos(XI))-cos(A))/sin(XI))^2*(E/(8.0*PI^2));
      if(U > UMAX)
         UMAX = U;
      end
   end
   UA = U*sin(XI)*THETA*2.0*PI;
   PRAD = PRAD+UA;
   I = I+1;
end
D = (4.0*PI*UMAX)/PRAD;
DDB = 10.0*log10(D);
RR = 2.0*PRAD;
if(A ~= PI)
   RIN = RR/(sin(A))^2;
end

fprintf("Radiation resistance of dipole antenna: %d Ohm", RR);
