from prettytable import PrettyTable
from lista_firmy import firmy
def ladna_tabela(dane):
    index = 0
    for row in dane:
        if index == 0:
            x = PrettyTable(dane[row])
        else:
            x.add_row(dane[row])
        index += 1
    return x

# print(ladna_tabela(firmy))

def analiza_akcji2(dane):
    lista = dane["Nazwa firmy"]
    dane["Wzrost/Spadek"] = [None for i in range(len(lista))]
    dane.setdefault("Wartość",[i for i in range(len(lista))])
    
    for index in range(len(lista)):
        akcje_wczoraj = dane["Kurs akcji wczoraj"][index]
        akcje_dzis = dane["Kurs akcji dziś"][index]
        roznica = akcje_dzis - akcje_wczoraj
        tekst = ''
        if akcje_dzis > akcje_wczoraj:
            tekst = 'wzrosło'
        else:
            tekst = 'zmalalo'
        dane["Wzrost/Spadek"][index] = tekst
        dane["Wartość"][index] = round(roznica,2)
    return dane

# print(analiza_akcji2(firmy))

def analiza_akcji(dane):
    lista = firmy["Nazwa firmy"]
    
    for index in range(len(lista)):
        akcje_wczoraj = firmy["Kurs akcji wczoraj"][index]
        akcje_dzis = firmy["Kurs akcji dziś"][index]
        roznica = akcje_dzis - akcje_wczoraj
        tekst = ''
        if akcje_dzis > akcje_wczoraj:
            tekst = 'wzrosło'
        else:
            tekst = 'zmalalo'
        firmy["Wzrost/Spadek"][index] = tekst
        firmy["Wartość"][index] = round(roznica,2)
    return dane


##print(analiza_akcji(firmy))




    

