# logiquant

Quantum Vehicle Routing Problem (QVRP)
Problem:
A fleet of delivery trucks must visit several customer locations and return to the depot with minimum distance/time, considering capacity constraints. This is a classic NP-hard VRP, which quantum can accelerate.

Quantum Approach:
Formulate the VRP as a QUBO, and solve it with QAOA (using Qiskit) or D-Wave Hybrid Sampler.

# Quantum Vehicle Routing Problem (QVRP) with Qiskit QAOA

Solve the Vehicle Routing Problem using QUBO formulation and Qiskit QAOA.

## Structure
- `data/customer_locations.csv`: Customer XY positions
- `qubo_formulation.py`: Builds QUBO model
- `qvrp_solver.py`: QAOA-based QUBO solver using Qiskit
- `plot_solution.py`: Visualizes customer locations

## Requirements
bash
pip install -r requirements.txt

## Run
bash
python plot_solution.py
python qvrp_solver.py


### requirements.txt
pandas
matplotlib
networkx
qiskit
qiskit-optimization




quantum-logistics-vrp/
├── data/
│   └── customer_locations.csv
├── qvrp_solver.py
├── qubo_formulation.py
├── plot_solution.py
├── README.md
└── requirements.txt

Tech Stack:
Qiskit SDK
NetworkX
Matplotlib / Plotly
NumPy
