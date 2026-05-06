
lista = [2,4,6,8]
lista2 = lista.copy()

ktory = 0
for el in lista:
    lista[ktory] += 2
    ktory += 1

print(lista)

print("lista2 = ", lista2)


lista2 = [x + 2 for x in lista2]

print(lista2)

#                <nowa lista> = [<operacja><pętla><warunek>]

lista2 = [x + 10 for x in lista2 if x >= 6]

print(lista2)


def zmien_listę(i):
    if i>=6:
        i += 10
    else:
        i =0
    return i

lista2 = [zmien_listę(x) for x in lista]

print(lista2)

#odwzorowanie list

lista3 = [a for a in range(100)]
print(lista3)

wartość = sum( [a for a in range(10)] )
print(wartość)

wartość = sum( a for a in range(10) )

