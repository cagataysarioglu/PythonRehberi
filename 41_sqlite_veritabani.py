import sqlite3

baglanti = sqlite3.connect("chinook.db")
imlec = baglanti.cursor()

imlec.execute("SELECT * FROM customers")
islem = imlec.fetchall()

for i in islem:
    print(i)

baglanti.close()
