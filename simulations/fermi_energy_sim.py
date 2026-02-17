#!/usr/bin/env python3
"""Fermi Energy Calculator for Metallic Systems"""
import numpy as np

# Constants
hbar = 1.055e-34   # Reduced Planck constant (J·s)
m_e = 9.109e-31    # Electron mass (kg)
eV = 1.602e-19     # Electron-volt (J)
k_B = 1.381e-23    # Boltzmann constant (J/K)

# Free electron densities (electrons/m^3)
metals = {
    "Na": {"n": 2.65e28, "valence": 1, "desc": "Alkali metal"},
    "Cu": {"n": 8.49e28, "valence": 1, "desc": "Noble metal (coin/wire)"},
    "Al": {"n": 18.1e28, "valence": 3, "desc": "Trivalent, lightweight"},
    "Au": {"n": 5.90e28, "valence": 1, "desc": "Noble metal (contacts)"},
    "Ag": {"n": 5.86e28, "valence": 1, "desc": "Highest conductivity"},
    "Fe": {"n": 17.0e28, "valence": 2, "desc": "Structural/magnetic"},
}

print("Fermi Energy Analysis for Metallic Wearable Components")
print("=" * 70)
print(f"E_F = (hbar^2 / 2m) * (3*pi^2 * n)^(2/3)")
print()
print(f"{'Metal':<6} {'n(10^28/m3)':<14} {'E_F(eV)':<10} {'T_F(K)':<12} {'v_F(m/s)':<12} {'Notes'}")
print("-" * 70)

for name, m in metals.items():
    n = m["n"]
    E_F = (hbar**2 / (2 * m_e)) * (3 * np.pi**2 * n)**(2/3)
    E_F_eV = E_F / eV
    T_F = E_F / k_B
    v_F = np.sqrt(2 * E_F / m_e)
    print(f"{name:<6} {n/1e28:<14.2f} {E_F_eV:<10.2f} {T_F:<12.0f} {v_F:<12.0f} {m['desc']}")

print()
print("Temperature dependence of electron energy:")
temps = [4, 77, 300, 310, 500]
print(f"{'T(K)':<8}", end="")
for name in metals:
    print(f"{name:<10}", end="")
print()
print("-" * 68)

for T in temps:
    print(f"{T:<8}", end="")
    for name, m in metals.items():
        n = m["n"]
        E_F = (hbar**2 / (2 * m_e)) * (3 * np.pi**2 * n)**(2/3)
        correction = 1 - (np.pi**2 / 12) * (k_B * T / E_F)**2
        print(f"{E_F/eV*correction:<10.4f}", end="")
    print()

print()
print("Wearable relevance:")
print(f"  Body temp (310K) << T_F (~50000K) for all metals")
print(f"  Electrons remain deeply degenerate at body temperature")
print(f"  Fermi-Dirac statistics essential, classical Boltzmann fails")
print(f"  Conductivity of wearable contacts determined by E_F and scattering")
