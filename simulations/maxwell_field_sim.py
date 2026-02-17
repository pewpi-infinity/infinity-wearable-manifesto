#!/usr/bin/env python3
"""
Maxwell Field Simulation — Unified Electromagnetic Analysis
C13B0 Structural Engine — Module A

Connects electrostatics, magnetostatics, and wave propagation.
Shows how ion currents generate fields and fields propagate as waves.
"""
import numpy as np

# Constants
eps0 = 8.854e-12    # Permittivity of free space (F/m)
mu0 = 4 * np.pi * 1e-7  # Permeability of free space (H/m)
c = 1 / np.sqrt(eps0 * mu0)  # Speed of light (m/s)
e = 1.602e-19       # Elementary charge (C)
k_B = 1.381e-23     # Boltzmann constant (J/K)

print("Maxwell Field Simulation — Unified EM Analysis")
print("=" * 70)

# ─── PART 1: Gauss's Law — Charge → Field ───
print("\n─── PART 1: Gauss's Law (∇·E = ρ/ε₀) ───")
print("Point charge electric field vs distance\n")

charges = {
    "Na+":  {"q":  1*e, "desc": "Sodium ion"},
    "Ca2+": {"q":  2*e, "desc": "Calcium ion"},
    "Cl-":  {"q": -1*e, "desc": "Chloride ion"},
    "Al3+": {"q":  3*e, "desc": "Aluminum ion"},
}

print(f"{'Ion':<8} {'q(e)':<8} {'E at 1nm (V/m)':<18} {'E at 10nm':<18} {'E at 1um':<16}")
print("-" * 70)

for name, ch in charges.items():
    q = ch["q"]
    for_display = []
    for r in [1e-9, 10e-9, 1e-6]:
        E = abs(q) / (4 * np.pi * eps0 * r**2)
        for_display.append(E)
    print(f"{name:<8} {q/e:<+8.0f} {for_display[0]:<18.3e} {for_display[1]:<18.3e} {for_display[2]:<16.3e}")

# ─── PART 2: Ampere's Law — Current → Magnetic Field ───
print("\n─── PART 2: Ampère's Law (∇×B = μ₀J + μ₀ε₀∂E/∂t) ───")
print("Ion current in a nerve fiber → magnetic field\n")

# Typical nerve parameters
nerve_currents = {
    "Resting leak":    {"I": 1e-12,  "desc": "Single channel (~1 pA)"},
    "Single channel":  {"I": 5e-12,  "desc": "Open Na+ channel"},
    "Action potential": {"I": 1e-9,  "desc": "Net membrane current"},
    "Nerve bundle":    {"I": 1e-6,   "desc": "Whole nerve (~1 μA)"},
    "Cardiac":         {"I": 1e-3,   "desc": "Heart muscle (~1 mA)"},
}

print(f"{'Source':<20} {'I':<12} {'B at 1mm (T)':<16} {'B at 1cm':<16} {'Detectable?'}")
print("-" * 70)

for name, nc in nerve_currents.items():
    I = nc["I"]
    B_1mm = mu0 * I / (2 * np.pi * 1e-3)
    B_1cm = mu0 * I / (2 * np.pi * 1e-2)
    # Earth's field ~50 μT, MEG detects ~100 fT
    detectable = "MEG" if B_1cm > 1e-13 else "SQUID only" if B_1cm > 1e-15 else "Below noise"
    print(f"{name:<20} {I:<12.1e} {B_1mm:<16.2e} {B_1cm:<16.2e} {detectable}")

# ─── PART 3: Faraday's Law — Changing B → E ───
print("\n─── PART 3: Faraday's Law (∇×E = -∂B/∂t) ───")
print("Induction from changing magnetic fields\n")

# EMF = -dΦ/dt = -A * dB/dt
areas = {"Wearable coil (1cm²)": 1e-4, "Watch coil (4cm²)": 4e-4, "Chest patch (100cm²)": 100e-4}
dBdt_values = {"Slow (1 T/s)": 1, "RF (1kHz, 1mT)": 2*np.pi*1e3*1e-3, "NFC (13.56MHz, 10μT)": 2*np.pi*13.56e6*10e-6}

print(f"{'Coil':<24} {'dB/dt source':<24} {'EMF (V)':<14} {'Power @ 1kΩ'}")
print("-" * 70)
for aname, A in areas.items():
    for dname, dBdt in dBdt_values.items():
        emf = A * dBdt
        P = emf**2 / 1000  # Power into 1kΩ load
        unit = "W" if P > 1e-3 else "mW" if P > 1e-6 else "μW" if P > 1e-9 else "nW"
        pval = P * (1 if P > 1e-3 else 1e3 if P > 1e-6 else 1e6 if P > 1e-9 else 1e9)
        print(f"{aname:<24} {dname:<24} {emf:<14.4e} {pval:.2f} {unit}")

# ─── PART 4: Wave Equation — Fields Propagate ───
print("\n─── PART 4: Wave Propagation (c = 1/√(μ₀ε₀)) ───")
print(f"Speed of light: c = {c:.6e} m/s\n")

# EM spectrum relevant to wearable tech
spectrum = {
    "DC (battery)":      {"f": 0,        "use": "Power storage"},
    "ELF (nerve)":       {"f": 1e3,      "use": "Neural signals"},
    "RF (BLE)":          {"f": 2.4e9,    "use": "Bluetooth Low Energy"},
    "NFC":               {"f": 13.56e6,  "use": "Payment/ID"},
    "Sub-GHz (LoRa)":    {"f": 868e6,    "use": "Long-range IoT"},
    "WiFi":              {"f": 5.8e9,    "use": "Data transfer"},
    "IR (body heat)":    {"f": 3e13,     "use": "Thermal emission"},
    "Visible (display)": {"f": 5e14,     "use": "LED/OLED display"},
}

print(f"{'Band':<20} {'Freq':<14} {'λ':<14} {'Wearable use'}")
print("-" * 70)
for name, s in spectrum.items():
    f = s["f"]
    if f > 0:
        lam = c / f
        if lam > 1: lam_s = f"{lam:.1f} m"
        elif lam > 1e-3: lam_s = f"{lam*1e3:.1f} mm"
        elif lam > 1e-6: lam_s = f"{lam*1e6:.1f} μm"
        else: lam_s = f"{lam*1e9:.0f} nm"
    else:
        lam_s = "∞"
    print(f"{name:<20} {f:<14.2e} {lam_s:<14} {s['use']}")

# ─── PART 5: Energy in Fields ───
print("\n─── PART 5: Field Energy Density ───")
print("u_E = ½ε₀E²  |  u_B = B²/(2μ₀)\n")

scenarios = {
    "Nerve membrane (10⁷ V/m)": {"E": 1e7, "B": 0},
    "Cell phone antenna":        {"E": 1,   "B": 3.3e-9},
    "MRI scanner (3T)":          {"E": 0,   "B": 3},
    "Earth surface":             {"E": 100, "B": 50e-6},
    "Lightning (nearby)":        {"E": 3e6, "B": 1e-4},
}

print(f"{'Scenario':<30} {'u_E (J/m³)':<16} {'u_B (J/m³)':<16} {'Dominant'}")
print("-" * 70)
for name, s in scenarios.items():
    u_E = 0.5 * eps0 * s["E"]**2
    u_B = s["B"]**2 / (2 * mu0)
    dominant = "Electric" if u_E > u_B else "Magnetic" if u_B > u_E else "Equal"
    print(f"{name:<30} {u_E:<16.3e} {u_B:<16.3e} {dominant}")

# ─── PART 6: Maxwell Unification Summary ───
print("\n─── MAXWELL UNIFICATION ───")
print("┌─────────────────────────────────────────────────────────┐")
print("│  ∇·E = ρ/ε₀           Charge → Electric field          │")
print("│  ∇·B = 0               No magnetic monopoles            │")
print("│  ∇×E = -∂B/∂t          Changing B → Electric field      │")
print("│  ∇×B = μ₀J + μ₀ε₀∂E/∂t  Current + changing E → B      │")
print("├─────────────────────────────────────────────────────────┤")
print("│  Ions create ρ → E field (Gauss)                        │")
print("│  Moving ions = J → B field (Ampère)                     │")
print("│  Changing fields → waves at c (Faraday + Ampère)        │")
print("│  Everything links back to charge and its motion.        │")
print("└─────────────────────────────────────────────────────────┘")
