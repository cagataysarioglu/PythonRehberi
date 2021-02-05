# import math
# 1. YÖNTEM
# import math as matematik # Diye kendimiz de adlandırabiliriz.

# deger = dir(math)
# deger = help(math)
# deger = math.sqrt(49) # Karekökü
# deger = math.factorial(5)

# 2. YÖNTEM
# from math import * # Şeklinde de kullanabiliriz. Burda math'in tüm yöntemlerini aldık.

# def sqrt(x):
#     print("x: " + str(x))
# from math import factorial, sqrt # Böyle ise yalnız bu ikisini almış oluruz.

# deger = factorial(5) # math. dememize gerek kalmaz.
# deger = sqrt(9)

# print(deger)
##############################################

# import random

# sonuc = random.random() # 0.0 ila 1.0 arasında rastgele bir sayı üretilir.
# sonuc = random.random() * 70
# sonuc = random.uniform(552, 639) # 552 ila 639 arasında üretilecek.
# sonuc = int(random.uniform(552, 639)) # Kesirleri ortadan kaldırdık.
# sonuc = random.randint(552, 639) # Ya da bunu, bu yöntemle de yapabiliyoruz.

# adlar = ["Haluk", "Bumin", "Kürşad", "İstemi", "Yavuz", "Sencer", "Çağatay"]
# sonuc = adlar[random.randint(0, len(adlar) - 1)]
# sonuc = random.choice(adlar) # Bir üstteki kullanımın yerine kullanılabilecek bir yöntem.

# liste = list(range(10))
# random.shuffle(liste) # Bir üstteki listeyi rastgele sıralar.
# sonuc = liste

# liste = range(100)
# sonuc = random.sample(liste, 3)
# sonuc = random.sample(adlar, 2)

# print(sonuc)

############################################
import mod

islem = mod.sayi
islem = mod.sayilar
islem = mod.kisiSozlugu["ad"]
islem = mod.fonksiyon(70)

kisiNesnesi = mod.Kisi()
kisiNesnesi.konus()

print(islem)
