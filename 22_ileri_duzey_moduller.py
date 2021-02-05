### DATETIME MODÜLÜ #################
# from datetime import datetime
# from datetime import timedelta

# imdi = datetime.now()
# dogut = datetime(1990, 12, 10, 10, 37, 40)
# kacGunGecti = imdi - dogut
# print(kacGunGecti)

# ilerikiTarih = imdi + timedelta(days=47)
# print(ilerikiTarih)

### OS MODÜLÜ #########################
# import os

# sonuc = dir(os)
# sonuc = os.name

# os.chdir("C:\\") # chdir: change directory | os.chdir("..") ile bir dizin geriye gidilir.
# os.mkdir("yeni_klasor") # mkdir: make directory | Klasör oluşturur.
# os.makedirs("yeni_klasor/dosyalar") # Klasörler oluşturur.
# os.rename("yeni_klasor", "depo")
# os.rmdir("depo") # rmdir: remove directory
# os.removedirs("depo/dosyalar")

# sonuc = os.getcwd() # Bulunduğumuz dizin
# sonuc = os.listdir("D:\\") # Belirttiğimiz yolu listeledik.

# for dosya in os.listdir(): # Sonu .py olan dosyaları listeledik.
#     if dosya.endswith(".py"):
#         print(dosya)

# sonuc = os.stat("22_ileri_duzey_moduller.py") # Belirttiğimiz dosyanın bilgilerini verir. Aşağıda ise bu bilgileri çözümledik.
# sonuc = sonuc.st_size/1024
# sonuc = datetime.fromtimestamp(sonuc.st_ctime) # Oluşturulma tarihi
# sonuc = datetime.fromtimestamp(sonuc.st_atime) # Son erişilme tarihi
# sonuc = datetime.fromtimestamp(sonuc.st_mtime) # Değiştirilme tarihi

# os.system("notepad.exe") # Belirtilen programı çalıştırır.

# sonuc = os.path.abspath("22_ileri_duzey_moduller.py") # Kesin yolu gösterir.
# sonuc = os.path.dirname("D:/Kullanıcılar/CagataySarioglu/Belgeler/Python/22_ileri_duzey_moduller.py")
# sonuc = os.path.dirname(os.path.abspath("22_ileri_duzey_moduller.py"))
# sonuc = os.path.exists("01_ilk_uygulama.py")
# sonuc = os.path.isdir("D:/Kullanıcılar/") # isdir: is directory?
# sonuc = os.path.isfile("D:/Kullanıcılar/")
# sonuc = os.path.join("C:\\", "Deneme")
# sonuc = os.path.split("C:\\Deneme")
# sonuc = os.path.splitext("22_ileri_duzey_moduller.py")
# print(sonuc)

### REGULAR EXPRESSION MODÜLÜ ######################
# import re

# metin = "Abra Yazılım Ltd. Şti. Tel: +90..."

# islem = re.findall("Abra", metin)
# islem = len(islem)

# islem = re.split(" ", metin)

# islem = re.sub("\s", "/", metin) # \s, boşluk (" ") demektir.

# islem = re.search("Abra", metin)
# islem = islem.span()
# islem = islem.start()
# islem = islem.end()
# islem = islem.group()
# islem = islem.string()

# islem = re.findall("[a-s]")
# islem = re.findall("[0-7]")
# islem = re.findall("[^a-s]") # Belirtilenler dışındakileri arar.
# islem = re.findall("[^0-7]")
# islem = re.findall("...", metin) # Üç basamaklıları arar.
# islem = re.findall("^a", metin) # a ile başlayanı arar.
# islem = re.findall("a$", metin) # a ile başlamayanı arar.
# islem = re.findall("sa*t", metin) # Karakterin 0 ya da daha fazla olmasını kontrol eder. 
# islem = re.findall("sa?t", metin) # Karakterin 0 ya da 1 kez olmasını kontrol eder.
# islem = re.findall("[0-9]{2}", metin) # En az 2 an çok 4 basamaklı sayıları arar.
# islem = re.findall("a|b", metin)
# islem = re.findall("(a|b|c)ad", metin)

# print(islem)

### JSON MODÜLÜ #####################
import json

# metin_kisi = '{"ad": "Baybars", "diller": ["Python", "Javascript", "CSS"]}' # Harici json dosyasının içi de böyle olacaktır. (Metinsel yapıda bir sözlük)
# islem = json.loads(metin_kisi)
# # islem = islem["ad"]
# islem = islem["diller"][1]

# print(type(islem))
# print(islem)

# with open("kisiler.json") as k: # Harici json dosyasından veri alma işlemi.
#     veriler = json.load(k)
#     print(veriler["ad"])

kisi_sozlugu = {
    "ad": "Baybars",
    "diller": ["Python", "Javascript", "CSS"]
}
islem = json.dumps(kisi_sozlugu) # Burada ise sözlüğü json yapısına çevirmiş olduk.
print(type(kisi_sozlugu))
print(type(islem))
print(islem)

# with open("kisiler.json", "w") as k: # Burada dosyayı yazma modunda açıp sözlüğü json dosyasına aktarıyoruz.
#     json.dump(kisi_sozlugu, k)
