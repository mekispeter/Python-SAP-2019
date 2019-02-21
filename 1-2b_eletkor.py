"""
    Életkor b
    Python SAP tananyag
    Skool 2019

    Új eszköz: "if: ... else: ..." és indentálás, "=="
"""

szuletesi_ev_szoveggel = input("Mikor születtél?")
szuletesi_ev_szammal = int(szuletesi_ev_szoveggel)
elmult_e = input("Elmúlt már a születésnapod?")
if elmult_e == "igen":
    eletkor = 2019 - szuletesi_ev_szammal
else:
    eletkor = 2018 - szuletesi_ev_szammal
print("Pontosan", eletkor, "éves vagy!")
