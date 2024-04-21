from czy_zbiezna import czy_diagonalnie_dominujaca
from metoda_jacobi import jacobi
from odczyt_macierz import stworz_macierz

menu = True
iter = None
eps = None

while menu:
    dobryPlik = True
    print("""Witaj w moim programie! Co chcesz zrobić?
             1. Wczytać macierz z pliku
             2. Wyjść z programu""")
    wybor = int(input("Wpisz 1 lub 2: "))
    if wybor == 1:
        while dobryPlik:
            stop = True
            nazwa_pliku = input("Podaj nazwę pliku z danymi (np. przyklad_a, przyklad_b, itd.): ")
            nazwa_pliku += ".txt"
            A, b, ilosc_rzedow = stworz_macierz(nazwa_pliku)
            if A is None or b is None or ilosc_rzedow is None:
                dobryPlik = True
            else:
                dobryPlik = False
                print("Macierz A:")
                print(A)
                print("Macierz b:")
                print(b)
                if czy_diagonalnie_dominujaca(A):
                    rownania = True
                    print("Macierz jest diagonalnie dominująca!")
                    while rownania:
                        ilosc_rownan = int(input("Podaj ilość równań do rozwiązania w podanej macierzy: "))
                        if ilosc_rownan > ilosc_rzedow:
                            print("Ilość równań do obliczenia nie może być większa niż ilość wierszy macierzy! \n")
                        elif ilosc_rownan < 1:
                            print("Ilość równań do obliczenia musi być równa przynajmniej 1! \n")
                        else:
                            rownania = False
                    while stop:
                        koniec = True
                        print("""Wybierz warunek stopu:
                                     1. Wykonanie zadanej liczby iteracji
                                     2. Uzyskanie podanej dokładności
                                     3. Powrót do początku""")
                        warunek = int(input("Wybierz warunek (1-2) lub 3 by cofnąć do wczytania macierzy: "))
                        if warunek == 1:
                            while koniec:
                                iter = int(input("Podaj liczbę iteracji: "))
                                if iter > 0:
                                    print("Rozwiązanie układu równań metodą Jacobiego:")
                                    x = jacobi(A, b, ilosc_rownan, iter, eps)
                                    for i, val in enumerate(x, start=1):
                                        print(f"x{i} = {val}")
                                    print("")
                                    koniec = False
                                else:
                                    print("Liczba iteracji musi być liczbą naturalną!\n")
                        elif warunek == 2:
                            while koniec:
                                eps = float(input("Podaj dokladność: "))
                                if eps > 0:
                                    print("Rozwiązanie układu równań metodą Jacobiego:")
                                    x = jacobi(A, b, ilosc_rownan, iter, eps)
                                    for i, val in enumerate(x, start=1):
                                        print(f"x{i} = {val}")
                                    print("")
                                    koniec = False
                                else:
                                    print("Dokładność musi być liczbą całkowita dodatnia!\n")
                        elif warunek == 3:
                            koniec = False
                            stop = False
                            dobryPlik = False
                        else:
                            print("Nieprawidłowy wybór. Proszę wpisać liczbę naturalną z zakresu 1-3!\n")
                else:
                    print("Macierz nie jest diagonalnie dominująca! Wczytaj inna macierz. \n")
                    dobryPlik = True
    elif wybor == 2:
        menu = False
        print("Do następnego razu!")
    else:
        print("Nieprawidłowy wybór. Proszę wpisać 1 lub 2!\n")
