from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

kullaniciadi = "905375871310"
parola = "umolon27"

class Vkontakte:
    def __init__(self, kullaniciadi, parola):
        self.surucu = webdriver.Firefox(executable_path="D:/Program Dosyaları/Selenium Firefox Sürücüsü/geckodriver.exe")
        self.kullaniciadi = kullaniciadi
        self.parola = parola
    def girisYap(self):
        self.surucu.get("https://vk.com/")
        time.sleep(2)
        self.surucu.find_element_by_id("index_email").send_keys(self.kullaniciadi)
        self.surucu.find_element_by_id("index_pass").send_keys(self.parola)
        self.surucu.find_element_by_id("index_login_button").click()
    def arkadaslariYukle(self):
        listeIcerigi = self.surucu.find_element_by_id("list_content")
        arkadasSayisi = len(listeIcerigi.find_elements_by_css_selector(".friends_list_bl"))
        print(f"İlk sayım: {arkadasSayisi}")
        hareket = webdriver.ActionChains(self.surucu)
        while True:
            listeIcerigi.click()
            hareket.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            yeniSayi = len(listeIcerigi.find_elements_by_css_selector(".friends_list_bl"))
            if arkadasSayisi != yeniSayi:
                arkadasSayisi = yeniSayi
                print(f"Güncel sayı: {yeniSayi}")
                time.sleep(1)
            else:
                break
        arkadasListesi = listeIcerigi.find_elements_by_css_selector(".friends_list_bl div")
        liste = []
        for i in arkadasListesi:
            baglanti = i.find_elements_by_css_selector("a").get_attribute("href")
            liste.append(i)
            print(liste)
    def arkadaslariGetir(self):
        time.sleep(7)
        self.surucu.get("https://vk.com/friends?id=144528327&section=all")
        time.sleep(2)
        self.arkadaslariYukle()


vk = Vkontakte(kullaniciadi, parola)
vk.girisYap()
vk.arkadaslariGetir() 