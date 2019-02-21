"""
    Akasztottember b
    Python SAP tananyag
    Skool 2019

    Új eszköz: len(), list(), range(), remove()

"""
import random

feladvanyok = [
    'KÜLÖNBEN DÜHBE JÖVÜNK', 'MORCOS MISSZIONÁRIUSOK', 'BŰNVADÁSZOK',
    'ÉS MEGINT DÜHBE JÖVÜNK', 'ÉN A VÍZILOVAKKAL VAGYOK', 'KINCS, AMI NINCS',
    'NYOMÁS UTÁNA!', 'NINCS KETTŐ NÉGY NÉLKÜL', 'SZUPERHEKUSOK',
    'BUNYÓ KARÁCSONYIG', 'VESZTESEK ÉS GYŐZTESEK', 'ÉLET VAGY HALÁL',
    'NÉGY LÉGY A SZÜRKE BÁRSONYON', 'VADNYUGATI CASANOVA', 'A MAFFIA MARKÁBAN',
    'PIEDONE, A ZSARU', 'AZ ANGYALOK IS ESZNEK BABOT', 'PIEDONE HONGKONGBAN',
    'ZSOLDOSKATONA', 'CHARLESTON', 'PIEDONE AFRIKÁBAN', 'ARANYESŐ YUCCÁBAN',
    'AKIT BULDÓZERNEK HÍVTAK', 'SERIFF AZ ÉGBŐL', 'PIEDONE EGYIPTOMBAN',
    'A SERIFF ÉS AZ IDEGENEK', 'BANÁNOS JOE', 'BOMBAJÓ BOKSZOLÓ',
    'RABLÓ-PANDÚR', 'ALADDIN', 'FÉL LÁBBAL A PARADICSOMBAN', 'A VÉGSŐ HATÁR']
abece = list('AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ')

def intro():
    print("Akasztófa játék")
    print("Találj ki Bud Spencer -- Terence Hill filmcímeket 7 tippeléssel!")
    input("Indulhatunk?")

def rejtsd_el(eredeti):
    elrejtett = ""
    for x in eredeti:
        if x in abece:
            elrejtett += "_"
        else:
            elrejtett += x
    return elrejtett

def tippelj(nem_volt_meg):
    tipp = ""
    while not tipp in nem_volt_meg:
        tipp = input("Tippelj! ").upper()
    return tipp

def frissitsd (itt_tartunk, feladvany, tipp):
    itt_tartunk_uj = ""
    for i in range(len(feladvany)):
        if feladvany[i] == tipp:
            itt_tartunk_uj += tipp
        else:
            itt_tartunk_uj += itt_tartunk[i]
    return itt_tartunk_uj

def jatssz(feladvany):
    itt_tartunk = rejtsd_el(feladvany)
    nem_volt_meg = abece
    volt_mar = []
    hiba = 0
    while not feladvany == itt_tartunk and hiba < 7:
        print(itt_tartunk)
        print("Ennyi hibád volt eddig:", hiba)
        print("Ezek a betűk voltak már:", volt_mar)
        tipp = tippelj(nem_volt_meg)
        if tipp in feladvany:
            itt_tartunk = frissitsd(itt_tartunk, feladvany, tipp)
        else:
            hiba += 1
        nem_volt_meg.remove(tipp)
        volt_mar.append(tipp)
    if 7 <= hiba:
        print("Sajnos kifogytál a találgatásokból! :(")
    else:
        print("Szuper, sikerült kitalálnod! :)")

def outro(feladvany):
    print("Ez volt a megfejtés:", feladvany)

intro()
feladvany = feladvanyok[random.randrange(len(feladvanyok))]
jatssz(feladvany)
outro(feladvany)
