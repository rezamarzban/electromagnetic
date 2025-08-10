V = 10.0;
R_r = 50.0;
X = 25.0;

I_mag = V / sqrt(R_r^2 + X^2);
phi = atan(X / R_r);

I_real = I_mag * cos(phi)
I_reac = I_mag * sin(phi)

P_rad = 0.5 * (I_mag ^ 2) * R_r
