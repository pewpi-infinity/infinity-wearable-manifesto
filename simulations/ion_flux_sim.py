#!/usr/bin/env python3
"""Nernst-Planck Ion Flux Simulator for Wearable Ion Systems"""
import numpy as np

# Constants
F = 96485      # Faraday constant (C/mol)
R = 8.314      # Gas constant (J/mol·K)
T = 310        # Body temperature (K)
kT = R * T     # Thermal energy

# Ion properties
ions = {
    "Na+": {"z": 1, "D": 1.33e-9, "C_in": 12e-3, "C_out": 145e-3},
    "K+":  {"z": 1, "D": 1.96e-9, "C_in": 140e-3, "C_out": 4e-3},
    "Ca2+":{"z": 2, "D": 0.79e-9, "C_in": 0.1e-6, "C_out": 2.5e-3},
    "Cl-": {"z":-1, "D": 2.03e-9, "C_in": 4e-3, "C_out": 110e-3},
}

print("Nernst-Planck Ion Flux Analysis")
print("=" * 65)
print(f"Temperature: {T}K (body temp)")
print()

# Nernst potential for each ion
print(f"{'Ion':<8} {'z':<4} {'C_in(mM)':<12} {'C_out(mM)':<12} {'E_nernst(mV)':<14} {'Direction'}")
print("-" * 65)

for name, ion in ions.items():
    z = ion["z"]
    E_nernst = (R * T / (z * F)) * np.log(ion["C_out"] / ion["C_in"])
    E_mV = E_nernst * 1000
    direction = "inward" if (z > 0 and E_mV > 0) or (z < 0 and E_mV < 0) else "outward"
    print(f"{name:<8} {z:<4} {ion['C_in']*1e3:<12.2f} {ion['C_out']*1e3:<12.1f} {E_mV:<14.1f} {direction}")

# Fick's diffusion flux (no field)
print()
print("Diffusion Flux (Fick's Law, no electric field)")
print("J = -D * dC/dx")
print("-" * 65)
dx = 10e-9  # membrane thickness ~10nm

for name, ion in ions.items():
    dC = ion["C_out"] - ion["C_in"]
    J = -ion["D"] * (dC / dx)
    print(f"{name:<8} D={ion['D']:.2e} m^2/s  dC/dx={dC/dx:.2e}  J={J:.2e} mol/(m^2·s)")

# Full Nernst-Planck with membrane potential
V_m = -0.070  # resting membrane potential -70mV
print()
print(f"Full Nernst-Planck flux at V_m = {V_m*1000:.0f} mV")
print("J = -D(dC/dx + zFC/RT * dV/dx)")
print("-" * 65)

for name, ion in ions.items():
    z = ion["z"]
    C_avg = (ion["C_in"] + ion["C_out"]) / 2
    dC = ion["C_out"] - ion["C_in"]
    J_diff = -ion["D"] * dC / dx
    J_migr = -ion["D"] * z * F * C_avg / (R * T) * (V_m / dx)
    J_total = J_diff + J_migr
    print(f"{name:<8} J_diff={J_diff:+.2e}  J_migr={J_migr:+.2e}  J_total={J_total:+.2e}")

print()
print("Key insights:")
print("  - K+ has outward diffusion gradient but inward electrical drive")
print("  - Na+ has both inward diffusion AND electrical drive (strong inward)")
print("  - Ca2+ has massive concentration gradient (25000:1 out:in)")
print("  - At resting potential, net fluxes are maintained by Na/K ATPase")
