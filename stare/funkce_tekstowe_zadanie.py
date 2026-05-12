#zadanie
tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"

mc = tekst_CSV[0:2]
dzien = tekst_CSV[3:5]
rok = tekst_CSV[6:10]
print( f'rok: {rok}   mc: {mc}   dzien: {dzien}')

imie_nazwisko = tekst_CSV[11:23].title()
print(imie_nazwisko)

pozycja = tekst_CSV.find(":") 
liczba_str = tekst_CSV[pozycja + 2:]
wyplata_EUR = float(liczba_str) / 4.33

print( f'EUR: {wyplata_EUR:,.2f}')





from datetime import datetime

data = tekst_CSV[0:10]
data_obiekt = datetime.strptime(data, '%m/%d/%Y' ) #parsowanie daty
# zmiana tekstu na "prawidłową" datę

data_ladna = data_obiekt.strftime( '%Y-%m-%d')
# zmiana formatu daty na inny - string (tekst)
print(data_ladna)


