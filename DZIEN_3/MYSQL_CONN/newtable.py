import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database='dbtestowa')
cursorObject = db.cursor()

newtable = "CREATE TABLE IF NOT EXISTS student(firstname VARCHAR(50),lastname VARCHAR(50),idstudenta int primary key);"
cursorObject.execute(newtable)

dodajstudenta = "INSERT INTO student(firstname,lastname,idstudenta) VALUES(%s,%s,%s);"
# std1 = ("Jan","Kowalski",4456)
# cursorObject.execute(dodajstudenta,std1)

studenci = [
    ("Anna","Kot",2342),
    ("Olga","Knot",3342),
    ("Tomek","Nowak",2882),
    ("Nadia","Kos",2343),
    ("Paweł","Kot",6342),
]
cursorObject.executemany(dodajstudenta,studenci)

db.commit()
db.close()
