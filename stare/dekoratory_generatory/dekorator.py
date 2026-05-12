# 1. Definicja dekoratora
def moj_dekorator(func):
    # 2. Definicja 'wrappera' (opakowania)
    def wrapper():
        print(f"--- Zaczynam owijać funkcję: {func.__name__} ---")
        func()  # 3. Wywołanie oryginalnego prezentu (funkcji)
        print("--- Skończyłem owijać! ---")
    return wrapper  # Zwracamy gotowe opakowanie z prezentem w środku

# 4. Użycie dekoratora
@moj_dekorator
def zwykla_funkcja():
    print("Działam!")

# Uruchamiamy
zwykla_funkcja()

from datetime import datetime
# 1. Definicja dekoratora
def audyt_funkcji(funkcja):
    def wrapper(*args, **kwargs):
        # --- ZANIM FUNKCJA WYSTARTUJE ---
        czas_startu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nazwa = funkcja.__name__
        print(f"[AUDYT | {czas_startu}] Uruchomiono proces: '{nazwa}'")
        print(f"[AUDYT | SZCZEGÓŁY] Przekazane argumenty: {args}")
        # --- URUCHOMIENIE WŁAŚCIWEJ FUNKCJI ---
        wynik = funkcja(*args, **kwargs)
        # --- PO ZAKOŃCZENIU FUNKCJI ---
        print(f"[AUDYT] Proces '{nazwa}' zakończył pracę pomyślnie.\n")
        return wynik
    return wrapper
logi_systemowe = [
    "   INFO: System wystartował pomyślnie ",
    "ERROR: brak pliku config.json   ",
    " WARNING: Mało miejsca na dysku",
    "  ERROR: utrata połączenia z bazą danych "
]
# 2. Nałożenie dekoratora na funkcję biznesową
@audyt_funkcji
def wydobadz_bledy_krytyczne(dane):
    return (linia.split(":")[1].strip().upper() for linia in dane if "ERROR" in linia)
# 3. Uruchomienie programu
generator_wynikowy = wydobadz_bledy_krytyczne(logi_systemowe)
# Wyświetlenie wyników z generatora
print("ZWRÓCONE DANE: ", list(generator_wynikowy))
