import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.find("tbody", {"class":"lister-list"}).find_all("tr", limit= 70)
say = 0

for tr in liste:
    filmBasligi = tr.find("td", {"class":"titleColumn"}).find("a").text
    filmYili = tr.find("td", {"class":"titleColumn"}).find("span").text.strip("()")
    filmReytingi = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text
    say += 1
    
    print(f"{say}- Film: {filmBasligi.ljust(55)} / Yıl: {filmYili} / Puan: {filmReytingi}")

