import this # Easter Egg (ukryta ciekawostka) w Pythonie

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

dlugosc = len(thislist)

print(dlugosc)

thislist.append("jabłko")

print(thislist)
thislist.insert(2, "gruszka")
thislist.remove("gruszka")

thislist.pop(3)

del thislist[0]
print(thislist)

#del thislist
thislist.clear()
thislist = []

lista1 = ["biały","czerwony"]

lista2  = lista1

lista3 = lista1.copy()

lista1.append("czarny")
print(lista3)


print(lista2)

lista=["ala","ma",3,"koty"]
krotka=("koty","jedzą","karmę")

lista.append(krotka)

print(lista)

lista.extend(krotka)

print(lista)


while "banan" in lista:
        lista.remove("banan")



auta = [["audi", "czerwony", 153000],["kia", "biały", 40000]]
for x in auta:
   print(x[1])

tekst = "Ala ma kota"

print(tekst[0:5])

print(tekst[-3])

print(tekst.upper())

print(tekst.title())