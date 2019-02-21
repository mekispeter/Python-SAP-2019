"""
    Szajmonszez a
    Python SAP tananyag
    Skool 2019

    Új eszköz: upper()
"""

import random

szinek = ["K", "P", "F", "S", "Z", "L"]
feladvany = []
tipp = []
score = 0
while feladvany == tipp:
    print("\n" * 80)
    uj_szin = szinek[random.randrange(len(szinek))]
    feladvany.append(uj_szin)
    print(uj_szin)
    tipp = list(input("Tipp: ").upper())
    score += 1
print("Ügyes vagy! {} pontot értél el!".format(score))
