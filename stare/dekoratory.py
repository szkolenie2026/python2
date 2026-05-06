def dekor(funkcja):
    def wew():
        print("Dekorujemy funkcję")
        return funkcja()

    return wew


@dekor
def zwykłaFunkcja():
    print("To jest zwykła funkcja")

# nowaFunkcja = dekor(zwykłaFunkcja)
# nowaFunkcja()
zwykłaFunkcja()

def dekor(funkcja):
    def wew(*args, **kwargs):
        print("Dekorujemy funkcję")
        return funkcja(*args, **kwargs)

    return wew


@dekor
def zwykłaFunkcja(a, b, c):
    print("To jest zwykła funkcja, która dodaje liczby:")
    print(a + b + c)

zwykłaFunkcja(1,2,3)