from przedzial_unimodalny import znajdz_przedzial_unimodalny
from dychotomia import dychotomia
from wart_wzor import wart
from wykresy import narysuj_wykres

menu = True
iter = None
eps = None

while menu:
    przedzial = True
    print("""Wybierz funkcję:
             1. Wielomianowa: 5x^3+4x^2-3x+2
             2. Trygonometryczna: 2cos(x)+sin(x)
             3. Wykładnicza: e^x-2x
             4. Złożona: x^2-9x+4sin(x)
             5. Wyjście z programu""")
    wybor = int(input("Wybierz funkcję (1-4) lub 5 by zakończyć: "))
    if wybor == 5:
        menu = False
        print("Do następnego razu!")
    elif wybor in [1, 2, 3, 4]:
        while przedzial:
            stop = True
            x = float(input("Podaj punkt startowy: "))
            d = float(input("Podaj dokladnosc wyznaczenia przedzialu unimodalnego: "))
            lewo_unimodal, prawo_unimodal = znajdz_przedzial_unimodalny(x, d, wybor)
            if lewo_unimodal is None or prawo_unimodal is None:
                print("Zmień punkt startowy.\n")
            else:
                print("Przedział unimodalny: (" + str(lewo_unimodal) + " ; " + str(prawo_unimodal) + ")\n")
                narysuj_wykres(lewo_unimodal, prawo_unimodal, wybor)
                przedzial = False
        while stop:
            koniec = True
            print("""Wybierz warunek stopu:
                         1. Wykonanie zadanej liczby iteracji
                         2. Zawężenie przedziału poszukiwań
                         3. Cofnij""")
            warunek = int(input("Wybierz warunek (1-2) lub 3 by cofnąć do wyboru funkcji: "))
            if warunek == 1:
                while koniec:
                    iter = int(input("Podaj liczbę iteracji: "))
                    if iter > 0:
                        wynik = wart(dychotomia(lewo_unimodal, prawo_unimodal, wybor, eps, iter),
                                     wybor)
                        print("Minimum lokalne znajduję się w punktcie x = " + str(
                            dychotomia(lewo_unimodal, prawo_unimodal, wybor, eps, iter))
                              + " i wynosi " + str(wynik) + "\n")
                        koniec = False
                    else:
                        print("Liczba iteracji musi być liczbą naturalną!\n")
            elif warunek == 2:
                while koniec:
                    eps = float(input("Podaj wartość epsilon: "))
                    if eps > 0:
                        wynik = wart(dychotomia(lewo_unimodal, prawo_unimodal, wybor, eps, iter),
                                     wybor)
                        print("Minimum lokalne znajduję się w punktcie x = " + str(
                            dychotomia(lewo_unimodal, prawo_unimodal, wybor, eps, iter))
                              + " i wynosi " + str(wynik) + "\n")
                        koniec = False
                    else:
                        print("Musi być to liczba całkowita dodatnia!\n")
            elif warunek == 3:
                koniec = False
                stop = False
            else:
                print("Nieprawidłowy wybór. Proszę wpisać liczbę naturalną z zakresu 1-3!\n")
    else:
        print("Nieprawidłowy wybór. Proszę wpisać liczbę naturalną z zakresu 1-5!\n")
