PROGRAM SHORT_DIPOLE_NUMERICAL
  IMPLICIT NONE
  
  REAL :: r, theta, I, l, K, eth0
  COMPLEX :: E_theta, H_phi
  REAL :: S_theta, P_rad, Rr
  
  r = 1000.0
  theta = 0.0
  I = 2.0
  l = 0.1
  K = 2.0 * 3.14159 / 6.0
  eth0 = 377.0
  P_rad = 0.0
  
  DO WHILE (theta <= 3.14159)
    theta = theta + 0.01
    
    E_theta = ((CMPLX(0.0, 1.0) * K * I * l * eth0) / (4.0 * 3.14159 * r)) * SIN(theta) * EXP(-CMPLX(0.0, 1.0) * K * r)
    
    H_phi = E_theta / eth0
    
    S_theta = 0.5 * REAL(E_theta * CONJG(H_phi))
    
    P_rad = P_rad + S_theta * r**2 * SIN(theta) * 2 * 3.14 * 0.01
  END DO
  
  Rr = 2.0 * P_rad / (I**2)
  
  PRINT *, "P_rad:", P_rad
  PRINT *, "Rr:", Rr
  
END PROGRAM SHORT_DIPOLE_NUMERICAL
