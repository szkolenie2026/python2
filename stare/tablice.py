lista = ["ala",3,"koty"]
lista.pop(1)
print(lista)
del lista[1]
print(lista)

lista = list(("ala",3,"koty"))
print("Konstruktor=",lista)


tab = [1 for c in range(5)]
print(tab)

tab = [[0 for col in range(5)] for row in range(10)]
print(tab)


krotka = ("ala",3,"koty")
#krotka[0]="a"

set = {'ala','ma','kota'}

set.add("i żółwia")
set.update(['Kasia','ma','wróbelka'])
print(set)



dict = {"auto1":"KIA", "kolor1":'biały',"rocznik1":2015,
        "auto2":"Opel", "kolor2":'red',"rocznik2":2018}
for x in dict:
  print(dict[x])
  
for x, y in dict.items():
  print(x, y)

cars = ["bmw", "opel", "kia"]
it = iter(cars)
print(next(it))
print(it)

lista_1 = []
# [ ]
 
lista_2 = ["O"]
# ["O"]
lista_1.append(lista_2) 
# [ ["O"] ]
 
lista_1.append( ["A","B","C"] ) 
# [ ["O"], ["A","B","C"] ]
 
lista_1[0].append("P")
# [ ["O", "P"], ["A","B","C"] ]
 
lista_1[1].append( ["X", "Y", "Z"] )
# [ ["O", "P"], ["A","B","C", ["X", "Y", "Z"]] ]

