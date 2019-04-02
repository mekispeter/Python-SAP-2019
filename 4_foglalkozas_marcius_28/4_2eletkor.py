
csoport = [
			["Niki",2003],
			["Tünde",2002],
			["Nóri",2003],
			["Rebeka",2002],
			["Timi",2002],
			["Prisca",2003], 
			["Virág",2002], 
			["Mira",2002],
			["Kami",2003], 
			["Lilla",2003], 
			["Odett",2002], 
			["Lívia",2002], 
			["Dóra",2003], 
			["Viki",2002], 
			["Tami",2003]
			]

print ("Megmondom ki az idősebb ")
nev1 = input("1. név: ")
nev2 = input("2. név: ")
eletkor1 = 0
eletkor2 = 0

for sor in csoport:
	if sor[0] == nev1:
		eletkor1 = 2019 - sor[1]

for sor in csoport:
	if sor[0] == nev2:
		eletkor2 = 2019 - sor[1]

if eletkor1 == 0 or eletkor2 == 0:
	print(nev1, "vagy", nev2, "nem a csoport tagja")
else:
	if eletkor1 == eletkor2:
		print(nev1, "és", nev2, "egykorúak ")
	elif eletkor1 > eletkor2:
		print(nev1, "idősebb")
	else:
		print(nev2, "idősebb")
