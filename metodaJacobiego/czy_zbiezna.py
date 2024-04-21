import numpy as np

def czy_diagonalnie_dominujaca(A):
    A = np.array(A)
    n = A.shape[0]
    for i in range(n):
        diagonal_sum = np.sum(np.abs(A[i, :])) - np.abs(A[i, i])
        if np.abs(A[i, i]) <= diagonal_sum:
            return False
    return True
