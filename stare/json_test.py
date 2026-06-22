import json

marki_statystyki = {
    "Toyota": {"suma": 150000, "sztuk": 3},
    "BMW": {"suma": 200000, "sztuk": 2}
}

# # Zapis do pliku
# with open("raport.json", "w", encoding="utf-8") as plik:
#     # indent=4 sprawia, że plik jest czytelny dla oka (ładne wcięcia)
#     # ensure_ascii=False pozwala poprawnie zapisywać polskie znaki
#     tekst = json.dumps(marki_statystyki, indent=4, ensure_ascii=False, sort_keys=True)
#     print(tekst)
#     json.dump(marki_statystyki, plik, indent=4, ensure_ascii=False)

with open("raport.json", "r", encoding="utf-8") as plik:
    dane = json.load(plik)

for pojazd in dane:
    suma = dane[pojazd]["suma"]
    ile = dane[pojazd]["sztuk"]
    print(f'Marka: {pojazd} wartość: {suma} sztuki: {ile}') 

marki_statystyki_tekst = '{"Toyota": {"suma": 150000, "sztuk": 3},    "BMW": {"suma": 200000, "sztuk": 2}}'
# Zamieniamy tekst na słownik 
slownik = json.loads(marki_statystyki_tekst)
print(slownik)

# import json

# x =  '{ "name":"Rafał", "color":"black", "city":"Wwa"}'

# y = json.loads(x)

# print(y["color"])