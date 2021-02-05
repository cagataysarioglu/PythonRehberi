# KALITIM (INHERITANCE)
class Kisi():
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
        print("Kişi oluşturuldu.")
    def benKimim(self):
        print("Ben bir kişiyim.")
    def yemekYe(self):
        print("Yemek yiyorum.")

class Ogrenci(Kisi):
    def __init__(self, ad, soyad, numara): # Ogrenci'ye özel eklentiler uygulanabilir.
        Kisi.__init__(self, ad, soyad) # Kisi sınıfının özellikleri kalıtılıyor.
        self.ogrenciNu = numara
        print("Öğrenci oluşturuldu.")
    def benKimim(self): # Kisi sınıfına ait özellik, Ogrenci için değiştirildi. Aynı addaki yöntem, temel sınıftakini ezer. (Override)
        print("Ben bir öğrenciyim.")

class Ogretmen(Kisi):
    def __init__(self, ad, soyad, alan):
        super().__init__(ad, soyad) # Bu, kalıtçısındaki Kisi.__init__ yöntemi için alternatif bir kullanımdır.
        self.bilimAlani = alan
        print("Öğretmen oluşturuldu.")
    def benKimim(self):
        print(f"Ben bir {self.bilimAlani} öğretmeniyim.")

# k1 = Kisi() # Temel sınıftan oluşturulan nesne.
o1 = Ogrenci("Sencer", "Sungurtegin", 169) # Bunu çağırınca da Kisi'nin __init__ yöntemi çalışacaktır.
print(o1.ad + " " + o1.soyad + " / " + str(o1.ogrenciNu))

h1 = Ogretmen("Hakan", "Pusat", "Tarih")
print(h1.ad + " " + h1.soyad + " / " + h1.bilimAlani)

o1.benKimim()
o1.yemekYe()
h1.benKimim()