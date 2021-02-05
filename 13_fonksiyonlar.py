# UYGULAMALAR (DEF-FONKSİYONLAR)
################
# def kereGoster(sozcuk, adet): # Gönderilen sözcüğü, belirtilen sayıda döndüren fonksiyon.
#     print(sozcuk * adet)
# kereGoster("İstemi\n", 40) # '\n'yi alt satıra geçirerek döndürmesi için kullanırız.
#########################################
# def listeyeCevir(*prmt): # Gönderilen sınırsız sayıda parametreyi listeye çevirme. ("*" = Tuple'a çevirme.)
#     liste = []
#     for x in prmt:
#         liste.append(x)
#     return liste
# sonuc = listeyeCevir(10, 40, 50, "Sencer", "Bumin", 70, 140)
# print(sonuc)
#########################################
# def asalSayiBul(birinciSayi, ikinciSayi): # Gönderilen iki sayı arasındaki bütün asal sayıları bulan fonksiyon.
#     for sayi in range(birinciSayi, ikinciSayi + 1): # "ikinciSayi" da hesaba katılsın diye 1 ile topladık.
#         if sayi > 1:
#             for x in range(2, sayi):
#                 if (sayi % x == 0):
#                     break
#             else:
#                 print(sayi)
# birinciSayi = int(input("Birinci sayı: "))
# ikinciSayi = int(input("İkinci sayı: "))
# asalSayiBul(birinciSayi, ikinciSayi)
#########################################
# def tamBolenleriBul(sayi): # Gönderilen bir sayının tam bölenlerini listeler.
#     tamBolenler = []
#     for i in range(2, sayi):
#         if (sayi % i == 0):
#             tamBolenler.append(i)
#     return tamBolenler
# sayi = int(input("Sayı: "))
# print(tamBolenleriBul(sayi))
#########################################
# MAP, FILTER ve LAMBDA
######################################
# def karesiniAl(sayi): return sayi ** 2
sayilar = [1, 3, 5, 9, 20]
# sonuc = list(map(karesiniAl, sayilar))
# print(sonuc)
# VEYA
# for i in map(karesiniAl, sayilar):
#     print(i)
# VEYA
# sonuc = list(map(lambda sayi: sayi ** 2, sayilar))
# print(sonuc)
#####################################
def sayiYokla(sayi): return sayi % 2 == 0
sonuc = list(filter(sayiYokla, sayilar)) # Burası, lambda'yla fonksiyon kurmaksızın, {sonuc = list(filter(lambda sayi: sayi % 2 == 0, sayilar))} biçiminde olur.
print(sonuc)