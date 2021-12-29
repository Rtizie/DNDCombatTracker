from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re

class Enemy:
    name = ""
    hp = 0
    ac = 0
    speed = 0

    strg = 0
    strM = 0
    dex = 0
    dexM = 0
    wis = 0
    wisM = 0
    con = 0
    conM = 0
    inte = 0
    intM = 0
    cha = 0
    chaM = 0

    URL = None

    def __init__(self,URL=None) -> None:
        self.URL = URL
        self.getData(self.URL)

    def getData(self,URL=None):  
        try:  
            session = HTMLSession()
            page = session.get(URL)
            soup = BeautifulSoup(page.content,"html.parser")
            session.close()

            #Information

            name = str(soup.find("a",class_="mon-stat-block__name-link").get_text()).strip()
            self.name = name

            stats = str(soup.find("div",class_="mon-stat-block__attributes").getText)
            
            HP = re.search(pattern="\dd([0-1]?[0-9]|20) \+ \d",string=stats).group(0)
            self.hp = HP

            AC = re.search(pattern="[0-1]?[0-9]",string=stats).group(0)
            self.ac = AC

            S = re.search(pattern="\d\d ft.",string=stats).group(0)
            self.speed = S

            #Ability Stats
            abStats = soup.find("div",class_="ability-block")

            strDiv = abStats.find("div",class_="ability-block__stat--str")
            STR = strDiv.find("div",class_="ability-block__data")
            self.strg = STR.find("span",class_="ability-block__score").get_text()
            self.strM = STR.find("span",class_="ability-block__modifier").get_text()
            print(f"{self.strg},{self.strM}")

            dexDiv = abStats.find("div",class_="ability-block__stat--dex")
            DEX = dexDiv.find("div",class_="ability-block__data")
            self.dex = DEX.find("span",class_="ability-block__score").get_text()
            self.dexM = DEX.find("span",class_="ability-block__modifier").get_text()
            print(f"{self.dex},{self.dexM}")

            wisDiv = abStats.find("div",class_="ability-block__stat--wis")
            WIS = wisDiv.find("div",class_="ability-block__data")
            self.wis = WIS.find("span",class_="ability-block__score").get_text()
            self.wisM = WIS.find("span",class_="ability-block__modifier").get_text()
            print(f"{self.wis},{self.wisM}")

            conDiv = abStats.find("div",class_="ability-block__stat--con")
            CON = conDiv.find("div",class_="ability-block__data")
            self.con = CON.find("span",class_="ability-block__score").get_text()
            self.conM = CON.find("span",class_="ability-block__modifier").get_text()
            print(f"{self.con},{self.conM}")

            intDiv = abStats.find("div",class_="ability-block__stat--int")
            INT = intDiv.find("div",class_="ability-block__data")
            self.inte = INT.find("span",class_="ability-block__score").get_text()
            self.intM = INT.find("span",class_="ability-block__modifier").get_text()
            print(f"{self.inte},{self.intM}")

            chaDiv = abStats.find("div",class_="ability-block__stat--cha")
            CHA = chaDiv.find("div",class_="ability-block__data")
            self.cha = CHA.find("span",class_="ability-block__score").get_text()
            self.chaM = CHA.find("span",class_="ability-block__modifier").get_text()
            print(f"{self.cha},{self.chaM}")

        except Exception as e:
            print("Stránka nenalezena")
            exit(1)

    def getStats(self):
        return f"Name: {self.name}, HP: {self.hp}, AC: {self.ac}, Speed: {self.speed}"