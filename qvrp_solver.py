from qubo_formulation import create_qubo
import networkx as nx
import pandas as pd
import numpy as np
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import QAOA
from qiskit import Aer
from qiskit.utils import algorithm_globals

# Load customer data
locations = pd.read_csv('data/customer_locations.csv')

# Compute distance matrix (Haversine or Euclidean for lat/long)
def euclidean(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

distance_matrix = [
    [euclidean(locations.iloc[i][['x','y']], locations.iloc[j][['x','y']]) for j in range(len(locations))] 
    for i in range(len(locations))
]

# Create QUBO
Q = create_qubo(distance_matrix)

# Build Qiskit Quadratic Program
qp = QuadraticProgram()
n = len(distance_matrix)

for i in range(n):
    qp.binary_var(name=f'x_{i}')

linear = {f"x_{i}": 0 for i in range(n)}
quadratic = {(f"x_{i}", f"x_{j}"): Q[(i, j)] for i in range(n) for j in range(n) if (i, j) in Q}

qp.minimize(linear=linear, quadratic=quadratic)

# Solve with QAOA
algorithm_globals.random_seed = 123
backend = Aer.get_backend('qasm_simulator')
qaoa = QAOA(reps=1, quantum_instance=backend)
optimizer = MinimumEigenOptimizer(qaoa)
result = optimizer.solve(qp)

print("Optimal route (binary encoding):", result.x)
