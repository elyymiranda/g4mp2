"""

 Library for thermochemistry of atoms and molecules

"""

import numpy as np

R = 0.00000316679085237                                     # Kelvin to Hartree
NA = 6.02214086e23
kB = R/NA
P_conv = 3.4439667564003e-9                                 # atm to a.u.
mass_conv = 1836.15267389                                   # a.m.u to a.u.
vib_temp_conv = 1.438786296                                 # cm-1 to (equivalent) Kelvin
anharmonic_corr = 0.9854                                    # empirical anharmonic correction for the frequencies.
#anharmonic_corr = 1.0                                       # empirical anharmonic correction for the frequencies.

# Energy of molecules
def Et(T):
    return 1.5*R*T

def Er(T, is_linear):
    if is_linear == True:
        return R*T
    return 1.5*R*T

def Ev(T, vib_temp):
    nvib = len(vib_temp)
    Ev = 0
    if T == 0.:
        for i in range(nvib):
            if vib_temp[i] < 0:
                continue
            theta = vib_temp[i]
            Ev += theta*0.5
        return R*Ev
    
    for i in range(nvib):
        if vib_temp[i] < 0:
            continue
        theta = vib_temp[i]
        Ev += theta*(0.5 + 1/(np.exp(theta/T)-1))
    return R*Ev
 
def Etot(T, vib_temp, is_linear):
    print(" (T = " + str(T) + ")") 
    print(" Translational energy:\t" + str(Et(T)))
    print(" Rotational energy:\t" + str(Er(T, is_linear)))
    print(" Vibrational energy:\t" + str(Ev(T, vib_temp)) + "\n")

    return Et(T) + Er(T, is_linear) + Ev(T, vib_temp)

# Energy of atoms
def Et_atomic(T):
    return 1.5*R*T
 
def Etot_atomic(T):
    print(" (T = " + str(T) + ")") 
    print(" Translational energy:\t" + str(Et_atomic(T)) + "\n")
    return Et(T)

# Entropy of molecules
def St(mass, T, P):
    Zt = (mass*R*T/(2*np.pi))**1.5
    qt = Zt*R*T/P
    return R*(np.log(qt) + 2.5)

def Sr(Ix, Iy, Iz, T, sigmar, is_linear):
    if is_linear == True:
        Zr = T/Ix
        qr = Zr/sigmar
        return R*(np.log(qr) + 1.0)
    
    else:
        Zr = T**1.5/np.sqrt(Ix*Iy*Iz)
        qr = np.sqrt(np.pi)*Zr/sigmar    
        return R*(np.log(qr) + 1.5)

def Sv(T, vib_temp):
    nvib = len(vib_temp)
    Sv = 0
    for i in range(nvib):
        if vib_temp[i] < 0:
            continue
        theta = vib_temp[i]/T
        Sv += theta/(np.exp(theta)-1) - np.log(1-np.exp(-theta))
    return R*Sv

def Se(spin_mult):
    return R*np.log(spin_mult)

def Stot(mass, T, P, Ix, Iy, Iz, sigmar, is_linear, vib_temp, spin_mult):
    print(" Translational entropy:\t" + str(St(mass, T, P)))
    print(" Rotational entropy:\t" + str(Sr(Ix, Iy, Iz, T, sigmar, is_linear)))
    print(" Vibrational entropy:\t" + str(Sv(T,vib_temp)))
    print(" Electronic entropy:\t" + str(Se(spin_mult)) + "\n")
    return St(mass, T, P) + Sr(Ix, Iy, Iz, T, sigmar, is_linear) + Sv(T, vib_temp) + Se(spin_mult)

# Entropy of atoms
def St_atomic(mass, T, P):
    Zt = (mass*R*T/(2*np.pi))**1.5
    qt = Zt*R*T/P
    return R*(np.log(qt) + 2.5)

def Se_atomic(spin_mult):
    return R*np.log(spin_mult)

def Stot_atomic(mass, T, P, spin_mult):
    print(" Translational entropy:\t" + str(St_atomic(mass,T,P)))
    print(" Electronic entropy:\t" + str(Se_atomic(spin_mult)) + "\n")
    return St_atomic(mass, T, P) + Se_atomic(spin_mult)