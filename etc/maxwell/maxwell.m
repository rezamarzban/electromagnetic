clear all
clc

syms mu_0 epsilon_0
syms X [3 1] matrix
syms E(X,t) B(X,t) [3 1] matrix keepargs

Maxwell1 = divergence(E,X) == 0

Maxwell2 = curl(E,X) == -diff(B,t)

Maxwell3 = divergence(B,X) == 0

Maxwell4 = curl(B,X) == mu_0*epsilon_0*diff(E,t)

wave_E = curl(Maxwell2,X)

wave_E = subs(wave_E,lhs(Maxwell1),rhs(Maxwell1))

dMaxwell4 = diff(Maxwell4,t)

wave_E = subs(wave_E,lhs(dMaxwell4),rhs(dMaxwell4))

wave_B = curl(Maxwell4,X)

wave_B = subs(wave_B,lhs(Maxwell3),rhs(Maxwell3))

dMaxwell2 = diff(Maxwell2,t)

wave_B = subs(wave_B,lhs(dMaxwell2),rhs(dMaxwell2))
