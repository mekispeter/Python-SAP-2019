"""
    pong
    Python SAP tananyag
    Skool 2019

    Pygame játék dinamikus objektumgenerálás nélkül.
    Elkészítési idő: kb. 1-2 alkalom.
    Játékmenet: Két játékos billentyűkkel mozgatja jobbra-balra az ütőket
    a kijelző két oldalán, a labda pedig közöttük pattog. Ha a labda eléri a
    kijelző szélét, a találatszámláló ugrik egyet, és a labda középről indul
    újra.

    Továbbfejlesztési lehetőségek:
    - design: más színek, ütőformák, labda helyett angry bird stb.
    - ütő szélénél más szögben pattan a labda
    - választható ütőméret és labdasebesség
    - négy ütő (egy-egy "csatárként" elöl)
    - faltenisz verzió
"""

import sys
import pygame as pg
import random as r

def mozdulj():
    labda_hely.centerx += sebesseg_x
    labda_hely.centery += sebesseg_y

def figyeld_az_esemenyeket():
    for esemeny in pg.event.get():
        # Ablak kiixelése.
        if esemeny.type == pg.QUIT:
            sys.exit()

def figyeld_a_szeleket():
    if labda_hely.centerx < 20 or  940 < labda_hely.centerx:
        return sebesseg_x * -1, sebesseg_y
    elif labda_hely.centery < 20 or 700 < labda_hely.centery:
        return sebesseg_x, sebesseg_y * -1
    else:
        return sebesseg_x, sebesseg_y

def frissitsd_a_kijelzot():
    kijelzo.fill(hatterszin)
    kijelzo.blit(labda_jelmez, labda_hely)
    pg.display.flip()

pg.init()
meret = (960, 720)
kijelzo = pg.display.set_mode(meret)
hatterszin = (15, 15, 60)
pg.display.set_caption("Skool Labdás")
ora = pg.time.Clock()

labda_jelmez = pg.image.load("labda.png")
labda_hely = labda_jelmez.get_rect()
labda_hely.centerx = 480
labda_hely.centery = 360
sebesseg_x = 9
sebesseg_y = 3

while True:
    figyeld_az_esemenyeket()
    sebesseg_x, sebesseg_y = figyeld_a_szeleket()
    mozdulj()
    frissitsd_a_kijelzot()
    ora.tick(30)
