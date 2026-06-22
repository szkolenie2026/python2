from tkinter import simpledialog

# minvalue i maxvalue automatycznie pilnują zakresu danych
# initialvalue - wartość domyślna
# askfloat – Pobieranie liczb z przecinkiem
kurs = simpledialog.askfloat("Waluta", "Podaj kurs Euro:                                    ", minvalue=1.0, maxvalue=10.0, initialvalue=4)
# askinteger – Pobieranie liczb całkowitych
# wiek = simpledialog.askinteger("Wiek", "Ile masz lat?", minvalue=0, maxvalue=120)
# # askstring – Pobieranie tekstu
# imie = simpledialog.askstring("Dane", "Jak masz na imię?")

if kurs is not None:
    print(f"Użytkownik podał kurs: {kurs}")