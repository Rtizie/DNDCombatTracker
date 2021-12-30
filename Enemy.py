import tkinter as tk
import tkinter.ttk as ttk
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
import random as r

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

            dexDiv = abStats.find("div",class_="ability-block__stat--dex")
            DEX = dexDiv.find("div",class_="ability-block__data")
            self.dex = DEX.find("span",class_="ability-block__score").get_text()
            self.dexM = DEX.find("span",class_="ability-block__modifier").get_text()

            wisDiv = abStats.find("div",class_="ability-block__stat--wis")
            WIS = wisDiv.find("div",class_="ability-block__data")
            self.wis = WIS.find("span",class_="ability-block__score").get_text()
            self.wisM = WIS.find("span",class_="ability-block__modifier").get_text()

            conDiv = abStats.find("div",class_="ability-block__stat--con")
            CON = conDiv.find("div",class_="ability-block__data")
            self.con = CON.find("span",class_="ability-block__score").get_text()
            self.conM = CON.find("span",class_="ability-block__modifier").get_text()

            intDiv = abStats.find("div",class_="ability-block__stat--int")
            INT = intDiv.find("div",class_="ability-block__data")
            self.inte = INT.find("span",class_="ability-block__score").get_text()
            self.intM = INT.find("span",class_="ability-block__modifier").get_text()

            chaDiv = abStats.find("div",class_="ability-block__stat--cha")
            CHA = chaDiv.find("div",class_="ability-block__data")
            self.cha = CHA.find("span",class_="ability-block__score").get_text()
            self.chaM = CHA.find("span",class_="ability-block__modifier").get_text()

        except Exception as e:
            print("Stránka nenalezena")
            exit(1)

    def getStats(self):
        return f"Name: {self.name}, HP: {self.hp}, AC: {self.ac}, Speed: {self.speed}\n"
    
    def getAbilityBlock(self,frame):
        abilityBlocks = []
        STRblock = ttk.Button(frame, text=f"STR: {self.strg} {self.strM}", command=lambda: self.roll('STR'))
        DEXblock = ttk.Button(frame, text=f"DEX: {self.dex} {self.dexM}", command=lambda: self.roll('DEX'))
        CONblock = ttk.Button(frame, text=f"CON: {self.con} {self.conM}", command=lambda: self.roll('CON'))
        INTblock = ttk.Button(frame, text=f"INT: {self.inte} {self.intM}", command=lambda: self.roll('INT'))
        WISblock = ttk.Button(frame, text=f"WIS: {self.wis} {self.wisM}", command=lambda: self.roll('WIS'))
        CHAblock = ttk.Button(frame, text=f"CHA: {self.cha} {self.chaM}", command=lambda: self.roll('CHA'))
        INIblock = ttk.Button(frame, text=f"INI: 0 {self.dexM}", command=lambda: self.roll('INI'))
        
        abilityBlocks.append(STRblock)
        abilityBlocks.append(DEXblock)
        abilityBlocks.append(CONblock)
        abilityBlocks.append(INTblock)
        abilityBlocks.append(WISblock)
        abilityBlocks.append(CHAblock)
        abilityBlocks.append(INIblock)

        for block in abilityBlocks:
            block.pack(side=tk.LEFT)


        # Roll label
        self.rollLabel = ttk.Label(frame,text="Rolled")
        self.rollLabel.pack(side=tk.TOP)

    def roll(self,ability):
        throw = r.randint(1,20)
        match ability:
            case 'STR':
                if self.strM[1] == '+':
                    modifier = int(self.strM[2])
                    throw = throw + modifier
                elif self.strM[1] == '-':
                    modifier = int(self.strM[2])
                    throw = throw - modifier
            case 'CON':
                if self.conM[1] == '+':
                    modifier = int(self.conM[2])
                    throw = throw + modifier
                elif self.conM[1] == '-':
                    modifier = int(self.conM[2])
                    throw = throw - modifier
            case 'INT':
                if self.intM[1] == '+':
                    modifier = int(self.intM[2])
                    throw = throw + modifier
                elif self.intM[1] == '-':
                    modifier = int(self.intM[2])
                    throw = throw - modifier
            case 'CHA':
                if self.chaM[1] == '+':
                    modifier = int(self.chaM[2])
                    throw = throw + modifier
                elif self.chaM[1] == '-':
                    modifier = int(self.chaM[2])
                    throw = throw - modifier
            case 'DEX':
                if self.dexM[1] == '+':
                    modifier = int(self.dexM[2])
                    throw = throw + modifier
                elif self.dexM[1] == '-':
                    modifier = int(self.dexM[2])
                    throw = throw - modifier
            case 'INI':
                if self.dexM[1] == '+':
                    modifier = int(self.dexM[2])
                    throw = throw + modifier
                elif self.dexM[1] == '-':
                    modifier = int(self.dexM[2])
                    throw = throw - modifier
            case 'WIS':
                if self.wisM[1] == '+':
                    modifier = int(self.wisM[2])
                    throw = throw + modifier
                elif self.wisM[1] == '-':
                    modifier = int(self.wisM[2])
                    throw = throw - modifier

        self.rollLabel.config(text=f"Rolled:{str(throw)}")