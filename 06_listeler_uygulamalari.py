# aracListesi = ["BMW", "Mercedes", "TOGG", "Opel", "Mazda"]

# islem_01 = len(aracListesi)
# islem_02 = aracListesi[2]
# islem_03 = "TOGG" in aracListesi
# islem_04 = aracListesi[0:3]

# aracListesi[-2:] = ["Audi", "Volkswagen"]
# islem_05 = aracListesi
# del aracListesi[3]
# islem_06 = aracListesi[::-1]

# ogrenciNotListesi =["Kürşad", "Gökbörü", 1990, [75, 67, 92]]
# islem_07 = ogrenciNotListesi[3]
# islem_08 = f"{ogrenciNotListesi[0]} {ogrenciNotListesi[1]} öğrencisi {2020-ogrenciNotListesi[2]} yaşında, ve not ortalaması {(ogrenciNotListesi[3][0] + ogrenciNotListesi[3][1] + ogrenciNotListesi[3][2])/3}'dir."

# print(islem_08)

adlar = ["Sencer", "Atilla", "Kürşad", "Çağatay", "Bumin"]
yaslar = [1987, 1982, 1990, 1990, 1993]

# ornek_01 = adlar.append("Cenk")
# ornek_02 = adlar.insert(0, "Mete")
# ornek_03 = adlar.pop(0)
ornek_04 = adlar.index("Kürşad")
ornek_05 = "Çağatay" in adlar
ornek_06 = adlar.reverse()
ornek_07 = yaslar.sort()
ornek_08 = yaslar.count(1990)

print(ornek_08)

pusatlar = []

pusat = input("Pusat: ")
pusatlar.append(pusat)
print(pusatlar)