import pandas as pd
import numpy as np

### DATAFRAME İLE SATIR-SÜTUN SEÇİMLERİ #######
# df = pd.read_csv('veri.csv')

# df = pd.DataFrame(randn(3, 3), index= ["A", "B", "C"], columns= ["1. Sutun", "2. Sutun", "3. Sutun"])

# islem = df
# islem = df["2. Sutun"] # 2. sütunu döndürür.
# islem = type(df["2. Sutun"])
# islem = df[["1. Sutun", "2. Sutun"]] # 1. ve 2. sütunu döndürür.
# islem = df.loc["A"] # 1. satırı döndürür. / loc["satır", "sütun"] => loc["satır"] => loc[":", "sütun"]
# islem = df.loc[:, "1. Sutun"]
# islem = df.loc[:, ["1. Sutun", "2. Sutun"]]
# islem = df.loc[:, "1. Sutun" : "3. Sutun"] # Aralık belirtildi.
# islem = df.loc[:, : "3. Sutun"] # Baştan başlayıp.
# islem = df.loc["A" : "B", : "3. Sutun"]
# islem = df.loc[: "B", : "3. Sutun"]
# islem = df.iloc[2] # İndis adına bakmaksızın.

# df["4. Sutun"] = pd.Series(randn(3), ["A", "B", "C"])
# df["5. Sutun"] = df["1. Sutun"] + df["3. Sutun"]
# df.drop("5. Sutun", axis= 1, inplace= True) # Silme

# print(islem)
# print(df)

### DATAFRAME İLE FİLTRELEME #######
veri = np.random.randint(10, 100, 75).reshape(15, 5)
df = pd.DataFrame(veri, columns= ["1. Sutun", "2. Sutun", "3. Sutun", "4. Sutun", "5. Sutun",])

sonuc = df
sonuc = df.columns
sonuc = df.head() # İlk beşini döndürür.
sonuc = df.head(10)
sonuc = df.tail() # Son beş...
sonuc = df["1. Sutun"].head()
sonuc = df[["1. Sutun", "2. Sutun"]]
sonuc = df[5:15][["1. Sutun", "2. Sutun"]].head()

sonuc = df > 50
sonuc = df[df > 50]
sonuc = df[df % 2 == 0]
sonuc = df[df["1. Sutun"] > 50][["1. Sutun", "2. Sutun"]]
sonuc = df[(df["1. Sutun"] > 50) & (df["1. Sutun"] <= 70)]
sonuc = df[(df["1. Sutun"] > 50) & (df["2. Sutun"] <= 70)]
sonuc = df[(df["1. Sutun"] > 50) | (df["2. Sutun"] > 50)][["1. Sutun", "2. Sutun"]]
sonuc = df.query("1. Sutun >= 50 & 1. Sutun % 2 == 0")
sonuc = df.query("1. Sutun >= 50 & 1. Sutun % 2 == 0")[["1. Sutun", "2. Sutun"]]

print(sonuc)