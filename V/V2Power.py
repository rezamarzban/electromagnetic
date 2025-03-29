import math

def calculate_current(V, R_r, X):
    # Equation 1: |I| = V / sqrt(R_r^2 + X^2)
    I_mag = V / math.sqrt(R_r**2 + X**2)
    
    # Equation 2: phi = arctan(X / R_r)
    phi = math.atan(X / R_r)
    
    # Equation 3: I_real = |I| * cos(phi)
    I_real = I_mag * math.cos(phi)
    
    # Equation 4: I_reac = |I| * sin(phi)
    I_reac = I_mag * math.sin(phi)
    
    return I_mag, I_real, I_reac, phi

def calculate_radiated_power(I_mag, R_r):
    # Equation 5: P_rad = 0.5 * |I|^2 * R_r
    P_rad = 0.5 * (I_mag ** 2) * R_r
    return P_rad

def print_equations():
    print("Key Equations:")
    print("1. Current Magnitude: |I| = V / sqrt(R_r^2 + X^2)")
    print("2. Phase Angle:       phi = arctan(X / R_r)")
    print("3. In-phase Current:  I_real = |I| * cos(phi)")
    print("4. Reactive Current:  I_reac = |I| * sin(phi)")
    print("5. Radiated Power:    P_rad = 0.5 * |I|^2 * R_r")
    print()

def main():
    # Sample input values:
    V = 10.0      # Voltage in volts
    R_r = 50.0    # Radiation resistance in ohms
    X = 25.0      # Reactance in ohms

    print("Input Parameters:")
    print("  Voltage (V):", V, "V")
    print("  Radiation Resistance (R_r):", R_r, "ohms")
    print("  Reactance (X):", X, "ohms")
    print()

    # Print the equations
    print_equations()
    
    # Calculate current components
    I_mag, I_real, I_reac, phi = calculate_current(V, R_r, X)
    
    # Calculate radiated power
    P_rad = calculate_radiated_power(I_mag, R_r)
    
    # Print computed values:
    print("Calculated Results:")
    print("  |I| (Current Magnitude): {:.4f} A".format(I_mag))
    print("  I_real (In-phase component): {:.4f} A".format(I_real))
    print("  I_reac (Reactive component): {:.4f} A".format(I_reac))
    print("  Phase Angle (phi): {:.2f} degrees".format(math.degrees(phi)))
    print("  Radiated Power (P_rad): {:.4f} W".format(P_rad))

if __name__ == '__main__':
    main()
