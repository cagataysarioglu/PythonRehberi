# SELENIUM İLE GITHUB TAKİPÇİ LİSTESİNİN ALINMASI
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

kullaniciadi = "cagataysarioglu"
parola = "aVcAr999"

class Github:
    def __init__(self, kullaniciadi, parola):
        self.surucu = webdriver.Firefox(executable_path="D:/Program Dosyaları/Selenium Firefox Sürücüsü/geckodriver.exe")
        self.kullaniciadi = kullaniciadi
        self.parola = parola
        self.takipciler = []
    def girisYap(self):
        self.surucu.get("https://github.com/login")
        time.sleep(2)
        self.surucu.find_element_by_id("login_field").send_keys(self.kullaniciadi)
        self.surucu.find_element_by_id("password").send_keys(self.parola)
        self.surucu.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]").click()
    def takipcileriYukle(self):
        takipciListesi = self.surucu.find_elements_by_css_selector(".d-table.table-fixed")
        for i in takipciListesi:
            self.takipciler.append(i.find_elements_by_css_selector("span.f4").text)
    def takipcileriGetir(self):
        self.surucu.get(f"https://github.com/{self.kullaniciadi}?tab=followers")
        time.sleep(2)
        self.takipcileriYukle()
        while True:
            gezinti = self.surucu.find_element_by_class_name("BtnGroup").find_elements_by_tag_name("a")
            if len(gezinti) == 1:
                if gezinti[0].text == "Next":
                    gezinti[0].click()
                    time.sleep(1)
                    self.takipcileriYukle()
                else:
                    break
            else:
                for gezi in gezinti:
                    if gezi.text == "Next":
                        gezi.click()
                        time.sleep(1)
                        self.takipcileriYukle()
                    else:
                        continue

github = Github(kullaniciadi, parola)
github.girisYap()
github.takipcileriGetir()
print(len(github.takipciler))
print(github.takipciler)