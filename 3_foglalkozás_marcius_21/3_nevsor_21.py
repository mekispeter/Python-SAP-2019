
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

#tovabb_e = "igen"
#while tovabb_e == "igen":
nev = input("Kit keresel? ")
tag = "nem"
for sor in csoport:
	if sor[0] == nev:
		eletkor = 2019 - sor[1]
		tag = "igen"
if tag == "nem":
	print(nev,"nem a csoport tagja")
else:
	print(nev, eletkor, "éves")
#	tovabb_e = input("Kiváncsi vagy még valakire? ")

#print("Bye!")