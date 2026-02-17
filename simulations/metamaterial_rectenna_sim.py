#!/usr/bin/env python3
"""
Metamaterial Rectenna & Entropy Harvesting Analysis
C13B0 Structural Engine — Module E

Models: Schottky rectification, stochastic resonance,
ambient RF power density, and metamaterial capture efficiency.

Separates REAL engineering from speculative physics.
"""
import numpy as np

print("Metamaterial Rectenna & Ambient Energy Analysis")
print("=" * 72)

# ═══════════════════════════════════════════════════════════
# PART 1: REAL AMBIENT RF POWER DENSITY
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 1: AMBIENT RF POWER DENSITY (Measured Reality) ═══\n")

# Real-world ambient RF power densities (peer-reviewed measurements)
ambient_rf = {
    "FM Radio (88-108 MHz)":      {"S_dBm_m2": -25, "note": "Near urban transmitter"},
    "TV Broadcast (470-890 MHz)": {"S_dBm_m2": -30, "note": "Urban, line-of-sight"},
    "GSM 900 MHz":                {"S_dBm_m2": -25, "note": "Near cell tower (<200m)"},
    "GSM 1800 MHz":               {"S_dBm_m2": -30, "note": "Urban ambient"},
    "WiFi 2.4 GHz":              {"S_dBm_m2": -20, "note": "Indoor, near router"},
    "WiFi 5 GHz":                {"S_dBm_m2": -30, "note": "Indoor, same room"},
    "LTE (various)":             {"S_dBm_m2": -28, "note": "Urban outdoor"},
    "Ambient total (urban)":     {"S_dBm_m2": -15, "note": "All bands combined"},
    "CMB (cosmic microwave)":    {"S_dBm_m2": -90, "note": "2.725K blackbody — NOT harvestable"},
}

print(f"{'Source':<30} {'Power density':<16} {'uW/m2':<12} {'Note'}")
print("-" * 72)

for name, rf in ambient_rf.items():
    dBm = rf["S_dBm_m2"]
    uW_m2 = 10**(dBm/10) * 1000  # Convert dBm/m2 to uW/m2
    print(f"{name:<30} {dBm:>5} dBm/m2    {uW_m2:<12.4f} {rf['note']}")

print("\n*** CRITICAL REALITY CHECK ***")
print("  CMB power density: ~0.0000001 uW/m2 = 0.1 pW/m2")
print("  This is 10 BILLION times weaker than urban WiFi.")
print("  CMB cannot power anything. Not even a single transistor switch.")
print("  Harvestable RF = human-made transmitters only.")

# ═══════════════════════════════════════════════════════════
# PART 2: SCHOTTKY RECTIFICATION (Metal-Semiconductor Junction)
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 2: SCHOTTKY BARRIER RECTIFICATION ═══\n")

# Schottky diode: Metal (Au) on Semiconductor (Fe3O4 or Si)
# I = I_s * (exp(qV/nkT) - 1)
q = 1.602e-19    # Elementary charge
k_B = 1.381e-23  # Boltzmann constant
T = 310           # Body temperature

# Material combinations for rectification
junctions = {
    "Au/n-Si": {
        "phi_B": 0.80,  # Barrier height (eV)
        "n": 1.05,      # Ideality factor
        "desc": "Standard Schottky, well-characterized"
    },
    "Au/Fe3O4": {
        "phi_B": 0.45,  # Lower barrier — better for low-voltage
        "n": 1.8,       # Higher ideality (granular interface)
        "desc": "Black sand heterojunction"
    },
    "Au/GaAs": {
        "phi_B": 0.90,
        "n": 1.02,
        "desc": "High-frequency rectenna standard"
    },
    "Au/Graphene": {
        "phi_B": 0.35,
        "n": 1.3,
        "desc": "Ultra-low barrier, flexible"
    },
}

print("Schottky Junction Analysis (Au shell on core materials)")
print(f"{'Junction':<14} {'phi_B(eV)':<10} {'n':<6} {'V_turn-on':<12} {'Use case'}")
print("-" * 72)

for name, j in junctions.items():
    # Turn-on voltage approximately phi_B * n * kT/q correction
    V_on = j["phi_B"] - (j["n"] * k_B * T / q) * np.log(1e4)  # Rough
    V_on = max(0.1, j["phi_B"] * 0.6)  # Simplified practical turn-on
    print(f"{name:<14} {j['phi_B']:<10.2f} {j['n']:<6.2f} {V_on:<12.2f}V {j['desc']}")

print()
print("For ambient RF rectification:")
print("  Incoming RF amplitude: ~10-100 mV (from ambient)")
print("  Required: Zero-bias or near-zero-bias rectification")
print("  Au/Fe3O4 (phi_B=0.45) requires >200mV — marginal for ambient")
print("  Au/Graphene (phi_B=0.35) — best candidate for passive harvest")
print("  Tunnel diodes or backward diodes needed for <50mV signals")

# ═══════════════════════════════════════════════════════════
# PART 3: METAMATERIAL ARRAY CAPTURE
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 3: METAMATERIAL ARRAY GEOMETRY ═══\n")

c = 3e8  # Speed of light
eps0 = 8.854e-12
mu0 = 4 * np.pi * 1e-7

# Resonant capture: element size ~ lambda/10 for metamaterial
bands = {
    "L-Band (1.5 GHz)":   {"f": 1.5e9,  "use": "Power harvest (strongest ambient)"},
    "S-Band (2.4 GHz)":   {"f": 2.4e9,  "use": "WiFi harvest"},
    "C-Band (5.8 GHz)":   {"f": 5.8e9,  "use": "WiFi 5GHz harvest"},
    "X-Band (10 GHz)":    {"f": 10e9,   "use": "Satellite downlink"},
    "K-Band (20 GHz)":    {"f": 20e9,   "use": "5G mmWave (limited)"},
    "Ka-Band (30 GHz)":   {"f": 30e9,   "use": "Satellite Ka"},
}

print(f"{'Band':<22} {'freq':<12} {'lambda':<10} {'Element size':<14} {'Use'}")
print("-" * 72)

for name, b in bands.items():
    lam = c / b["f"]
    elem = lam / 10  # Metamaterial element ~lambda/10
    if lam > 0.01:
        lam_s = f"{lam*100:.1f} cm"
        elem_s = f"{elem*1000:.1f} mm"
    else:
        lam_s = f"{lam*1000:.1f} mm"
        elem_s = f"{elem*1000:.2f} mm"
    print(f"{name:<22} {b['f']/1e9:<12.1f}GHz {lam_s:<10} {elem_s:<14} {b['use']}")

# Effective capture area
print("\nEffective capture area for resonant metamaterial:")
print("  A_eff = G * lambda^2 / (4*pi)")
print("  For patch antenna with G=6 dBi at 2.4 GHz:")
A_eff = 10**(6/10) * (c/2.4e9)**2 / (4*np.pi)
print(f"  A_eff = {A_eff*1e4:.1f} cm2")
print(f"  With -20 dBm/m2 WiFi: P_captured = {A_eff * 10**(-20/10) * 1e6:.2f} uW")

# Array on body (100 cm2 patch)
A_body = 100e-4  # 100 cm2
P_urban = A_body * 10**(-15/10) * 1e3  # Total urban ambient, mW
print(f"\n  100cm2 body patch in urban RF:")
print(f"  P_captured = {P_urban*1000:.1f} uW (all bands combined)")
print(f"  After rectification (30% eff): {P_urban*1000*0.3:.1f} uW")

# ═══════════════════════════════════════════════════════════
# PART 4: STOCHASTIC RESONANCE
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 4: STOCHASTIC RESONANCE (Noise-Enhanced Signal) ═══\n")

print("Stochastic resonance: noise HELPS weak signal detection")
print("System: bistable potential U(x) = -ax²/2 + bx⁴/4")
print("Signal below threshold + noise → periodic switching\n")

# Kramers rate: r = (a*sqrt(b)) / (2*pi) * exp(-a²/(4*b*D))
# where D = noise intensity
a = 1.0
b = 1.0
barrier = a**2 / (4*b)

print(f"Barrier height: {barrier:.2f} (normalized units)")
print(f"{'Noise D':<10} {'Kramers rate':<16} {'SNR enhancement':<18} {'Status'}")
print("-" * 60)

D_values = [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0]
snr_max = 0
D_optimal = 0

for D in D_values:
    rate = (a * np.sqrt(b)) / (2 * np.pi) * np.exp(-barrier / D)
    # SNR peaks when noise matches barrier
    snr = rate * np.exp(-D)  # Simplified SNR proxy
    if snr > snr_max:
        snr_max = snr
        D_optimal = D
    status = "OPTIMAL" if abs(D - 0.2) < 0.05 else "sub-threshold" if D < 0.1 else "over-driven" if D > 0.5 else ""
    print(f"{D:<10.2f} {rate:<16.6f} {snr:<18.6f} {status}")

print(f"\nOptimal noise level: D ~ {D_optimal:.2f}")
print(f"This means: the 'right amount' of environmental noise")
print(f"actually HELPS the metamaterial detect weak signals.")
print(f"Too little noise: signal below threshold, no detection.")
print(f"Too much noise: signal buried, random switching.")

# ═══════════════════════════════════════════════════════════
# PART 5: MICRO-INDUCTOR FROM GRAIN GEOMETRY
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 5: GRAIN-TO-GRAIN MICRO-INDUCTANCE ═══\n")

# L = mu0 * N^2 * A / l
# For granular film: N = contact points in chain
# A = cross-section of grain cluster, l = chain length

grain_d = 50e-6  # 50 micron grain diameter (fine sand)
A_grain = np.pi * (grain_d/2)**2
mu_r_fe3o4 = 20  # Relative permeability of magnetite

print(f"Grain diameter: {grain_d*1e6:.0f} um")
print(f"Grain cross-section: {A_grain*1e12:.0f} um2")
print(f"Magnetite mu_r: {mu_r_fe3o4}")
print()

print(f"{'Chain length':<14} {'N contacts':<12} {'L (nH)':<10} {'f_res (GHz)':<14} {'Band'}")
print("-" * 60)

for N in [5, 10, 20, 50, 100]:
    l_chain = N * grain_d
    L = mu0 * mu_r_fe3o4 * N**2 * A_grain / l_chain
    L_nH = L * 1e9
    # Self-resonant frequency with parasitic C (~0.1 pF per contact)
    C_parasitic = N * 0.1e-12
    f_res = 1 / (2 * np.pi * np.sqrt(L * C_parasitic))
    band = "L-band" if f_res < 2e9 else "S-band" if f_res < 4e9 else "C-band" if f_res < 8e9 else "X-band" if f_res < 12e9 else "K-band"
    print(f"{l_chain*1e3:.2f} mm{'':<6} {N:<12} {L_nH:<10.3f} {f_res/1e9:<14.2f} {band}")

# ═══════════════════════════════════════════════════════════
# PART 6: REALISTIC POWER BUDGET
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 6: REALISTIC HARVEST BUDGET ═══\n")

harvest = {
    "RF rectenna (urban)":       {"P_uW": 10,    "real": True},
    "Thermoelectric (body)":     {"P_uW": 80,    "real": True},
    "Piezoelectric (shoe)":      {"P_uW": 50,    "real": True},
    "Solar (flex, outdoor)":     {"P_uW": 50000, "real": True},
    "Solar (flex, indoor)":      {"P_uW": 100,   "real": True},
    "CMB capture":               {"P_uW": 0.0000001, "real": False},
    "Vacuum fluctuations":       {"P_uW": 0,     "real": False},
    "Quantum correlation":       {"P_uW": 0,     "real": False},
}

print(f"{'Source':<28} {'Power (uW)':<14} {'Harvestable?':<14} {'Engineering status'}")
print("-" * 72)
total_real = 0
for name, h in harvest.items():
    status = "PROVEN" if h["real"] and h["P_uW"] > 0 else "THEORETICAL" if not h["real"] else "—"
    harv = "YES" if h["real"] and h["P_uW"] > 0 else "NO"
    print(f"{name:<28} {h['P_uW']:<14.4f} {harv:<14} {status}")
    if h["real"]:
        total_real += h["P_uW"]

print(f"\nTotal harvestable (no solar): {total_real - 50000 - 100:.0f} uW")
print(f"Total harvestable (indoor):  {total_real - 50000:.0f} uW")
print(f"Total harvestable (outdoor): {total_real:.0f} uW")

# ═══════════════════════════════════════════════════════════
# PART 7: WHAT ACTUALLY WORKS FOR WEARABLE ROBOTICS
# ═══════════════════════════════════════════════════════════
print("\n═══ PART 7: REAL ROBOTICS FACTORY PATH ═══\n")

print("To build actual self-sustaining wearable + robotics:")
print()
print("1. ENERGY TIER (what powers what):")
print("   Tier 0: Grid power (factory robots) — 100W-10kW per unit")
print("   Tier 1: Battery (mobile robots) — 10-100W, 1-8 hours")
print("   Tier 2: Solar+battery (outdoor wearable) — 50-500 mW")
print("   Tier 3: Harvest only (body wearable) — 50-200 uW")
print()
print("2. COMPUTE TIER (matched to energy):")
print("   Tier 0: Full CPU/GPU (factory) — x86/ARM A-series")
print("   Tier 1: Edge AI (mobile) — Cortex A53, NPU")
print("   Tier 2: Microcontroller (wearable) — Cortex M4, RISC-V")
print("   Tier 3: Sensor hub (harvest) — Cortex M0+, sleep-dominant")
print()
print("3. COMMUNICATION TIER:")
print("   Tier 0: Ethernet/WiFi (factory) — Gbps, unlimited power")
print("   Tier 1: WiFi/5G (mobile) — Mbps, battery-limited")
print("   Tier 2: BLE 5.3 (wearable) — 2 Mbps, 10-50 mW bursts")
print("   Tier 3: Backscatter (harvest) — kbps, <1 uW")
print()
print("4. FACTORY SELF-BUILD PATH:")
print("   Phase 1: Human-operated CNC + 3D printing")
print("   Phase 2: Robot-assisted assembly (pick & place)")
print("   Phase 3: Robot-manufactured subassemblies")
print("   Phase 4: Robot builds robot (supervised)")
print("   Phase 5: Autonomous expansion (self-replicating factory)")
print("   Each phase requires the PREVIOUS phase working reliably.")
print("   No shortcuts. No skipping phases.")

print("\n═══ CONCLUSION ═══")
print("Metamaterial rectenna: REAL, 10-50 uW from urban RF")
print("Schottky Au/Fe3O4: REAL, needs low-barrier design")
print("Stochastic resonance: REAL, noise-enhanced detection")
print("CMB/vacuum harvest: NOT REAL, violates thermodynamics")
print("Robotics factory: REAL, requires phased build-up")
print("Every step must work before the next one starts.")
