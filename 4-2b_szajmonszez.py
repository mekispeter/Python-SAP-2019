"""
    Szajmonszez b
    Python SAP tananyag
    Skool 2019

    Új eszköz: Time modul; time.sleep(); \n karakter; szöveg szorzása számmal

"""
import random
import time

intro = [
        "Szájmonszez: memóriajáték",
        "Betűk fognak felvillanni a kijelző alján.",
        "Jegyezz meg és gépelj be minél hosszabb sorozat!"]

szinek = ["K", "P", "F", "S", "Z", "L"]
feladvany = []
tipp = []
pont = 0
for szoveg in intro:
    print(szoveg)
    time.sleep(1)
_ = input("Indulhatunk?")
while feladvany == tipp:
    uj_szin = szinek[random.randrange(len(szinek))]
    feladvany.append(uj_szin)
    for szin in feladvany:
        print(szin)
        time.sleep(0.7)
        print("\n" * 80)
        time.sleep(0.3)
    tipp = list(input("Tipp: ").upper())
    print("\n" * 80)
    pont += 1
    time.sleep(0.5)
print("Ügyes vagy!", pont, "pontot értél el!")
