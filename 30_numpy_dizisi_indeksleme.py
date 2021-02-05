### NUMPY DİZİLERİNİN İNDEKSLENMESİ #######
import numpy as np

sayilar = np.array([0, 7, 8, 13, 17, 23, 37, 40])

islem = sayilar[7] # 40
islem = sayilar[-1] # 40
islem = sayilar[1] # 7
islem = sayilar[0:4] # [0 7 8 13]
islem = sayilar[:4] # [0 7 8 13]
islem = sayilar[5:] # [23 37 40]
islem = sayilar[::] # [0 7 8 13 17 23 37 40]
islem = sayilar[::-1] # [40 37 23 17 13 8 7 0]
islem = sayilar[::-2] # [40 23 13 7]

yeniSayilar = np.array([[0, 7, 8], [13, 17, 23], [37, 40, 45]]) # Bu 3x3'lük matristir.

islem = yeniSayilar[0] # [0 7 8]
islem = yeniSayilar[1] # [13 17 23]
islem = yeniSayilar[2, 1] # 40
islem = yeniSayilar[:, 2] # [8 23 45]
islem = yeniSayilar[:, 0:2] # [[ 0  7]
                            #  [13 17]
                            #  [37 40]]
islem = yeniSayilar[-1, :] # [37 40 45]
islem = yeniSayilar[:2, :2] # [[ 0  7]
                            #  [13 17]]
# print(islem)

dizi1 = np.arange(0, 10)
dizi2 = dizi1 # Referans verdik, bulunak gösterdik. Yani, artık bulunakları aynıdır.
dizi3 = dizi1.copy() # Burada ise farklı bulunaklar oluşur ve dizi1 etkilenmez.

dizi2[2] = 40
dizi3[0] = 70

# print(dizi1)
# print(dizi2)
# print(dizi3)

### NUMPY DİZİ OPERASYONLARI #######
sayilar1 = np.random.randint(10, 100, 6)
sayilar2 = np.random.randint(10, 100, 6)

print(sayilar1)
print(sayilar2)

sonuc = sayilar1 + sayilar2
sonuc = sayilar1 + 10
sonuc = sayilar1 - sayilar2
sonuc = sayilar1 - 10
sonuc = sayilar1 * sayilar2
sonuc = sayilar1 * 10
sonuc = np.sin(sayilar1)
sonuc = np.cos(sayilar2)
sonuc = np.sqrt(sayilar1)
sonuc = np.log(sayilar2)

csayilar1 = sayilar1.reshape(2, 3)
csayilar2 = sayilar2.reshape(2, 3)

print(csayilar1)
print(csayilar2)

sonuc = np.vstack((csayilar1, csayilar2)) # 2 adet olan 2x3'lük matrisi sütunsal olarak birleştirir. (4x3)
sonuc = np.hstack((csayilar1, csayilar2)) # 2 adet olan 2x3'lük matrisi satırsal olarak birleştirir. (2x6)

sonuc = sayilar1 >= 7 # Mantıksal veri türünde döndürür.
sonuc = sayilar2 % 2 == 0 # Mantıksal veri türünde döndürür.

print(sayilar2[sonuc])
print(sonuc)
