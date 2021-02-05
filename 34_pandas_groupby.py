### GROUPBY KULLANIMI #######
import pandas as pd
import numpy as np

calisanlar = {
    "Çalışan": ["Sencer Özkan", "Bumin Arslanalp", "İstemi Canikligil", "Mete Türkpençe", "Kürşad Gökbörü", "Baybars Karatuğlu", "Çağatay Sarıoğlu"],
    "Bölüm": ["İnsan Kaynakları", "Bilgi İşlem", "Muhasebe", "İnsan Kaynakları", "Muhasebe", "İnsan Kaynakları", "Bilgi İşlem"],
    "Yaş": [30, 27, 45, 47, 23, 34, 30],
    "İlçe": ["Maltepe", "Maltepe", "Üsküdar", "Kadıköy", "Üsküdar", "Kadıköy", "Maltepe"],
    "Maaş": [5000, 3000, 4500, 3500, 3700, 4200, 3800]
}

# df = pd.DataFrame(calisanlar)

# sonuc = df
# sonuc = df["Maaş"].sum()
# sonuc = df.groupby("Bölüm").groups
# sonuc = df.groupby(["Bölüm", "İlçe"]).groups

# ilceler = df.groupby("İlçe")
# for ad, grup in ilceler:
#     print(ad)
#     print(grup)

# for ad, grup in df.groupby("Bölüm"):
#     print(ad)
#     print(grup)

# sonuc = df.groupby("Bölüm").get_group("Bilgi İşlem")
# sonuc = df.groupby("Bölüm").sum()
# sonuc = df.groupby("Bölüm").mean()
# sonuc = df.groupby("Bölüm")["Maaş"].mean()
# sonuc = df.groupby("İlçe")["Çalışan"].count()
# sonuc = df.groupby("Bölüm")["Yaş"].max()
# sonuc = df.groupby("Bölüm")["Maaş"].min()
# sonuc = df.groupby("Bölüm")["Maaş"].min()["Muhasebe"]
# sonuc = df.groupby("Bölüm").agg(np.mean)
# sonuc = df.groupby("Bölüm")["Maaş"].agg([np.sum, np.mean, np.max, np.min])
# sonuc = df.groupby("Bölüm")["Maaş"].agg([np.sum, np.mean, np.max, np.min]).loc["Bilgi İşlem"]

# print(sonuc)

### KAYIP VE BOZUK VERİ ANALİZİ #######
veri = np.random.randint(10, 100, 15).reshape(5, 3)

df = pd.DataFrame(veri, index= ["a", "c", "e", "f", "h"], columns= ["sutun1", "sutun2", "sutun3"])
df = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
yeniSutun = [np.nan, 30, np.nan, 40, np.nan, 42, np.nan, 57]
df["sutun4"] = yeniSutun

sonuc = df
sonuc = df.drop("sutun1", axis= 1)
sonuc = df.drop(["sutun1", "sutun3"], axis= 1)
sonuc = df.drop("b", axis= 0)
sonuc = df.drop(["b", "e", "g"], axis= 0)

sonuc = df.isnull()
sonuc = df.notnull()
sonuc = df.notnull().sum()
sonuc = df["sutun1"].isnull()
sonuc = df[df["sutun1"].isnull()]
sonuc = df[df["sutun1"].isnull()]["sutun1"]
sonuc = df[df["sutun1"].notnull()]["sutun1"]

sonuc = df.dropna() # Varsayılanı axis= 0 (Satır)
sonuc = df.dropna(axis= 1)
sonuc = df.dropna(how= "any")
sonuc = df.dropna(how= "all")
sonuc = df.dropna(subset= ["sutun1", "sutun2"], how= "all")
sonuc = df.dropna(subset= ["sutun1", "sutun2"], how= "any")
sonuc = df.dropna(thresh= 3) # En az sayıda normal veri

sonuc = df.fillna(value= "Girdi yok")
sonuc = df.fillna(value= 1)

sonuc = df.sum()
sonuc = df.sum().sum()
sonuc = df.size
sonuc = df.isnull().sum()
sonuc = df.isnull().sum().sum()

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

sonuc = df.fillna(value= ortalama(df))

print(sonuc)
# print(df)