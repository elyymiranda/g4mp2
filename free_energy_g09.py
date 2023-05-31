"""

 Thermochemistry based on gaussian09 FREQ calculation

 python3 free_energy_g09.py [g09file.log] [temperature]

"""

import numpy as np
import sys
import readLog
from thermochemistry import *

if __name__=="__main__":

    T = float(sys.argv[2])                                  # Temperature (Kelvin)
    print(" => Analysis of thermochemistry quantities at T = %f K <= \n"%T)

    # Reading gaussian log file
    LogFile = sys.argv[1]
    hp = readLog.catch_hp_g09(LogFile)
    freq = readLog.catch_freq_g09(LogFile, hp)
    vib_temp = anharmonic_corr*vib_temp_conv*np.array(freq) # vibrational temperatures

    # Checking for imaginary frequencies
    imag_freq = 0 
    for i in range(len(vib_temp)):
        if vib_temp[i] < 0:
            imag_freq += 1
    if imag_freq > 0:
        print("Warning: => Ignoring %d imaginary frequency(ies) <= \n"%imag_freq)

    P = 1.0                                                 # Pressure (atm)
    P *= P_conv

    Natoms = readLog.catch_N_atoms_g09(LogFile)             # number of atoms
    spin_mult = readLog.catch_spin_mult(LogFile)            # spin multiplicity
    mass = readLog.catch_mol_mass(LogFile)                  # mass (a.m.u)
    mass *= mass_conv
    if Natoms == 1:
        print(" Atomic thermochemistry\n")
        E = Etot_atomic(T)
        S = Stot_atomic(mass, T, P, spin_mult)
        print(" Internal energy correction at T = %fK:\t"%T + str(E))
        print(" Free energy correction at T = %fK:\t"%T + str(E + T*R - T*S))
        sys.exit()

    is_linear = readLog.catch_is_linear(LogFile)            # Check if molecule is linear
    Ix, Iy, Iz = readLog.catch_rot_temp(LogFile)            # Rotational temperatures (Kelvin)
    sigmar = readLog.catch_rot_symmetry_number(LogFile)     # Rotational symmetry number

    # Calculating thermochemistry quantities
    E0 = Etot(0., vib_temp, is_linear)
    E = Etot(T, vib_temp, is_linear)
    S = Stot(mass, T, P, Ix, Iy, Iz, sigmar, is_linear, vib_temp, spin_mult)
    print(" Free energy correction at T = 0K (ZPE):\t" + str(E0))
    print(" Internal energy correction at T = %fK:\t"%T + str(E))
    print(" Free energy correction at T = %fK:\t"%T + str(E + T*R - T*S))