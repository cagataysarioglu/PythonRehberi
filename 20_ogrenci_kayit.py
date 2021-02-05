def notHesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama >= 90 and ortalama <= 100:
        harfNotu = "AA"
    elif ortalama >= 85 and ortalama <= 89:
        harfNotu = "BA"
    elif ortalama >= 80 and ortalama <= 84:
        harfNotu = "BB"
    elif ortalama >= 75 and ortalama <= 79:
        harfNotu = "CB"
    elif ortalama >= 70 and ortalama <= 74:
        harfNotu = "CC"
    elif ortalama >= 65 and ortalama <= 69:
        harfNotu = "DC"
    elif ortalama >= 60 and ortalama <= 64:
        harfNotu = "DD"
    elif ortalama >= 50 and ortalama <= 59:
        harfNotu = "FD"  
    else:
        harfNotu = "FF"
    return ogrenciAdi + ": " + harfNotu + "\n"

def ortalamaOku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as dizelge:
        for satir in dizelge:
            print(notHesapla(satir))
def notGir():
    ad = input("Öğrencinin adı: ")
    soyad = input("Öğrencinin soyadı: ")
    not1 = input("Birinci not: ")
    not2 = input("İkinci not: ")
    not3 = input("Üçüncü not: ")

    with open("sinav_notlari.txt", "a", encoding="utf-8") as dizelge:
        dizelge.write(ad + " " + soyad + ": " + not1 + ", " + not2 + ", " + not3 + "\n")

def notSakla():
    with open("sinav_notlari.txt", "a", encoding="utf-8") as dizelge:
        liste = []

        for i in dizelge:
            liste.append(notHesapla(i))

        with open("sonuclar.txt", "w", encoding="utf-8") as cizelge:
            for i in liste:
                cizelge.write(i)

while True:
    islem = input("1- Notları oku\n2- Not gir\n3- Notları sakla\n4- Çıkış\n")

    if islem == "1":
        ortalamaOku()
    elif islem == "2":
        notGir()
    elif islem == "3":
        notSakla()
    else:
        break