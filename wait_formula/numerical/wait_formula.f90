program wait_formula
    implicit none
    
    real :: beta, a, h
    real, dimension(:), allocatable :: rho
    complex :: norm_deltaZ
    complex :: integral1, integral2, integral3
    real :: rho_start, rho_end, rho_step
    real :: rho_current
    integer :: i
    
    beta = 2.0 * 3.14 / 100.0
    a = 18.0
    h = 20.0
    
    rho_start = a
    rho_end = 1000.0
    rho_step = 0.01
    
    allocate(rho((rho_end - rho_start) / rho_step + 1))
    
    rho_current = rho_start
    do i = 1, size(rho)
        rho(i) = rho_current
        rho_current = rho_current + rho_step
    end do
    
    integral1 = 0.0
    integral2 = 0.0
    integral3 = 0.0
    do i = 1, size(rho)
        integral1 = integral1 + (exp(-2.0 * cmplx(0.0, 1.0) * beta * sqrt(rho(i)**2 + h**2)) / rho(i)) * rho_step
        integral2 = integral2 + (exp(-beta * cmplx(0.0, 1.0) * (sqrt(rho(i)**2 + h**2) + rho(i))) / rho(i)) * rho_step
        integral3 = integral3 + (exp(-2.0 * cmplx(0.0, 1.0) * beta * rho(i)) / rho(i)) * rho_step
    end do
    
    norm_deltaZ = (-2.0 / (sin(beta * h)**2)) * (integral1 - 2.0 * cos(beta * h) * integral2 - cos(beta * h)**2 * integral3)
    
    print *, "Result:", norm_deltaZ
    
    deallocate(rho)
    
end program wait_formula
