# C13B0 Structural Engine

## Simulation Modules

### Module A — Maxwell Fields
- `simulations/maxwell_field_sim.py`
- Gauss, Ampere, Faraday applied to ion systems
- EM spectrum for wearable bands
- Field energy density analysis

### Module B — Thermal Safety
- `simulations/thermal_safety_sim.py`
- IEC 60601-1 limits, component heat modeling
- Thermal resistance stack, graphene spreader
- Skin temperature prediction

### Module C — Distributed RAM
- `simulations/memory_map_sim.py`
- 24-node distributed memory (15.6 MB total)
- Data pipeline: sense > filter > compress > route > infer > report
- Energy-memory equivalence (RAM is power)

### Module D — Power Grid
- `simulations/power_density_sim.py`
- Textile IR drop simulation (Poisson relaxation)
- Stretch-zone resistance mapping
- Thermal feedback from hotspots

### Core Simulations
- `simulations/ion_flux_sim.py` — Nernst-Planck ion transport
- `simulations/fermi_energy_sim.py` — Fermi energy for metals
- `simulations/lattice_energy_sim.py` — Born-Lande lattice energies
- `simulations/thermoelectric_model.py` — Wearable thermoelectric

### Schematics
- `schematics/node_generator.py` — Node type specifications + placement map

## Manifesto Chapters
- [I. Electrostatics](https://pewpi-infinity.github.io/infinity-manifesto/)
- [II. Electrochemistry](https://pewpi-infinity.github.io/infinity-currency/)
- [III. Fermi Layer](https://pewpi-infinity.github.io/infinity-energy/)
- [IV. Ion Transport](https://pewpi-infinity.github.io/infinity-dynamics/)
- [V. Ion Gradients](https://pewpi-infinity.github.io/infinity-memory/)
- [VI. Maxwell](https://pewpi-infinity.github.io/infinity-quantum-lighting/)

## Ecosystem
- [Crown Index](https://pewpi-infinity.github.io/infinity-crown-index/)
- [Version Viewer](https://pewpi-infinity.github.io/infinity-crown-index/version_viewer.html)
- [Mega Labs](https://pewpi-infinity.github.io/infinity-mega-labs/)
- [Wearable Engine](https://pewpi-infinity.github.io/infinity-wearable-manifesto/)
