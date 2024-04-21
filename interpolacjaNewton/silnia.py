def funkcja_silnia(x):
    n = x
    if x > 1:
        for i in range(1, x):
            n = n * (x - i)
        return n
    elif x == 0 or x == 1:
        return 1
    else:
        print("Liczba niepoprawna! Musi byc dodatnia naturalna")
        return None
