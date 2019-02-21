"""
    Pizzaválasztó b
    Python SAP tananyag
    Skool 2019

    Új eszköz: elemhivatkozás indexszel; beágyazott lista; for-ciklus
"""

pizza_menu = [
        ["Margherita", 1600],
        ["Prosciutto", 1800],
        ["Capricciosa", 1900],
        ["Quattro formaggi", 1900],
        ["Hawaiiana", 2100]]

pizza = input("Milyen pizzát kérsz?")
for sor in pizza_menu:
    if sor[0] == pizza:
        print(sor[1], "forint lesz!")
