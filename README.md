# logiquant

Quantum Vehicle Routing Problem (QVRP)
Problem:
A fleet of delivery trucks must visit several customer locations and return to the depot with minimum distance/time, considering capacity constraints. This is a classic NP-hard VRP, which quantum can accelerate.

Quantum Approach:
Formulate the VRP as a QUBO, and solve it with QAOA (using Qiskit) or D-Wave Hybrid Sampler.

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
