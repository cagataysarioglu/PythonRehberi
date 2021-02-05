"""
maasKursad = 5000
maasSencer = 4000
vergi = 0.27

print(maasKursad - (maasKursad * vergi))
print(maasSencer - (maasSencer * vergi))

# Değişken Tanımlama Kuralları
# - Rakamla başlayamaz.
# - Değişken tanımlarken büyük/küçük harf duyarlılığı vardır.
# - Tanımlanan değişken adları arsında boşluk bırakılamaz.

x = 7               # int
y = 3.4             # float
ad = "Kürşad"       # string
ogrenciMi = True    # boolean

x, y, ad, ogrenciMi = (7, 3.4, "Kürşad", True) # Yukarıdaki ile aynıdır.
"""

musteriAdi = "Bengü"
musteriSoyadi = "Sungurtegin"
musteriAdiSoyadi = musteriAdi + " " + musteriSoyadi
musteriCinsiyeti = False # Kadın - Metin veri türünde de yazabilirdik ama böyle daha işlevsel olabilir.
musteriTCKimlik = "57845738203" # Bir hesaplamaya sokmayacağımızdan sayı veri türünde kullanmadık.
musteriDogut = 1993 # Bunu, yaş bulma hesabına sokacağız, bu yüzden sayı veri türünde kullandık.
musteriBulunak = "İstanbul, Kadıköy, Erenköy"
musteriYasi = 2020 - musteriDogut

print(musteriAdiSoyadi)
print(musteriYasi)

siparis_01 = 110
siparis_02 = 1100.5
siparis_03 = 356.95
toplam = siparis_01 + siparis_02 + siparis_03

print(toplam)
