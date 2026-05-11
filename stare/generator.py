# 1. Definicja generatora
def generuj_kolejne_liczby(limit):
    for i in range(limit):
        yield i  # <--- To słowo czyni funkcję generatorem!

# 2. Użycie generatora
moj_generator = generuj_kolejne_liczby(3)

# Generatory pobieramy za pomocą wbudowanej funkcji next() lub pętli for
print(next(moj_generator))  # Wynik: 0
print(next(moj_generator))  # Wynik: 1
print(next(moj_generator))  # Wynik: 2
# print(next(moj_generator))  # To rzuciłoby błąd StopIteration, bo limit to 3

# Przeważnie używamy ich po prostu w pętlach:
for liczba in generuj_kolejne_liczby(5):
    print(liczba)