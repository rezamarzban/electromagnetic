PROGRAM SHORT_DIPOLE_NUMERICAL
  IMPLICIT NONE
  
  REAL :: r, theta, theta_step, I, l, K, eth0, pi
  COMPLEX :: E_theta, H_phi
  REAL :: S_theta, P_rad, Rr
  
  r = 1000.0
  pi = 3.14
  I = 2.0
  l = 0.1
  K = 2.0 * pi / 6.0
  eth0 = 377.0
  theta = 0.0
  theta_step = 0.01
  P_rad = 0.0
  
  DO WHILE (theta <= pi)
    theta = theta + theta_step
    E_theta = ((CMPLX(0.0, 1.0) * K * I * l * eth0) / (4.0 * pi * r)) * SIN(theta) * EXP(-CMPLX(0.0, 1.0) * K * r)
    H_phi = E_theta / eth0
    S_theta = 0.5 * REAL(E_theta * CONJG(H_phi))
    P_rad = P_rad + S_theta * r**2 * SIN(theta) * 2 * pi * theta_step
  END DO
  
  Rr = 2.0 * P_rad / (I**2)
  
  PRINT *, "Radiated power:", P_rad
  PRINT *, "Radiation resistance:", Rr
  
END PROGRAM SHORT_DIPOLE_NUMERICAL
