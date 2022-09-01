from re import L
import requests
from bs4 import BeautifulSoup
url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser")

liste=soup.find_all("li",{"class":"column"},limit=1)
for li in liste:
    name=li.div.a.h3.text.strip()
    link=li.div.a.get("href")
    oldPrice=li.find("div",{"class":"priceContainer"}).find_all("span")[0].text
    newPrice=li.find("div",{"class":"priceContainer"}).find_all("span")[2].text
    print(f"name: {name} \nlink: {link} \nold price: {oldPrice} \nnew price: {newPrice}")
    