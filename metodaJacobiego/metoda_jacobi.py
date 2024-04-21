import numpy as np


def jacobi(A, b, ilosc_rownan, iter=None, eps=None):
    A = np.array(A)
    b = np.array(b)
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    x = np.zeros(len(A))

    czy_warunek_stopu = False
    iterations = 0
    while not czy_warunek_stopu:
        x_new = np.zeros(len(A))
        for i in range(len(A)):
            x_new[i] = (b[i] - np.dot(L[i, :], x) - np.dot(U[i, :], x)) / A[i, i]
        if iter is not None and iterations >= iter:
            czy_warunek_stopu = True
        if eps is not None and np.linalg.norm(x_new - x) < eps:
            czy_warunek_stopu = True
        x = x_new
        iterations += 1

    return x[:ilosc_rownan]
