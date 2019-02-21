"""
    Leetgenerátor b
    Python SAP tananyag
    Skool 2019

    Új eszköz: szótár definiálása elemfelsorolással; szótár lekérdezés
"""

leetszotar = {"a":"4", "e":"3", "g":"9", "i":"1", "l":"1", "o":"0",
    "s":"5", "t":"7", "z":"2"}

def csere(betu):
    if betu in leetszotar:
        return leetszotar[betu]
    else:
        return betu

eredeti_szoveg = input("Mit alakítunk át?")

uj_szoveg = ""
for eredeti_betu in eredeti_szoveg:
    kis_betu = eredeti_betu.lower()
    cserelt_betu = csere(kis_betu)
    uj_szoveg += cserelt_betu
print(uj_szoveg)
