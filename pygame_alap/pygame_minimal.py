"""
    Pygame minimálkód
    Python SAP tananyag
    Skool 2019

    Ezzel a kóddal már lehet egyszerű játékokat készíteni, de csak kevés
    szereplővel, mert mindent példányonként külön kell megírni. A "pygame_alap"
    verzióban már tudatos osztályhasználat van; az sokkal alkalmasabb
    kiindulópont a játékkészítéshez.
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

# A szereplők sorban kerülnek fel a kijelzőre; a lista későbbi elemei kitakarják
# a korábbiakat. Ha ezen változtatni akartok, módosítsátok a szereplők sorrendjét
# a listában.
def jelenitsd_meg_a_szereploket():
    jatekter.fill(hatterszin)
    labda_hely = labda_jelmez.get_rect()
    labda_hely.centerx = labda_x
    labda_hely.centery = labda_y
    jatekter.blit(labda_jelmez, labda_hely)
    pg.display.flip()

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

# Létrehozunk egy új szereplőt.
labda_jelmez = pg.image.load("labda.png")
labda_x = 460
labda_y = 360
labda_sebesseg_x = 1
labda_sebesseg_y = 1

# A játék fő ciklusa.
jatek_vege = False
while not jatek_vege:
    kezeld_az_esemenyeket()
    labda_x += labda_sebesseg_x
    labda_y += labda_sebesseg_y
    jelenitsd_meg_a_szereploket()
    ora.tick(30)
