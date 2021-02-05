# SINAV UYGULAMASI

class Soru():
    def __init__(self, g_soru, g_secenek, g_yanit):
        self.soru = g_soru
        self.secenek = g_secenek
        self.yanit = g_yanit
    def yanitiYokla(self, g_yanit):
        return self.yanit == g_yanit

class Sinav:
    def __init__(self, g_sorular):
        self.sorular = g_sorular
        self.sonuc = 0
        self.soruBankasi = 0
    def soruyuGetir(self):
        return self.sorular[self.soruBankasi]
    def soruyuGoster(self):
        soru = self.soruyuGetir()
        print(f"{self.soruBankasi + 1}. soru: {soru.g_soru}")

        for s in soru.secenek:
            print("-" + s)
        
        yanit = input("Yanıt: ")
        self.tahmin(yanit)
        self.soruyuYukle()
    def tahmin(self, g_yanit):
        soru = self.soruyuGetir()

        if soru.yanitiYokla(yanit):
            self.sonuc += 1
        self.soruBankasi += 1

        self.soruyuGoster()
    def soruyuYukle(self):
        if len(self.sorular) == self.soruBankasi:
            self.sonucGoster()
        else:
            self.ilerlemeyiGoster()
            self.soruyuGoster()
    def sonucGoster(self):
        print("Puanınız: " + self.sonuc)
    def ilerlemeyiGoster(self):
        toplamSoru = len(self.soruBankasi)
        soruSirasi = self.soruBankasi + 1

        if soruSirasi > toplamSoru:
            print("Sınav bitti.")
        else:
            print(f"{toplamSoru} sorudan {soruSirasi}. sorudasın." .center(100, "*"))


s1 = Soru("En iyi programlama dili hangisidir?", ["C#", "Python", "C++", "JavaScript", "C", "Java"], "Python")
s2 = Soru("En çok tercih edilen programlama dili hangisidir?", ["JavaScript", "C++", "Python", "PHP", "Java", "Ruby"], "Python")
s3 = Soru("En çok kazandıran programlama dili hangisidir?", ["C", "Python", "CSS", "PHP", "C++", "JavaScript"], "Python")
soruListesi = [s1, s2, s3]

sinav = Sinav(soruListesi)
sinav.soruyuYukle()

