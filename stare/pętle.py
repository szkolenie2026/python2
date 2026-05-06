

for u in (1,2,3,4,5):
    print("Krok pętli=", u)

for u in range(5):
    print("Iteracja=" + str(u))
## [subcode]

for u in range(1,5):
    print("Iteracja=", u)


for u in range(1,5,2):
    print("Iteracja=", u)

for c in "Ala ma kota":
    print("Znak = ", c)
## [subcode]



cars = ['audi','bmw','skoda','kia']
ile = len(cars)
for car in range(ile):
    print("Pojazd nr = ", car)
    print("to: ", cars[car])



for car in cars:
    for c in ("biały","czarny","czerwony"):
        print("Pojazd: ",car, " w kolorze: ",c)

wynik = ""
pierwszy=""

for wiersz in range (0,11):
    wynik =  ""
    for kolumna in range(1,11):
        if wiersz == 0:
            pierwszy += "*" + str(kolumna) + "*"
        else:
            if kolumna == 1:
                wynik += str(wiersz) + " *" + str(wiersz*kolumna) +"*"
            else:
                wynik += " *" + str(wiersz*kolumna) +"*"

    if wiersz==0:
        print(pierwszy)
    else:
        #print(wiersz * kolumna)
        print(wynik)
