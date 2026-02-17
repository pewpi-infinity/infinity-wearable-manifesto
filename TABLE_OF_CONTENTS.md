# C13B0 Wearable Manifesto Engine

## Table of Contents

### Volume I — Ion Foundations
- [Electrostatics (Root Layer)](https://pewpi-infinity.github.io/infinity-manifesto/)
- [Fermi Layer (Quantum Materials)](https://pewpi-infinity.github.io/infinity-energy/)
- [Electrochemistry](https://pewpi-infinity.github.io/infinity-currency/)
- [Ion Transport](https://pewpi-infinity.github.io/infinity-dynamics/)
- [Ion Gradients (Biology)](https://pewpi-infinity.github.io/infinity-memory/)
- [Maxwell Unification](https://pewpi-infinity.github.io/infinity-quantum-lighting/)

### Simulations
- `simulations/ion_flux_sim.py` — Nernst-Planck ion transport
- `simulations/fermi_energy_sim.py` — Fermi energy for metallic systems
- `simulations/lattice_energy_sim.py` — Born-Lande lattice energies
- `simulations/thermoelectric_model.py` — Wearable thermoelectric harvesting

### Schematics
- `schematics/node_schematics.md` — Wearable node type specifications
- `schematics/node_generator.py` — Automated schematic generator

### Ecosystem Links
- [Crown Index](https://pewpi-infinity.github.io/infinity-crown-index/)
- [Version Viewer](https://pewpi-infinity.github.io/infinity-crown-index/version_viewer.html)
- [Mega Labs](https://pewpi-infinity.github.io/infinity-mega-labs/)

---

## Design Constraints

- Total wearable power budget: ~200 uW (realistic body harvest)
- Active compute bursts: max 10ms every 10s
- BLE beacon: 1 packet/second max
- All materials biocompatible (no Pb, Cd)
- Washable: sealed nodes with flex interconnects

---

*Part of the Infinity Ecosystem — C13B0 Structural Engine*
