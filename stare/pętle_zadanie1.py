from tkinter import messagebox

firmy = ["Firma 1","Firma 2","Firma 3","Firma 4","Firma 5","Firma 6","Firma 7"]
Kurs_akcji_wczoraj = [16.48, 25.24,57.23,37.92,99.59,94.39,91.56]  
Kurs_akcji_dzis    = [16.71,25.64 ,57.11, 38.16, 99.14, 94.52, 91.11]

komunikat_do_mb = ''
ile = len(firmy)
for x in range(ile):
    firma = firmy[x]
    kurs_w = Kurs_akcji_wczoraj[x]
    kurs_d = Kurs_akcji_dzis[x]
    wynik = round(  kurs_d - kurs_w  , 2)
    if wynik<0:
        tekst = 'spadł'
    else:
        tekst = 'wzrósł'
    komunikat = f'Firma: {firma}, kurs akcji {tekst} o {wynik}'
    print( komunikat  )
    komunikat_do_mb += komunikat + '\n'
    
messagebox.showinfo('Informacja', komunikat_do_mb)
