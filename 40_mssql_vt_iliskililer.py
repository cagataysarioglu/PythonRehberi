import pypyodbc

def urunleriGetir():
    baglanti = pypyodbc.connect("Driver={SQL Server};""Server=𐰲𐰍𐱃𐰖∶𐰽𐰺𐰃;""Database=Ayakkabici_VT;""Trusted_Connection=True;")
    imlec = baglanti.cursor()

    # tumce = "SELECT * FROM dbo.Ayakkabilar"
    # tumce = "SELECT * FROM dbo.Kategoriler"
    # tumce = "SELECT * FROM dbo.Ayakkabilar INNER JOIN dbo.Kategoriler ON dbo.Kategoriler.Kategori_Kimlik = dbo.Ayakkabilar.Ayakkabi_Kategorisi"
    # tumce = "SELECT dbo.Ayakkabilar.Ayakkabi_Adi, dbo.Ayakkabilar.Ayakkabi_Rengi, dbo.Kategoriler.Kategori_Adi FROM dbo.Ayakkabilar INNER JOIN dbo.Kategoriler ON dbo.Kategoriler.Kategori_Kimlik = dbo.Ayakkabilar.Ayakkabi_Kategorisi"
    # tumce = "SELECT dbo.Ayakkabilar.Ayakkabi_Adi, dbo.Ayakkabilar.Ayakkabi_Rengi, dbo.Kategoriler.Kategori_Adi FROM dbo.Ayakkabilar INNER JOIN dbo.Kategoriler ON dbo.Kategoriler.Kategori_Kimlik = dbo.Ayakkabilar.Ayakkabi_Kategorisi WHERE dbo.Kategoriler.Kategori_Adi = 'Babet'"
    tumce = "SELECT ayk.Ayakkabi_Adi, ayk.Ayakkabi_Rengi, ktg.Kategori_Adi FROM dbo.Ayakkabilar AS ayk INNER JOIN dbo.Kategoriler AS ktg ON ktg.Kategori_Kimlik = ayk.Ayakkabi_Kategorisi WHERE ktg.Kategori_Adi = 'Babet'"
    imlec.execute(tumce)

    try:
        sonuc = imlec.fetchall()
        for urun in sonuc:
            print(urun)
    except pypyodbc.Error as hata:
        print("Bir hata oluştu: ", hata)
    finally:
        baglanti.close()
        print("*******")
        print("Veritabanına erişim kapandı.")

urunleriGetir()
