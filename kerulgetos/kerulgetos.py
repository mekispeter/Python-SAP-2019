"""
    Kerülgetős
    Python SAP tananyag
    Skool 2019

    Pygame játék intenzív dinamikus objektumgenerálással.
    Elkészítési idő: kb. 3 alkalom.
    Játékmenet: A játékos billentyűkkel mozgatja jobbra-balra a "hosunk" nevű
    szereplőt a kijelző alján, és lő vele az ellenségekre. Az ellenségek a
    kijelző tetején keletkeznek, ereszkednek lefelé, és maguk is lőnek. Minden
    ütközésért pont jár. Ha egy szereplő ütközik, életet veszít. Ha "hosunk"
    három élete elfogy, vége a játéknak.

    Továbbfejlesztési lehetőségek a hasonló játékok logikája szerint:
    - az ellenség egyre gyakrabban jön
    - az ellenség egyre gyorsabban jön
    - az ellenség egyre gyakrabban lő
    - többféle ellenség, az erősebbeket több lövéssel kell kilőni
    - nincs korlátlan lőszer, ha kifogy, várni kell
    - lőszer- és életcsomagok is érkeznek
    - pajzs, ami megvéd ütközéskor
    - kétjátékosos mód: hosunk1, hosunk2
    stb.
"""

# Ezek a szokásos csomagok, minden pygame projektben importáljuk őket.
import sys
import random as r
import pygame as pg

"""
    Ez egy általános szereplőosztály. Nagyrészt közös más projektekkel, de van
    benne néhány új attribútum is. A specifikus szereplőosztályok ennek az
    alosztályai lesznek.

    A "szereplő" és a "jelmez" kifejezések a Scratch-ből származnak, a "sprite"
    és a "costume" magyar megfelelői. Pygame terminológiában a jelmez egy
    surface objektum. A "hely" elnevezést jobb híján választottam a "rect"
    magyarítására.
"""
class Szereplo():
    def __init__(self, jelmeznev, x, y, seb_x = 0, seb_y = 0, elet = 1):
        self.jelmez = pg.image.load(jelmeznev + ".png")
        self.hely = self.jelmez.get_rect()
        self.x = x
        self.y = y
        self.sebesseg_x = seb_x
        self.sebesseg_y = seb_y
        # A főhősnek három élete van, és ha elfogy, vége a játéknak. A többi
        # szereplőnek egy, és ha elfogy, törlődik.
        self.elet = elet
    # Elhelyezi a kijelzőn a szereplőt.
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
    # Beállítja a szereplő vízszintes és függőleges koordinátáit.
    def mozdulj(self):
        self.x += self.sebesseg_x
        self.y += self.sebesseg_y
    # Ütközésfigyelés. A colliderect nem pixelpontos; azt figyeli, hogy az
    # egyik téglalap fedi-e a másikat, függetlenül az átlátszóságtól.
    # Pixelpontos ütközéshez a rect-ből mask-ot kell előállítani.
    # Ütközéskor mindkét szereplő életet veszít, és a fő szereplő kap egy
    # pontot.
    def utkozol_e_vele(self, masik_szereplo):
        if self.hely.colliderect(masik_szereplo.hely):
            self.elet -= 1
            masik_szereplo.elet -= 1
            hosunk.pont += 1
    # Ütközésfigyelés szereplő és szereplőlista között.
    def utkozol_e_veluk(self, szereplok):
        for szereplo in szereplok.lista:
            self.utkozol_e_vele(szereplo)
    # Azt figyeli, hogy függőlegesen benne van-e a szereplő a kijelzőben.  Ha
    # nem, akkor nullára állítja az életét.
    def kimentel_e(self):
        if self.y < 0 or 960 < self.y:
            self.elet = 0

"""
    Ez egy egypéldányos szereplőosztály; ennek az egy példányát irányítja a
    játékos. Az erre az alosztályra jellemző default paraméterekkel hívja meg a
    szuperosztályát; és bevezet két új attribútumot is.
"""
class Hosunk(Szereplo):
    def __init__(self):
        Szereplo.__init__(self, "hosunk", 360, 840, 0, 0, elet = 3)
        self.pont = 0
    # A lövedékek az őket kilövő szereplőtől indulnak.
    def loj(self):
        lovedekek_hosunk.lista.append(Lovedek_hosunk(self.x, self.y))

"""
    Az "Ellenseg" osztály objektumai felülről-lefelé mozognak, és a
    "Hosunk"-höz hasonlóan lőnek, de másfajta lövedékkel.
"""
class Ellenseg(Szereplo):
    def __init__(self):
        Szereplo.__init__(self, "ellenseg", r.randrange(60, 661), 0, 0, 5)
    # A lövedékek az őket kilövő szereplőtől indulnak.
    def loj(self):
        lovedekek_ellenseg.lista.append((Lovedek_ellenseg(self.x, self.y)))

"""
    Az ellenséges lövedékek az ellenséghez hasonlóan lefelé mozognak, csak
    gyorsabban.
"""
class Lovedek_ellenseg(Szereplo):
    def __init__(self, x, y):
        Szereplo.__init__(self, "lovedek_ellenseg", x, y, 0, 12)

"""
    Az játékos által indított lövedékek felfelé mozognak.
"""
class Lovedek_hosunk(Szereplo):
    def __init__(self, x, y):
        Szereplo.__init__(self, "lovedek_hosunk", x, y, 0, -12)

"""
    A szereplőlisták absztrakt objektumok. Azért hasznosak, mert jól
    strukturálják a kódot, és mert ha a listák attribútumok, akkor nem kell
    hatókörökkel foglalkozni, amikor függvények módosítják őket. Viszonylag
    egyszerűen módosítani lehet a kódot úgy, hogy erre az osztályra ne legyen
    szükség.
"""
class Szereplolista():
    def __init__(self):
        self.lista = []
    # A lista összes elemét mozgatja.
    def mozduljanak(self):
        for szereplo in self.lista:
            szereplo.mozdulj()
    # A lista összes elemére figyeli az ütközéseket.
    def utkoznek_e(self, masikak):
        for szereplo in self.lista:
            szereplo.utkozol_e_veluk(masikak)
    # A lista összes elemére figyeli, hogy kiment-e a kijelzőről.
    def kimentek_e(self):
        for szereplo in self.lista:
            szereplo.kimentel_e()
    # Törli a listáról azokat az elemeket, amelyeknek az élete lenullázódott.
    def torold_a_felesleget(self):
        uj_lista = []
        for szereplo in self.lista:
            if 0 < szereplo.elet:
                uj_lista.append(szereplo)
        self.lista = uj_lista
    # Megjeleníti a lista összes elemét.
    def jelenjenek_meg(self):
        for szereplo in self.lista:
            szereplo.jelenj_meg()

# Pygame eseménykezelés. a get() a két hívás között történt események listáját
# adja vissza.
def kezeld_a_billentyuket():
    # Ablak kiixelése.
    for esemeny in pg.event.get():
        if esemeny.type == pg.QUIT:
            sys.exit()
        elif esemeny.type == pg.KEYDOWN:
            # Kilépés Esc-re.
            if esemeny.key == pg.K_ESCAPE:
                sys.exit()
            # Jobb/bal billentyűnyomásra a billentyű elengedéséig megy
            # jobbra/balra.
            elif esemeny.key == pg.K_LEFT:
                hosunk.sebesseg_x = -5
            elif esemeny.key == pg.K_RIGHT:
                hosunk.sebesseg_x = 5
            # A Fel billentyű lenyomására egyszer lő (nem amíg le van nyomva a
            # billentyű).
            elif esemeny.key == pg.K_UP:
                hosunk.loj()
        elif esemeny.type == pg.KEYUP:
            if esemeny.key  == pg.K_LEFT and hosunk.sebesseg_x < 0:
                hosunk.sebesseg_x = 0
            elif esemeny.key == pg.K_RIGHT and 0 < hosunk.sebesseg_x:
                hosunk.sebesseg_x = 0

# Átlag kétmásodpercenként keletkezik új ellenség, és az ellenségek átlag
# kétmésodpercenként lőnek. A függvény neve nem szerencsés, mert a két feladat
# közül csak az egyikre utal.
def csinalj_ellenseget():
    if r.randrange(60) == 0:
        ellensegek.lista.append(Ellenseg())
    for ellenseg in ellensegek.lista:
        if r.randrange(60) == 0:
            ellenseg.loj()

# Minden szereplőlistán meghívjuk az elemek mozgatását.
def mozgasd_a_szereploket():
    hosunk.mozdulj()
    ellensegek.mozduljanak()
    lovedekek_hosunk.mozduljanak()
    lovedekek_ellenseg.mozduljanak()

# Figyeljük az ütközéseket egymással és a kijelzőhatárokkal.
def figyeld_az_utkozeseket():
    ellensegek.utkoznek_e(lovedekek_hosunk)
    hosunk.utkozol_e_veluk(lovedekek_ellenseg)
    hosunk.utkozol_e_veluk(ellensegek)
    ellensegek.kimentek_e()
    lovedekek_hosunk.kimentek_e()
    lovedekek_ellenseg.kimentek_e()

# Töröljük azokat a szereplőket, amelyeknek az élet attribútuma lenullázódott.
def torold_a_felesleget():
    ellensegek.torold_a_felesleget()
    lovedekek_hosunk.torold_a_felesleget()
    lovedekek_ellenseg.torold_a_felesleget()

# Megjelenítjük az összes szereplőt, a hátteret is beleértve, és frissítjük a
# kijelzőt.
def jelenitsd_meg_a_szereploket():
    hatter.jelenj_meg()
    elet = betu.render("élet: "+str(hosunk.elet), False, betuszin)
    kijelzo.blit(elet, (60,60))
    pont = betu.render("pont: "+str(hosunk.pont), False, betuszin)
    kijelzo.blit(pont, (450,60))
    hosunk.jelenj_meg()
    ellensegek.jelenjenek_meg()
    lovedekek_hosunk.jelenjenek_meg()
    lovedekek_ellenseg.jelenjenek_meg()
    pg.display.flip()

# Intro: megjelenik a háttér, a főszereplő és a cím, majd várunk két
# másodpercet.
def cim():
    cim = betu.render("Kerülgetős játék", False, betuszin)
    cim_helye = cim.get_rect()
    cim_helye.center = (360, 480)
    hatter.jelenj_meg()
    hosunk.jelenj_meg()
    kijelzo.blit(cim, cim_helye)
    kijelzo.blit(cim, cim_helye)
    pg.display.flip()
    ora.tick(0.5)

# Outro: A kijelzőre (az eddigi kép törlése nélkül) kitesszük a végfeliratot,
# majd várunk két másodpercet.
def jatek_vege():
    vege = betu.render("Vége!", False, betuszin)
    vege_helye = vege.get_rect()
    vege_helye.center = (360, 480)
    kijelzo.blit(vege, vege_helye)
    pg.display.flip()
    ora.tick(0.5)

# Létrehozzuk a Pygame működéséhez szükséges objektumokat.
pg.init()
kijelzo = pg.display.set_mode((720, 960))
betuszin = (30, 30, 120)
pg.display.set_caption("Kerülgetős játék")
betu = pg.font.SysFont(pg.font.get_default_font(), 90)
ora = pg.time.Clock()

# A korábbiaktól eltérően itt nem színt, hanem képet használunk háttérnek, ami
# maga is szereplő.
hatter = Szereplo("hatter", 360, 480)
# A játék kezdetén egyetlen szereplőnk van; a három szereplőlista menet közben
# töltődik fel elemekkel.
hosunk = Hosunk()
ellensegek = Szereplolista()
lovedekek_ellenseg = Szereplolista()
lovedekek_hosunk = Szereplolista()

# És most jön a voltaképpeni játék. Itt már nincsenek technikai részletek,
# csak egy olyan kód, ami a játékmenet leírásaként is jól olvasható.
cim()
while 0 < hosunk.elet:
    csinalj_ellenseget()
    mozgasd_a_szereploket()
    figyeld_az_utkozeseket()
    torold_a_felesleget()
    kezeld_a_billentyuket()
    jelenitsd_meg_a_szereploket()
    ora.tick(30)
jatek_vege()
