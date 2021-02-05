from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

kullaniciadi = "KULLANICIADI"
parola = "PAROLA"

class Civildak:
    def __init__(self, kullaniciadi, parola):
        self.tarayici = webdriver.Firefox(executable_path="D:/Program Dosyaları/Selenium Firefox Sürücüsü/geckodriver.exe")
        self.kullaniciAdi = kullaniciadi
        self.parola = parola
    def girisYap(self):
        self.tarayici.get("https://twitter.com/login")
        time.sleep(3)

        kullaniciAdiGirisi = self.tarayici.find_element_by_name("session[username_or_email]")
        parolaGirisi = self.tarayici.find_element_by_name("session[password]")
        girisDugmesi = self.tarayici.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
        
        kullaniciAdiGirisi.send_keys(self.kullaniciAdi)
        parolaGirisi.send_keys(self.parola)
        girisDugmesi.click()
        time.sleep(3)
    def aramaYap(self, etiket):
        aramaGirdisi = self.tarayici.find_element_by_xpath("")
        aramaGirdisi.send_keys(etiket)
        time.sleep(2)
        aramaGirdisi.send_keys(Keys.ENTER)
        time.sleep(3)

        sonuclar = []

        liste = self.tarayici.find_element_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")
        time.sleep(2)
        print("Sayı: " + str(len(liste)))

        for c in liste:
            sonuclar.append(c.text)

        donguSayaci = 0
        sonYukseklik = self.tarayici.execute_script("return document.documentElement.scrollHeight") # Burada JavaScript kodu döndürüyoruz.
        while True:
            if donguSayaci > 5:
                break
            self.tarayici.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);") # Burada da JavaScript kodu çalıştıryoruz.
            time.sleep(2)
            yeniYukseklik = self.tarayici.execute_script("return document.documentElement.scrollHeight") # Burada da öyle.
            if sonYukseklik == yeniYukseklik:
                break
            sonYukseklik = yeniYukseklik
            donguSayaci += 1

            liste = self.tarayici.find_element_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]")
            time.sleep(2)
            print("Sayı: " + str(len(liste)))

            for c in liste:
                sonuclar.append(c.text)

        say = 1                        
        with open("civiltilar.txt", "w", encoding="UTF-8") as dosya:
            for i in sonuclar:
                dosya.write(f"{say}- {i}\n")
                say += 1                        

civildak = Civildak(kullaniciadi, parola)
civildak.girisYap() # Giriş işlemi
civildak.aramaYap("python") # Arama işlemi
