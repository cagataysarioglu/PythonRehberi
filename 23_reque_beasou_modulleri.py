import requests
import json

# sonuc = requests.get("https://jsonplaceholder.typicode.com/todos")
# sonuc = json.loads(sonuc.text)
# for i in sonuc:
#     print(i)
# print(type(sonuc))

######### EXCHANGE API İLE DÖVİZ UYGULAMASI ##########
# api_url ="https://api.exchangeratesapi.io/latest?base="

# bozdurulan_doviz = input("Bozdurulacak döviz türü: ")
# alinan_doviz = input("Alınacak döviz türü: ")
# miktar = int(input(f"Ne kadar {bozdurulan_doviz} bozdurmak istersiniz: "))

# sonuc = requests.get(api_url + bozdurulan_doviz)
# sonuc = json.loads(sonuc.text)

# print("1 {0} = {1} {2}".format(bozdurulan_doviz, sonuc["rates"][alinan_doviz], alinan_doviz))
# print("{0} {1} = {2} {3}".format(miktar, bozdurulan_doviz, miktar * sonuc["rates"][alinan_doviz], alinan_doviz))

######## GITHUB API ##################################
# class Github:
#     def __init__(self):
#         self.api_url = "https://api.github.com"
#         self.bilet = "77Kuc9lkoP08d76fgOYikol023710cDA33552mlK63A9u7"
#     def kullaniciGetir(self, kullaniciadi):
#         istek = requests.get(self.api_url + "/users/" + kullaniciadi)
#         return istek.json()
#     def depoGetir(self, kullaniciadi):
#         istek = requests.get(self.api_url + "/users/" + kullaniciadi + "/repos")
#         return istek.json()
#     def depoOlustur(self, depoadi):
#         istek = requests.post(self.api_url + "/user/repos?access_token=" + self.bilet + json={
#             "name": depoadi,
#             "description": "Bu sizin ilk deponuz",
#             "homapage": "https://hcsyazilim.com",
#             "private": False,
#             "has_issues": True,
#             "has_projects": True,
#             "has_wiki": True
#         })
#         return istek.json()
#     def depoSil(self, depoadi):
#         istek = requests.delete(self.api_url + "/user/repos?access_token="+ self.bilet)
#         return istek.json()

# github = Github()

# while True:
#     secim = input("1- Kullanıcı bul\n2- Depoya bak\n3- Depo oluştur\n4- Depo sil\n5- Çıkış\nSeçim: ")
#     if secim == "5":
#         break
#     else:
#         if secim == "1":
#             kullaniciadi = input("Kullanıcı adı: ")
#             sonuc = github.kullaniciGetir(kullaniciadi)
#             print(f"Ad: {sonuc['name']} / Açık depo: {sonuc['public_repos']} / Takipçi: {sonuc['followers']}")
#         elif secim == "2":
#             kullaniciadi = input("Kullanıcı adı: ")
#             sonuc = github.depoGetir(kullaniciadi)
#             for depo in sonuc:
#                 print(depo["name"])
#         elif secim == "3":
#             depoadi = input("Depo adı: ")
#             sonuc = github.depoOlustur(depoadi)
#             print(sonuc)
#         elif secim == "4":
#             depoadi = input("Depo adı: ")
#             sonuc = github.depoSil(depoadi)
#             print(sonuc)
#         else:
#             print("Yanlış bir seçim yapıldı!")
############ BEAUTIFULSOUP ###################
html_belgesi = '''<!doctype html><html lang="tr-TR"><head><meta http-equiv="content-type" content="text/html; charset=utf-8"><title>HCS YAZILIM</title></head><body style="background-color: #000000;" onload="onKosul()">
<div class="birinci_bicim" style="padding-top: 5px;">𐱅𐰭𐰼𐰃𐰤𐰤𐰓𐰖𐰞𐰀</div><div style="font-family: cambria; margin-top: -30px; margin-left: 7px; text-align: left; color: green;">Saat: <span id="taban_zaman"></span></div>
<div style="font-family: cambria; margin: auto; margin-left: 7px; text-align: left; color: green;">Tarih: <span id="taban_tarih"></span></div><hr>
<h2 id="abra_yazilim" class="ikinci_bicim" style="margin-bottom: 0%;" onmouseover="abraBuyut()" onmouseout="abraKucult()">𐰉𐰺𐰀∶𐰖𐰔𐰞𐰢</h2><div class="ikinci_bicim" style="font-family: Cambria; font-style: italic; margin-top: 0%;">- Abra Yazılım -</div><p class="ucuncu_bicim" style="margin-bottom: 3px;">𐰉𐰺𐰀∶𐰖𐰔𐰞𐰢∶𐰉𐱁𐱃𐰀∶𐰆𐰞𐰽𐰞∶𐰾𐰃𐰋𐰼𐰏𐰇𐰋𐰤𐰠𐰚∶𐰆𐰞𐰢𐰴∶𐰇𐰔𐰼𐰀∶𐰋𐰃𐰠𐱁𐰢∶𐰋𐰀∶𐱅𐰚𐰣𐰆𐰞𐰲𐰃∶𐰞𐰣𐰦𐰀∶𐰃𐱅𐰚𐰤𐰠𐰚∶𐰏𐰇𐰾𐱅𐰼𐰤∶𐰋𐰃𐰼∶𐱅𐰇𐰼𐰜∶𐰋𐰃𐰠𐱁𐰢∶𐱁𐰃𐰼𐰚𐱅𐰓𐰼∶𐰉𐰺𐰀∶𐰖𐰔𐰞𐰢∶𐰇𐰔𐰠∶𐰾𐰃𐰋𐰼𐰏𐰇𐰋𐰤𐰠𐰚∶𐰲𐰇𐰔𐰢𐰠𐰼𐰃∶𐰇𐰼𐱅𐰼∶𐰘𐰃𐰼𐰠𐰃∶𐰖𐰔𐰞𐰢𐰞𐰺∶𐰋𐰀∶𐰆𐰖𐰍𐰞𐰢𐰞𐰺𐰞𐰀∶𐰇𐰔𐰏𐰤∶𐰚𐰃𐰔𐰢𐱅∶𐰽𐰆𐰣𐰢𐰴𐱃𐰑𐰺</p>
<p style="color: skyblue; text-align: center; margin-top: 0%;">Abra Yazılım, başta siber güvenlik olmak üzere bilişim ve teknoloji alanında etkinlik gösteren bir Türk bilişim şirketidir. Özel siber güvenlik çözümleri üretmekte, yerli yazılımlar ve uygulamalarla özgün hizmet sunmaktayız.</p><img src="uzay_gorseli.jpeg" alt="uzay_gorseli" style="width: 100%;">
<h1 style="font-family: Cambria; color: green; text-align: center; margin-top: 30px; letter-spacing: 2px;">Hizmetlerimiz:</h1><div id="siber_guvenlik" class="css-toggle" style="margin-left: 77px;" onmouseover="siberGuvenlik()" onmouseout="siberGuvenlikDuzelt()">SİBER GÜVENLİK
<span><ol><li><font face="Cambria">Sızma Testleri</li><li><font face="Cambria">DoS/DDoS, Performans ve Yük Testleri</li><li><font face="Cambria">Kaynak Kod Güvenlik Denetimi Hizmeti</li><li><font face="Cambria">Linux Sistem Güvenliği Sıkılaştırma Hizmeti</li>
<li><font face="Cambria">Windows Sistem Güvenliği Sıkılaştırma Hizmeti</li><li><font face="Cambria">Zararlı Yazılım Tahlili<details><summary>Zararlılar:</summary>- Solucan <br>- Casus <br>- Truva atı <br>- Virüs</details>
</li><li><font face="Cambria">Bilgi Güvenliği Proje Yönetimi Hizmeti</li><li><font face="Cambria">Siber Tatbikat ve Güvenlik Verimlilik Ölçümü</li>
<li><font face="Cambria">Siber Tehdit İstihbaratı Hizmeti</li><li><font face="Cambria">Kurumsal Bilgi Güvenliği Eğitimleri</li><li><font face="Cambria">SCADA Kurulumu</li></ol></span></div><div id="yazilim" class="css-toggle" onmouseover="yazilim()" onmouseout="yazilimDuzelt()">YAZILIM<span>
<ol><li><font face="Cambria">Özel Amaçlı Yazılımlar</li><li><font face="Cambria">Süreçsel Yönetim Yazılımları</li><li><font face="Cambria">İçerik Yönetim Sistemleri</li><li><font face="Cambria">Masaüstü Uygulamaları</li><li><font face="Cambria">Müşteri Yönetim Sistemleri</li><li><font face="Cambria">BS Koruma ve Yönetim Sistemleri</li>
<li><font face="Cambria">Uzak Erişim Yazılımları</li><li><font face="Cambria">Depo, Stok ve Barkod Programları</li><li><font face="Cambria">Web Tasarımı ve e-Ticaret Siteleri</li><li><font face="Cambria">Laboratuvar Yazılımları</li>
<li><font face="Cambria">Profesyonel SEO Hizmetleri</li></ol></span></div><div id="oyun" class="css-toggle" onmouseover="oyun()" onmouseout="oyunDuzelt()">OYUN
<span><ol><li><font face="Cambria">Birinci Şahıs Nişancı</li><li><font face="Cambria">Üçüncü Şahıs Nişancı</li><li><font face="Cambria">Rol Yapma Oyunu</li>    <li><font face="Cambria">Devasa Çok Oyunculu Çevrimiçi Rol Yapma Oyunu</li>
<li><font face="Cambria">Çok Oyunculu Çevrimiçi Savaş Meydanı</li><li><font face="Cambria">Gerçek Zamanlı Strateji</li><li><font face="Cambria">Macera</li></ol></span></div><div id="mobil_uygulama" class="css-toggle" onmouseover="mobilUygulama()" onmouseout="mobilUygulamaDuzelt()">MOBİL UYGULAMA
<span><ol><li><font face="Cambria">Arama Motoru Uygulamaları</li><li><font face="Cambria">Fotoğraf ve Video Uygulamaları</li><li><font face="Cambria">Mobil Oyunlar<details><summary>Oyun Türleri:</summary>- ÇÇSM <br>- ÜŞN <br>- Macera</details></li><li><font face="Cambria">Mobil İletişim Uygulamaları</li><li><font face="Cambria">Sosyal Medya Uygulamaları</li></ol></span>
</div><br><br><br><br><br><br><br><br><b><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><h3 style="color: skyblue; margin-left: 80px;">Seçiminizi buradan yapabilirsiniz.</h3>
<form action="#" style="float: right;"><h3 style="color: skyblue; margin-right: 80px; margin-top: -70px; padding-bottom: 30px;">Bültenimize buradan kaydolabilirsiniz.</h3>
<fieldset style="margin-right: 80px; margin-top: -35px; width: 370px;"><legend style="color: green; font-size: large;">Üyelik</legend><label for="odak_1" style="color: green; margin: 25px;">Ad:</label><input id="odak_1" type="text" name="ad" style="margin-right: 70px;" onfocus="odaklan(this)" onblur="odaklanma(this)"><br><br>
<label for="odak_2" style="color: green; margin: 14px;">Soyad:</label><input id="odak_2" type="text" name="soyad" onfocus="odaklan(this)" onblur="odaklanma(this)"><br><br><label for="odak_3" style="color: green; margin: 8px;">e-Posta:</label><input id="odak_3" type="email" name="eposta" onfocus="odaklan(this)" onblur="odaklanma(this)"><br><br>
<label for="odak_4" style="color: green; margin: 13px;">Doğut:</label><input id="odak_4" type="date" name="dogut" onfocus="odaklan(this)" onblur="odaklanma(this)"><br><br><input type="submit" value="Kaydol" onclick="uyelikAl()"></fieldset></form><form action="#" method="get" style="color: green;"><label for="hizmetListesi" style="margin-left: 80px;">Hizmet seçiminizi buradaki listeden yapınız: </label><input list="hizmetler" name="hizmetListesi" id="hizmetListesi"><datalist id="hizmetler">
<option value="Siber Güvenlik"><option value="Yazılım"><option value="Oyun"><option value="Mobil Uygulama"></datalist><input type="submit" value="Seç" onclick="yeniPencereAc()"></form><br><br><table border="1" height="25" width="400" align="left" onmouseover="belirt()" onmouseout="belirtme()" style="margin-left: 80px;">
<tr><td colspan="5" align="center" height="30"><font color="green">Fırsatlar (<span id="belirti"><cite>Tüm seçimlerde geçerlidir</cite></span>)</font></td></tr><tr><td width="100" height="25" align="center"><font face="Cambria" color="#FFFFFF"></font></td><td width="100" height="25" align="center"><font face="Cambria" color="#FFFFFF">Ay</font></td>
<td width="100" height="25" align="center"><font face="Cambria" color="#FFFFFF">Tasarruf</font></td></tr><tr><td width="100" height="25" align="center"><font face="Cambria" color="#FFFFFF">1</font></td>
<td width="100" height="25" align="center"><font face="Cambria" color="#FFFFFF">Şubat</font></td><td width="100" height="25" align="center"><font face="Cambria" color="green">400₺</font></td></tr><tr><td width="100" height="25" align="center"><font face="Cambria" color="#FFFFFF">2</font></td><td width="100" height="25" align="center"><font face="Cambria" color="#FFFFFF">Eylül</font></td>
<td width="100" height="25" align="center"><font face="Cambria" color="green">450₺</font></td></tr></table><br><br><br><br><br><br><br><br><br><br><br><div class="dorduncu_bicim">𐰔𐰢𐰣𐰃∶𐰘𐰇𐰲𐰀∶𐱅𐰭𐰼𐰃∶𐰯𐰖𐰞𐱁𐱃𐰺𐰺∶𐰃𐰘𐰃∶𐰋𐰀∶𐰚𐰇𐱅𐰇∶𐰏𐰇𐰤𐰠𐰼𐰃∶𐰃𐰤𐰽𐰣𐰞𐰺∶𐰺𐰽𐰦𐰀∶𐰘𐰃𐰤𐰀∶𐰆∶𐰓𐰇𐰦𐰼𐰼∶𐰑𐰆𐰞𐱁𐱃𐰺𐰺∶𐰚𐰃𐱁𐰃𐰆𐰍𐰞𐰣𐰣∶𐰚𐰯𐰾𐰃∶𐰇𐰠𐰢𐰚∶𐰱𐰃𐰤∶𐰑𐰆𐰍𐰺∶𐰇𐰠𐰢𐰾𐰔∶𐰆𐰞𐰣∶𐰖𐰞𐰭𐰔∶𐰘𐰇𐰲𐰀∶𐱅𐰭𐰼𐰃𐰓𐰼∶𐰉𐰆𐰨𐰀∶𐱅𐰇𐰼𐰘𐰃∶𐰓𐰇𐰔𐰤𐰃∶𐰴𐰔𐰦𐰶𐱃𐰣∶𐰽𐰆𐰭𐰺𐰀∶𐰚𐰇𐰲𐰜∶𐰴𐰺𐰓𐱁𐰢∶𐰚𐰇𐰠∶𐱅𐰃𐰏𐰤∶𐰇𐰡𐰇∶𐰚𐰇𐰠∶𐱅𐰃𐰏𐰤∶𐰶𐰃𐰺𐰴∶𐰘𐰃𐰓𐰃∶𐰖𐱁𐰦𐰀∶𐰯𐰆𐰽𐰞𐰆∶𐰉𐰆𐰞𐱃∶𐰺𐰑𐰦𐰀∶𐰆𐰲𐰯∶𐰴𐰖𐰉𐰆𐰞𐰯∶𐰏𐰃𐱅𐱅𐰃∶𐰋𐰤∶𐰇𐰔𐰦𐰠𐰼𐰀∶𐰖𐰽𐰞𐰺𐰀∶𐰉𐰆𐰍𐰡𐰢∶𐰏𐰇𐰼𐰼∶𐰏𐰇𐰔𐰢∶𐰏𐰇𐰼𐰢𐰔∶𐰏𐰃𐰋𐰃∶𐰋𐰃𐰠𐰼∶𐰴𐰞𐰢∶𐰋𐰃𐰠𐰢𐰔∶𐰏𐰃𐰋𐰃∶𐰆𐰡𐰆∶𐰇𐰘𐰠𐰀∶𐰓𐰼𐰭∶𐰓𐰇𐱁𐰨𐰠𐰼𐰀∶𐰑𐰡𐰢∶𐰏𐰇𐰔𐰢𐰓𐰤∶𐰖𐱁∶𐰏𐰠𐰾𐰀∶𐰴𐱃𐰢𐰖𐰺𐰴∶𐰏𐰇𐰭𐰡𐰤∶𐰍𐰞𐰢𐰴∶𐰏𐰠𐰾𐰀∶𐰽𐰆𐰽𐱃𐰺𐰯∶𐰖𐰣𐰺𐰴∶𐰲𐰸∶𐰓𐰼𐰭∶𐰓𐰇𐱁𐰨𐰠𐰼𐰀∶𐰑𐰡𐰢∶𐰋𐰘𐰠𐰼𐰢𐰤∶𐰆𐰞𐰽𐰢𐰣∶𐰘𐰃𐰏𐰤𐰢𐰤∶𐰆𐰍𐰞𐰢𐰣∶𐰲𐰆𐰲𐰸𐰞𐰺𐰢𐰣∶𐰏𐰇𐰔𐰇∶𐰴𐱁𐰃∶𐰲𐰖𐰞𐰀∶𐰲𐱃𐰞𐰲𐰴∶𐰲𐰸∶𐰚𐰇𐱅𐰇∶𐰋𐰀∶𐰯𐰼𐱁𐰣∶𐰆𐰞𐰲𐰴∶𐰓𐰃𐰘𐰀∶𐰓𐰇𐱁𐰨𐰠𐰼𐰢∶𐰴𐱃𐰡𐰃∶𐰴𐰡𐰃∶𐰚𐰼∶𐰢𐰃𐰠𐰠𐱅𐱅𐰤∶𐰖𐰽𐰲𐰞𐰺∶𐰍𐰞𐰖𐰲𐰞𐰺∶𐰏𐰡𐰃∶𐱃𐰔𐰘𐰀∶𐰱𐰃𐰤∶𐰯𐰔𐰞𐰀∶𐰯𐰔𐰞𐰀∶𐰴𐰔𐰤𐰠𐰼∶𐰡𐰣𐰞𐰺∶𐰋𐰀∶𐰏𐰇𐰢𐱁𐰠𐰼𐰠𐰀∶𐰉𐱁𐰴𐰀∶𐰓𐰋𐰠𐱅𐰠𐰼𐰓𐰤∶𐰘𐰇𐰭𐱅𐰱𐰠𐰼∶𐰋𐰔𐰼𐰠𐰼∶𐰃𐰠𐰲𐰠𐰼∶𐰸𐰆𐰢𐱃𐰣𐰞𐰺∶𐰏𐰡𐰃∶𐰲𐰃𐰤∶𐰴𐰍𐰣𐰦𐰣∶𐰼𐰾𐰽𐰢𐰞𐰺∶𐰃𐰾𐱅𐰓𐰢∶𐰉𐰭𐰀∶𐰚𐰦𐰃∶𐰼𐰾𐰽𐰢𐰣𐰃∶𐰏𐰇𐰦𐰼𐰓𐰃
𐰘𐰃𐰏𐱅∶𐰴𐰺𐰓𐱁𐰢𐰤∶𐰖𐰽∶𐱅𐰇𐰼𐰤𐰤𐰃∶𐱃𐰢𐰢𐰞𐰑𐰶∶𐰆𐰭𐰀∶𐰖𐰴𐱁𐰲𐰴∶𐰯𐰺𐰴𐰞𐰃∶𐰋𐰃𐰼∶𐱅𐰇𐰼𐰋𐰀∶𐰖𐰯𐱃𐰺𐰑𐰶∶𐰋𐰃𐰤𐰣𐰣∶𐰱𐰃𐰤𐰃∶𐰑𐰃𐱁𐰣𐰃∶𐰾𐰇𐰾𐰠𐰘𐰯∶𐰋𐰔𐰓𐰚∶𐰏𐰇𐰔∶𐰞𐰲𐰃∶𐰼𐰾𐰢𐰠𐰼𐰠𐰀∶𐰑𐰆𐰣𐱃𐱃𐰶∶𐰑𐰣𐰀∶𐰇𐰠𐰢𐰾𐰔∶𐱃𐱁∶𐰖𐰆𐰦𐱃𐰺𐰑𐰸∶𐰏𐰇𐰭𐰠𐰢𐰓𐰚𐰃∶𐰾𐰇𐰔𐰠𐰼𐰃∶𐰇𐰾𐱅𐰤𐰀∶𐰖𐰔𐰯∶𐰓𐰃𐰚𐱅𐰚∶𐰾𐰃𐰔∶𐰓𐰀∶𐰆𐰣𐰆∶𐰏𐰇𐰼𐰤∶𐰋𐰇𐰘𐰠𐰲𐰀∶𐰋𐰃𐰠𐰤∶𐰘∶𐰋𐰤𐰢∶𐱅𐰇𐰼𐰜∶𐰢𐰃𐰠𐰠𐱅𐰢𐰤∶𐰋𐰇𐱅𐰤∶𐰋𐰘𐰠𐰼𐰃∶𐰘𐰇𐰭𐱅𐰱𐰠𐰼𐰃∶𐰆𐱃𐰔∶𐰉𐰆𐰖𐰑𐰣∶𐰆𐰞𐱁𐰣∶𐱃𐱃𐰺∶𐰢𐰃𐰠𐰠𐱅𐰢𐰤∶𐰑𐰸𐰆𐰔∶𐰉𐰆𐰖𐰑𐰣∶𐰆𐰞𐱁𐰣∶𐰆𐰍𐰔∶𐰢𐰃𐰠𐰠𐱅𐰢𐰤∶𐰋𐰘𐰠𐰼𐰃∶𐰉𐰆𐰖𐰺𐰸∶𐰋𐰘𐰠𐰼𐰃∶𐰾𐰃𐰔∶𐰓𐰀∶𐰇𐰔𐰠𐰠𐰚𐰠𐰀∶𐱁𐰆∶𐰾𐰇𐰔𐰠𐰼𐰢𐰃∶𐰃𐰘𐰱𐰀∶𐰃𐱁𐱅𐰤∶𐰲𐰣∶𐰸𐰆𐰞𐰍𐰖𐰞𐰀∶𐰓𐰃𐰭𐰠𐰘𐰤∶𐰆𐰞𐰽𐰢𐰞𐰀∶𐰃𐰘𐰃∶𐰋𐰀∶𐰖𐰴𐰦𐰣∶𐰃𐰠𐰏𐰠𐰤𐰤∶𐰆𐰣𐰆∶𐰋𐰾𐰠𐰘𐰤∶𐰋𐰇𐰘𐱅𐰤∶𐰏𐱅𐰤∶𐰘𐰃𐱅𐱁𐱅𐰼𐰤∶𐰴𐰞𐰴𐰦𐰺𐰣∶𐰘𐰇𐰲𐰡𐰤∶𐰘𐰜𐰾𐰡𐰤∶𐰽𐰴𐰣∶𐰆𐰞𐰀∶𐰚𐰃∶𐰢𐰃𐰠𐰠𐱅𐰢𐰃∶𐰔𐰢𐰘𐰤∶𐰇𐰔𐰢𐰘𐰤∶𐰃𐰨𐱅𐰢𐰘𐰤∶𐰆𐰭𐰀∶𐰽𐰶𐰃𐰦𐰃∶𐰋𐰃𐰼𐰢𐰘𐰤∶𐰔𐰀∶𐰲𐰯𐰀∶𐱅𐰢𐰘𐰤∶𐰲𐰃∶𐰲𐰚𐱅𐰼𐰢𐰘𐰤∶𐰔𐰆𐰺𐰀∶𐰸𐰆𐱁𐰢𐰖𐰣∶𐰢𐰃𐰠𐰠𐱅𐰢𐰃∶𐰽𐰶𐰢𐰖𐰣∶𐰽𐰶𐰃𐱁𐱃𐰺𐰢𐰖𐰣∶𐰢𐰃𐰠𐰠𐱅𐰢𐰀∶𐰘𐰜∶𐰆𐰞𐰢𐰖𐰣∶𐰇𐰔𐰼𐰦𐰤∶𐰍𐰺∶𐰘𐰜𐰠𐰼𐰃∶𐰴𐰡𐰺𐰣</div>
<h3 id="yararli_baglanti" class="ikinci_bicim">Yararlı Bağlantılar:</h3><div class="iframe_bicim"><iframe src="https://www.ttk.gov.tr" title="Türk Tarih Kurumu" width="748px" height="270px" style="float: left; border: 2px dotted green;"></iframe>
<iframe src="http://www.tdk.org.tr" title="Türk Dil Kurumu" width="748px" height="270px" style="float: right; border: 2px dotted green;"></iframe><br></div><br><br><br><hr><footer style="bottom: 0%; position: static; right: 4px; font-size: small; font-family: Cambria;" dir="rtl">
<p style="color: green;">𐰴𐰞𐰸∶𐰲𐰍𐱃𐰖∶𐰽𐰺𐰃𐰆𐰍𐰞𐰆<br><a href="mailto:hcs@abrayazilim.com" style="color: green;">hcs@abrayazilim.com</a></p></footer><br><div id="kayan_yazi"><marquee direction="rtl" onmouseover="this.stop()" onmouseout="this.start()">Yüksel ey Türk, senin için yükselmenin sınırı yoktur!</marquee></div>
</body></html>'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_belgesi, "html.parser")
sonuc = soup.prettify()
sonuc = soup.div.name
sonuc = soup.h2.string
sonuc = soup.find_all("a")
sonuc = soup.find_all("a")[3]
sonuc = soup.find_all("div")[1].ul.find_all("li")

sonuc = soup.ul.findChildren()
sonuc = soup.div.findNextSibling()


print(sonuc)
