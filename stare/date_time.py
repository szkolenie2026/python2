from datetime import datetime, date, timedelta

# 1. Pobranie aktualnego czasu
teraz = datetime.now()
print(f"Teraz jest: {teraz}")

# 2. Tworzenie konkretnej daty
urodziny = date(1995, 10, 25)
print(f"Urodziny: {urodziny}")

# 3. Arytmetyka dat (timedelta)
# Co będzie za 100 dni?
przyszlosc = teraz + timedelta(days=100)
print(f"Za 100 dni będzie: {przyszlosc.date()}")

# 4. Odejmowanie dat
teraz = date.today()
#lub 
teraz = datetime.now().date()
wynik_dni = (teraz - urodziny).days
print("Dni, które minęły: " , wynik_dni)

dzisiaj = datetime.now()

print(f"Rok: {dzisiaj.year}")          # np. 2026
print(f"Miesiąc: {dzisiaj.month}")     # np. 5
print(f"Dzień: {dzisiaj.day}")         # np. 11
print(f"Godzina: {dzisiaj.hour}")      # np. 22
print(f"Dzień tygodnia: {dzisiaj.weekday()}") # 0 = Poniedziałek, 6 = Niedziela

# Dodawanie czasu
za_tydzien = dzisiaj + timedelta(weeks=1)
za_30_dni = dzisiaj + timedelta(days=30)
godzina_pozniej = dzisiaj + timedelta(hours=1)

# Odejmowanie czasu
wczoraj = dzisiaj - timedelta(days=1)

# 5. Porównywanie dat
termin_platnosci = date(2026, 5, 20)

if date.today() > termin_platnosci:
    print("ALARM: Termin minął!")
else:
    print("Masz jeszcze czas.")

# now.strftime("%Y-%m-%d") # 2026-05-11 (Standard ISO)
# now.strftime("%d/%m/%y") # 11/05/26 (Krótki format)
# now.strftime("%A") # Monday (Nazwa dnia tygodnia)
#Jeśli chcesz, aby nazwy dni tygodnia były po polsku, najprościej jest stworzyć własną listę:
dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Niedz"] 
print(  dni[dzisiaj.weekday()]  )

# Obiekt -> Tekst
ladna_data = teraz.strftime("%d.%m.%y %H:%M")
print(f"Format europejski: {ladna_data}") 
# Wynik: 11.05.2026 21:59

# Tekst -> Obiekt
data_z_pliku = "2026-12-31"
obiekt_daty = datetime.strptime(data_z_pliku, "%Y-%m-%d")