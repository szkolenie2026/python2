a = [[1, 2, 3], [4, 5, 6]]
print(a[0][1]);

# komentarz z języku Python
msg = "Hello World"
print(msg)
# kolejny komentarz

"""
wielolinijkowy
komentarz
"""
print('Taki sam',"'komunikat'", "jak przedtem,")
print("\ttylko",
"nieco",
"większy." + " konkatenacja")
print(  """Ala
ma
kota
""")
print("a"*10)
print("100+10=",100+10)



varA, varB, varC = 4, 14, 'kawa'


x = 1
print(eval('x + 1'))
#name = input("Cześć. Jak masz na imię? ")
#print(name)

print(type("tekst"))

print(type(10.5))

lista = ["ala",3,"koty"]
print(lista[0])
lista[0]="Krysia"
print(lista[0])

krotka = ("ala",3,"koty")
#krotka[0] = "Zosia"
print(krotka[0])

słownik = {"audi":"czerwony","bmw":"zielony","skoda":"biały"}
słownik["audi"]
#słownik[0]     błąd!
print(słownik.keys())
print(list(słownik.keys()))
print(słownik.values())
print("bmw" in słownik)


x = 10
x is 10 
#true
x is not 13 
#True
x is '10' 
#False
x in [ 1, 12, 10 ] 
#True
x in [ 1, 12, 'txt' ] 
#False
x not in [ 1, 12, 'txt' ] 
#True
'str' is 'str' 
#True
'str' is 'string' 
#False
'str' in 'string'
#true

if x==12:
    print ("jest 12")
else:
    if x==10:
        print("jest 10")
    else:
        print("inne niz 10")


input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
