To calculate the radiation resistance (
R_r
) of the Clam Lake ELF transmitter using real data, we’ll use the formula for a ground dipole antenna operating at extremely low frequency (ELF):
R_r = \frac{Z_s^2 \cdot \pi \cdot l_y^2}{4 \cdot \eta_0 \cdot h \cdot \lambda}
where:
Z_s
: Surface impedance of the Earth (ohms)
l_y
: Antenna length (meters)
\eta_0
: Free-space impedance (ohms)
( h ): Effective ionosphere height (meters)
\lambda
: Wavelength (meters)
The Clam Lake facility, part of the U.S. Navy’s Project ELF, operated at 76 Hz with a ground dipole antenna system. Below, we’ll determine each parameter using real-world data and compute 
R_r
.
Step 1: Frequency and Wavelength
Frequency (( f )): 76 Hz (actual operating frequency of Clam Lake).
Speed of Light (( c )): 299,792,458 m/s (exact value).
The wavelength is calculated as:
\lambda = \frac{c}{f} = \frac{299,792,458}{76} \approx 3,944,637.6 \, \text{meters}
Step 2: Antenna Length
Antenna Length (
l_y
): The Clam Lake transmitter used two ground dipoles, each approximately 14 miles long. Converting to meters:
l_y = 14 \times 1,609.34 = 22,530.76 \, \text{meters}
We’ll use one dipole’s length, as the formula applies to a single antenna element.
Step 3: Free-Space Impedance
Free-Space Impedance (
\eta_0
): Defined as 376.730313668 ohms (exact value based on physical constants). We’ll use this precise value instead of the common approximation of 377 ohms.
Step 4: Ionosphere Height
Effective Ionosphere Height (( h )): For ELF frequencies, the ionosphere acts as a reflecting layer at approximately 70–90 km. Lacking site-specific data for Clam Lake, we adopt a typical value of 80 km:
h = 80,000 \, \text{meters}
Step 5: Surface Impedance
Earth Conductivity (
\sigma
): The Clam Lake site in Wisconsin was selected for its low ground conductivity, enhancing ELF performance. A representative value for the region is 0.0005 S/m (5 × 10⁻⁴ S/m).
Angular Frequency (
\omega
): 
\omega = 2 \pi f = 2 \pi \times 76 \approx 477.522 \, \text{rad/s}
.
Permeability of Free Space (
\mu_0
): 1.25663706212 × 10⁻⁶ H/m (exact value).
For ELF, where 
\sigma \gg \omega \epsilon_0
, the surface impedance magnitude is:
|Z_s| = \sqrt{\frac{\omega \mu_0}{\sigma}}
Calculate:
\omega \mu_0 = 477.522 \times 1.25663706212 \times 10^{-6} \approx 6.000 \times 10^{-4}
|Z_s| = \sqrt{\frac{6.000 \times 10^{-4}}{5 \times 10^{-4}}} = \sqrt{1.2} \approx 1.095 \, \text{ohms}
Z_s^2 \approx (1.095)^2 \approx 1.199 \, \text{ohms}^2
Step 6: Radiation Resistance Calculation
Substitute the values into the formula:
R_r = \frac{1.199 \cdot \pi \cdot (22,530.76)^2}{4 \cdot 376.730313668 \cdot 80,000 \cdot 3,944,637.6}
Numerator:
(22,530.76)^2 \approx 5.076 \times 10^8
\pi \cdot 5.076 \times 10^8 \approx 1.595 \times 10^9
1.199 \times 1.595 \times 10^9 \approx 1.913 \times 10^9
Denominator:
4 \times 376.730313668 \approx 1,506.921
1,506.921 \times 80,000 \approx 1.206 \times 10^8
1.206 \times 10^8 \times 3,944,637.6 \approx 4.756 \times 10^{14}
Final Calculation:
R_r = \frac{1.913 \times 10^9}{4.756 \times 10^{14}} \approx 4.02 \times 10^{-6} \, \text{ohms}
Verification
This result is consistent with ELF systems, where radiation resistance is extremely small due to the antenna’s length being a tiny fraction of the wavelength (
l_y / \lambda \approx 0.0057
). The low 
R_r
 reflects the challenge of radiating power at ELF frequencies, requiring high currents to achieve effective communication.
Thus, the radiation resistance of the Clam Lake ELF transmitter, based on real data, is approximately 4.02 × 10⁻⁶ ohms.
