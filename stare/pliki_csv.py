import csv

# Otwieramy plik do odczytu
with open('dane.csv', mode='r', encoding='utf-8') as plik:
    # Tworzymy czytnik, który traktuje wiersze jak słowniki
    czytnik = csv.DictReader(plik, delimiter=';')
# Pobieranie nazw kolumn (Nagłówków)
    kolumny = czytnik.fieldnames
    print(f"Znalezione kolumny: {kolumny}")

    # for wiersz in czytnik:
    #     # Odwołujemy się do danych po nazwie nagłówka
    #     print(f"Pojazd: {wiersz['Marka pojazdu']}, Cena: {wiersz['Cena netto']}")

# import csv

# with open('dane.csv', mode='r', encoding='utf-8') as plik:
#     # Używamy zwykłego reader zamiast DictReader
#     czytnik = csv.reader(plik, delimiter=';') 
# Jeśli korzystasz ze zwykłego csv.reader (który zwraca wiersze jako listy, np. wiersz[2]), Python nie wie, że pierwszy wiersz to nagłówki. Jeśli od razu puścisz pętlę for, Twój program spróbuje potraktować słowo "Cena netto" jak liczbę, co wyrzuci błąd.
# next() pobiera pierwszy wiersz i przesuwa kursor do drugiego
naglowki = next(czytnik) 
print(f"Nagłówki to: {naglowki}")

# Liczenie liczby rekordów (wierszy)
wszystkie_dane = list(czytnik) 
liczba_rekordow = len(wszystkie_dane)
# # Dodaje 1 za każdy odczytany wiersz z iteratora
# liczba_rekordow = sum(1 for wiersz in czytnik)
#     # Przechodzimy przez każdy wiersz
#     for wiersz in czytnik:
#         # Odwołujemy się do indeksów (numerów kolumn)
#         print(f"Marka: {wiersz[1]}, Cena: {wiersz[2]}")
# import csv

# dane_pojazdu = {"Marka": "Toyota", "Kolor": "Czerwony", "Cena": 50000}
# # Tryb 'a' (append) dopisuje na końcu pliku
# with open('dane.csv', mode='a', encoding='utf-8', newline='') as plik:
#     naglowki = ['Marka', 'Kolor', 'Cena']
    
    #   zapisywacz = csv.DictWriter(plik, fieldnames=naglowki)
#     # Jeśli plik jest pusty, używasz zapisywacz.writeheader() aby dodać nagłówki
#     # Zapisujemy pojedynczy wiersz
#     zapisywacz.writerow(dane_pojazdu)

# # Zapisywanie hurtowe: writerows()
# nowe_dane = [
#     ["BMW", "150000", "Czarny"],
#     ["Audi", "120000", "Biały"],
#     ["Skoda", "80000", "Niebieski"]
# ]
# zapisywacz.writerows(nowe_dane) # Hurtowy zapis całej listy list