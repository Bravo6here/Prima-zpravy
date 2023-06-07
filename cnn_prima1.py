from bs4 import BeautifulSoup
import requests

site = BeautifulSoup(requests.get("https://cnn.iprima.cz/").text, "html.parser")
all_a = site.find_all("a", class_="ccf-item-title") # ccf-item-title    text-white
for a in all_a:
    print(a.text)
    print(a.get("href"))
    print("\n")