logi = [
    "   INFO: System wystartował pomyślnie ",
    "ERROR: brak pliku config.json   ",
    " WARNING: Mało miejsca na dysku",
    "  ERROR: utrata połączenia z bazą danych "
]

# Wyrażenie generatorowe z filtrem
generator_bledow = (linia.split(":")[1].strip().upper() for linia in logi if "ERROR" in linia)
print(generator_bledow)

# Wymuszenie wszystkiego na raz (Zamiana na listę)
print(list(generator_bledow))
# Wyciąganie po jednym w pętli 
for blad in generator_bledow:
    print(blad)
# Ręczne pobieranie pojedynczych elementów (Funkcja next)
pierwszy = next(generator_bledow)
print(pierwszy)