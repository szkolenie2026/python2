from prettytable import PrettyTable
import pymysql

# connection = pymysql.connect(host='beje.kylos.pl',
#                              user='beje_php',
#                              password='!Qwe123!@',
#                              db='beje_samochody')
connection = pymysql.connect(host='beje.kylos.pl',
                             user='beje_php',
                             password='!Qwe123!@',
                             db='beje_samochody',
                             charset='utf8mb4')
cursor = connection.cursor()
sql = "SELECT marka_pojazdu,cena,rocznik from samochody where kolor like 'biały' and rocznik >=2014"
cursor.execute(sql)
result = cursor.fetchall()
column_names = cursor.description
column_names = [i[0] for i in cursor.description]

x = PrettyTable(column_names)

for row in result:
    x.add_row(row)
print(x)

connection.close()




