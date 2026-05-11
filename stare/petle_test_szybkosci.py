import csv
import time
from prettytable import PrettyTable
import openpyxl

def test_wydajnosci_petla():
    nazwa_pliku = 'sprzedaz.csv'
    
    print("1. Rozpoczynam przetwarzanie pliku wiersz po wierszu...")
    start_time = time.time()
    
    # Słownik, w którym będziemy trzymać wyniki dla każdego roku.
    # Struktura: {'2012': {'suma': 0.0, 'liczba': 0}, '2013': ...}
    wyniki_lata = {}

    try:
        # Otwieramy plik w trybie do odczytu
        with open(nazwa_pliku, mode='r', encoding='utf-8') as plik:
            # Używamy wbudowanego czytnika CSV (jest szybszy niż ręczne splitowanie tekstu)
            czytnik = csv.reader(plik, delimiter=';')
            
            # Pomijamy pierwszy wiersz (nagłówki: LP;Data;Kwota;Kod)
            next(czytnik) 
            
            for wiersz in czytnik:
                if len(wiersz) < 4:
                    continue # Pomijamy puste lub uszkodzone linie
                
                # --- A. Wyciąganie roku ---
                # wiersz[1] to np. "05.02.2012 11:00"
                # Zamiast powolnego konwertowania całej daty, używamy wycinania (slicing).
                # Rok zaczyna się na 6 indeksie i ma 4 znaki. To znacznie przyspieszy pętlę!
                rok = wiersz[1][6:10] 
                
                # --- B. Wyciąganie kwoty ---
                # wiersz[2] to np. "3,39"
                # Zamieniamy przecinek na kropkę, aby Python zrozumiał, że to ułamek (float)
                kwota_str = wiersz[2].replace(',', '.')
                kwota = float(kwota_str)
                
                # --- C. Agregacja (Dodawanie do słownika) ---
                if rok not in wyniki_lata:
                    # Jeśli widzimy ten rok po raz pierwszy, tworzymy dla niego miejsce
                    wyniki_lata[rok] = {'suma': 0.0, 'liczba': 0}
                    
                wyniki_lata[rok]['suma'] += kwota
                wyniki_lata[rok]['liczba'] += 1
                
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{nazwa_pliku}'.")
        return

    czas_obliczen = time.time()
    print(f"Przetworzono 3 mln rekordów w: {czas_obliczen - start_time:.2f} sekund.")

    print("\n2. Obliczanie średnich i formatowanie tabeli...")
    
    # Inicjalizacja tabeli do wyświetlania w konsoli
    tabela = PrettyTable()
    tabela.field_names = ["Rok", "Suma Wartości", "Średnia Wartości", "Liczba Rekordów"]
    
    # Lista do przechowania gotowych danych do Excela
    dane_do_zapisu = []
    
    # Przechodzimy po posortowanych latach (aby w konsoli były po kolei, np. od 2010 do 2016)
    posortowane_lata = sorted(wyniki_lata.keys())
    
    for rok in posortowane_lata:
        suma = wyniki_lata[rok]['suma']
        liczba = wyniki_lata[rok]['liczba']
        # Zabezpieczenie przed dzieleniem przez zero (choć u nas liczba będzie min. 1)
        srednia = suma / liczba if liczba > 0 else 0
        
        # Zaokrąglamy do 2 miejsc po przecinku
        suma_zaokr = round(suma, 2)
        srednia_zaokr = round(srednia, 2)
        
        # Przygotowujemy jeden wiersz wyników
        wiersz_wyniku = [rok, suma_zaokr, srednia_zaokr, liczba]
        
        # Dodajemy wiersz do formatowania PrettyTable i do zapisu
        tabela.add_row(wiersz_wyniku)
        dane_do_zapisu.append(wiersz_wyniku)

    # Wyrównanie w PrettyTable
    tabela.align = "r"
    tabela.align["Rok"] = "c"

    # --- WYJŚCIA ---

    print("\nWYNIK W KONSOLI:")
    print(tabela)

    print("\n3. Rozpoczynam zapis plików...")

    # Zapis CSV (PrettyTable)
    with open('podsumowanie_petla.csv', 'w', encoding='utf-8') as f:
        f.write(tabela.get_string())
    print("Zapisano: podsumowanie_petla.csv")

    # Zapis XLSX (Czyste dane przy pomocy openpyxl)
    skoroszyt = openpyxl.Workbook()
    arkusz = skoroszyt.active
    arkusz.title = "Podsumowanie"
    
    # Najpierw dodajemy nagłówki do arkusza Excel
    arkusz.append(["Rok", "Suma Wartości", "Średnia Wartości", "Liczba Rekordów"])
    
    # Następnie dorzucamy nasze wyliczone wiersze
    for wiersz in dane_do_zapisu:
        arkusz.append(wiersz)
        
    skoroszyt.save('podsumowanie_petla.xlsx')
    print("Zapisano: podsumowanie_petla.xlsx")

    czas_koncowy = time.time()
    
    print("\n" + "="*40)
    print("STATYSTYKI CZASOWE (PĘTLA FOR):")
    print(f"- Obliczenia i odczyt: {czas_obliczen - start_time:.2f} s")
    print(f"- Obliczanie średnich i zapis: {czas_koncowy - czas_obliczen:.2f} s")
    print(f"CAŁKOWITY CZAS: {czas_koncowy - start_time:.2f} s")
    print("="*40)

if __name__ == "__main__":
    test_wydajnosci_petla()