from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re

class Enemy:
    name = ""
    hp = 0
    ac = 0
    speed = 0

    URL = None

    def __init__(self,URL=None) -> None:
        self.URL = URL
        self.getData(self.URL)

    def getData(self,URL=None):  
        try:  
            session = HTMLSession()
            page = session.get(URL)
            session.close()

            soup = BeautifulSoup(page.content,"html.parser")

            name = str(soup.find("a",class_="mon-stat-block__name-link").get_text()).strip()

            self.name = name

            stats = str(soup.find("div",class_="mon-stat-block__attributes").getText)
            
            HP = re.search(pattern="\dd([0-1]?[0-9]|20) \+ \d",string=stats).group(0)
            self.hp = HP

            AC = re.search(pattern="[0-1]?[0-9]",string=stats).group(0)
            self.ac = AC

            S = re.search(pattern="\d\d ft.",string=stats).group(0)
            self.speed = S
        except Exception as e:
            print("Stránka nenalezena")
            exit(1)

    def getStats(self):
        print(f"Name: {self.name}, HP: {self.hp}, AC: {self.ac}, Speed: {self.speed}")