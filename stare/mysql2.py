import pymysql

connection = pymysql.connect(host='beje.kylos.pl',
                             user='beje_php',
                             password='!Qwe123!@',
                             db='beje_samochody',
                             charset='utf8mb4')

cursor = connection.cursor()


sql = "SELECT marka_pojazdu,cena,rocznik,rodzaj_paliwa from samochody"# where kolor like 'biały'"


cursor.execute(sql)


result = cursor.fetchall()  #fetchone()

print("Ilość rekordów=",len(result))

##for i in cursor.description:
##    print(i)

column_names = cursor.description

column_names = [i[0] for i in cursor.description]
print(column_names)

for row in result:
    print(row)

    #for record in cursor:
    #    print(record[0])
##finally:
connection.close()
