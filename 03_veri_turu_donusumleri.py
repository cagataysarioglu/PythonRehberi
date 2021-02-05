"""
x = input('1. sayı: ')
y = input('2. sayı: ')

print(type(x))
print(type(y))

toplam = int(x) + int(y)

print(toplam)
"""
"""
x = 27              # int
y = 13.8            # float
name = "Bailey"     # str
isOnline = True     # bool

# int to float (int'ten float'a dönüşüm)
x = float(x)
print(x)
print(type(x))

# float to int (float'tan int'e dönüşüm)
y = int(y)
print(y)
print(type(y))

# bool to str (bool'dan str'ye dönüşüm)
isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))
 
# bool to int (bool'dan int'e dönüşüm)
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))
"""

# Dairenin alanı: πr²
# Dairenin çevresi: 2πr
# Yarıçapı verilen (Bunu biz veriyoruz) bir dairenin alan ve çevresini hesaplayınız.
# π: 3.14
"""
pi = 3.14

r = float(input("Yarıçap: "))

daireAlani = pi * (r ** 2)
daireCevresi = 2 * pi * r

# print("Alan: ", daireAlani)
# print("Çevre: ", daireCevresi)
# veya aşağıdaki şekilde de uygulnabilir.
print("Alan: " + str(daireAlani) + ", " + "Çevre: " + str(daireCevresi))
"""
# ad = "Hüseyin Nihâl"
# soyad = "Atsız"
# # print("Benim adım {} {}".format(ad, soyad)) # Buradaki yöntem (format ve süslü parantez) ile ad değerlerini daha kolayca değişkenden aktardık.
# print(f"Benim adım {ad} {soyad}.") # Bu da f-string yöntemi.
# # print("Benim adım {0} {1}".format(ad, soyad))
# # print("Benim adım {a} {s}".format(a=ad, s=soyad)) # İndis yerlerinde değişiklik de yapılabilmektedir.

# # islem = 200 / 700

# print("İşlemin sonucu {i:1.3}".format(i=islem)) # Burada i'ye atadık ve 1 ile sayının başında kaç karakterlik boşluk kalacağını ayarladık, 3 ile ise 3'üncü haneye kadar al dedik, yoksa daha uzun bir sayı dönüyordu.