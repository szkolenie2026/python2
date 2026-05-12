import pandas as pd

# Odczyt pliku
# df = pd.read_excel('dane.xlsx', usecols="B,C")

# Wyświetlenie pierwszych 5 wierszy
# print(df.head())

# # Po nazwie
# df = pd.read_excel('dane.xlsx', sheet_name='Arkusz2')

# # Po indeksie (pierwszy arkusz)
# df = pd.read_excel('dane.xlsx', sheet_name=0)


# Pobranie konkretnej kolumny:
# nazwy = df['Marka pojazdu'].unique()
# print(nazwy)

# # Filtrowanie danych (np. tylko pojazdy droższe niż 50 000):
# drogie_pojazdy = df[  df['Cena netto'] > 50000  ] 
# print(drogie_pojazdy)

# # Iteracja po wierszach (pętla):
# for index, row in df.iterrows():
#     print(f"Pojazd: {row['Marka pojazdu']}, Cena: {row['Cena netto']}")

wybrany_kolor = "BiAłY"
wybrany_kolor = wybrany_kolor.lower()
kurs_euro = 4.30  
df = pd.read_excel('dane.xlsx', sheet_name=0)

# 2. Filtrujemy dane tylko dla wybranego koloru
df_kolor = df[df['Kolor'].str.lower() == wybrany_kolor].copy()

if df_kolor.empty:
    print(f"Brak pojazdów o kolorze: {wybrany_kolor}")
    exit()
# 3. Przeliczamy cenę na Euro i dodajemy nową kolumnę
df_kolor['Cena EUR'] = (df_kolor['Cena netto'] / kurs_euro).round(2)

# 5. Obliczenia
suma_pln = df_kolor['Cena netto'].sum()
srednia_pln = df_kolor['Cena netto'].mean()
liczba_pojazdow = len(df_kolor)
# 6. Tworzymy słownik
dane_stat = {
        "Opis": ["Liczba pojazdów", "Suma (PLN)", "Średnia (PLN)"],
        "Wartość": [
            liczba_pojazdow, 
            suma_pln, 
            round(srednia_pln, 2)
        ]
    }
df_stat = pd.DataFrame(dane_stat)
df_stat.index = range(1, len(df_stat) + 1)
df_stat.index.name = "Lp"

# 4. Zapisujemy do pliku (tryb 'a' - append, engine 'openpyxl')
# mode='a' pozwala dopisywać arkusze do istniejącego pliku
with pd.ExcelWriter('dane.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    df_kolor.to_excel(writer, sheet_name=f"Raport_{wybrany_kolor}", index=False)
    df_stat.to_excel(writer, sheet_name=f"Raport_{wybrany_kolor}", 
                         index=True, startcol=13, startrow=0)
print(f"Dodano arkusz: Raport_{wybrany_kolor}")