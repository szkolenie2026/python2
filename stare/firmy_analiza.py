firmy = {}
firmy["Nazwa firmy"] = ["Firma 1","Firma 2","Firma 3","Firma 4","Firma 5","Firma 6","Firma 7"]
firmy["Kurs akcji wczoraj"] = [16.48,25.24,57.23,37.92,99.59,94.39,91.56]
firmy["Kurs akcji dziś"] = [16.71,25.64,57.11,38.16,99.14,94.52,91.11]
firmy["Wzrost/Spadek"]=[None,None,None,None,None,None,None]
firmy["Wartość"]=[None,None,None,None,None,None,None]
kurs=0
for klucz, wartosc in firmy.items():
    print(klucz + "value: ",wartosc)
for kurs in firmy["Nazwa firmy"]:
    print (kurs)
    wynik = firmy["Kurs akcji wczoraj"][0] - firmy["Kurs akcji dziś"][0]
    if wynik > 0:
        WS = "Wzrost"
    else:
        WS = "Spadek"
    firmy["Wzrost/Spadek"][0] = WS
    firmy["Wartość"][0] = wynik
print(firmy["Nazwa firmy"],"/n",firmy["Kurs akcji wczoraj"],"/n",firmy["Kurs akcji dziś"],"/n",firmy["Wzrost/Spadek"],"/n",firmy["Wartość"])