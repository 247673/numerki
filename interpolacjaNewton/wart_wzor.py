import numpy as np
import sympy as sp
from horner import schemat_hornera


def wart(x, wybor):
    if wybor == 1:
        wynik = schemat_hornera(x, [5, 4, -3, 2])
    elif wybor == 2:
        wynik = 2*np.cos(x)+np.sin(x)
    elif wybor == 3:
        wynik = np.exp(x)-2*x
    elif wybor == 4:
        wynik = x**2-9*x+4*np.sin(x)
    else:
        print("Podano nieprawidlowa wartosc!")
        wynik = None
    return wynik


def wzor(wybor):
    x = sp.Symbol('x')
    if wybor == 1:
        wz = schemat_hornera(x, [5, 4, -3, 2])
    elif wybor == 2:
        wz = 2*sp.cos(x)+sp.sin(x)
    elif wybor == 3:
        wz = sp.exp(x)-2*x
    elif wybor == 4:
        wz = x**2-9*x+4*sp.sin(x)
    else:
        print("Podano nieprawidlowa wartosc!")
        wz = None
    return wz
