# sayilar = [1, 2, 3, 4, 5, 6, 7]
# for sayi in sayilar:
#     print(sayi)

# adlar = ["Çağatay", "Kürşad", "Atilla", "Sencer", "Kapgan", "Mete"]
# for ad in adlar:
#     print(f"Benim adım {ad}.")
#############################################
#UYGULAMALAR (FOR)

sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# for s in sayilar:
#     if (s % 3 == 0): # 3'ün katı olan sayıları bulduk.
#         print(s)

# toplam = 0
# for s in sayilar:
#     toplam += s # toplam = toplam + s demektir.
# print(toplam)

# for s in sayilar:
#     if (s % 2 == 1): # Tek sayıları edinme.
#         print(s ** 2) # Tek sayıların karesi.

kentler = ["İstanbul", "Ankara", "Erzurum", "Trabzon", "Osmaniye", "Rize"]

# for kent in kentler:
#     if (len(kent) <= 5): # Karakterleri en fazla 5 olan kenti bulduk.
#         print(kent)

# urunler = [
#     {"ad": "Tulpar A4", "fiyat": "3000"},
#     {"ad": "Tulpar A5", "fiyat": "4000"},
#     {"ad": "Tulpar A6", "fiyat": "5000"},
#     {"ad": "Abra C3", "fiyat": "6000"},
#     {"ad": "Abra C4", "fiyat": "7000"}
# ]

# toplam = 0
# for urun in urunler:
#     para = int(urun["fiyat"]) # Metni sayıya çevirerek toplamaya gönderiyoruz.
#     toplam += para
# print(toplam)

    # if (int(urun["fiyat"]) <= 5000): # Fiyatı en fazla 5000 olan ürünleri arıyoruz.
    #     print(urun["ad"])

##########################################
# UYGULAMALAR (WHILE)

# ad = "" # False
# while not ad: # Buası True demek, yani False olana dek çalışır.
#     ad = input("Adınızı giriniz: ")
# print(f"Merhaba {ad}, hoş geldin.")

# x = 1
# while x <= 21:
#     if (x % 2 == 1):
#         print(x)
#     x += 1

# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1

# x = int(input("Başlangıç sayısı giriniz: "))
# y = int(input("Bitiş sayısı giriniz: "))
# while x < y:
#     if (x % 2 == 0):
#         print(f"Girdiğiniz aralıktaki {x} sayısı çifttir.")
#     else:
#         print(f"Girdiğiniz aralıktaki {x} sayısı tektir.")
#     x += 1

# x = 100
# while x > 0:
#     print(x)
#     x -= 1

# sayiDizisi = []
# i = 0
# while i < 5:
#     sayi = int(input("Sayı: "))
#     sayiDizisi.append(sayi) # Gelen sayıları diziye ekledik.
#     i += 1
# sayiDizisi.sort() # Gelen sayıları sıraya soktuk.
# print(sayiDizisi)

# urunlerDizisi = []
# adet = int(input("Kaç adet ürün eklemek istiyorsunuz: "))
# i = 0
# while (i < adet):
#     urunAdi = input("Ürün adı: ")
#     urunFiyati = input("Ürün fiyatı: ")
#     urunlerDizisi.append({
#         "ad": urunAdi,
#         "fiyat": urunFiyati
#     })
#     i += 1
# for urun in urunlerDizisi:
#     print(f"Ürün adı: {urun['ad']} - Ürün fiyatı: {urun['fiyat']}")
################################################
# UYGULAMALAR (BREAK ve CONTINUE)

# x = 0
# toplam = 0
# while x <= 100:
#     x += 1
#     if x % 2 == 1:
#         continue
#     toplam += x
# print(f"1'den 100'e kadar olan tek sayıların toplamı: {toplam}")

###############################################
# ÖRNEKLER (LIST COMPREHENSIONS)

# for x in range(10): # Bunun yerine...
#     print(x ** 2)
# sayilar = [x ** 2 for x in range(10)] # Bu kullanılabilir.
# print(sayilar)

# sayilar =[x * x for x in range(10) if x % 3 == 0] # Döngüde sayıların karelerini ve yalnız üçe tam bölünenleri tek satırda istedik.
# print(sayilar)

# metin = "Fenerbahçe"
# liste = []
# for yazi in metin: # Bunun yerine...
#     liste.append(yazi)
# print(liste)

# yeniListe = [yazi for yazi in metin] # Bu kullanılabilir.
# print(yeniListe)

# yillar = [1953, 1963, 1982, 1990, 2003, 2018]
# yaslar = [2020 - yil for yil in yillar]
# print(yaslar)

# islem = [x if x % 2 == 0 else "Tek" for x in range(1, 10)]
# print(islem)

sonuc = []
for x in range(3): # Bunun yerine...
    for y in range(3):
        sonuc.append((x, y))
print(sonuc)

sayilar = [(x, y) for x in range(3) for y in range(3)] # Bu kullanılabilir.
print(sayilar)