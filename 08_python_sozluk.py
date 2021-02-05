# # anahtar (key) - değer (value)
# # 34 => İstanbul, 61 => Trabzon

# kentler = ["İstanbul", "Trabzon"]
# plakalar = [34, 61]
# print(plakalar[kentler.index("İstanbul")]) # Bu, sıradan usül ile eşleştirme yoludur.

# plakalar = {"İstanbul": 34, "Trabzon": 61} # Ancak burada, anahtar-değer işlevini ekledik.
# print(plakalar["İstanbul"]) # Ve böylelikle tek listeden eşleştirme ve döndürme yaptık.

# plakalar["Ankara"] = 6 # Sonradan da değer ekleyebilmekte ve değiştirebilmekteyiz.

# kullanicilar = {
#     "kursad_gokboru": {
#         "dogut": 1990,
#         "eposta": "kursadgokboru@eposta.com",
#         "bulunak": "Ötüken",
#         "telefon": "3456789123",
#         "roller": ["Yönetici", "Kullanıcı"]
#     },
#     "bumin_ulgen": {
#         "dogut": 1997,
#         "eposta": "buminulgen@eposta.com",
#         "bulunak": "Karabalsagun",
#         "telefon": "789123456",
#         "roller": ["Kullanıcı"]
#         }
# }

# print(kullanicilar["kursad_gokboru"]["roller"][0])

# musteriler = {
#     "m_001": {
#         "ad": "Bengü",
#         "soyad": "Atasagun",
#         "telefon": "5370000001",
#         "eposta": "bng.atasagun@eposta.com"
#     },
#     "m_002": {
#         "ad": "Aybüke",
#         "soyad": "Sungurtegin",
#         "telefon": "5350000002",
#         "eposta": "a_sungurtegin@eposta.com"
#     },
#     "m_003": {
#         "ad": "Burcu",
#         "soyad": "Öztunga",
#         "telefon": "5320000003",
#         "eposta": "burcuoztunga@eposta.com"
#     }
# }

# print(musteriler["m_002"]["eposta"])
#######

musteriler = {}

musteri_nu = input("Müşteri Numarası: ")
ad = input("Müşteri Adı: ")
soyad = input("Müşteri Soyadı: ")
iletisim = input("Telefon Numarası: ")

# musteriler[musteri_nu] = {
#     "musteriAdi": ad,
#     "musteriSoyadi": soyad,
# } # Bunun yerine aşağıdaki update yöntemi de kullanılabilir.

musteriler.update({
    musteri_nu: {
        "musteriAdi": ad,
        "musteriSoyadi": soyad,
        "musteriIletisim": iletisim
    }
}) # Bu yöntem daha kullanışlıdır, art arda yeni değerler eklenebilir.

musteri_nu = input("Müşteri Numarası: ")
ad = input("Müşteri Adı: ")
soyad = input("Müşteri Soyadı: ")
iletisim = input("Telefon Numarası: ")

musteriler.update({
    musteri_nu: {
        "musteriAdi": ad,
        "musteriSoyadi": soyad,
        "musteriIletisim": iletisim
    }
})

musteri_nu = input("Müşteri Numarası: ")
ad = input("Müşteri Adı: ")
soyad = input("Müşteri Soyadı: ")
iletisim = input("Telefon Numarası: ")

musteriler.update({
    musteri_nu: {
        "musteriAdi": ad,
        "musteriSoyadi": soyad,
        "musteriIletisim": iletisim
    }
})

print("*" * 40)

musteriNu = input("Müşteri Numarası: ")
musteri = musteriler[musteriNu]
print(musteri)

print(f"Aradığın {musteriNu} numaralı müşterinin adı-soyadı {musteri["musteriAdi"]} {musteri["musteriSoyadi"]}.")
