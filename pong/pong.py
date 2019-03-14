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

# Ezek a szokásos csomagok, minden pygame projektben importáljuk őket.
import sys
import pygame as pg
import random as r

"""
    Ez egy általános szereplőosztály. Nagyrészt közös más projektekkel. A
    specifikus szereplőosztályok ennek az alosztályai lesznek.

    A "szereplő" és a "jelmez" kifejezések a Scratch-ből származnak, a "sprite"
    és a "costume" magyar megfelelői. Pygame terminológiában a jelmez egy
    surface objektum. A "hely" elnevezést jobb híján választottam a "rect"
    magyarítására.
"""
class Szereplo():
    def __init__(self, jelmeznev, x, y, sebesseg_x = 0, sebesseg_y = 0):
        self.jelmez = pg.image.load(jelmeznev + ".png")
        self.hely = self.jelmez.get_rect()
        self.x = x
        self.y = y
        self.sebesseg_x = sebesseg_x
        self.sebesseg_y = sebesseg_y
        # A pontot csak az ütőknél fogjuk használni.
        self.pont = 0
    # Beállítjuk a szereplő vízszintes és függőleges koordinátáit.
    def mozdulj(self):
        self.x += self.sebesseg_x
        self.y += self.sebesseg_y
    # Elhelyezzük a kijelzőn a szereplőt.
    def jelenj_meg(self):
        # A hely frissítésére tulajdonképpen ebben a játékban nem lenne
        # szükség, mert a szereplők nem forognak, nem nőnek-zsugorodnak, és nem
        # váltanak jelmezt. mégis egyszerűbb itt hagyni, mert nem lassítja a
        # játékot, és egy esetleges fejlesztéskor hasznos lehet.
        self.hely = self.jelmez.get_rect()
        self.hely.centerx = self.x
        self.hely.centery = self.y
        # A "blit" helyezi el a kijelzőben a jelmez-hely párost.
        kijelzo.blit(self.jelmez, self.hely)

# Pygame eseménykezelés. a get() a két hívás között történt események listáját
# adja vissza.
def kezeld_a_billentyuket():
    for esemeny in pg.event.get():
        # Ablak kiixelése.
        if esemeny.type == pg.QUIT:
            sys.exit()
        elif esemeny.type == pg.KEYDOWN:
            # Kilépés Esc-re.
            if esemeny.key == pg.K_ESCAPE:
                sys.exit()
            # bal uto fel
            elif esemeny.key == pg.K_w:
                bal_uto.sebesseg_y = -8
            # bal ütő le
            elif esemeny.key == pg.K_s:
                bal_uto.sebesseg_y = 8
            # jobb ütő fel
            elif esemeny.key == pg.K_UP:
                jobb_uto.sebesseg_y = -8
            # jobb ütő le
            elif esemeny.key == pg.K_DOWN:
                jobb_uto.sebesseg_y = 8
        elif esemeny.type == pg.KEYUP:
            # jobb ütő megáll
            if esemeny.key in [pg.K_w, pg.K_s]:
                bal_uto.sebesseg_y = 0
            # bal ütő megáll
            elif esemeny.key in [pg.K_UP, pg.K_DOWN]:
                jobb_uto.sebesseg_y = 0

# A labda számos helyen válthat irányt vagy pozíciót:
def figyeld_az_utkozeseket():
    # Labda vs bal ütő. (Azért kell azt is nézni, hogy a sebessége
    # negatív legyen, hogy ne kezdjen el az ütőben rezegni.)
    if labda.hely.colliderect(bal_uto.hely) and labda.sebesseg_x < 0:
        labda.sebesseg_x *= -1
    # Labda vs. jobb ütő.
    elif labda.hely.colliderect(jobb_uto.hely) and 0 < labda.sebesseg_x:
        labda.sebesseg_x *= -1
    # Labda a bal szélen: bal játékos gólt kapott.
    elif labda.x < 20:
        jobb_uto.pont += 1
        kozepkezdes()
    # Labda a jobb szélen: jobb játékos gólt kapott.
    elif 940 < labda.x:
        bal_uto.pont += 1
        kozepkezdes()
    # Labda a felső vagy alsó szélen.
    if labda.y < 20 or 700 < labda.y:
        labda.sebesseg_y *= -1

# Mindhárom szereplőn meghívjuk a mozdulj() metódust.
def mozgasd_a_szereploket():
    bal_uto.mozdulj()
    jobb_uto.mozdulj()
    labda.mozdulj()

# Visszahelyezzük középre a labdát, és várunk egy kicsit.
def kozepkezdes():
    labda.x = 480
    labda.y = 360
    ora.tick(3)

# Elhelyezzük a hátteret, a feliratot és a szereplőket.
def frissitsd_a_kijelzot():
    # Itt egyszínű a háttér; de lehetne kép is.
    kijelzo.fill(hatterszin)
    # A felirat hátrébb van, mint a labda.
    eredmeny_szoveg = str(bal_uto.pont) + " : " + str(jobb_uto.pont)
    eredmeny_kep = betu.render(eredmeny_szoveg, True, betuszin)
    eredmeny_hely = eredmeny_kep.get_rect()
    eredmeny_hely.center = (480, 60)
    kijelzo.blit(eredmeny_kep, eredmeny_hely)
    bal_uto.jelenj_meg()
    jobb_uto.jelenj_meg()
    labda.jelenj_meg()
    # Kijelző frissítése, hogy megjelenjenek a változtatások.
    pg.display.flip()

# Létrehozzuk a Pygame működéséhez szükséges objektumokat.
pg.init()
meret = (960, 720)
kijelzo = pg.display.set_mode(meret)
hatterszin = (15, 15, 60)
betuszin = (210, 210, 30)
pg.display.set_caption("Skool Pong")
betu = pg.font.SysFont(pg.font.get_default_font(), 120)
ora = pg.time.Clock()

# Létrehozzuk a három szereplőt.
bal_uto = Szereplo("uto", 30, 360)
jobb_uto = Szereplo("uto", 930, 360)
labda = Szereplo("labda", 480, 360)
# Kisorsoljuk, merre menjen a labda.
labda.sebesseg_x = r.choice([-9,9])
labda.sebesseg_y = r.choice([-3,3])

# És most jön a voltaképpeni játék. Itt nincsenek technikai részletek,
# csak egy olyan kód, ami a játékmenet leírásaként is jól olvasható.
while True:
    kezeld_a_billentyuket()
    figyeld_az_utkozeseket()
    mozgasd_a_szereploket()
    frissitsd_a_kijelzot()
    ora.tick(30)
