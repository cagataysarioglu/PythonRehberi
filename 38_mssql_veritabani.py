import pypyodbc

# def urunEkle(ad, yazar, yayin, baski, tur):
#     baglanti = pypyodbc.connect(
#         "Driver={SQL Server};"
#         "Server=HCS;"
#         "Database=Kitabevi_VT;"
#         "Trusted_Connection=True;"
#     )
#     imlec = baglanti.cursor()

#     sql = "INSERT INTO dbo.Kitaplar(Ad, Yazar, Yayin, Baski, Tur) VALUES (?, ?, ?, ?, ?)"
#     degerler = (ad, yazar, yayin, baski, tur)

#     imlec.execute(sql, degerler)
#     try:
#         baglanti.commit()
#         print(f"{imlec.rowcount} adet kayıt eklendi.")
#     except pypyodbc.Error as hata:
#         print("Bir hata oluştu: ", hata)
#     finally:
#         baglanti.close()
#         print("Veritabanı bağlantısı kapandı.")

# def urunleriEkle(liste):
#     baglanti = pypyodbc.connect(
#         "Driver={SQL Server};"
#         "Server=HCS;"
#         "Database=Kitabevi_VT;"
#         "Trusted_Connection=True;"
#     )
#     imlec = baglanti.cursor()

#     sql = "INSERT INTO dbo.Kitaplar(Ad, Yazar, Yayin, Baski, Tur) VALUES (?, ?, ?, ?, ?)"
#     degerler = liste

#     imlec.executemany(sql, degerler)
#     try:
#         baglanti.commit()
#         print(f"{len(liste)} adet kitap kaydedildi.")
#     except pypyodbc.Error as hata:
#         print("Bir hata oluştu: ", hata)
#     finally:
#         baglanti.close()
#         print("Veritabanı bağlantısı kapandı.")

# liste = []
# while True:
#     ad = input("Kitabın adı: ")
#     yazar = input("Kitabın yazarı: ")
#     yayin = input("Yayıncı: ")
#     baski = input("Kaçıncı baskı: ")
#     tur = input("Kitabın türü: ")

#     liste.append((ad, yazar, yayin, baski, tur))

#     sonuc = input("Ekleme işlemini sürdürmek istiyor musunuz? (E/H): ")
#     if sonuc == "h":
#         print("Kayıtlarınız veritabanına aktarılıyor.")
#         print(liste)
#         urunleriEkle(liste)
#         break

# urunEkle(ad, yazar, yayin, baski, tur)

def urunleriGetir():
    baglanti = pypyodbc.connect(
        "Driver={SQL Server};"
        "Server=HCS;"
        "Database=Kitabevi_VT;"
        "Trusted_Connection=True;"
    )
    imlec = baglanti.cursor()

    # imlec.execute("SELECT * FROM Urunler")
    imlec.execute("SELECT Ad, Yazar, Yayin FROM dbo.Kitaplar") # "SELECT * FROM Urunler WHERE ID=3" biçiminde filtrelenebilir.
    
    islem = imlec.fetchall() # fetchone() olur ise döngüye gerek kalmaz.

    for urun in islem:
        # print(f"Ürünün adı: {urun[1]} - Fiyatı: {urun[2]}")
        print(f"Kitabın adı: {urun[0]} - Yazarı: {urun[1]} - Yayıncısı: {urun[2]}")

urunleriGetir()

def kimligeGoreUrunGetir():
    baglanti = pypyodbc.connect(host = "localhost", user = "root", password = "mysqlparola", database = "urunler_veritabani")
    imlec = baglanti.cursor()

    sql = "SELECT * FROM Urunler WHERE ID=%s" # "SELECT * FROM Urunler ORDER BY Ad, Fiyat"
    params = (id,)

    imlec.execute(sql, params)
    sonuc = imlec.fetchone()
    print(sonuc)

# kimligeGoreUrunGetir(3)

def urunBilgisiniGetir():
    baglanti = pypyodbc.connect(host = "localhost", user = "root", password = "mysqlparola", database = "urunler_veritabani")
    imlec = baglanti.cursor()

    # sql = "SELECT COUNT(*) FROM Urunler WHERE Fiyat > 3000"
    # sql = "SELECT COUNT(Ad) FROM Urunler"
    # sql = "SELECT AVG(Fiyat) FROM Urunler"
    # sql = "SELECT SUM(Fiyat) FROM Urunler"
    # sql = "SELECT MIN(Fiyat) FROM Urunler"
    # sql = "SELECT MAX(Fiyat) FROM Urunler"
    sql = "SELECT Ad FROM Urunler WHERE Fiyat = (SELECT MAX(Fiyat) FROM Urunler)" # En pahalı ürünün ad bilgisi istendi.

    imlec.execute(sql)
    sonuc = imlec.fetchone()
    print(f"Sonuç: {sonuc[0]}")

# urunBilgisiniGetir()

def urunuGuncelle(ad, yazar, yayin, tur, id):
    baglanti = pypyodbc.connect(
        "Driver={SQL Server};"
        "Server=HCS;"
        "Database=Kitabevi_VT;"
        "Trusted_Connection=True;"
    )
    imlec = baglanti.cursor()

    sql = "UPDATE dbo.Kitaplar SET Ad = ?, Yazar = ?, Yayin = ?, Tur = ?  WHERE Id = ?"
    degerler = (ad, yazar, yayin, tur, id)
    imlec.execute(sql, degerler)
    try:
        baglanti.commit()
        print(f"{imlec.rowcount} kayıt güncellendi.")
    except pypyodbc.Error as hata:
        print("Bir hata oluştu: ", hata)
    finally:
        baglanti.close()
        print("Veritabanı bağlantısı kapandı.")

# urunuGuncelle("Katre-i Matem", "İskender Pala", "", "Roman", 5 )

def urunuSil(kimlik):
    baglanti = pypyodbc.connect(host = "localhost", user = "root", password = "mysqlparola", database = "urunler_veritabani")
    imlec = baglanti.cursor()

    sql = "DELETE FROM Urunler WHERE Id = %s"
    degerler = (kimlik,)
    imlec.execute(sql, degerler)
    try:
        baglanti.commit()
        print(f"{imlec.rowcount} adet kayıt silindi.")
    except pypyodbc.Error as hata:
        print("Bir hata oluştu: ", hata)
    finally:
        baglanti.close()
        print("Veritabanı bağlantısı kapandı.")

# urunuSil(4)
