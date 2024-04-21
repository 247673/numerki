def stworz_macierz(file_name):
    A = []
    b = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                row = [float(x) for x in line.strip().split()]
                A.append(row[:-1])  # Dodajemy wszystkie elementy oprócz ostatniego
                b.append(row[-1])  # Dodajemy ostatni element jako część ostatniej kolumny
            # Poprawiamy ostatnią kolumnę tak, aby była osobną macierzą
            n = len(A)
            b = [[b[i]] for i in range(n)]
            return A, b, n
    except FileNotFoundError:
        print("Plik nie został odnaleziony.\n")
        return None, None, None

