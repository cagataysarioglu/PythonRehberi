# kullaniciAdi = "kursadgokboru"
# kullaniciParolasi = "1234567"

# girilenKullaniciAdi = input("Kullanıcı adı: ")
# girilenKullaniciParolasi = input("Parola: ")

# girildiMi = (girilenKullaniciAdi == kullaniciAdi) and (girilenKullaniciParolasi == kullaniciParolasi)

# if girildiMi:
#     print("Hoş geldiniz.")
# else:
#     print("Giriş başarısız!")

#########################################
# x, y, z = float(input("x: ")), float(input("y: ")), float(input("z: "))

# if x > (y + z):
#     print("x, y ile z'nin toplamından büyüktür.")
# elif x == (y + z):
#     print("x, y ile z'nin toplamına eşittir.")
# else:
#     print("x, y ile z'nin toplamından küçüktür.")

###########################################
# kullaniciAdi = input("Kullanıcı adı: ")
# kullaniciYasi = int(input("Yaşınız: "))
# kullaniciEgitimDurumu = input("Eğitim durumunuz: ")

# egitimYetergesi = "üniversite" or "lise"
# surucuBelgesiAlabilme = (kullaniciYasi >= 18) and (kullaniciEgitimDurumu == egitimYetergesi)

# if surucuBelgesiAlabilme:
#     print("Sürücü belgesi alabilirsiniz.")
# elif kullaniciYasi < 18:
#     print("18 yaşından küçükler sürücü belgei alamaz.")
# elif kullaniciEgitimDurumu != egitimYetergesi:
#     print("Eğitim durumunuz sürücü belgesi almaya uygunsuzdur.")
# else:
#     print("Sürücü belgesi alamazsınız.")

#################################################

# birinciYazili = float(input("Birinici yazılı notu: "))
# ikinciYazili = float(input("İkinci yazılı notu: "))
# sozlu = float(input("Sözlü notu: "))

# ortalama = (birinciYazili + ikinciYazili + sozlu) / 3

# if (ortalama >= 0) and (ortalama <= 24):
#     print(f"Ortalamanız: {ortalama}, Notunuz: 0")
# elif (ortalama >= 25) and (ortalama <= 44):
#     print(f"Ortalamanız: {ortalama}, Notunuz: 1")
# elif (ortalama >= 45) and (ortalama <= 54):
#     print(f"Ortalamanız: {ortalama}, Notunuz: 2")
# elif (ortalama >= 55) and (ortalama <= 69):
#     print(f"Ortalamanız: {ortalama}, Notunuz: 3")
# elif (ortalama >= 70) and (ortalama <= 84):
#     print(f"Ortalamanız: {ortalama}, Notunuz: 4")
# elif (ortalama >= 85) and (ortalama <= 100):
#     print(f"Ortalamanız: {ortalama}, Notunuz: 5")
# else:
#     print("Geçerli notunuz bulunmamaktadır.")

##################################################

# import datetime

# tarih = input("Aracınız hangi tarihte (Yıl/Ay/Gün) trafiğe çıktı?: ")
# tarih = tarih.split("/")
# trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
# simdi = datetime.datetime.now()
# aradakiFark = simdi - trafigeCikis
# gun = aradakiFark.days

# if gun <= 365:
#     print("1'inci servis aralığındasınız.")
# elif gun > 365 and gun <= 365 * 2:
#     print("2'nci servis aralığındasınız.")
# elif gun > 365 * 2 and gun <= 365 * 3:
#     print("3'üncü servis aralığındasınız.")
# else:
#     print("Yanlış bilgi girdiniz!")

#####################################################

# sayi = float(input("Sayı: "))
# sonuc = (sayi > 0) and (sayi % 2 == 0)

# if sonuc:
#     print(f"Girdiğiniz sayı ({int(sayi)}) çift sayıdır.")
# else:
#     print(f"Girdiğiniz sayı ({int(sayi)}) tek sayıdır.")

######################################################
ad = input("Adınız: ")
kilo = float(input("Kilonuz: "))
boy = float(input("Boyunuz: "))

indeks = kilo / (boy ** 2)

zayif = (indeks >= 0) and (indeks <= 18.4)
normal = (indeks >= 18.5) and (indeks <= 24.9)
kilolu = (indeks >= 25.0) and (indeks <= 29.9)
sisman = (indeks >= 30.0) and (indeks <= 34.9)

if zayif:
    print(f"{ad}, vucüt indeksin {indeks}, yani zayıfsın.")
elif normal:
    print(f"{ad}, vucüt indeksin {indeks}, yani normalsin.")
elif kilolu:
    print(f"{ad}, vucüt indeksin {indeks}, yani kilolusun.")
elif sisman:
    print(f"{ad}, vucüt indeksin {indeks}, yani şişmansın.")
else:
    print("Girdiğin bilgilerde yanlışlık var.")