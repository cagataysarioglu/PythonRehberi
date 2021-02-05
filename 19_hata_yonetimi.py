liste = ["1", "2", "5a", "10b", "abc", "10", "40"]
# Liste elemanları içerisindeki sayısal değerleri bulma
for x in liste:
    try:
        sonuc = int(x)
        print(sonuc)
    except Exception as hata:
        continue # Dersek çevrilemeyecek olanları atlayarak yalnız sayısalları döndürür.
###########################################
while True:
    sayi = input("Sayı: ")
    if sayi == "ç":
        break

    try:
        sonuc = float(sayi)
        print("Girdiğiniz sayı: ", sonuc)
        break
    except ValueError:
        print("Geçersiz sayı!")
        continue
############################################
def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Eksi değer!")

    sonuc = 1
    for i in range(1, x+1):
        sonuc *= i
    return sonuc

for x in [5, 10, 40, -7, "12c"]:
    try:
        y = faktoriyel(x)
    except ValueError as hata:
        print(hata)
        continue
    print(y)