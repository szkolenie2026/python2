from lista_firmy_analiza import ladna_tabela
import pliki_funkcje as plik
import kwiatki_oferta as kwiatki

tabelka = ladna_tabela(kwiatki.oferta).get_string()

plik.zapisz_nowy_plik(r'D:\Documents\Szkolenia\Python\cwiczenia\oferta_handlowa.csv', tabelka)

print(plik.odczytaj_plik("D:\\Documents\\Szkolenia\\Python\\cwiczenia\\oferta_handlowa.csv"))

