file = open("d:\Documents\Szkolenia\Python\cwiczenia\plik.txt","rt")
#print(file.read())

##zawartosc = file.read()
##print(zawartosc)

##print(file.readline())
##print(file.readlines())
wiersz = file.readline()
while wiersz:
       print(wiersz.strip())
       wiersz = file.readline()

       
##for line in file: 
##  print(line)

##import codecs
##f = codecs.open('d:\Documents\Szkolenia\Python\cwiczenia\plik.txt', encoding='utf-8')
##print(f.read())
##for line in f:
##    print(line)

## [subcode]
file = open("d:\Documents\Szkolenia\Python\cwiczenia\plik2.txt", "w")
file.write("Zosia ma kotka.")
file.close()
 

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
