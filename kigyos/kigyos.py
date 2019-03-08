"""
    Kígyós
    Python SAP tananyag
    Skool 2019

    Pygame játék mérsékelt mennyiségű dinamikus objektumgenerálással,
    érintésfigyelés nélkül.
    Elkészítési idő: kb. 2 alkalom.
    Játékmenet: A játékos billentyűkkel mozgatja egy griden a kígyó fejét,
    amit követ a kígyó egyre hosszabb teste. A játéktéren random helyeken
    megjelennek fánkok, ha ezekkel érintkezik a kígyó feje, a kígyó teste
    növekszik. A játék addig tart, amíg a kígyó bele nem ütközik a saját testébe.

    Továbbfejlesztési lehetőségek a hasonló játékok logikája szerint:
    - falak a játéktéren (pályák)
    - különböző minőségű fánkok
    - az FPS növekszik
    - kétjátékosos mód: kigyo1, kigyo2
    - önjáró kígyó bot
    - irányítás csak bal és jobb gombbal, relatív irányváltásokkal (fordulj
      balra / fordulj jobbra) 
    stb.
"""

# Ezek a szokásos csomagok, minden pygame projektben importáljuk őket.
import pygame as pg
import sys
import random as r

"""
    Ez a kiinduló szereplőosztályunk, közös más projektekkel. A specifikus
    szereplőosztályok ennek az alosztályai lesznek.

    A "szereplő" és a "jelmez" kifejezések a Scratch-ből származnak, a "sprite"
    és a "costume" magyar megfelelői. Pygame terminológiában a jelmez egy
    surface objektum. A "hely" elnevezést jobb híján választottam a "rect"
    magyarítására.
"""
class Szereplo():
    def __init__(self, jelmeznevek, x, y):
        self.jelmezek = [pg.image.load(nev + ".png") for nev in jelmeznevek]
        self.jelmez = self.jelmezek[0]
        self.x = x
        self.y = y
    def jelenj_meg(self):
        self.hely = self.jelmez.get_rect()
        self.hely.center = (self.x, self.y)
        kijelzo.blit(self.jelmez, self.hely)

"""
    A kígyószelvény olyan szereplő, aminek egyetlen jelmeze van. Más speciális
    attribútuma nincs.
"""
class Szelveny(Szereplo):
    def __init__(self, x, y):
        Szereplo.__init__(self, ["szelveny"], x, y)
    def mozdulj(self, kinek_a_helyere):
        self.x = kinek_a_helyere.x
        self.y = kinek_a_helyere.y

"""
    A kígyófej is egyjelmezes szereplő. Sajátos irányítási metódusa van: egy
    szöveges irányparaméter dönti el, hogy változnak a koordinátái.
"""
class Fej(Szereplo):
    def __init__(self, x, y):
        Szereplo.__init__(self, ["fej"], x, y)
    def mozdulj(self, irany):
        if irany == "le":
            self.y += 30
            if self.y == 720:
                self.y = 30
        elif irany == "fel":
            self.y -= 30
            if self.y == 0:
                self.y = 690
        elif irany == "jobbra":
            self.x += 30
            if self.x == 960:
                self.x = 30
        elif irany == "balra":
            self.x -= 30
            if self.x == 0:
                self.x = 930

"""
    A kígyó egy összetett szereplő: fejből és szelvényekből áll, és még egy sor
    attribútumból. Az ellentétpárok határozzák meg, merre fordulhat és merre
    nem. Az iránya határozza meg a fej mozgását.
"""
class Kigyo():
    def __init__(self, hossz, x, y):
        self.fej = Fej(x, y)
        self.ellentetek = {"jobbra":"balra", "balra":"jobbra",
                            "fel":"le", "le":"fel"}
        self.irany = "jobbra"
        self.test = [self.fej]
        self.novekedj(hossz-1)
        # Azért mozdítjuk el a fejet, hogy ne ütközéssel induljon a játék.
        self.fej.mozdulj(self.irany)
    # Megjeleníti a fejet és a szelvényeket.
    def jelenj_meg(self):
        for szelveny in self.test:
            szelveny.jelenj_meg()
    # A fej a kígyó irányába mozdul, a többi szelvény pedig mind az előtte lévő
    # szelvény helyére kerül.
    def mozdulj(self):
        for i in range(len(self.test)-1, 0, -1):
            szelveny = self.test[i]
            szelveny_elotted = self.test[i-1]
            szelveny.mozdulj(szelveny_elotted)
        self.fej.mozdulj(self.irany)
    # Ezt a metódust hívjuk meg, ha billentyűnyomást érzékelünk. A kígyó csak
    # a jelenlegi irányával nem ellentétes irányba fordul.
    def fordulj(self, irany):
        if not irany == self.ellentetek[self.irany]:
            self.irany = irany
    # A kígyó úgy növekszik, hogy a végére új szelvények kerülnek. Ezek
    # kezdetben a korábbi utolsó szelvénnyel egy helyen vannak, aztán
    # fokozatosan elmozdulnak; ez kelti azt a benyomást, hogy az új szelvények
    # egyenként adódnak a kígyóhoz.
    def novekedj (self, hossz):
        vege = self.test[-1]
        for i in range(hossz):
            self.test.append(Szelveny(vege.x, vege.y))
    # "Ütközésfigyelés": van-e olyan szelvény, amely a fejjel azonos
    # koordinátákon van. A visszatérési érték Boolean típusú.
    def utkozol_e(self):
        valasz = False
        for szelveny in self.test[1:]:
            if self.fej.x == szelveny.x and self.fej.y == szelveny.y:
                valasz = True
        return valasz
    # Még egy "ütközésfigyelés": ha a fej és a fánk azonos koordinátákon van,
    # akkor a test növekszik, a fánk meg átkerül máshova.
    def egyel_ha_tudsz(self, fank):
        if self.fej.x == fank.x and self.fej.y == fank.y:
            self.novekedj(12)
            fank.reset()

# A fánk egy nagyon egyszerű sereplő. Nem mozog, csak az életciklusa végén
# mindig jelmezt vált és átkerül máshova.
class Fank(Szereplo):
    def __init__(self):
        Szereplo.__init__(self, ["1", "2", "3"], 0, 0)
        self.reset()
    # A fánk életciklusát a "kor" attribútom méri. Az életciklus végén a fánk
    # véletlenszerűen átkerül máshova, és jelmezt vált.
    def reset(self):
        self.jelmez = r.choice(self.jelmezek)
        self.x = r.randrange(1,32) * 30
        self.y = r.randrange(1,24) * 30
        self.kor = 0
    # Növeljük a "kor" attribútomot, amíg el nem érjük az életciklus végét.
    def frissits(self):
        self.kor += 1
        if self.kor == 30:
            self.reset()

# A billentyűfigyelés a megszokott módon.
def figyeld_a_billentyuket():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            elif event.key == pg.K_LEFT:
                kigyo.fordulj("balra")
            elif event.key == pg.K_RIGHT:
                kigyo.fordulj("jobbra")
            elif event.key == pg.K_UP:
                kigyo.fordulj("fel")
            elif event.key == pg.K_DOWN:
                kigyo.fordulj("le")

# A kígyó mozdul, a fánk várakozik, vagy arrébb ugrik.
def frissitsd_a_szereploket():
    kigyo.mozdulj()
    fank.frissits()

# Megjelenítjük az összes szereplőt, és frissítjük a kijelzőt.
def jelenitsd_meg_a_szereploket():
    kijelzo.fill(hatterszin)
    # A pont a kígyó mindenkori hossza.
    pont = betu.render("Pont: " + str(len(kigyo.test)), False, betuszin)
    kijelzo.blit(pont, (50,50))
    kigyo.jelenj_meg()
    fank.jelenj_meg()
    pg.display.flip()

# Intro: megjelenik a háttér és a cím, majd várunk két
# másodpercet.
def cim():
    kijelzo.fill(hatterszin)
    cim = betu.render("Kígyós játék", False, betuszin)
    kijelzo.blit(cim, (375,345))
    pg.display.flip()
    ora.tick(0.5)

# Outro: A kijelzőre (az eddigi kép törlése nélkül) kitesszük a végfeliratot,
# majd várunk két másodpercet.
def vege():
    vege = betu.render("Sajnos... :(", False, betuszin)
    kijelzo.blit(vege, (375,345))
    pg.display.flip()
    ora.tick(0.5)

# Létrehozzuk a Pygame működéséhez szükséges objektumokat.
pg.init()
kijelzo = pg.display.set_mode((960,720))
pg.display.set_caption("Kígyós játék")
hatterszin = (20,20,50)
betuszin = (180, 180, 60)
betu = pg.font.SysFont(pg.font.get_default_font(), 60)
ora = pg.time.Clock()

# Létrehozzuk a szereplőket.
kigyo = Kigyo(hossz=12, x=480, y=360)
fank = Fank()

# És most jön a voltaképpeni játék. Itt nincsenek technikai részletek,
# csak egy olyan kód, ami a játékmenet leírásaként is jól olvasható.
cim()
while not kigyo.utkozol_e():
    figyeld_a_billentyuket()
    frissitsd_a_szereploket()
    kigyo.egyel_ha_tudsz(fank)
    jelenitsd_meg_a_szereploket()
    ora.tick(3)
vege()
