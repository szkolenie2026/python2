firmy = {}
firmy["Nazwa firmy"] = ["Firma 1","Firma 2","Firma 3","Firma 4","Firma 5","Firma 6","Firma 7"]
firmy["Kurs akcji wczoraj"] = [16.48, 25.24,57.23,37.92,99.59,94.39,91.56]  
firmy["Kurs akcji dziś"] = [ 16.71,25.64 ,57.11, 38.16, 99.14, 94.52, 91.11  ]
##firmy["Wzrost/Spadek"]=[None,None,None,None,None,None,None]
##firmy["Wartość"]=[None,None,None,None,None,None,None]

from lista_firmy_analiza import ladna_tabela, analiza_akcji2
#lub
#from lista_firmy_analiza import *
import moje_dane as md


##print(ladna_tabela(analiza_akcji2(firmy)))
##
##print(md.pracownik["imię"])
##
##
##print(md.info_o_pracowniku())






from pliki_funkcje import *

print(odczytaj_plik("dane.txt"))


zapisz_nowy_plik("C:\\users\\rpros\\nowe_dane.txt", "Ala ma kota")

dopisz_dane_do_pliku("C:\\users\\rpros\\nowe_dane.txt", "Krzyś ma żabę")








