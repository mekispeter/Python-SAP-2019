alkatreszek = [
    [ "Olcsó váz", 12000],
    [ "Drága váz", 18000],
    [ "Olcsó kerék", 6000],
    [ "Drága kerék", 10000]
]

festesek = [
    [ "Kék-fehér", 12000],
    [ "Piros-fekete", 13500]
]

kosar = []
nev = ""
cim = ""
telefon = ""

def alkatresz_valasztas():
    print("Válassz alkatrészeket. Ha végeztél, írd be hogy Kész.")

    # Alkatrészek listázása és bekérése
    for elem in alkatreszek:
        print(elem[0], " (", elem[1], ")")

    valasztas = ""
    while valasztas != "Kész":
        valasztas = input("Melyik alkatrészt szeretnéd? ")
        megtalaltam = False
        for elem in alkatreszek:
            if elem[0] == valasztas:
                kosar.append(elem)
                megtalaltam = True
        
        if not megtalaltam and valasztas != "Kész":
            print("Nincs ilyen alkatrész.")
        else:
            print("Kosárba raktuk.")

def festes_valasztas():
    print("Válassz egy festést.")

    # Festések listázása
    for elem in festesek:
        print(elem[0], " (", elem[1], ")")

    megtalaltam = False
    while not megtalaltam:
        valasztas = input("Melyik festést szeretnéd? ")
        for elem in festesek:
            if elem[0] == valasztas:
                kosar.append(elem)
                megtalaltam = True
        
        if not megtalaltam:
            print("Nincs ilyen festés.")

def szemelyes_adatok():
    global nev
    global cim
    global telefon

    nev = input("Neved: ")
    cim = input("Címed: ")
    telefon = input("Telefonszám: ")

def megrendel():
    print("Köszönjük a megrendelésed. Adatok: ")
    print("Név: ", nev)
    print("Cím: ", cim)
    print("Telefon: ", telefon)
    print("Megrendelt konfiguráció:")
    for elem in kosar:
        print(elem[0], "   ",elem[1])

alkatresz_valasztas()
festes_valasztas()
szemelyes_adatok()
megrendel()
    