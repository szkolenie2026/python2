
# #pętla od 0 do 4
# for u in (0,1,2,3,4):
#     print("Krok pętli=", u)

# #zapis równoważny od 0 do 4
# for u in range(5):
#     print("Krok pętli=" + str(u) )

# #zapis równoważny od 0 do 4
# for u in range(0,5):   #step = 1
#     print("Krok pętli=" + str(u) )

# # Od 10 do 18 co dwa
# for i in range(10, 20, 2):  
#    print(f"Numer: {i}") 

#iteracja po tekście
# for litera in "Ala ma kota":  
#     print(litera)

# cars = ['audi','bmw','skoda','kia']

# for car in cars:  #iteracja po liście
#     print( "Pojazd: ", car )


# cars = ['audi','bmw','skoda','kia']

# ile = len(cars)
# for car in range(ile):
#     print("Pojazd nr = ", car, end=" ")
#     print("to: ", cars[car])

# cars = ['audi','bmw','skoda','kia']
# ile = 0

# for car in cars:  #iteracja po liście
#     print("Pojazd nr = ", ile, end=' ')
#     print("to: ", car)
#     ile += 1

# for car in cars:
#     for c in ("biały","czarny","czerwony"):
#         print("Pojazd: ",car, " w kolorze: ",c)


# cars = ['audi','bmw','skoda','kia']

# # start=1 sprawia, że liczenie zacznie się od 1, a nie od 0
# for ile, car in enumerate(cars, start=0):
#     print("Pojazd nr = ", ile, end=' ')
#     print("to: ", car)

# cars = ['audi','bmw','skoda','kia']
# colors = ("biały","czarny","czerwony")
# for car in cars:
#     for color in colors:
#         print("Pojazd: ",car, " dostępny w kolorze: ",color)

# garaz = {
#     "Toyota": "Corolla",
#     "Mazda": "CX-5",
#     "BMW": "M3",
#     "Tesla": "Model S"
# }
# print("--- MOJA KOLEKCJA ---")
# for marka, model in garaz.items():
#     print(f"Marka: {marka} | Model: {model}")
# print("\n--- POSIADANE MARKI ---")
# for marka in garaz.keys():
#     print(f"Mam w garażu samochód marki: {marka}")
for marka in garaz.values():
    print(f"Mam w garażu pojazd: {marka}")

auta_szczegoly = {
    "WA12345": {"marka": "Toyota", "rok": 2020, "przebieg": 50000},
    "KR67890": {"marka": "BMW", "rok": 2018, "przebieg": 120000}
}
for rejestracja, dane in auta_szczegoly.items():
    print(f"Auto o numerze {rejestracja}:")
    # Odwołujemy się do wewnętrznego słownika 'dane'
    marka    = dane["marka"]
    rok      = dane["rok"]
    przebieg = dane["przebieg"]
    print(f"  -> {marka} z roku {rok} ma przebieg: {przebieg}")


# wynik = ""
# pierwszy=""

# for wiersz in range (0,11):
#     wynik =  ""
#     for kolumna in range(1,11):
#         if wiersz == 0:
#             pierwszy += "*" + str(kolumna) + "*"
#         else:
#             if kolumna == 1:
#                 wynik += str(wiersz) + " *" + str(wiersz*kolumna) +"*"
#             else:
#                 wynik += " *" + str(wiersz*kolumna) +"*"

#     if wiersz==0:
#         print(pierwszy)
#     else:
#         #print(wiersz * kolumna)
#         print(wynik)
