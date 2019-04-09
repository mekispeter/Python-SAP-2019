
allitasok = [
			["Niki:","a:boxolok", "b:fogyózok", "c:19. kerületben lakom", "c"],
			["Tünde:","a:szeretek aludni", "b:ártam Dániában", "c:sokat járok színházba", "b"],
			["Nóri:","a:kutyás vagyok", "b:előbb a tejet öntöm a tálba:aztán a műzlit", "c:Marvel fan vagyok", "b"],
#			["Rebeka:","a:tuduk ukulelézni", "b:szeretek úszni", "c:tériszonyom van", "c"],
#			["Timi:","a:macskás vagyok", "b:AKG-ba járok", "c:gyerekekkel szeretnék foglalkozni", "a"],
#			["Prisca:","a:nem szeretem a bolognait", "b:öt testvérem van, ebből egy sem édestestvér", "c:Két anyukámat tekintek anyukámnak, egy lelki és egy biológia", "a"], 
#			["Virág:","a:empatikus vagyok", "b:nem szeretem a paradicsomlevest", "c:türelmes vagyok", "c"], 
#			["Mira:","a:Disneynél dolgoznék", "b:cserkész vagyok 6 éve", "c:kedvenc tárgyam az infó és a mat#ek", "b"],
#			["Kami:","a:szeretem a főzelekékeket", "b:Budaörsön élek", "c:van egy 10 évvel idősebb bátyám", "a"], 
#			["Lilla:","a:szeretem a Fortnightot", "b:Warcraft volt az első játékom", "c:matek a kedvencem", "a"], 
#			["Odett:","a:", "b:", "c:", "c"], 
#			["Lívia:","a:szívesen lennék hangtechnikus", "b:szívesen lennék programozó", "c:szívesen lennék webfejlesztő", "c"], 
#			["Dóra:","a:göndörítem a hajam", "b:szeretem a spenótot", "c:kiskoromban megöltem a bogarakat", "a"], 
#			["Viki:","a:18 éves vagyok", "b:kötélmászó vagyok", "c:rengeteget eszem", "a"], 
#			["Tami:","a:11 éve szeretnék egy jegesmedvét", "sokáig hittem a Fogtündérben", "c:Arany János leszármazottja vagyok", "c"]
			]

valasz = ""
pont = 0

def kerdezz(kerdes):
	for elem in kerdes[0:4]:
		print(elem)
	valasz = input("Válasz (a,b vagy c): ")
	if valasz == kerdes[4]:
		return 1
	else:
		return 0

for kerdes in allitasok:
		pont += kerdezz(kerdes)
print("Eredmény:", pont)