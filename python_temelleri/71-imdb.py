
import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
html_doc=requests.get(url).content

soup=BeautifulSoup(html_doc,"html.parser")
list=soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=65)
count=1
for tr in list:
    title=tr.find("td",{"class":"titleColumn"}).find("a").text
    year=tr.find("td",{"class":"titleColumn"}).find("span").text
    rating=tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    print(f"{count}-){title}{year} IMDB:{rating}")
    count+=1
    

