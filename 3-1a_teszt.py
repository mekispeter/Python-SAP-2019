"""
    Teszt a
    Python SAP tananyag
    Skool 2019

    Új eszköz: lista szeletelése indextartománnyal; while-ciklus; not operátor
"""

feladvany = ["Ki nem Marvel karakter?", "(a) Hulk", "(b) Superman", "(c) Captain America", "b"]

for elem in feladvany[0:4]:
    print(elem)
valasz = ""
while not valasz in "abc":
    valasz = input("Válasz (a, b vagy c): ")

if valasz == feladvany[4]:
    print("Ügyes vagy!")
else:
    print("Ehhh...")
