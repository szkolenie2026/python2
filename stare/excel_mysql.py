import xlsxwriter

import pymysql

connection = pymysql.connect(host='beje.kylos.pl',
                             user='beje_php',
                             password='!Qwe123!@',
                             database='beje_samochody')
cursor = connection.cursor()
sql = "SELECT marka_pojazdu,cena,rocznik from samochody where kolor like 'biały' or kolor like 'czarny'"
cursor.execute(sql)

result = cursor.fetchall()

print("Ilość rekordów=",len(result))
# column_names = cursor.description
column_names = [i[0] for i in cursor.description]

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook(r'd:\Documents\Szkolenia\Python\cwiczenia\dane.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:C', 20)
bold = workbook.add_format({'bold': True})

for header in range(len(column_names)):
##    worksheet.write('A1'+str(header+1), column_names[header])
    worksheet.write(0,header, column_names[header],bold)

row_index = 1
for row in result:
    column = 0
    for cell in row:
        worksheet.write(row_index, column, cell)
        column += 1
    row_index += 1
    
workbook.close()
connection.close()
