print("Hi")
#wyświetlimy tekst
print("Wspisałem komentarz")
#shift+f10
"""
komentarz wielolinijkowy
w kilku wierszach
"""


txt = "Jaki ładny dzisiaj dzień"
print(txt)

print("Ala ", "ma ", "kota.")
print("Ala\nma\nkota")
print("Ala\tma\tkota")

#obliczenia
print("wynik 100+10=", 100+10  )

#obliczenia z tekstu
print( eval('100+10'))
print("Mam na imię 'Rafał'")
print('Mam na imię "Rafał"')

print("Ala",
      "ma",
      "kota..."

      )

print (  type("ala")     )
print (  type(123)     )
print (  type(123.12)     )
print (  type(True)     )
print ( "ala ma "
        ""
        ""
        "kota")

imię = input("cZEŚĆ. podaj swoje imię:")
print("Witaj " + imię)



#Zmienna
x = "sierpień"
print(x)
x = 12
print(x + 10)
b = "Ala"
x = b
print(x)

x = 10
x *= 5
print(x)
#print x
print(R"znak specjalny \n")

print(U"ółćś")
a = "Ala"
b=" ma"
c = " kota"
print( a+b+c)


print(a * 5)

wiek = input("Podaj swój wiek:")

print("Urodziłeś się w roku: 19" + wiek)

szerokosc = input("podaj szerokość")
dlugosc = input("podaj dlugosc")

print("Powierzchnia = " + str(int(szerokosc) * int(dlugosc))  )

x = 10.99
y = "ala"
z = True
b = None

Auto = input("Podaj markę:")
if Auto == "Opel":
    Rabat = "15%"
elif Auto =="Skoda":
    Rabat = "18%"
elif Auto =="Audi":
    Rabat = "20%"
else:
    Rabat = "5%"
print("Rabat wynosi: " + Rabat)


Auto = input("Podaj markę:")
if Auto == "Opel":
    print("15%")
elif Auto =="Skoda":
    print("18%")
elif Auto =="Audi":
    print("20%")
else:
    print("5%")
print(Rabat)













