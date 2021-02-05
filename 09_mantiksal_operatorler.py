# sayi_01 = input("Sayı: ")

# sonuc = (float(sayi_01) > 0) and (float(sayi_01) < 100)

# sonuc = (float(sayi_01) > 0) and (float(sayi_01) % 2 == 0)

# eposta = "hcs@eposta.com.tr"
# parola = "1234567"

# epoastaGir = input("E-posta: ")
# parolaGir = input("Parola: ")

# islem = (epoastaGir == eposta) and (parolaGir == parola)

vize_01 = float(input("İlk vize notu: "))
vize_02 = float(input("İkinci vize notu: "))
final = float(input("Final notu: "))

ortalama = (((vize_01 + vize_02) / 2) * 0.6) + (final * 0.4)
islem = ((ortalama >= 50) and ((ortalama >= 50) and (final >= 50))) or (final >= 70)



print(f"Geçme durumu nedir? {islem}")
