def odczytaj_plik(nazwa_pliku):
    plik = open(nazwa_pliku)
    zawartosc = plik.read()
    plik.close()
    return zawartosc

def zapisz_nowy_plik(sciezka, tekst):
    plik = open(sciezka, "w")
    plik.write(tekst)
    plik.close()

def dopisz_dane_do_pliku(sciezka, tekst):
    plik = open(sciezka, "a")
    plik.write("\n")
    plik.write(tekst)
    plik.close()
