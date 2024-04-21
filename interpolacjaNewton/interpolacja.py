import numpy as np
import matplotlib.pyplot as plt

def interpolacjaNewton(funkcja, a, b, liczbaWezlow):
    # Obliczanie równoodległych węzłów interpolacji
    h = (b - a) / (liczbaWezlow)
    wezly = np.linspace(a, b, liczbaWezlow)


def roznice_progresywne(y_values):
    n = len(y_values)
    differences = [[j for j in range(n - i)] for i in range(n)]  # Tworzenie tablicy dla różnic progresywnych
    for j in range(0, n):
        differences[0][j] = y_values[j]  # Różnice progresywne stopnia 0
    for k in range(1, n):
        for i in range(0, n - k):
            differences[k][i] = differences[k - 1][i + 1] - differences[k - 1][i]
    return differences