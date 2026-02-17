#!/usr/bin/env python3
"""Thermoelectric Harvesting Model for Wearables"""
import numpy as np

# Thermoelectric figure of merit: ZT = S^2 * sigma * T / kappa

# Material properties at ~300K
materials = {
    "Bi2Te3": {"S": 200e-6, "sigma": 1.1e5, "kappa": 1.5, "desc": "Classic TE"},
    "PbTe":   {"S": 250e-6, "sigma": 5e4,   "kappa": 2.0, "desc": "High-temp TE"},
    "SnSe":   {"S": 500e-6, "sigma": 1e4,   "kappa": 0.5, "desc": "Record ZT"},
    "Organic":{"S": 50e-6,  "sigma": 1e3,   "kappa": 0.3, "desc": "Flexible/wearable"},
}

T = 310       # Body temp (K)
dT_body = 5   # Skin-to-air temperature difference (K)
A = 100e-4    # Harvesting area (100 cm^2)
L = 1e-3      # TE element length (1mm)

print("Thermoelectric Wearable Energy Harvesting")
print("=" * 65)
print(f"Body temp: {T}K, dT: {dT_body}K, Area: {A*1e4:.0f} cm^2")
print()
print(f"{'Material':<10} {'S(uV/K)':<10} {'ZT':<8} {'P(uW)':<10} {'P(uW/cm2)':<12} {'Note'}")
print("-" * 65)

for name, m in materials.items():
    ZT = m["S"]**2 * m["sigma"] * T / m["kappa"]
    P = m["S"]**2 * m["sigma"] * dT_body**2 * A / L
    P_uW = P * 1e6
    P_per_cm2 = P_uW / (A * 1e4)
    print(f"{name:<10} {m['S']*1e6:<10.0f} {ZT:<8.2f} {P_uW:<10.1f} {P_per_cm2:<12.2f} {m['desc']}")

print()
print("Reality check:")
print(f"  Bluetooth LE beacon: ~10-50 uW (achievable with Bi2Te3)")
print(f"  MCU sleep mode: ~1-10 uW (achievable)")
print(f"  Active MCU: ~1-10 mW (NOT achievable from body heat alone)")
print(f"  Phone charging: ~5W (IMPOSSIBLE from body heat)")
print()
print("Conclusion: Body thermoelectric can power sensors + sleep-mode MCU.")
print("Cannot power active computation or charging.")
