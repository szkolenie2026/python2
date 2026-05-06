import sys
import codecs
import xlsxwriter
# sys.setdefaultencoding('utf-8')
print(sys.stdout.encoding)

file = open("plik.txt","rt")
zawartosc = file.read()
print(zawartosc.encode('UTF-8',errors='strict'))

file.close()


f = codecs.open('plik2.txt', encoding='utf-8')

# print(f.read())
wiersz = f.readline()
while wiersz:
    print(wiersz.strip())
    wiersz = f.readline()
f.close()