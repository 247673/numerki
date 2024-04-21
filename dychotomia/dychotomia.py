from wart_wzor import wart


def dychotomia(a, b, wybor, eps=None, iter=None):
    czy_warunek_stopu = False
    i = 0
    while not czy_warunek_stopu:
        L0 = b - a
        x1 = a + L0 / 2 - (10 ** -8) / 2
        x2 = a + L0 / 2 + (10 ** -8) / 2
        if wart(x1, wybor) >= wart(x2, wybor):
            a = x1
        elif wart(x1, wybor) <= wart(x2, wybor):
            b = x2
        if iter is not None and i >= iter:
            czy_warunek_stopu = True
        if eps is not None and b - a < eps:
            czy_warunek_stopu = True
        i += 1
    x_min = (a + b) / 2
    return x_min
