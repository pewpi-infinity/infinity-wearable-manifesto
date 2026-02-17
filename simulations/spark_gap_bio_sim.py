#!/usr/bin/env python3
"""
Spark Gap Bio-Electrochemistry — Schottky Junction Analysis
C13B0 Structural Engine — Module F

Models: Au/Fe3O4 Schottky rectification, micro-plasma discharge,
electroporation thresholds, sulfide degradation, and bio-current
delivery through metal-semiconductor heterojunctions.

Grounded in real electrochemistry. Speculative elements flagged.
"""
import numpy as np

print("Spark Gap Bio-Electrochemistry — Module F")
print("=" * 72)

# Constants
q = 1.602e-19      # Elementary charge (C)
k_B = 1.381e-23    # Boltzmann constant (J/K)
T = 310             # Body temperature (K)
kT = k_B * T        # Thermal energy (J)
kT_eV = kT / q      # ~0.0267 eV at 310K

print(f"Body temperature: {T}K  |  kT = {kT_eV*1000:.1f} meV")

# ═══════════════════════════════════════════════════════════
# PART 1: SCHOTTKY JUNCTION — Au/Fe3O4 INTERFACE
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 1: Au/Fe3O4 SCHOTTKY JUNCTION ═══\n")

# Gold work function: 5.1 eV
# Fe3O4 electron affinity: ~4.5 eV (varies with stoichiometry)
# Barrier height: phi_B = phi_metal - chi_semiconductor

phi_Au = 5.1     # Gold work function (eV)
chi_Fe3O4 = 4.5  # Magnetite electron affinity (eV)
phi_B = phi_Au - chi_Fe3O4

print(f"Gold work function:     {phi_Au} eV")
print(f"Fe3O4 electron affinity: {chi_Fe3O4} eV")
print(f"Schottky barrier:       {phi_B} eV")
print(f"kT at body temp:        {kT_eV*1000:.1f} meV")
print(f"phi_B / kT ratio:       {phi_B/kT_eV:.1f} (>>1 means strong rectification)")

# Reverse saturation current
A_star = 1.2e6  # Richardson constant for Fe3O4 (A/m2/K2) — approximate
A_junction = (50e-6)**2 * np.pi  # Single grain contact area (50um grain)
I_s = A_junction * A_star * T**2 * np.exp(-phi_B * q / kT)

print(f"\nReverse saturation current per grain contact:")
print(f"  I_s = {I_s:.2e} A = {I_s*1e12:.2f} pA")
print(f"  Contact area: {A_junction*1e12:.1f} um2")

# I-V curve
print(f"\nI-V Characteristic (single grain Schottky contact):")
print(f"{'V_forward (mV)':<16} {'I (nA)':<12} {'P (pW)':<12} {'Regime'}")
print("-" * 55)

for V_mV in [1, 5, 10, 25, 50, 100, 200, 300, 500]:
    V = V_mV * 1e-3
    I = I_s * (np.exp(q * V / (1.5 * kT)) - 1)  # n=1.5 ideality
    P = V * I
    regime = "sub-threshold" if V_mV < 50 else "transition" if V_mV < 200 else "forward"
    print(f"{V_mV:<16} {I*1e9:<12.4f} {P*1e12:<12.4f} {regime}")

# ═══════════════════════════════════════════════════════════
# PART 2: SULFIDE CONTAMINATION — THE PYRITE PROBLEM
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 2: SULFIDE CONTAMINATION (PYRITE PROBLEM) ═══\n")

print("Pyrite (FeS2) at the Au/Fe3O4 interface creates:")
print("  - High-impedance layer (resistive barrier)")
print("  - Increased contact resistance")
print("  - Parasitic capacitance")
print("  - Reduced rectification efficiency\n")

# Contact resistance with and without sulfide layer
R_clean = 100       # Ohms — clean Au/Fe3O4 contact
R_sulfide_thin = 10000   # Thin sulfide layer
R_sulfide_thick = 1e6    # Thick sulfide (fully passivated)

print(f"{'Interface state':<24} {'R_contact (Ω)':<16} {'I at 100mV (nA)':<18} {'Efficiency loss'}")
print("-" * 72)

for name, R in [("Clean Au/Fe3O4", R_clean), ("Thin FeS2 layer", R_sulfide_thin), ("Thick FeS2 (dead)", R_sulfide_thick)]:
    V = 0.1  # 100mV
    I = V / R  # Simplified ohmic regime
    eff_loss = (1 - R_clean/R) * 100
    print(f"{name:<24} {R:<16.0f} {I*1e9:<18.2f} {eff_loss:.1f}%")

# Purification methods
print("\nSulfide removal / prevention methods:")
print("  1. Acid wash (HCl) — dissolves FeS2, preserves Au and Fe3O4")
print("  2. Thermal annealing (400°C N2) — decomposes sulfides")
print("  3. Thiol-blocked Au — self-assembled monolayer prevents sulfide adhesion")
print("  4. Gold overcoat — fresh Au sputtered over cleaned interface")
print("  5. Inert atmosphere storage — prevents re-contamination")
print("\n  Method 3 (thiol-blocked) is best for wearable: biocompatible + stable")

# ═══════════════════════════════════════════════════════════
# PART 3: ELECTROPORATION THRESHOLDS
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 3: ELECTROPORATION — REAL BIO-ELECTRIC EFFECTS ═══\n")

print("Electroporation: electric field opens pores in cell membranes")
print("This IS a real medical technology (used in gene therapy, drug delivery)")
print()

# Real electroporation parameters
print(f"{'Parameter':<30} {'Value':<18} {'Note'}")
print("-" * 72)
params = [
    ("Reversible threshold",    "0.2-1.0 V/cm",    "Membrane pores open temporarily"),
    ("Irreversible threshold",  "1.0-3.0 kV/cm",   "Permanent membrane damage"),
    ("Pulse duration",          "1-100 μs",         "Short = reversible, long = lethal"),
    ("Membrane thickness",      "5-10 nm",          "Lipid bilayer"),
    ("Transmembrane potential", "200-500 mV",       "At which pores form"),
    ("Pore diameter",           "1-50 nm",          "Size-dependent transport"),
    ("Recovery time",           "seconds-minutes",  "For reversible poration"),
]
for p, v, n in params:
    print(f"{p:<30} {v:<18} {n}")

# Can our system reach these thresholds?
print("\nCan Au/Fe3O4 mesh produce electroporation?")
print("-" * 50)

# Grain spacing ~50 um, voltage from ambient RF
grain_gap = 50e-6  # 50 micron gap
V_ambient = 50e-3  # 50 mV from ambient RF rectification
E_field = V_ambient / grain_gap

print(f"  Grain gap: {grain_gap*1e6:.0f} μm")
print(f"  Rectified voltage: {V_ambient*1000:.0f} mV")
print(f"  Local E-field: {E_field:.0f} V/m = {E_field/100:.2f} V/cm")
print(f"  Reversible threshold: 20-100 V/cm")
print(f"  Result: {E_field/100:.2f} V/cm << 20 V/cm threshold")
print()
print("  VERDICT: Ambient RF rectification CANNOT produce electroporation.")
print("  Need 100-1000x higher voltage (external power source required).")

# What CAN micro-currents do?
print("\n  What micro-currents from body harvest CAN do:")
print("  - Galvanic skin response sensing (~μA level)")
print("  - Iontophoresis (drug delivery with ~0.5 mA external source)")
print("  - Transcutaneous nerve stimulation (TENS, needs 10-50 mA)")
print("  - Wound healing acceleration (10-100 μA, proven in literature)")
print("  - ALL of these need MORE power than ambient RF provides")
print("  - Minimum viable: battery-assisted with harvest for sensing only")

# ═══════════════════════════════════════════════════════════
# PART 4: MICRO-PLASMA DISCHARGE (THE ACTUAL SPARK)
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 4: MICRO-PLASMA DISCHARGE ═══\n")

# Paschen's law: V_breakdown = f(p*d)
# For air at STP: minimum ~327V at p*d = 7.5e-6 m*atm
print("Paschen's Law — minimum voltage for spark across air gap")
print()

# Paschen curve (simplified for air)
# V = B * p * d / (ln(A * p * d) - ln(ln(1 + 1/gamma_se)))
# A = 15 /cm/torr, B = 365 V/cm/torr, gamma_se = 0.01 for typical
A_p = 15     # 1/(cm*torr)
B_p = 365    # V/(cm*torr)
p_atm = 760  # torr (1 atm)

print(f"{'Gap (μm)':<12} {'p*d (cm*torr)':<16} {'V_breakdown (V)':<18} {'Achievable?'}")
print("-" * 60)

for d_um in [1, 5, 10, 50, 100, 500, 1000]:
    d_cm = d_um * 1e-4
    pd = p_atm * d_cm
    if pd > 0.01:
        V_break = B_p * pd / (np.log(A_p * pd + 1e-10) - np.log(np.log(1 + 1/0.01)))
        V_break = max(V_break, 327)  # Paschen minimum
    else:
        V_break = 327  # Near minimum
    achievable = "NO (ambient)" if V_break > 1 else "possible"
    achievable = "NO — need >300V" if V_break > 100 else "Marginal"
    print(f"{d_um:<12} {pd:<16.4f} {V_break:<18.0f} {'NEED >300V source'}")

print()
print("VERDICT: Micro-plasma discharge requires >300V minimum.")
print("Ambient RF gives ~50-200 mV. Gap of ~10^3x.")
print("Spark discharge needs external power or piezo-generated voltage.")
print()
print("Piezoelectric option: PZT can generate 10-100V from deformation.")
print("If grain mesh includes piezo elements, body movement COULD")
print("produce occasional micro-sparks at 1μm gaps.")

# ═══════════════════════════════════════════════════════════
# PART 5: REALISTIC BIO-ELECTRIC INTERFACE
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 5: WHAT ACTUALLY WORKS FOR BIO-INTERFACE ═══\n")

print("Proven bio-electric technologies (real, in use):")
print("-" * 60)

bio_tech = [
    ("TENS (pain relief)",        "10-50 mA",   "Battery",     "FDA approved"),
    ("Wound healing stim",        "10-100 μA",  "Battery",     "Clinical evidence"),
    ("Iontophoresis",             "0.5 mA",     "Battery",     "Transdermal drug delivery"),
    ("Galvanic skin sensing",     "~1 μA",      "Harvestable", "Stress/arousal monitoring"),
    ("ECG sensing",               "~1 μA",      "Harvestable", "Heart rhythm monitoring"),
    ("EEG sensing",               "~0.1 μA",    "Harvestable", "Brain activity"),
    ("Bioimpedance",              "~10 μA",     "Harvestable", "Body composition"),
]

print(f"{'Technology':<28} {'Current':<12} {'Power source':<14} {'Status'}")
print("-" * 68)
for tech, curr, src, status in bio_tech:
    print(f"{tech:<28} {curr:<12} {src:<14} {status}")

print()
print("═══ DESIGN PATH: HYBRID SYSTEM ═══")
print()
print("Tier A (harvest-only): Sensing + data")
print("  - Galvanic skin, ECG, EEG, bioimpedance")
print("  - Powered by thermoelectric + piezo + RF (~150 μW)")
print("  - Data via BLE backscatter")
print()
print("Tier B (battery-assisted): Stimulation + healing")
print("  - TENS, wound stim, iontophoresis")
print("  - Requires battery (10-100 mW)")
print("  - Harvest extends battery life, doesn't replace it")
print()
print("Tier C (clinical): Electroporation + therapy")
print("  - Gene therapy, drug delivery, tumor ablation")
print("  - Requires medical-grade power supply")
print("  - NOT achievable with body harvest or ambient RF")
print()
print("The Au/Fe3O4 mesh fits TIER A perfectly:")
print("  → Sensing through impedance changes in the grain mesh")
print("  → RF rectification for sensor power")
print("  → Magnetite responds to external magnetic fields (MRI-compatible sensing)")
print("  → Gold biocompatible for long-term skin contact")
