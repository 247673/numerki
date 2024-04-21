def schemat_hornera(x, wspolczynniki):
    wynik = 0
    for wsp in wspolczynniki:
        wynik = wynik * x + wsp
    return wynik
