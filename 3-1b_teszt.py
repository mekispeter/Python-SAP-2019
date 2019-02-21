"""
    Teszt b
    Python SAP tananyag
    Skool 2019

    Új eszköz: +=
"""

feladvanyok = [
    ["Ki nem Marvel karakter?", "(a) Hulk", "(b) Superman", "(c) Captain America", "b"],
    ["Miből van a legtöbb a világon?", "(a) ember", "(b) bicikli", "(c) legókocka", "c"],
    ["Melyik magyar sorozat?", "(a) A mi kis falunk", "(b) Dr. Csont", "(c) Agymenők", "a"],
    ["Ki volt a legfiatalabb, amikor meghalt?", "(a) Petőfi Sándor", "(b) Freddie Mercury", "(c) Gollam", "a"],
    ["Melyik nem programozási nyelv?", "Scratch", "C", "HTML", "c"]
    ]

def kerdezz(feladvany):
    for elem in feladvany[0:4]:
        print(elem)
    valasz = input("Válasz (a, b vagy c): ")
    if valasz == feladvany[4]:
        return 1
    else:
        return 0

pont = 0
for feladvany in feladvanyok:
    pont += kerdezz(feladvany)

if pont == len(feladvanyok):
    print("Wow! Hibátlan! :)")
elif pont == 0:
    print("Fogadjunk, hogy direkt tippeltél rosszakat! :)")
else:
    print("Ennyi volt!", pont, "pontot értél el! :)")
