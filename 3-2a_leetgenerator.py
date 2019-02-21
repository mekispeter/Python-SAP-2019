"""
    Leetgenerátor a
    Python SAP tananyag
    Skool 2019

    Új eszköz: += szöveges adatra; visszatérési érték
"""

def csere(betu):
    if betu == "a":
        return "4"
    elif betu == "e":
        return "3"
    elif betu == "g":
        return "9"
    elif betu == "i" or betu == "l":
        return "1"
    elif betu == "o":
        return "0"
    elif betu == "s":
        return "5"
    elif betu == "t":
        return "7"
    elif betu == "z":
        return "2"
    else:
        return betu

eredeti_szoveg = input("Mit alakítunk át?")

uj_szoveg = ""
for eredeti_betu in eredeti_szoveg:
    kis_betu = eredeti_betu.lower()
    cserelt_betu = csere(kis_betu)
    uj_szoveg += cserelt_betu
print(uj_szoveg)
