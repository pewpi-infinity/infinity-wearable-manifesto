#!/usr/bin/env python3
"""
Distributed RAM Memory Map — Wearable Mesh Architecture
C13B0 Structural Engine — Module C

Maps memory across distributed wearable nodes.
RAM as power, power as memory — unified energy-information model.
"""
import numpy as np

print("Distributed RAM Memory Map — Wearable Mesh")
print("=" * 70)

# ─── Node Memory Architecture ───
print("\n─── NODE MEMORY SPECIFICATIONS ───\n")

nodes = {
    "SensorNode": {
        "count": 12,
        "sram_KB": 64,
        "flash_KB": 512,
        "mram_KB": 0,
        "role": "Data acquisition + local filter",
        "data_rate_bps": 1000,
    },
    "ComputeNode": {
        "count": 2,
        "sram_KB": 256,
        "flash_KB": 2048,
        "mram_KB": 4096,
        "role": "Processing + inference",
        "data_rate_bps": 100000,
    },
    "PowerNode": {
        "count": 4,
        "sram_KB": 16,
        "flash_KB": 128,
        "mram_KB": 0,
        "role": "Energy management + logging",
        "data_rate_bps": 100,
    },
    "MeshRouter": {
        "count": 6,
        "sram_KB": 128,
        "flash_KB": 512,
        "mram_KB": 0,
        "role": "Routing + buffering",
        "data_rate_bps": 250000,
    },
}

print(f"{'Node':<14} {'#':<4} {'SRAM':<10} {'Flash':<10} {'MRAM':<10} {'Total/node':<12} {'Role'}")
print("-" * 70)

total_sram = 0
total_flash = 0
total_mram = 0
total_nodes = 0

for name, n in nodes.items():
    total_per = n["sram_KB"] + n["flash_KB"] + n["mram_KB"]
    total_sram += n["sram_KB"] * n["count"]
    total_flash += n["flash_KB"] * n["count"]
    total_mram += n["mram_KB"] * n["count"]
    total_nodes += n["count"]
    print(f"{name:<14} {n['count']:<4} {n['sram_KB']}KB{'':<5} {n['flash_KB']}KB{'':<5} {n['mram_KB']}KB{'':<5} {total_per}KB{'':<7} {n['role']}")

total_all = total_sram + total_flash + total_mram
print(f"\n{'TOTAL':<14} {total_nodes:<4} {total_sram}KB{'':<5} {total_flash}KB{'':<5} {total_mram}KB{'':<5} {total_all}KB")
print(f"{'':14} {'':4} {total_sram/1024:.1f}MB{'':<4} {total_flash/1024:.1f}MB{'':<4} {total_mram/1024:.1f}MB{'':<4} {total_all/1024:.1f}MB")

# ─── Memory Map Layout ───
print("\n─── DISTRIBUTED MEMORY MAP ───\n")

# Address space: 24-bit distributed (16M addressable bytes)
# Upper 4 bits = node type, next 4 = node ID, lower 16 = local address
print("Address Format: [NodeType:4][NodeID:4][LocalAddr:16]")
print()
print("Addr Range          Node           Memory Type    Size")
print("-" * 65)

addr_map = [
    ("0x00_0000-0x00_FFFF", "SensorNode[0]",  "SRAM+Flash",  "576KB"),
    ("0x01_0000-0x01_FFFF", "SensorNode[1]",  "SRAM+Flash",  "576KB"),
    ("0x0B_0000-0x0B_FFFF", "SensorNode[11]", "SRAM+Flash",  "576KB"),
    ("0x10_0000-0x11_FFFF", "ComputeNode[0]", "SRAM+Flash+MRAM", "6.25MB"),
    ("0x12_0000-0x13_FFFF", "ComputeNode[1]", "SRAM+Flash+MRAM", "6.25MB"),
    ("0x20_0000-0x20_FFFF", "PowerNode[0]",   "SRAM+Flash",  "144KB"),
    ("0x30_0000-0x30_FFFF", "MeshRouter[0]",  "SRAM+Flash",  "640KB"),
]

for addr, node, mtype, size in addr_map:
    print(f"{addr:<22} {node:<16} {mtype:<15} {size}")
print("...")

# ─── Data Flow Model ───
print("\n─── DATA FLOW: SENSOR → COMPUTE → MESH → OUT ───\n")

# Pipeline stages
stages = [
    ("1. Sense",     "SensorNode",  "ADC sample → local SRAM buffer",     "16 bytes/sample"),
    ("2. Filter",    "SensorNode",  "Moving average in SRAM",              "1KB working set"),
    ("3. Compress",  "SensorNode",  "Delta encode → Flash log",            "4:1 compression"),
    ("4. Transfer",  "MeshRouter",  "BLE packet → router SRAM buffer",    "20 bytes/packet"),
    ("5. Aggregate", "ComputeNode", "Collect from 12 sensors → MRAM",     "240 bytes/cycle"),
    ("6. Infer",     "ComputeNode", "TinyML model in Flash, state in SRAM","32KB model"),
    ("7. Report",    "MeshRouter",  "Result → BLE → phone/cloud",         "50 bytes/report"),
]

print(f"{'Stage':<14} {'Node':<14} {'Operation':<40} {'Size'}")
print("-" * 70)
for stage, node, op, size in stages:
    print(f"{stage:<14} {node:<14} {op:<40} {size}")

# ─── Energy-Memory Equivalence ───
print("\n─── ENERGY-MEMORY EQUIVALENCE ───")
print("RAM is the power. Power is the memory.\n")

# Energy per bit for different memory types
mem_energy = {
    "SRAM read":     {"E_fJ": 5,     "desc": "Fastest, volatile"},
    "SRAM write":    {"E_fJ": 5,     "desc": "Same as read"},
    "Flash read":    {"E_fJ": 50,    "desc": "Non-volatile, slow write"},
    "Flash write":   {"E_fJ": 10000, "desc": "Page erase needed"},
    "MRAM read":     {"E_fJ": 100,   "desc": "Non-volatile, fast"},
    "MRAM write":    {"E_fJ": 200,   "desc": "Spin-transfer torque"},
    "BLE transmit":  {"E_fJ": 50000, "desc": "Over-the-air per bit"},
}

print(f"{'Operation':<18} {'Energy/bit (fJ)':<18} {'bits/μJ':<14} {'Note'}")
print("-" * 65)
for name, m in mem_energy.items():
    bits_per_uJ = 1e9 / m["E_fJ"]  # 1 μJ = 1e-6 J = 1e9 fJ
    print(f"{name:<18} {m['E_fJ']:<18} {bits_per_uJ:<14.0f} {m['desc']}")

print("\nWith 200 μW harvest budget:")
harvest_uW = 200
print(f"  SRAM ops/sec:   {harvest_uW * 1e9 / 5:.2e} bits/s = {harvest_uW * 1e9 / 5 / 8 / 1e6:.0f} MB/s")
print(f"  Flash reads/sec: {harvest_uW * 1e9 / 50:.2e} bits/s = {harvest_uW * 1e9 / 50 / 8 / 1e6:.0f} MB/s")
print(f"  BLE bits/sec:    {harvest_uW * 1e9 / 50000:.2e} bits/s = {harvest_uW * 1e9 / 50000 / 1000:.0f} kbps")
print(f"\nConclusion: Energy budget constrains BLE bandwidth, not compute.")
print(f"Memory access is cheap. Communication is expensive.")
print(f"This is why local processing + compressed reporting wins.")
