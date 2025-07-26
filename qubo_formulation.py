def create_qubo(distance_matrix):
    Q = {}
    n = len(distance_matrix)
    for i in range(n):
        for j in range(n):
            if i != j:
                Q[(i, j)] = distance_matrix[i][j]
    return Q
