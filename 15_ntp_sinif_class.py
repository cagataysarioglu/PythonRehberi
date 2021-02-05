# SINIF (CLASS)
# NİTELİK (ATTRIBUTE) => Sınıf Nitelikleri, Nesne Nitelikleri
# YÖNTEM (METHOD)
#####################################
# Sınıf
class Kisi: # "Kisi" adında bir sınıf oluşturduk.
    # pass => Yer tutucu (Tanımlama/içerik olmadığında kullanılır.)
    # Sınıf nitelikleri (Class attributes)
    bulunak = "Bilgi yok"
    # Yapıcı yöntem/işlev (Constructor)
    def __init__(self, ad, dogut): # Burada "constructor" oluşturduk ve "self" ile türetilen nesnelerin özellikleri tanımlanır. "ad" ve "dogut" ise kullanıcı tarafından tanımlanacak.
        # Nesne nitelikleri (Object attributes)
        self.ad = ad
        self.dogut = dogut
        print("init yöntemi çalıştı.") # "ad" ve "dogut" verileri girilmeden çalışmaz.
    # Yöntemler (Methods)
    def girizgah(self):
        print("Merhaba, ben " + self.ad + ".")
    def yasHesapla(self):
        return 2020 - self.dogut
# NESNE (OBJECT/INSTANCE)
####################################
# Nesne
k1 = Kisi("Bumin", 1990) # "Kisi" sınıfı üzerinden "k1" nesnesi tanımladık.
k2 = Kisi(ad = "İstemi", dogut = 1993)
# Güncelleme (Updating)
k2.dogut = 1994
k1.bulunak = "İstanbul"
print(type(k1)) # <class '__main__.Kisi'>
print(type(k2)) # <class '__main__.Kisi'>
# Nesne niteliklerine erişim (Accessing object attributes)
print(f"k1'in adı {k1.ad}, doğutu {k1.dogut}. Bulunak: {k1.bulunak}")
print(f"k2'nin adı {k2.ad}, yaşı {k2.yasHesapla()}. Bulunak: {k2.bulunak}")
# Nesne yöntemini çağırma (Instance method)
k1.girizgah()
k2.girizgah()
### ÖRNEK #################################
class Cember: # Sınıf
    pi = 3.14 # Sınıf niteliği
    def __init__(self, yaricap = 1): # Yapıcı yöntem/işlev
        self.yaricap = yaricap # Nesne niteliği
    def cevreHesapla(self): # Nesne yöntemi
        return (2 * self.pi) * self.yaricap
    def alanHesapla(self): # Nesne yöntemi
        return self.pi * (self.yaricap ** 2)
c1 = Cember() # Yarıçap, belirtilmediği durumda 1 olur.
c2 = Cember(5)
print(f"c1'in alanı {c1.alanHesapla()}, çevresi {c1.cevreHesapla()}.")
print(f"c2'nin alanı {c2.alanHesapla()}, çevresi {c2.cevreHesapla()}.")