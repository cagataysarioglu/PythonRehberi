import pandas as pd
import numpy as np

### PANDAS SERİLERİ #######
sayilar = [30, 40, 50, 70, 80]
yazilar = ["a", "b", "e", "f", "g"]
# sozluk = {"a": 10, "b": 20, "c": 30, "d": 40}
rastgeleSayilar = np.random.randint(10, 100, 6)

# pandasSerisi = pd.Series()
# pandasSerisi = pd.Series(sayilar)
# pandasSerisi = pd.Series(yazilar)
# pandasSerisi = pd.Series(5, [0, 1, 2, 3])
# pandasSerisi = pd.Series(sayilar, ["a", "b", "c", "d", "e"])
# pandasSerisi = pd.Series(sozluk)
# pandasSerisi = pd.Series(rastgeleSayilar)

pandasSerisi = pd.Series([20, 30, 40, 51], ["a", "b", "c", "d"])

# sonuc = pandasSerisi[0] # 20
# sonuc = pandasSerisi[-1] # 50
# sonuc = pandasSerisi[:2] # 20, 30
# sonuc = pandasSerisi[-2:] # 40, 50
# sonuc = pandasSerisi["a"] # 20
# sonuc = pandasSerisi["c"] # 40
# sonuc = pandasSerisi[["a", "c", "e"]]
# sonuc = pandasSerisi.ndim
# sonuc = pandasSerisi.dtype
# sonuc = pandasSerisi.shape
# sonuc = pandasSerisi.sum()
# sonuc = pandasSerisi.max()
# sonuc = pandasSerisi.min()
# sonuc = pandasSerisi + pandasSerisi
# sonuc = pandasSerisi + 50
sonuc = np.sqrt(pandasSerisi)
sonuc = pandasSerisi >= 50
sonuc = pandasSerisi % 2 == 0

# print(pandasSerisi[pandasSerisi % 2 == 0])
# print(pandasSerisi)
# print(sonuc)

opel2018 = pd.Series([20, 30, 40, 10], ["Astra", "Corsa", "Mokka", "Insignia"])
opel2019 = pd.Series([40, 30, 20, 10], ["Astra", "Corsa", "Grandland", "Insignia"])

# toplam = opel2018 + opel2019
# print(toplam)

### PANDAS DATAFRAME TANIMLAMALARI #######
s1 = pd.Series([3, 2, 0, 1])
s2 = pd.Series([0, 3, 7, 2])

veri = dict(elmalar= s1, armutlar= s2)
df = pd.DataFrame(veri)

liste = [["Bengü", 38], ["Aybüke", 40], ["Gökçe", 41], ["Çağla", 39], ["Bensu", 41], ["Tomris", 38], ["Elçin", 42]]
sozluk = {"Ad": ["Ali", "Hakan", "Soner", "Mete", "Ahmet"], "Yaş": [39, 29, 33, 25, 28]}
sozluk_liste = [
    {"Ad": "Kürşad", "Not": 71},
    {"Ad": "Bumin", "Not": 52},
    {"Ad": "İstemi", "Not": 83},
    {"Ad": "Sencer", "Not": 47}
]
df = pd.DataFrame(liste, index= [1, 2, 3, 4, 5, 6, 7], columns= ["Ad", "Beden"])
df = pd.DataFrame(sozluk)
df = pd.DataFrame(sozluk_liste)

print(df)