#include <iostream>
#include <cmath>
#include <complex>

int main() {
    double r = 1000;
    double theta_step = 0.01;
    double I = 2;
    double l = 0.1;
    double K = 2 * M_PI / 6;
    double eth0 = 377;

    double P_rad = 0.0;

    for (double theta = 0; theta < M_PI; theta += theta_step) {
        double E_theta_real = ((-1 * K * I * l * eth0) / (4 * M_PI * r)) * sin(theta) * cos(K * r);
        double E_theta_imag = ((-1 * K * I * l * eth0) / (4 * M_PI * r)) * sin(theta) * sin(K * r);
        std::complex<double> E_theta(E_theta_real, E_theta_imag);

        double H_phi_real = E_theta_real / eth0;
        double H_phi_imag = E_theta_imag / eth0;
        std::complex<double> H_phi(H_phi_real, H_phi_imag);

        double S_theta = 0.5 * (E_theta_real * H_phi_real + E_theta_imag * H_phi_imag);

        P_rad += (S_theta * r * r * sin(theta) * theta_step) * 2 * M_PI;
    }

    double Rr = 2 * P_rad / (I * I);

    std::cout << P_rad << std::endl;
    std::cout << Rr << std::endl;

    return 0;
}
