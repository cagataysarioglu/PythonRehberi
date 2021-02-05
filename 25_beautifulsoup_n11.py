import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.find_all("li", {"class":"column"}, limit= 10)

say = 0

for li in liste:
    urunBilgisi = li.div.a.h3.text.strip()
    urunFiyati = li.find("div", {"class":"proDetail"}).find("a", {"class":"newPrice"}).ins.text.strip().strip("TL")

    say += 1
    print(f"{say}- Ürün: {urunBilgisi.ljust(70)} / Fiyat: {urunFiyati}")
