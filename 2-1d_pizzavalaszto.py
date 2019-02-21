"""
    Pizzaválasztó d
    Python SAP tananyag
    Skool 2019

    Új eszköz: föggvénydefiniálás, függvényhívás, ==, metódusok: append(), lower()
"""

pizza_menu = [
        ["Margherita", 1600, ["paradicsom", "bazsalikom", "mozzarella"]],
        ["Prosciutto", 1800, ["paradicsom", "sonka", "mozzarella"]],
        ["Capricciosa", 1900, ["paradicsom", "gomba", "sonka", "mozzarella"]],
        ["Quattro formaggi", 1900, ["paradicsom", "gorgonzola", "stracchino", "ricotta", "mozzarella"]],
        ["Hawaiiana", 2100, ["paradicsom", "gorgonzola", "mozzarella", "sonka", "ananász"]]]

def pizzarendeles_nevvel():
    pizza = input("Milyen pizzát kérsz?")
    megvan_e = "nem"
    for sor in pizza_menu:
        if sor[0] == pizza:
            print(sor[1], "forint lesz!")
            megvan_e = "igen"
    if megvan_e == "nem":
        print("Sajnos ilyet ma nem sütünk, gyere vissza holnap!")

def pizzarendeles_feltettel():
    feltet = input("Milyen feltét legyen rajta?")
    szurt_menu = []
    for sor in pizza_menu:
        if feltet in sor[2]:
            szurt_menu.append(sor)
    if szurt_menu == []:
        print("Sajnos azt mi nem teszünk a pizzákra!")
    else:
        print("Ezt tudjuk ajánlani:")
        for sor in szurt_menu:
            print("-", sor[0], sor[1], "Ft")

valasztas = input("Név vagy feltét szerint választasz?")
if valasztas.lower() == "név":
    pizzarendeles_nevvel()
else:
    pizzarendeles_feltettel()
