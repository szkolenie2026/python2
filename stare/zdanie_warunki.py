cena = 100000

pojazd = input("podaj markę pojazdu: ").lower()

#1 sposób
if pojazd == "":
   print("Nie podano marki pojazdu!")
else:
    if pojazd == "opel":
        rabat = 0.15
    elif pojazd == "skoda":
        rabat = 0.18
    elif pojazd in "audi":
        rabat = 0.20
    else:
        rabat = 0.05

    cena_po_rabacie = round( cena * (1-rabat), 2)
    print("Cena po rabacie: ", cena_po_rabacie)
#2 sposób
if pojazd == "":
   print("Nie podano marki pojazdu!")
   exit()

if pojazd == "opel":
    rabat = 0.15
elif pojazd == "skoda":
    rabat = 0.18
elif pojazd in "audi":
    rabat = 0.20
else:
    rabat = 0.05

cena_po_rabacie = round( cena * (1-rabat), 2)
print("Cena po rabacie: ", round(cena_po_rabacie , 2)   )