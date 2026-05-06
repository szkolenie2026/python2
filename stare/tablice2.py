tbl = [["audi",33000,"biały"],["ford",50000,"czarny"]]

for dane in tbl:
    #print(dane)
    print("Marka: ", dane[0])
    print("Cena: ", dane[1])
    print("Kolor: ",dane[2])


dict = {"auto1":"KIA", "kolor1":'biały',"rocznik1":2015,
        "auto2":"Opel", "kolor2":'red',"rocznik2":2018}
for x in dict:
    print("Klucz o nazwie: ",x," ma wartość: ", dict[x])
    

tbl = [["audi",33000,"biały"],["ford",50000,"czarny"]]
x = 0
for dane in tbl:
    x += 1
    print("Pojazd ",x," ma parametry:")
    for parametr in dane:
        print(parametr)


txt = ""
for a in range(5):
    for b in range(4):
        txt = txt + " petla głowna " + str(a)
        txt += " petla podrzedna " + str(b) + "\n\n"

print(txt)















