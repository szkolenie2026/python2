try:
    plik = open("dane.txt", "r")
except FileNotFoundError:
    print("Nie znaleziono pliku!")
finally:
    print("Kończenie operacji...") 
    # Tutaj zwykle zamykamy połączenia lub pliki