import time
# 1. Definicja dekoratora
def stoper(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        
        # Wywołanie oryginalnej funkcji
        wynik = funkcja(*args, **kwargs) 
        
        koniec = time.time()
        print(f"Funkcja '{funkcja.__name__}' wykonała się w {koniec - start:.4f} sekund.")
        return wynik
        
    return wrapper
# 2. Użycie dekoratora
@stoper
def policz_do_miliona():
    suma = 0
    for i in range(1_000_000):
        suma += i
    return suma

# Wywołanie funkcji (dekorator uruchomi się automatycznie!)
policz_do_miliona()