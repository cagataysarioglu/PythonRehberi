import pandas as pd

musteriler = {
    "MusteriID": [1, 2, 3, 4, 5, 6, 7],
    "MusteriAdi": ["Baybars", "Sencer", "Kürşad", "Bumin", "İstemi", "Mete", "Atilla"],
    "MusteriSoyadi": ["Özkan", "Kapganoğlu", "Gökbörü", "Türkpençe", "Karatuğlu", "Sungurtegin", "Arslanalp"]
}
siparisler = {
    "SiparisID": [10, 11, 12, 13, 14, 15, 16],
    "MusteriID": [2, 3, 6, 7, 8, 9, 13],
    "SiparisTarihi": ["2010-07-04", "2011-03-28", "2011-09-12", "2011-12-21", "2012-07-04", "2012-07-14", "2013-06-05"]
}
# df_musteriler = pd.DataFrame(musteriler, columns= ["MusteriID", "MusteriAdi", "MusteriSoyadi"])
# df_siparisler = pd.DataFrame(siparisler, columns= ["SiparisID", "MusteriID", "SiparisTarihi"])

# print(df_musteriler)
# print(df_siparisler)

# islem = pd.merge(df_musteriler, df_siparisler, how= "inner")
# islem = pd.merge(df_musteriler, df_siparisler, how= "left")
# islem = pd.merge(df_musteriler, df_siparisler, how= "right")
# islem = pd.merge(df_musteriler, df_siparisler, how= "outer")

# print(islem)
#############################

musterilerA = {
    "MusteriID": [1, 2, 3, 4],
    "MusteriAdi": ["Bengü", "Gürkan", "Gökçe", "Müge"],
    "MusteriSoyadi": ["Kapganoğlu", "Canikligil", "Karatuğlu", "Sungurtegin"]
}
musterilerB = {
    "MusteriID": [5, 6, 7, 8],
    "MusteriAdi": ["Baybars", "Aybüke", "Kürşad", "Elçin"],
    "MusteriSoyadi": ["Özkan", "Arslan", "Gökbörü", "Türkpençe"]
}
df_musterilerA = pd.DataFrame(musterilerA, columns= ["MusteriID", "MusteriAdi", "MusteriSoyadi"])
df_musterilerB = pd.DataFrame(musterilerB, columns= ["MusteriID", "MusteriAdi", "MusteriSoyadi"])

islem = pd.concat([df_musterilerA, df_musterilerB])
islem = pd.concat([df_musterilerA, df_musterilerB], axis= 1)

print(islem)