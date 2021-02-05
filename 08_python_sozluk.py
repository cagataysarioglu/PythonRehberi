# # anahtar (key) - değer (value)
# # 34 => İstanbul, 41 => Kocaeli

# kentler = ["İstanbul", "Kocaeli"]
# plakalar = [34, 41]
# print(plakalar[kentler.index("İstanbul")]) # Bu, sıradan usül ile eşleştirme yoludur.

# plakalar = {"İstanbul": 34, "Kocaeli": 41} # Ancak burada, anahtar-değer işlevini ekledik.
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
#         "ayak_nu": "38",
#         "telefon": "5370000001",
#         "eposta": "bng.atasagun@eposta.com"
#     },
#     "m_002": {
#         "ad": "Aybüke",
#         "soyad": "Sungurtegin",
#         "ayak_nu": "40",
#         "telefon": "5350000002",
#         "eposta": "a_sungurtegin@eposta.com"
#     },
#     "m_003": {
#         "ad": "Burcu",
#         "soyad": "Öztunga",
#         "ayak_nu": "39",
#         "telefon": "5320000003",
#         "eposta": "burcuoztunga@eposta.com"
#     }
# }

# print(musteriler["m_002"]["ayak_nu"])
#######

musteriler = {}

musteri_nu = input("Müşteri Numarası: ")
ad = input("Müşteri Adı: ")
soyad = input("Müşteri Soyadı: ")
ayak_nu = input("Ayak Bedeni: ")
iletisim = input("Telefon Numarası: ")

# musteriler[musteri_nu] = {
#     "musteriAdi": ad,
#     "musteriSoyadi": soyad,
#     "musteriAyak": ayak_nu
# } # Bunun yerine aşağıdaki update yöntemi de kullanılabilir.

musteriler.update({
    musteri_nu: {
        "musteriAdi": ad,
        "musteriSoyadi": soyad,
        "musteriAyakNu": ayak_nu,
        "musteriIletisim": iletisim
    }
}) # Bu yöntem daha kullanışlıdır, art arda yeni değerler eklenebilir.

musteri_nu = input("Müşteri Numarası: ")
ad = input("Müşteri Adı: ")
soyad = input("Müşteri Soyadı: ")
ayak_nu = input("Ayak Bedeni: ")
iletisim = input("Telefon Numarası: ")

musteriler.update({
    musteri_nu: {
        "musteriAdi": ad,
        "musteriSoyadi": soyad,
        "musteriAyakNu": ayak_nu,
        "musteriIletisim": iletisim
    }
})

musteri_nu = input("Müşteri Numarası: ")
ad = input("Müşteri Adı: ")
soyad = input("Müşteri Soyadı: ")
ayak_nu = input("Ayak Bedeni: ")
iletisim = input("Telefon Numarası: ")

musteriler.update({
    musteri_nu: {
        "musteriAdi": ad,
        "musteriSoyadi": soyad,
        "musteriAyakNu": ayak_nu,
        "musteriIletisim": iletisim
    }
})

print("*" * 40)

musteriNu = input("Müşteri Numarası: ")
musteri = musteriler[musteriNu]
print(musteri)

print(f"Aradığın {musteriNu} numaralı müşterinin adı-soyadı {musteri["musteriAdi"]} {musteri["musteriSoyadi"]}, ayakkabı numarası ise {musteri["musteriAyakNu"]}.")