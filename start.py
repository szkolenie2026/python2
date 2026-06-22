#komunikacja - pol. print
"""
kom
wielolinijkowy


IntelliSense - CTRL spacja
"""

#print("Czesc"    ,   "Rafał")
print("Czesc"    +   "Rafał") # + konkatenacja tekstów
print("*" * 40)

#zmienne
imie = "rafał"
imię = 'rafał'

print("Czesc" , imię)
#typy zmiennych
imie = "rafał" #str
x = 5 #int
y = 5.99 #float
z = False #bool

y = "5.99"
w = 0.1
q     =     x + int(float(y))
print(q)


print("Jestem na szkoleniu." , "Imię: {imię}" , "wartość to: {q}", sep=".")
print("Jestem na szkoleniu." , end=".")
print(f"Imię: {imię}",         end=".") 
print(f"wartość to: {q}")

t1 = "Ala ma kota"
t2 = t1.replace("Ala", "Zuzia").replace("kota", "żółwia")
print(t2)