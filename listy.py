tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"
lista_z_tekstu = tekst_CSV.split()

print(lista_z_tekstu)

lista_z_tekstu.append( [100000, 150000] )
print(lista_z_tekstu)
print("*" * 50)
lista_z_tekstu.extend( [10000, 15000])
print(lista_z_tekstu)
