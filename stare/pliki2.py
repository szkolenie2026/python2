import os

# 1. Przygotowanie folderu (jeśli nie istnieje)
folder_wynikowy = r"d:\Documents\Szkolenia\Python\cwiczenia\lokalizacje"
if not os.path.exists(folder_wynikowy):
    os.makedirs(folder_wynikowy)

plik = open(r"d:\Documents\Szkolenia\Python\cwiczenia\dane.csv", "rt", encoding="utf8")
# Struktura: { 'Warszawa': { 'Toyota': [suma, ile], 'BMW': [suma, ile] }, 'Kraków': { ... } }
dane_lokalizacji = {} 

next(plik) 

for wiersz in plik:
    dane = wiersz.strip().split(";")
    marka = dane[1]
    cena = float(dane[2])
    lokalizacja = dane[7] 

    # Budujemy strukturę zagnieżdżoną
    if lokalizacja not in dane_lokalizacji:
        dane_lokalizacji[lokalizacja] = {}
    
    if marka not in dane_lokalizacji[lokalizacja]:
        dane_lokalizacji[lokalizacja][marka] = [cena, 1]
    else:
        dane_lokalizacji[lokalizacja][marka][0] += cena
        dane_lokalizacji[lokalizacja][marka][1] += 1
plik.close()
# 2. Generowanie osobnych plików dla każdej lokalizacji
for lokalizacja, marki in dane_lokalizacji.items():
    wiersze = ["Marka;Suma;Liczba_sztuk;Srednia_cena"]
    for marka, staty in marki.items():
        suma = staty[0]
        ile = staty[1]
        srednia = round(suma / ile, 2)
        wiersze.append(f"{marka};{suma};{ile};{srednia}")
    # Zapis do pliku o nazwie miasta
    sciezka_pliku = os.path.join(folder_wynikowy, f"{lokalizacja}.csv")
    with open(sciezka_pliku, "w", encoding="utf8") as f_out:
        f_out.write("\n".join(wiersze))

print(f"Zakończono! Pliki znajdują się w: {folder_wynikowy}")