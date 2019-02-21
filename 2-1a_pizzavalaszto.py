"""
    Pizzakaválasztó a
    Python SAP tananyag
    Skool 2019

    Új eszköz: lista definiálása elemfelsorolással, ...in... feltétel
"""

pizza_menu = ["Margherita", "Prosciutto", "Capricciosa", "Quattro formaggi",
    "Hawaiiana"]
pizza = input("Milyen pizzát szeretnél?")
if pizza in pizza_menu:
    print("Szuper, az pont van nálunk!")
else:
    print("Sajnos azt pont nem tartunk!")
