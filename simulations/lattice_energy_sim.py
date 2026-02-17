#!/usr/bin/env python3
"""Born-Lande Lattice Energy Calculator"""
import numpy as np

# Constants
N_A = 6.022e23     # Avogadro's number
e = 1.602e-19      # Elementary charge (C)
eps0 = 8.854e-12   # Permittivity of free space
pi = np.pi
eV = 1.602e-19

# Crystal data: Madelung constant, Born exponent, charges, r0 (pm)
crystals = {
    "NaCl": {"M": 1.7476, "n": 8, "z+": 1, "z-": 1, "r0": 281, "struct": "Rock salt"},
    "CsCl": {"M": 1.7627, "n": 10.5, "z+": 1, "z-": 1, "r0": 356, "struct": "CsCl-type"},
    "ZnS":  {"M": 1.6381, "n": 9, "z+": 2, "z-": 2, "r0": 235, "struct": "Zinc blende"},
    "MgO":  {"M": 1.7476, "n": 7, "z+": 2, "z-": 2, "r0": 210, "struct": "Rock salt"},
    "CaF2": {"M": 2.5194, "n": 8, "z+": 2, "z-": 1, "r0": 237, "struct": "Fluorite"},
    "TiO2": {"M": 2.408,  "n": 9, "z+": 4, "z-": 2, "r0": 196, "struct": "Rutile"},
}

print("Born-Lande Lattice Energy Analysis")
print("=" * 75)
print("U = -(N_A * M * z+ * z- * e^2) / (4*pi*eps0*r0) * (1 - 1/n)")
print()
print(f"{'Crystal':<8} {'Struct':<12} {'M':<8} {'z+z-':<6} {'r0(pm)':<8} {'n':<6} {'U(kJ/mol)':<12} {'U(eV/pair)'}")
print("-" * 75)

for name, c in crystals.items():
    r0_m = c["r0"] * 1e-12
    U = -(N_A * c["M"] * c["z+"] * c["z-"] * e**2) / (4 * pi * eps0 * r0_m) * (1 - 1/c["n"])
    U_kJ = U / 1000
    U_eV = U / (N_A * eV)
    print(f"{name:<8} {c['struct']:<12} {c['M']:<8.4f} {c['z+']*c['z-']:<6} {c['r0']:<8} {c['n']:<6} {U_kJ:<12.0f} {U_eV:<8.2f}")

# Energy vs spacing plot data (NaCl)
print()
print("NaCl Energy vs Spacing (for plotting)")
print("-" * 50)
M_nacl = 1.7476
n_nacl = 8
# Determine B from equilibrium: B = (N_A*M*z*z*e^2)/(4*pi*eps0) * r0^(n-1) / n
r0_nacl = 281e-12
A_coeff = (N_A * M_nacl * 1 * 1 * e**2) / (4 * pi * eps0)
B = A_coeff * r0_nacl**(n_nacl - 1) / n_nacl

r_range = np.linspace(200e-12, 500e-12, 30)
print(f"{'r(pm)':<10} {'U_attract(kJ)':<16} {'U_repel(kJ)':<16} {'U_total(kJ)'}")
for r in r_range:
    U_att = -A_coeff / r / 1000
    U_rep = B / r**n_nacl / 1000
    U_tot = (U_att + U_rep)
    print(f"{r*1e12:<10.0f} {U_att:<16.1f} {U_rep:<16.1f} {U_tot:<12.1f}")

print()
print("Wearable material insights:")
print("  - NaCl: Reference ionic compound, dissolves in sweat")
print("  - MgO: Ultra-stable, potential substrate for wearable sensors")
print("  - TiO2: Biocompatible, used in wearable UV sensors")
print("  - ZnS: Electroluminescent, used in flexible displays")
print("  - Higher lattice energy = more stable = harder to dissolve")
