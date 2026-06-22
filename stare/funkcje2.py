import funkcje_zewnętrzne as ff

import narzędzia
# Używamy funkcji z modułu narzędzia
tekst = narzedzia.powitanie("Marek")
podatek = narzedzia.oblicz_podatek(1000)
print(tekst)      # Wynik: Witaj Marek! Miłego programowania.
print(podatek)    # Wynik: 230.0



abc = None



def oblicz_brutto():
    print(100 * 1.23)


oblicz_brutto()

def oblicz_brutto2(netto, vat):
    wynik = netto*vat + netto
    print("Obliczenie = ", wynik)


oblicz_brutto2(100, 0.23)


def oblicz_brutto3(netto, vat):
    wynik = netto*vat + netto
    return wynik

print (    oblicz_brutto3(200, 0.23)    )


pomoc = oblicz_brutto3(200, 0.23)

print(pomoc)


def temperatura(stopnie):
    if stopnie > 30:
        return "gorąco"
    elif stopnie>20:
        return "w miarę"
    elif stopnie > 10:
        return "ok"
    else:
        "super"


print( temperatura(30) )

wynik = "Ala ma kota"


def temperatura2(stopnie):
    global wynik
    print ( wynik)
    if stopnie > 30:
        wynik =  "gorąco"
    elif stopnie>20:
        wynik =  "w miarę"
    elif stopnie > 10:
        wynik =  "ok"
    else:
        wynik = "super"
    return "Po zbadaniu temp., stwierdzamy, że jest: " + wynik

print ( temperatura2(20) )



print ( temperatura2(20) )


x = 10

def obliczenia():
    x = 5
    print("zmienna lokalna x = ", x)

obliczenia()
print("zmienna globalna x = ", x)



def  oblicz_brutto4(netto, vat = 0.23):
    wynik = netto * vat + netto
    return wynik

print ( oblicz_brutto4(500, 0.08))
print ( oblicz_brutto4(500) )

print( oblicz_brutto4(vat = 0.05,   netto = 1000)       )




def funkcja_coś_robi():
    x = (2+2)   *   2
    return x


print(funkcja_coś_robi())





tekst = ff.powitanie("Rafał")

print(tekst)











