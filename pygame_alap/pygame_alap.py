"""
    Pygame alapkód, játékokhoz indulásnak
    Python SAP tananyag
    Skool 2019

    Ennek az kiinduló kódnak a bővítésével könnyen és gyorsan tudtok különféle
    játékokat létrehozni. Ebben a verzióban már tudatos osztályhasználat van:
    a szereplők a Szereplo osztály példányai. A kód logikája bizonyos mértékig
    a Scratch-et követi.
"""

# A sys modul a kilépéshez kell.
import sys
# Véletlengenerálás szinte minden játékhoz kell. Javasolt függvények:
# r.randrange() egész számot ad; r.choice() listából választ véletlen elemet.
import random as r
# Ez a Pygame csomag, mindent tartalmaz, amire szükségünk lesz.
import pygame as pg

# Az event.get() egy eseménylistát ad, amelyben benne vannak az előző hívás óta
# történt egér- és billentyűesemények, valamint az ablak kiikszelése is.
def kezeld_az_esemenyeket():
    for esemeny in pg.event.get():
        if esemeny.type == pg.QUIT:
            sys.exit()
        elif esemeny.type == pg.KEYDOWN:
            if esemeny.key == pg.K_ESCAPE:
                sys.exit()

# Itt történhet a szereplőmozgatás mellett pl. az ütközésfigyelés is.
def frissitsd_a_szereploket():
    for szereplo in szereplok:
        szereplo.mozdulj()

# A szereplők sorban kerülnek fel a kijelzőre; a lista későbbi elemei kitakarják
# a korábbiakat. Ha ezen változtatni akartok, módosítsátok a szereplők sorrendjét
# a listában.
def jelenitsd_meg_a_szereploket():
    jatekter.fill(hatterszin)
    for szereplo in szereplok:
        szereplo.jelenj_meg()
    pg.display.flip()

"""
    A szereplő fogalma valószínűleg a résztvevők többsége számára ismerős lesz a
    Scratch-ből és társaiból. A jelmez szót is a Scratch-ből kölcsönöztem.

    Bizonyos játékoknál érdemes lesz majd alosztályokat létrehozni, pl:
      Class Ellenseg(Szereplo)
          def __init__(self):
              Szereplo.__init__(self, ["ellenseg"], r.randrange(50, 911), 0, 0, 5)
              ...
    Ekkor az ellenséges szereplők egységesen fognak kinézni és viselkedni, és
    igény szerint további attribútumokat és metódusokat adhatunk nekik.

    Sok játékban hatékonyabb, ha a szereplőnek nem két sebességvektora, hanem
    sebessége és iránya van. Ekkor szükség lesz egy minimális trigonometriára,
    amihez a kód elején importálni kell a math csomagot:
    import math as m
    Az alosztály definíciójában pedig két új attrribútumot vezetünk be, és
    felülírjuk a mozgatási metódust:
      Class Labda(Szereplo)
          def __init__(self, jelmeznevek, x, y, irany, sebesseg):
              Szereplo.__init__(self, jelmeznevek, x, y)
              self.irany = irany
              self.sebesseg = sebesseg
              ...
          def mozdulj(self):
              self.x += self.sebesseg * m.cos(m.radians(self.irany))
              self.y += self.sebesseg * m.sin(m.radians(self.irany))
    Innentől fogva gondolkodhatunk x és y helyett szögekben.
"""
class Szereplo():
    def __init__(self, jelmeznevek, x, y, sebesseg_x = 0, sebesseg_y = 0):
        # Jelmezgenerálás.
        # Egy egyszerűbb lehetőség, ha tudjuk, hogy csak egy jelmeze lesz minden
        # szereplőnknek:
        # __init(self, jelmeznev, ...)
        # self.jelmez = pg.image.load(jelmeznev + ".png")
        self.jelmezek = []
        for jelmeznev in jelmeznevek:
            self.jelmezek.append(pg.image.load(jelmeznev + ".png"))
        # Ha a listakomprehenzióval sikerül megbírkózni, akkor ezt sokkal
        # egyszerűbben is lehet:
        # [pg.image.load(jelmeznev + ".png") for jelmeznev in jelmeznevek]
        self.jelmez = self.jelmezek[0]
        # A szereplő koordinátái.
        self.x = x
        self.y = y
        # Ha nem mozognak a szereplők, akkor ezt el is lehet hagyni. Ez a
        # kattintgatós játékokban lehet hasznos egyszerűsítés, mint például a
        # szajmonszez.
        self.sebesseg_x = sebesseg_x
        self.sebesseg_y = sebesseg_y
    # Megjelenítés előtt frissítjük a szereplő koordinátáit.
    def mozdulj(self):
        self.x += self.sebesseg_x
        self.y += self.sebesseg_y
    # A megjelenítéshez frissítjük a szereplő rect-jét. Ezt azért érdemes
    # ilyenkor intézni, hogy menet közben tudjunk jelmezt váltani, kicsinyíteni,
    # forgatni stb. A rect-et jobb híján nevezem helynek.
    def jelenj_meg(self):
        self.hely = self.jelmez.get_rect()
        self.hely.centerx = self.x
        self.hely.centery = self.y
        jatekter.blit(self.jelmez, self.hely)

# Az összes Pygame modult egyszerre inicializáljuk. A legtöbb ezt akár el is
# lehetne hagyni, mert az objektumok létrehozásával a háttérben
# inicializálódnak a modulok, de nem mindig, és ez váratlan hibák forrása lehet.
pg.init()

# Léthrehozzuk a pygame kijelzőjét. A játéktér szó is a Scratch-ből van. Ha
# egész képernyős játékot szeretnénk, akkor kell még egy paraméter:
# pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
meret_x = 960
meret_y = 720
jatekter = pg.display.set_mode((meret_x, meret_y))

# Ez az ablak tetején jelenik meg (window title). Menet közben is módosítható.
pg.display.set_caption("játék neve")

# Interneten tudtok RGB-kódokat keresni. Képből a Gimp color pickerével tudtok
# RGB-kódot kinyerni. Ha nem egyszínű hátteret akartok, akkor a szereplőlista
# első eleme lehet egy háttérkép.
hatterszin = (30, 30, 70)

# Az általános time csomag helyett érdemes a Pygame saját time modulját
# használni. Ebben is van sleep(), csak másodperc helyett ezredmásodpercet vár;
# a tick() pedig FPS-t (Hz-et): hány ciklus menjen le egy másodperc alatt.
# Valószínűleg a résztvevők többsége ismeri videojátékokból vagy
# máshonnan az FPS fogalmát. Scratch-ben az FPS kb. 30.
ora = pg.time.Clock()

# Létrehozunk egy új szereplőt, és betesszük a játék szereplőlistájába.
labda = Szereplo(["labda"], 480, 360, 1, 1)

# Ide kerülnek a szereplők. Később a lista dinamikusan alakítható, ahogy
# létrehozunk és törlünk szereplőket. Ha szereplőkategóriákra is szükség
# lesz egy játékban, akkor ezt fel lehet bontani: ellensegek, lovedekek stb.,
# és akkor ha például kijelzéskor ezeket összevonni.
szereplok = [labda]

# A játék fő ciklusa. Ide ne tegyetek apróságokat, csak olyan függvényhívások
# kerüljenek bele, amik a játékmenet egészét befolyásolják. Minden más kerüljön
# az innen meghívott függvényekbe.
jatek_vege = False
while not jatek_vege:
    kezeld_az_esemenyeket()
    frissitsd_a_szereploket()
    jelenitsd_meg_a_szereploket()
    ora.tick(30)
