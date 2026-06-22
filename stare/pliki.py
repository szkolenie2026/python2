plik = open("d:\Documents\Szkolenia\Python\cwiczenia\dane.csv","rt",encoding="utf8")
marki= {}  #slownik marek pojazdow
next(plik) #pomijamy nagłówki
for  wiersz in plik:
  dane = wiersz.strip().split(";")
  marka = dane[1]
  cena = float(dane[2])
  if marka not in marki:
    marki[marka] = [ cena, 1 ]
  else:
    marki[marka][0] += cena
    marki[marka][1] += 1
plik.close()

for marka in marki:
  suma = marki[marka][0]
  ile = marki[marka][1]
  srednia = round(suma/ile,2)
  marki[marka].append(srednia)

# print(marki)

wiersze = []
wiersze.append("Marka;Suma;Liczba_sztuk;Srednia_cena")
for marka, dane in marki.items():
  suma = str(dane[0])
  ile = str(dane[1])
  srednia = str(dane[2])
  wiersze.append(f'{marka};{suma};{ile};{srednia}')
caly_plik = "\n".join(wiersze)
plik = open("d:\Documents\Szkolenia\Python\cwiczenia\dane_obliczone.csv","w",encoding="utf8")
plik.write(caly_plik)
plik.close()





# plik = open("d:\Documents\Szkolenia\Python\cwiczenia\dane_obliczone.csv","w",encoding="utf8")
# plik.write("Marka;Suma;Liczba_sztuk;Srednia_cena\n")
# for marka, dane in marki.items():
#   suma = str(dane[0])
#   ile = str(dane[1])
#   srednia = str(dane[2])
#   wiersz = f'{marka};{suma};{ile};{srednia}\n'
#   plik.write(wiersz)
# plik.close()

# file = open("d:\Documents\Szkolenia\Python\cwiczenia\stare\plik.txt","rt",encoding="utf8")
# #print(file.read())

# ##zawartosc = file.read()
# ##print(zawartosc)

# ##print(file.readline())
# ##print(file.readlines())
# wiersz = file.readline()
# while wiersz:
#        print(wiersz.strip())
#        wiersz = file.readline()

       
##for line in file: 
##  print(line)

##import codecs
##f = codecs.open('d:\Documents\Szkolenia\Python\cwiczenia\plik.txt', encoding='utf-8')
##print(f.read())
##for line in f:
##    print(line)

## [subcode]
# file = open("d:\Documents\Szkolenia\Python\cwiczenia\stare\plik2.txt", "w")
# file.write("Zosia ma kotka.")
# file.close()
 

##import os
##os.remove("demofile.txt")
##
##import os
##if os.path.exists("plik.txt"):
##  #os.remove("plik.txt")
##else:
##  print("The file does not exist")
##
##import os
##os.rmdir("myfolder")
