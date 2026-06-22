import csv
marki = {}
with open('dane.csv', mode='r', encoding='utf-8') as plik:
    czytnik = csv.DictReader(plik, delimiter=";")

    for wiersz in czytnik:
        marka = wiersz['Marka pojazdu']
        cena = float(wiersz['Cena netto'])
        if marka not in marki:
            marki[marka] = [ cena, 1 ]
        else:
            marki[marka][0] += cena
            marki[marka][1] += 1

for marka in marki:
  suma = marki[marka][0]
  ile = marki[marka][1]
  srednia = round(suma/ile,2)
  marki[marka].append(srednia)

pola = ["Marka", "Suma_Cen", "Liczba_Sztuk", "Srednia"]
with open('dane_obliczone.csv', mode='w', encoding='utf-8', newline="") as plik:
    obiekt = csv.DictWriter(plik, fieldnames=pola, delimiter=";")
    obiekt.writeheader()
    for marka, dane in marki.items():
        obiekt.writerow({
            "Marka": marka,
            "Suma_Cen": dane[0],
            "Liczba_Sztuk": dane[1],
            "Srednia": dane[2]
        })
