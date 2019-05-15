import random

eredmenyek = []

def menu():
    print("Kezdő")
    print("Haladó")
    print("Mester")

def jatek_keszitese():
    ervenyes_valasztas = False
    while not ervenyes_valasztas:
        szint = input("Válassz nehézségi szintet: ")
        min = 0
        max = 0
        if szint == "Kezdő":
            ervenyes_valasztas = True
            max = 100
            min = 0
        elif szint == "Haladó":
            ervenyes_valasztas = True
            max = 1000
            min = 0
        elif szint == "Mester":
            ervenyes_valasztas = True
            max = 100000
            min = 100
        else:
            print("Nincs ilyen szint.")

    return random.randint(min,max)

def tippelgetes(kigondolt_szam):
    tippek_szama = 1
    utolso_tipp = int(input("Mire gondoltam? "))
    while utolso_tipp != kigondolt_szam:
        if kigondolt_szam > utolso_tipp:
            print("Nagyobbra gondoltam!")
        elif kigondolt_szam < utolso_tipp:
            print("Kisebbre gondoltam!")

        tippek_szama = tippek_szama + 1
        utolso_tipp = int(input("Mire gondoltam? "))

    print("Gratulálok, ", tippek_szama, " tippelésből eltaláltad! A gondolt szám ez volt: ", kigondolt_szam)
    eredmenyek.append(tippek_szama)
    
def eredmeny_listazas():
    print("Eddigi eredményeid:")
    for elem in eredmenyek:
        print(elem, ". tippelés")


uj_jatek = True
while uj_jatek:
    menu()
    szam = jatek_keszitese()
    tippelgetes(szam)
    eredmeny_listazas()
    valasz = input("Új játék? (Igen/Nem): ")
    uj_jatek = valasz == "Igen"
