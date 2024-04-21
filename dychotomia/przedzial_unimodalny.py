from wart_wzor import wart


def znajdz_przedzial_unimodalny(x, d, wybor):
    for i in range(1000000):
        if (wart(x - d, wybor) > wart(x, wybor)
                and wart(x + d, wybor) > wart(x, wybor)):
            return x - d, x + d
        else:
            x += d
            i += 1
    print("Nie znaleziono przedziału unimodalnego!")
    return None, None
