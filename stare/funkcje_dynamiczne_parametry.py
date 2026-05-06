def obliczenia(x,y):
    return x+y

# print( obliczenia(2,3)  )

def obliczenia(x,y,z):
    return x+y+z


def obliczenia(x,y,z = 1):
    return x+y+z


# print(  obliczenia(2,3) )


def oblicz(   *args   ):
    print("Liczba arg wejściowych: ", len(args))
    wynik = 0
    for x in args:
        wynik += x
    print("wynik dodawania = ", wynik)


oblicz(1,2,3,4,6,7,8,9)


def oblicz2 ( x , y ):
    print(x+y)

def oblicz2(  **argumenty ):
    print("Liczba argumentów: ", len(argumenty))

    for klucz, wartość in argumenty.items():
        print("Argument o kluczu: ", klucz," wartość: " , wartość)

oblicz2(y=10, x= 15)


def oblicz2(  *arg, **argumenty_klucz_wartosc ):
    print("Liczba argumentów w krotce arg:  ", len(arg))

    for x in arg:
        print("Argument z krotki: ", x)

    print("Liczba argumentów w słowniku argumenty_klucz_wartosc:  ", len(argumenty_klucz_wartosc))

    for klucz, wartość in argumenty_klucz_wartosc.items():
        print("Argument o kluczu: ", klucz," wartość: " , wartość)


oblicz2(10, 15, [5,10,15], "Ala ma kota", x=10, y=20)





