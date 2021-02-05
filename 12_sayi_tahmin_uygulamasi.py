import random

sayi = random.randint(1, 70)
hak = 7
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Sayı tahmininiz:"))

    if sayi == tahmin:
        print(f"Tebrikler {sayac}. kerede bildiniz! Puanınız {70 - 10 * (sayac - 1)}.")
        break
    elif sayi > tahmin:
        print("Biraz daha büyük.")
    else:
        print("Biraz daha küçük.")

    if hak == 0:
        print(f"Hakkınız tükendi! Tuttuğum sayı {sayi} idi.")