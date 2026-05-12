x = 5
y = 6

# for a in range(x):
#     for b in range(y):
#         if a == 4 or b ==3:
#             continue
#         print(a*b)

# a,b = 0,0
# while a < x:
#     a += 1
#     while b < y:
#         b += 1
#         print(a*b)
             

# licznik = 0 
# while licznik < 5: 
#    print(f"Licznik wynosi: {licznik}") 
#    licznik += 1 # Ważne: musimy zmieniać warunek, by uniknąć pętli nieskończonej!

# n = input("Please enter 'hello':")
# while n != 'hello':
#     n = input("Please enter 'hello':")

# while True:
#     n = input("Please enter 'hello':")
#     if n == 'hello':
#         break


# for i in range(10): 
#    if i == 3: 
#       continue # Pominie liczbę 3 
#    if i == 8: 
#        break # Zatrzyma pętlę na liczbie 8 
#    print(i)

# cars = ['audi','bmw','skoda','kia']
# szukane = "honda"

# for auto in cars:
#     if auto == szukane:
#         print(f"Znaleziono: {auto}!")
#         break  # Przerywamy pętlę - blok ELSE się nie wykona
# else:
#     # Ten kod uruchomi się TYLKO, gdy pętla przejdzie całą listę i nie trafi na 'break'
#     print(f"Niestety, {szukane} nie ma na liście.")

poziom_paliwa = 3
cel = "Warszawa"

while poziom_paliwa > 0:
    print(f"Jadę dalej do: {cel}. Paliwo: {poziom_paliwa}")
    poziom_paliwa -= 1
    
    # Symulacja awarii
    # if awaria: break  <-- gdyby to nastąpiło, ELSE się nie wykona
else:
    print("Dojechano na miejsce lub bak jest pusty. Koniec podróży.")