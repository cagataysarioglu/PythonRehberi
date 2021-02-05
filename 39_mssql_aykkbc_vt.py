
import pypyodbc
from datetime import datetime
from vt_baglantisi import veritabaniBaglantisi

class Ayakkabi:
    baglanti = veritabaniBaglantisi
    imlec = baglanti.cursor()

    def __init__(self, ayk_kimlik, ayakkabi_bedeni, ayakkabi_adi, ayakkabi_rengi, musteri_adi, musteri_soyadi, siparis_tarihi):
        if ayk_kimlik is None:
            self.aykKimlik = 0
        else:
            self.aykKimlik = ayk_kimlik
        self.ayakkabiBedeni = ayakkabi_bedeni
        self.ayakkabiAdi = ayakkabi_adi
        self.ayakkabiRengi = ayakkabi_rengi
        self.musteriAdi = musteri_adi
        self.musteriSoyadi = musteri_soyadi
        self.siparisTarihi = siparis_tarihi

    def ayakkabiKaydet(self):
        sql = "INSERT INTO dbo.Ayakkabilar(Ayakkabi_Bedeni, Ayakkabi_Adi, Ayakkabi_Rengi, Musteri_Adi, Musteri_Soyadi, Siparis_Tarihi) VALUES (?, ?, ?, ?, ?, ?)"
        degerler = (self.ayakkabiBedeni, self.ayakkabiAdi, self.ayakkabiRengi, self.musteriAdi, self.musteriSoyadi, self.siparisTarihi)
        Ayakkabi.imlec.execute(sql, degerler)
        try:
            Ayakkabi.baglanti.commit()
            print(f"{Ayakkabi.imlec.rowcount} adet kayıt eklendi.")
        except pypyodbc.Error as hata:
            print("Bir hata oluştu: ", hata)
        finally:
            Ayakkabi.baglanti.close()
            print("Veritabanı bağlantısı kesildi.")

    @staticmethod
    def ayakkabilariKaydet(ayakkabilar):
        sql = "INSERT INTO dbo.Ayakkabilar(Ayakkabi_Bedeni, Ayakkabi_Adi, Ayakkabi_Rengi, Musteri_Adi, Musteri_Soyadi, Siparis_Tarihi) VALUES (?, ?, ?, ?, ?, ?)"
        degerler = ayakkabilar
        Ayakkabi.imlec.executemany(sql, degerler)
        try:
            Ayakkabi.baglanti.commit()
            print(f"{Ayakkabi.imlec.rowcount} adet kayıt eklendi.")
        except pypyodbc.Error as hata:
            print("Bir hata oluştu: ", hata)
        finally:
            Ayakkabi.baglanti.close()
            print("Veritabanı bağlantısı kesildi.")

    @staticmethod
    def ayakkabiBilgisi():
        sql = "SELECT * FROM dbo.Ayakkabilar"
        Ayakkabi.imlec.execute(sql)
        try:
            sonuclar = Ayakkabi.imlec.fetchall()
            for sonuc in sonuclar:
                print(f"Ayakkabının adı: {sonuc[2]} - Rengi: {sonuc[3]}")
        except pypyodbc.Error as hata:
            print("Bir hata oluştu: ", hata)
        finally:
            Ayakkabi.baglanti.close()
            print("Veritabanı bağlantısı kesildi.")

    @staticmethod
    def kimligeGoreAyakkabiGetir(ayk_kimlik):
        sql = "SELECT * FROM dbo.Ayakkabilar WHERE Ayk_Kimlik = ?"
        deger = (ayk_kimlik,)

        Ayakkabi.imlec.execute(sql, deger)
        try:
            urun = Ayakkabi.imlec.fetchone()
            return Ayakkabi(urun[0], urun[1], urun[2], urun[3], urun[4], urun[5], urun[5])
        except pypyodbc.Error as hata:
                print("Bir hata oluştu: ", hata)
        finally:
            Ayakkabi.baglanti.close()
            print("Veritabanı bağlantısı kesildi.")
    
    def ayakkabiyiGuncelle(self):
        sql = "UPDATE dbo.Ayakkabilar SET Ayakkabi_Bedeni = ?, Ayakkabi_Adi = ?, Ayakkabi_Rengi = ? Musteri_Adi = ?, Musteri_Soyadi = ?, Siparis_Tarihi = ? WHERE Ayk_Kimlik = ?"
        degerler = (self.ayakkabiBedeni, self.ayakkabiAdi, self.ayakkabiRengi, self.musteriAdi, self.musteriSoyadi, self.siparisTarihi, self.aykKimlik)
        Ayakkabi.imlec.execute(sql, degerler)
        try:
            Ayakkabi.baglanti.commit()
            print("Güncelleme işlemi yapıldı.")
        except pypyodbc.Error as hata:
                print("Bir hata oluştu: ", hata)
        finally:
            Ayakkabi.baglanti.close()
            print("Veritabanı bağlantısı kesildi.")

    @staticmethod
    def ayakkabilariGuncelle(liste):
        sql = "UPDATE dbo.Ayakkabilar SET Ayakkabi_Bedeni = ?, Ayakkabi_Adi = ?, Ayakkabi_Rengi = ? Musteri_Adi = ?, Musteri_Soyadi = ?, Siparis_Tarihi = ? WHERE Ayk_Kimlik = ?"
        degerler = []
        duzen = [1, 2, 3, 4, 5, 0]
        
        for urun in liste:
            urun = [urun[u] for u in duzen]
            degerler.append(urun)
        
        Ayakkabi.imlec.executemany(sql, degerler)
        try:
            Ayakkabi.baglanti.commit()
            print("Güncelleme işlemi yapıldı.")
        except pypyodbc.Error as hata:
                print("Bir hata oluştu: ", hata)
        finally:
            Ayakkabi.baglanti.close()
            print("Veritabanı bağlantısı kesildi.")
    
    @staticmethod
    def siparisTarihineGoreAyakkabiGetir(siparis_tarihi):
        sql = "SELECT * FROM dbo.Ayakkabilar WHERE Siparis_Tarihi = ?"
        deger = (siparis_tarihi,)

        Ayakkabi.imlec.execute(sql, deger)
        try:
            return Ayakkabi.imlec.fetchall()
        except pypyodbc.Error as hata:
                print("Bir hata oluştu: ", hata)
        finally:
            Ayakkabi.baglanti.close()
            print("Veritabanı bağlantısı kesildi.")


aykkb = Ayakkabi.kimligeGoreAyakkabiGetir(3)
aykkb.ayakkabiBedeni = 38
aykkb.ayakkabiyiGuncelle()

aykkblr = Ayakkabi.siparisTarihineGoreAyakkabiGetir(38)
print(aykkblr)

liste = []
for ayk in aykkblr:
    ayk = list(ayk)
    ayk[2] = 40
    liste.append(ayk)
Ayakkabi.ayakkabilariGuncelle(liste)

# Ayakkabi.ayakkabiBilgisi()

# yeniKayit = ayakkabi(38, "Topuklu", "Siyah", "Çağla", "Taşdelen", datetime(2020, 8, 25)),
# yeniKayit.ayakkabiKaydet()

ayakkabilar = [
    ("37", "Babet", "Sarı", "Bengü", "Karaogur", datetime(2020, 8, 22)),
    ("37", "Babet", "Siyah", "Bengü", "Karaogur", datetime(2020, 8, 22)),
    ("39", "Topuklu", "Siyah", "Aybüke", "Yavuzarslan", datetime(2020, 8, 23)),
    ("38", "Babet", "Lacivert", "Bensu", "Kapganoğlu", datetime(2020, 8, 23)),
    ("40", "Topuklu", "Siyah", "Gökçe", "Canikligil", datetime(2020, 8, 23)),
    ("40", "Topuklu", "Mavi", "Gökçe", "Canikligil", datetime(2020, 8, 23)),
    ("37", "Stiletto", "Sarı", "Elçin", "Atasagun", datetime(2020, 8, 24))
]
# Ayakkabi.ayakkabilariKaydet(ayakkabilar)