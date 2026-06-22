from tkinter import messagebox, simpledialog
# 1. dane
ceny_pln = [45000, 120000, 32500, 89900, 55000]
# 2. Obliczenia podstawowe (zawsze w PLN na początku)
suma_pln = sum(ceny_pln)
srednia_pln = suma_pln / len(ceny_pln)

kurs_do_obliczen = 1
waluta = "PLN"
# 3. Okno z pytaniem (Yes/No)
chce_euro = messagebox.askyesno("Wybór waluty", "Czy chcesz przeliczyć wyniki na Euro?")

if chce_euro:
    kurs = simpledialog.askfloat("Kurs waluty", "Podaj aktualny kurs Euro (np. 4.35):", minvalue=1.0, initialvalue=4.1)
    
    if kurs:  #to samo co kurs is not None
        kurs_do_obliczen = kurs    
        waluta = "EUR"
    else:
        messagebox.showwarning("Błąd", "Nie podano kursu. Przerywam obliczenia.")
        exit()
# Przeliczenia
suma_obliczona = suma_pln / kurs_do_obliczen
srednia_obliczona = srednia_pln / kurs_do_obliczen
# Wyświetlenie wyniku
wiadomosc = f"Suma cen: {suma_obliczona:.2f} {waluta}\n" \
            f"Wartość średnia: {srednia_obliczona:.2f} {waluta}"

if waluta=="EUR":
    wiadomosc += f"\n(Kurs: {kurs})"

messagebox.showinfo("Wyniki", wiadomosc)