import java.util.*;

public class Main {
    public static void main(String[] args) {
        double r = 1000;
        double theta_step = 0.01;
        double I = 2;
        double l = 0.1;
        double K = 2 * Math.PI / 6;
        double eth0 = 377;

        double P_rad = 0.0;

        for (double theta = 0; theta < Math.PI; theta += theta_step) {
            double E_theta_real = ((-1 * K * I * l * eth0) / (4 * Math.PI * r)) * Math.sin(theta) * Math.cos(K * r);
            double E_theta_imag = ((-1 * K * I * l * eth0) / (4 * Math.PI * r)) * Math.sin(theta) * Math.sin(K * r);
            Complex E_theta = new Complex(E_theta_real, E_theta_imag);

            double H_phi_real = E_theta_real / eth0;
            double H_phi_imag = E_theta_imag / eth0;
            Complex H_phi = new Complex(H_phi_real, H_phi_imag);

            double S_theta = 0.5 * (E_theta_real * H_phi_real + E_theta_imag * H_phi_imag);

            P_rad += (S_theta * r * r * Math.sin(theta) * theta_step) * 2 * Math.PI;
        }

        double Rr = 2 * P_rad / (I * I);

        System.out.println(P_rad);
        System.out.println(Rr);
    }
}

class Complex {
    double real;
    double imag;

    public Complex(double real, double imag) {
        this.real = real;
        this.imag = imag;
    }
}
