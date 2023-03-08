import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database='dbtestowa')
cursorObject = db.cursor()

ndane = "SELECT idstudenta,firstname,lastname FROM student"
cursorObject.execute(ndane)

wynik = cursorObject.fetchall()
for st in wynik:
    print(st)

print("__________________________________")

sdane = "SELECT idstudenta,firstname,lastname FROM student WHERE firstname like 'Jan';"
cursorObject.execute(sdane)

wynik = cursorObject.fetchall()
for st in wynik:
    print(st)
    

db.close()
