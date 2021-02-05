# print("Sibel")

### 1'DEN 100'E KADAR OLAN SAYILARIN TOPLANMASI ALGORİTMASI ###
'''
toplam = 0
sayac = 1
while sayac < 100:
    toplam = toplam + sayac
    sayac += 1
print(toplam)
'''
### GİRİLEN SAYILARDAN EN KÜÇÜĞÜNÜN BULUNMASI ALGORİTMASI ###
'''
x = input("x sayısını giriniz: ")
y = input("y sayısını giriniz: ")
z = input("z sayısını giriniz: ")
if x < y:
    if x < z:
        print(f"En küçük sayı: {x}")
    else:
        print(f"En küçük sayı: {z}")
else:
    if y < z:
        print(f"En küçük sayı: {y}")
    else:
        print(f"En küçük sayı: {z}")
'''
### GİRİLEN NOTLARIN ORTALAMASININ BULUNMASI ALGORİTMASI ###
'''
toplam = 0
sayac = 1
while sayac <= 5:
    dNotu = int(input("Notu giriniz: "))
    toplam = toplam + dNotu
    sayac += 1
    ortalama = toplam / 5
print(ortalama)
'''
### 0 İLA 10 ARASINDAKİ TEK SAYILARIN TOPLANMASI ALGORİTMASI ###
'''
s = 0
toplam = 0
while s <= 10:
    if s % 2 == 1:
        toplam = toplam + s
        s += 1
    else:
        s += 1
print(toplam)
'''