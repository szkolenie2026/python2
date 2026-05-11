def oblicz_brutto(netto):
    wynik = netto * 1.23
    return wynik
#koniec funkcji

##print(oblicz_brutto(100)) #wywołanie funkcji



def oblicz_brutto2(netto, vat=0.23):
    wynik = netto * vat + netto
    return wynik

##print(oblicz_brutto2(100))
##print(oblicz_brutto2(100, 0.08))
##print(oblicz_brutto2(vat=0.19, netto=100))


def jakie_wakacje(kwota):
    if kwota > 10000:
        return "wypasione"
    elif kwota > 5000:
        return "super"
    elif kwota > 1000:
        return "też fajne"
    else:
        return "ważne, że będzie wolne"

##print(jakie_wakacje(5600))

def jakie_wakacje2(kwota):
    txt = ""
    if kwota > 10000:
        txt = "wypasione"
    elif kwota > 5000:
        txt =  "super"
    elif kwota > 1000:
        txt = "też fajne"
    else:
        txt = "ważne, że będzie wolne"
    return "Moje wakacje będą: " + txt

a="asa"






def pokaz_najwieksza(n1,n2,n3,n4):
    lista = [n1,n2,n3,n4]
    najwieksza = max(lista)
    return najwieksza

print(pokaz_najwieksza(10,20,30,15))



def pokaz_najwieksza2(*args):
    najwieksza = max(args)
    return najwieksza

print(pokaz_najwieksza2(10,20,30,15,55,10))

##{
##    "Średnia:": 123,
##    "MAx:": 200,
##    "Min": 30,
##    "Sum": 300
##    }

def oblicz_agregaty(*dane):
    minimum = min(dane)
    maximum = max(dane)
    ilosc = len(dane)
    srednia = sum(dane)/ilosc
    suma = sum(dane)
    
    wynik = {
    "Średnia:": srednia,
    "Max:": maximum,
    "Min": minimum,
    "Sum": suma,
    "Ilość:": ilosc
        }
    return wynik

print(oblicz_agregaty(10,20,30,40,50,60,70,80,90,100))




def oblicz_agregaty2(**dane):
    for d in dane:
        print(d, dane[d])

oblicz_agregaty2(n0=30,n1=10,n2=20)

def oblicz_agregaty2(**dane):
    wynik = ""
    for d in dane:
        wynik += f"{d} {dane[d]}\n"
    return wynik.strip() # Zwracamy tekst zamiast go drukować wewnątrz

print(oblicz_agregaty2(n0=30, n1=10, n2=20))