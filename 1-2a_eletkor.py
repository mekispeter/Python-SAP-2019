"""
    Életkor a
    Python SAP tananyag
    Skool 2019

    Új eszköz: szöveg vs egész szám típus; "int()", aritmetikai operátorok
"""

szuletesi_ev_szoveggel = input("Mikor születtél?")
szuletesi_ev_szammal = int(szuletesi_ev_szoveggel) # elsőre konvertálás nélkül
eletkor = 2019 - szuletesi_ev_szammal
print("Kábé", eletkor, "éves vagy!")
