from tkinter import *
from tkinter import messagebox

master = Tk()
master.title("Pojazdy")
# master.iconbitmap("ikona_pojazdu.ico")
master.configure(bg="#f0f0f0")
master.geometry("300x230")

# Definiujemy styl odstępów w jednej zmiennej
M_GORNY = (20, 4)  #krotka
M_ZWYKLY = 4
M_X = 20
SZEROKOSC = 16
#lub
# Definiujemy wspólny styl dla etykiet
# styl_label = {
#     "sticky": "e",
#     "padx": 10,
#     "pady": (20, 5)
# }

# # Używamy ** aby "wstrzyknąć" wszystkie te parametry na raz
# Label(master, text="Nazwa pojazdu:").grid(row=0, column=0, **styl_label)

# pady=(20, 5) -> 20 pikseli od góry, 5 pikseli od dołu
#1 wiersz
Label(master, text="Nazwa pojazdu:").grid(row=0, column=0, sticky="e", padx=M_X, pady=M_GORNY) #e - east, n,s,w, lub ew
nazwa = Entry(master,width=SZEROKOSC)
nazwa.grid(row=0, column=1, pady=M_GORNY,sticky="w")
# To najpierw tworzysz Entry, potem go ustawiasz w oknie, a na koniec do zmiennej nazwa przypisujesz wynik działania .grid(), czyli None.
# Musisz rozbić tworzenie widżetu i jego układanie na dwie osobne linie
#2 wiersz: CENA
Label(master, text="Cena:").grid(row=1, sticky="e", padx=M_X, pady=M_ZWYKLY)
cena = Entry(master,width=SZEROKOSC)
cena.grid(row=1, column=1, pady=M_ZWYKLY,sticky="w")

#5 lista rozwijana
opcje_kolorow = ["Czerwony", "Niebieski", "Czarny", "Srebrny", "Biały"]
wybrany_kolor = StringVar(master)
wybrany_kolor.set(opcje_kolorow[0]) # Ustawienie domyślnej wartości
Label(master, text="Kolor:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=M_X, pady=M_ZWYKLY)
dropdown = OptionMenu(master, wybrany_kolor, *opcje_kolorow)
dropdown.config(width=SZEROKOSC-6) # Żeby pasowało szerokością do Entry
dropdown.grid(row=2, column=1, sticky="w", pady=M_ZWYKLY)


#6 radiobuttons
stan_pojazdu = IntVar()
stan_pojazdu.set(1)
Label(master, text="Stan:").grid(row=3, column=0, sticky="e", padx=M_X)
# Ramka pomocnicza, żeby stały obok siebie
frame_radio = Frame(master, bg="#f0f0f0")
frame_radio.grid(row=3, column=1, sticky="w")
Radiobutton(frame_radio, text="Nowy", variable=stan_pojazdu, value=1).pack(side=LEFT)
Radiobutton(frame_radio, text="Używany", variable=stan_pojazdu, value=2).pack(side=LEFT)

#7 checkbox
klima_var = IntVar()
Label(master, text="Dodatki:", bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=20)
c1 = Checkbutton(master, text="Klimatyzacja", variable=klima_var)
c1.grid(row=4, column=1, sticky="w")

#4 metody obsługi kliknięcia
def callback_ok():
    # Pobieramy tekst z pól
    nazwa_str = nazwa.get()
    cena_str = cena.get()
    kolor_str = wybrany_kolor.get()
    if stan_pojazdu.get() == 1:
        stan_str = "Nowy"
    else:
        stan_str = "Używany"
    if klima_var.get() == 1:
        dodatki = "Klimatyzacja"
    else:
        dodatki = "brak"

    # Prosta walidacja danych
    if not nazwa_str or not cena_str:
        messagebox.showwarning("Błąd", "Wypełnij wszystkie pola!")
        return
    cena_float = float(cena_str.replace(",", "."))
    print(f"Kupimy pojazd: {nazwa_str}, Cena: {cena_float} PLN, w kolorze: {kolor_str}, stan: {stan_str}, dodatki: {dodatki}")
    nazwa.delete(0, END)
    cena.delete(0, END)
    nazwa.focus_set()

def callback_cancel():
    master.destroy()
#3 - przycisk
btn_ok = Button(master, text = "OK", width = 10, command = callback_ok)
btn_ok.grid(row=5, column=0, pady=20, sticky="e")
btn_cancel = Button(master, text = "Anuluj", width = 10, command = callback_cancel)
btn_cancel.grid(row=5, column=1, padx=M_ZWYKLY, sticky="w")
#obsługa return
master.bind('<Return>', lambda event: callback_ok())
nazwa.focus_set()
master.mainloop()
