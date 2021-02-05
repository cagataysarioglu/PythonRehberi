from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

surucu = webdriver.Firefox(executable_path="D:/Program Dosyaları/Selenium Firefox Sürücüsü/geckodriver.exe")

url = "https://github.com"
surucu.get(url)

# time.sleep(2)
# surucu.maximize_window
# surucu.save_screenshot("github_ekran_goruntusu.png")

# url = "https://github.com/cagataysarioglu"
# surucu.get(url)

# print(surucu.title)
# if "kursadgokboru" in surucu.title:
#     surucu.save_screenshot("github_kursadgokboru_eg.png")

# time.sleep(2)
# surucu.back()

# time.sleep(2)
# surucu.close()

### SELENIUM İLE SAYFA ETKİLEŞİMİ ###############
aramaGirdisi = surucu.find_element_by_name("q") # find_element_by_xpath ile de kullanım yapabiliriz.
time.sleep(1)
aramaGirdisi.send_keys("python")
time.sleep(2)
aramaGirdisi.send_keys(Keys.ENTER)
time.sleep(2)
islem = surucu.find_elements_by_css_selector(".repo-list-item a")

for eleman in islem:
    print(eleman.text)

surucu.close()