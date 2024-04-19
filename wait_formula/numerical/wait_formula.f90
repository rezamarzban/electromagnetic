program wait_formula
    implicit none
    
    real :: beta, a, h, rho, rho_step, pi, infinity
    complex :: norm_deltaZ
    complex :: integral1, integral2, integral3

    pi = 3.14
    beta = 2.0 * pi / 100.0
    a = 18.0
    h = 20.0
    infinity = 1000
    rho = a
    rho_step = 0.01
    
    integral1 = 0.0
    integral2 = 0.0
    integral3 = 0.0
    do while (rho <= infinity)
        rho = rho + rho_step
        integral1 = integral1 + (exp(-2.0 * cmplx(0.0, 1.0) * beta * sqrt(rho**2 + h**2)) / rho) * rho_step
        integral2 = integral2 + (exp(-beta * cmplx(0.0, 1.0) * (sqrt(rho**2 + h**2) + rho)) / rho) * rho_step
        integral3 = integral3 + (exp(-2.0 * cmplx(0.0, 1.0) * beta * rho) / rho) * rho_step
    end do
    
    norm_deltaZ = (-2.0 / (sin(beta * h)**2)) * (integral1 - 2.0 * cos(beta * h) * integral2 - cos(beta * h)**2 * integral3)
    print *, "Normalized ∆Z:", norm_deltaZ
    
end program wait_formula
