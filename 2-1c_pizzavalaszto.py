"""
    Pizzaválasztó c
    Python SAP tananyag
    Skool 2019

    Új eszköz: -
"""

pizza_menu = [
        ["Margherita", 1600],
        ["Prosciutto", 1800],
        ["Capricciosa", 1900],
        ["Quattro formaggi", 1900],
        ["Hawaiiana", 2100]]

megvan_e = "nem"
pizza = input("Milyen pizzát kérsz?")
for sor in pizza_menu:
    if sor[0] == pizza:
        print(sor[1], "forint lesz!")
        megvan_e = "igen"
if megvan_e == "nem":
    print("Sajnos ezt nem tartjuk, gyere vissza holnap!")
