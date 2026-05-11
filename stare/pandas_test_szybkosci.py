import pandas as pd
import time
from prettytable import PrettyTable

def test_wydajnosci():
    nazwa_pliku = 'sprzedaz.csv'
    
    print("1. Wczytywanie 3 mln rekordów...")
    start_time = time.time()

    # Wczytanie zgodnie ze strukturą ze zdjęcia (średnik i przecinek)
    try:
        df = pd.read_csv(nazwa_pliku, sep=';', decimal=',')
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{nazwa_pliku}'.")
        return

    czas_wczytania = time.time()
    
    # 2. Obliczenia
    print("2. Przetwarzanie danych...")
    # Wyciągamy rok
    df['Rok'] = pd.to_datetime(df['Data transakcji'], format='%d.%m.%Y %H:%M').dt.year

    # Agregacja
    wynik = df.groupby('Rok').agg(
        Suma_Wartosci=('Kwota transakcji', 'sum'),
        Srednia_Wartosci=('Kwota transakcji', 'mean'),
        Liczba_Rekordow=('Kwota transakcji', 'count')
    ).reset_index()

    # Zaokrąglenia
    wynik = wynik.round(2)
    czas_obliczen = time.time()

    # 3. Przygotowanie PrettyTable
    tabela = PrettyTable()
    tabela.field_names = ["Rok", "Suma Wartości", "Średnia Wartości", "Liczba Rekordów"]
    tabela.add_rows(wynik.values.tolist())
    
    # Wyrównanie dla estetyki
    tabela.align = "r"
    tabela.align["Rok"] = "c"

    # --- WYJŚCIA ---

    # A. Konsola (Pretty)
    print("\nWYNIK W KONSOLI:")
    print(tabela)

    # B. Zapis "Pretty" do pliku CSV
    # Zapisujemy sformatowany tekst tabeli do pliku .csv
    with open('podsumowanie_sprzedazy.csv', 'w', encoding='utf-8') as f:
        f.write(tabela.get_string())
    print("\n3. Zapisano sformatowaną tabelę (Pretty) do: podsumowanie_sprzedazy.csv")

    # C. Zapis danych do XLSX
    wynik.to_excel('podsumowanie_sprzedazy.xlsx', index=False)
    print("4. Zapisano czyste dane do: podsumowanie_sprzedazy.xlsx")

    czas_koncowy = time.time()
    
    print(f"\nSTATYSTYKI CZASOWE:")
    print(f"- Wczytywanie: {czas_wczytania - start_time:.2f} s")
    print(f"- Obliczenia: {czas_obliczen - czas_wczytania:.2f} s")
    print(f"- Zapis i wyświetlanie: {czas_koncowy - czas_obliczen:.2f} s")
    print(f"Razem: {czas_koncowy - start_time:.2f} s")

if __name__ == "__main__": # Ten kod wykona się TYLKO, gdy uruchomimy ten plik bezpośrednio
    test_wydajnosci()