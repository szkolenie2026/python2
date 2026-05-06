
import sys

x = 10
try:
    print(x)
except:
    print("pojawił się błąd")

#opcjonalnie
finally:
    print("kończymy wykonanie programu")

#    sys.exit()


try:
    print (10/ z )
except ZeroDivisionError:
    print("nie wolno dzielić przez zero")
except Exception as exp:
    print("Pojawił się nieznany błąd: ", exp)
else:
    print ("all ok!")


try:
    wynik = 10/5
    if wynik <= 4:
        raise Exception("Błąd: Za mała liczba!")

    s = "ala ma kota"

except ZeroDivisionError:
    print("nie wolno dzielić przez zero")
except Exception as exp:
    print("Pojawił się nieznany błąd: ", exp)
else:
    print ("all ok!")


try:
    wynik = "10/5"
    if not type(wynik) is int:
        raise TypeError("Błąd: nie taki jak trzeba typ danych!")
except ZeroDivisionError:
    print("nie wolno dzielić przez zero")
except Exception as exp:
    print("Pojawił się nieznany błąd: ", exp)
else:
    print ("all ok!")


print("czy jest wartość zmiennej?", wynik)


