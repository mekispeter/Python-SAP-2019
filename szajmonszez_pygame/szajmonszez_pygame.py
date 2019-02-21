import pygame
import time
import sys
import random

# a Szereplo osztaly az osszes Pygame projektben megjelenik. 
class Szereplo():
    def __init__(self, jelmeznev1, jelmeznev2, kozeppont, billentyu):
        filenev1 = "{}.png".format(jelmeznev1)
        self.jelmez1 = pygame.image.load(filenev1).convert_alpha()
        filenev2 = "{}.png".format(jelmeznev2)
        self.jelmez2 = pygame.image.load(filenev2).convert_alpha()
        self.hely = self.jelmez1.get_rect()
        self.hely.center = kozeppont
        self.billentyu = billentyu
        self.villan = False
    def felvillan(self):
        self.villan = True
        kijelzofrissites()
        time.sleep(0.3)
        self.villan = False
        kijelzofrissites()
        time.sleep(0.2)

def kijelzofrissites(hatterszin = (50, 50, 50)):
    jatekter.fill(hatterszin)
    pont_kijelzes = font.render(str(len(tipp)), True, (32, 32, 128))
    jatekter.blit(pont_kijelzes, (30, 30))
    for szin in szinek:
        if szin.villan == False:
            jatekter.blit(szin.jelmez1, szin.hely)
        else:
            jatekter.blit(szin.jelmez2, szin.hely)
    pygame.display.flip()

def szinadas(szinek):
    feladvany.append(szinek[random.randrange(5)])
    for szin in feladvany:
        szin.felvillan()
        for esemeny in pygame.event.get():
            if esemeny.type == pygame.QUIT:
                sys.exit()
            if esemeny.type == pygame.KEYDOWN:
                if esemeny.key == pygame.K_ESCAPE:
                    sys.exit()
    return feladvany

def tippeles(szinek):
    tipp = []
    while len(tipp) < len(feladvany):
        for esemeny in pygame.event.get():
            if esemeny.type == pygame.QUIT:
                sys.exit()
            if esemeny.type == pygame.KEYDOWN:
                if esemeny.key == pygame.K_ESCAPE:
                    sys.exit()
                for szin in szinek:
                    if esemeny.key == szin.billentyu:
                        szin.felvillan()
                        tipp.append(szin)
            if esemeny.type == pygame.MOUSEBUTTONDOWN:
                egerx, egery = pygame.mouse.get_pos()
                if szinek[4].hely.collidepoint((egerx, egery)):
                    szinek[4].felvillan()
                    tipp.append(szinek[4])
                else:
                    for szin in szinek[:-1]:
                        if szin.hely.collidepoint((egerx, egery)):
                            szin.felvillan()
                            tipp.append(szin)
    for arnyalat in range(50, 250, 5):
        kijelzofrissites((arnyalat, arnyalat, arnyalat))
    for arnyalat in range(250, 50, -5):
        kijelzofrissites((arnyalat, arnyalat, arnyalat))
    return tipp

# kezdobeallitasok
pygame.init()
jatekter = pygame.display.set_mode((960, 720))
pygame.display.set_caption("Szájmonszez: memóriajáték színekkel")
font = pygame.font.SysFont(pygame.font.get_default_font(), 120)
tipp = []
feladvany = []
szinnevek = ["sarga", "zold", "kek", "lila", "piros"]
kozeppontok = {"sarga":(360, 240), "zold":(600, 240), "kek":(360, 480), "lila":(600, 480), "piros":(480, 360)}
billentyuk = {"sarga":pygame.K_t, "zold":pygame.K_u, "kek":pygame.K_b, "lila":pygame.K_m, "piros":pygame.K_h}
szinek = []
for szinnev in szinnevek:
    uj_szin = Szereplo(szinnev+"1", szinnev+"2", kozeppontok[szinnev], billentyuk[szinnev])
    szinek.append(uj_szin)
kijelzofrissites()
time.sleep(1)

# johet a jatek
while tipp == feladvany:
    feladvany = szinadas(szinek)
    tipp = tippeles(szinek)
    time.sleep(1)
#vege
vege_felirat = font.render("VÉGE!", True, (32, 32, 128))
jatekter.blit(vege_felirat, (360, 330))
pygame.display.flip()
time.sleep(3)
