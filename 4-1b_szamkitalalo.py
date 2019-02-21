"""
    Szamkitalalo b
    Python SAP tananyag
    Skool 2019

    Új eszköz: nincs
"""

import random

print("Mondok egy számot 1 és 100 között. Hány találgatással tudsz rájönni?")
feladvany = random.randrange(1, 101)

tipp = 0
szamlalo = 0
while tipp != feladvany:
    tipp = int(input("Tipp: "))
    if tipp < feladvany:
        print("Kevés!")
    elif feladvany < tipp:
        print("Sok!")
    szamlalo += 1

print("Ügyes vagy!", szamlalo, "lépésben kitaláltad!")
