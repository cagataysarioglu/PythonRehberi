### İÇ İÇE FONKSİYONLAR - KAPSÜLLEME ###
# def faktoriyel(sayi):
#     if not isinstance(sayi, int):
#         raise TypeError("Sayı, bir tamsayı olmalıdır.")
#     if not sayi >= 0:
#         raise ValueError("Sayı, sıfır ya da pozitif olmalıdır.")
#     def icFaktoriyel(sayi):
#         if sayi <= 1:
#             return 1
#         return sayi * icFaktoriyel(sayi - 1)
#     return icFaktoriyel(sayi)
# try:
#     print(faktoriyel(7))
# except Exception as bkz:
#     print(bkz)

### FONKSİYONDAN FONKSİYON DÖNDÜRME ###
# def usAlma(sayi):
#     def icFonksiyon(kuvvet):
#         return sayi ** kuvvet
#     return icFonksiyon
# iki = usAlma(2)
# print(iki(4))
#######################################
# def islem(islem_adi):
#     def toplama(*arg):
#         toplam = 0
#         for i in arg:
#             toplam += i
#         return toplam
#     def carpma(*arg):
#         carpim = 1
#         for i in arg:
#             carpim *= i
#         return carpim
#     if islem_adi == "toplama":
#         return toplama
#     else:
#         return carpma
# toplama = islem("toplama")
# print(toplama(3, 5, 7, 9, 13))
# carpma = islem("carpma")
# print(carpma(2, 4, 6, 8, 10))

### FONKSİYONU PARAMETRE OLARAK GÖNDERME ###
def toplama(a, b):
    return a + b
def cikarma(a, b):
    return a - b
def bolme(a, b):
    return a / b
def carpma(a, b):
    return a * b

def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(2, 3))
    elif islem_adi == "cikarma":
        print(f2(5, 2))
    elif islem_adi == "carpma":
        print(f3(3, 4))
    elif islem_adi == "bolme":
        print(f4(10, 2))
    else:
        print("Geçersiz işlem.")

islem(toplama, cikarma, carpma, bolme, "toplama")

### DECORATOR FONKSİYONLAR ###############
import math
import time

def zamanHesapla(fonk):
    def icFonksiyon(*arg, **anharg):
        baslat = time.time()
        time.sleep(1)
        fonk(*arg, **anharg)
        bitir = time.time()
        print(fonk.__name__ + " fonksiyonunun işlemi " + str(baslat - bitir) + " saniye sürdü.")
    return icFonksiyon

@zamanHesapla
def usAlma(a, b):
    print(math.pow(a, b))

@zamanHesapla
def faktoriyel(sayi):
    print(math.factorial(sayi))

usAlma(3, 7)
faktoriyel(11)

### ITERATORS ###################
class Sayilarim:
    def __init__(self, basla, dur):
        self.baslangic = basla
        self.bitis = dur
    def __iter__(self):
        return self
    def __next__(self):
        if self.baslangic <= self.bitis:
            x = self.baslangic
            self.baslangic += 1
            return x
        else:
            raise StopIteration

liste = Sayilarim(10, 20)

for x in liste:
    print(x)
