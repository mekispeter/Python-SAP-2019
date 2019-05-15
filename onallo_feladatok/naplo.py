tantargyak = [
    ["Történelem", [ [5, "Felelés"],[4, "Dolgozat"], [4, "Felelés"] ] ],
    ["Irodalom", [ [3, "Dolgozat"],[5, "Versmondás"], [5, "Dolgozat"] ] ],
]

def menu():
    print("(a)	Jegyek megtekintése")
    print("(b)	Átlag megtekintése")
    print("(c)	Feltételes átlag számítása")
    print("(d)	Kilépés")

    ervenyes_valasztas = False
    while not ervenyes_valasztas:
        valasz = input("Mit szeretnél? ")
        if(valasz == "a" or valasz == "b" or valasz == "c" or valasz == "d"):
            ervenyes_valasztas = True
            return valasz
        else:
            print("Érvénytelen választás.")

def jegyek_listazasa():
    tantargy = input("Tantárgy neve: ")
    talalat = False
    for elem in tantargyak :
        if elem[0] == tantargy:
            talalat = True
            for jegy in elem[1]:
                print(jegy[0], "(", jegy[1], ")")
            

    if not talalat:
        jegyek_listazasa()

def atlag_mutatasa():
    tantargy = input("Tantárgy neve: ")
    talalat = False
    for elem in tantargyak:
        if elem[0] == tantargy:
            osszeg = 0
            for jegy in elem[1]:
                osszeg = osszeg + jegy[0]
            
            atlag = round(osszeg / len(elem[1]), 1)
            print(elem[0], " átlagom: ", atlag)
            talalat = True

    if not talalat:
        atlag_mutatasa()

def uj_atlag_szamitasa():
    tantargy = input("Tantárgy neve: ")
    uj_jegy = int(input("Új jegy: "))

    talalat = False
    for elem in tantargyak:
        if elem[0] == tantargy:
            osszeg = 0
            for jegy in elem[1]:
                osszeg = osszeg + jegy[0]

            atlag = round(osszeg / len(elem[1]), 1)
            atlag = (atlag + uj_jegy) / 2
            print(elem[0], " átlagom, ha a következő jegyem", uj_jegy, ": ", atlag)
            talalat = True

    if not talalat:
        uj_atlag_szamitasa()

kilepes = False
while not kilepes:
    valasztas = menu()
    if valasztas == "a":
        jegyek_listazasa()
    elif valasztas == "b":
        atlag_mutatasa()
    elif valasztas == "c":
        uj_atlag_szamitasa()
    elif valasztas == "d":
        kilepes = True