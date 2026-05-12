from tkinter import messagebox


# odpowiedz = messagebox.askyesno("Wyjście", "Czy na pewno chcesz zamknąć program?")
odpowiedz = messagebox.askyesnocancel("Wyjście", "Czy na pewno chcesz zamknąć program?")

if odpowiedz:  # Jeśli True (kliknięto TAK)
    print("wciśnięto tak")
elif odpowiedz is False:      # Jeśli False (kliknięto NIE)
    print("wciśnięto nie")
else:
    print("wciśnięto anuluj")
    

# messagebox.showinfo("Info", "komunikat")
# messagebox.showwarning("warning", "komunikat")
# messagebox.showerror("error", "komunikat")

# odpowiedz = messagebox.askquestion("Wyjście", "Czy na pewno chcesz zamknąć program?")

