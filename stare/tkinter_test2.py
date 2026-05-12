from tkinter import *
import pymysql
connection = pymysql.connect(host='beje.kylos.pl',
                             user='beje_php',
                             password='!Qwe123!@',
                             db='beje_samochody')
cursor = connection.cursor()
sql = "SELECT marka_pojazdu,cena,rocznik from samochody where kolor like 'biały' and rocznik >=2014"
cursor.execute(sql)
result = cursor.fetchall()
column_names = [i[0] for i in cursor.description]

root = Tk()
height = len(result)
width = len(column_names)
for i in range(height): #Rows
    for j in range(width): #Columns

        b = Entry(root)
        b.grid(row=i, column=j)
        a = Label(root, text=result[i][j],
         borderwidth=1)
        a.grid(row=i,column=j)
        
mainloop()
connection.close()
